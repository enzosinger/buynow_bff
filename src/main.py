from flask import Flask, request, jsonify
from src.services.user_service import UserService
from src.services.product_service import ProductService

app = Flask(__name__)

# Inicialize as instâncias dos serviços
user_service = UserService()
product_service = ProductService()

# Endpoints para CRUD de Usuários
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    response = user_service.create_user(data)
    return jsonify(response), 201 if "message" in response else 500

@app.route('/api/users', methods=['GET'])
def get_users():
    response = user_service.get_all_users()
    return jsonify(response), 200 if isinstance(response, list) else 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    response = user_service.update_user(user_id, data)
    return jsonify(response), 200 if "message" in response else 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = user_service.delete_user(user_id)
    return jsonify(response), 200 if "message" in response else 404

# Endpoint para registrar uma compra
@app.route('/api/users/<int:user_id>/comprar', methods=['POST'])
def register_purchase(user_id):
    data = request.get_json()
    product_id = data.get("product_id")

    if not product_id:
        return jsonify({"error": "O campo product_id é obrigatório"}), 400

    response = user_service.register_purchase(user_id, product_id)
    return jsonify(response), 200 if "message" in response else 500

# Endpoints para CRUD de Produtos
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    response = product_service.create_product(data)
    return jsonify(response), 201 if "message" in response else 500

@app.route('/api/products', methods=['GET'])
def get_products():
    response = product_service.get_all_products()

    # Verificar se response é uma lista
    if isinstance(response, list):
        return jsonify(response), 200  # Retorna 200 se for uma lista (sucesso)
    else:
        # Caso response seja um dicionário (provavelmente com um erro)
        return jsonify(response), response.get("status", 500)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    response = product_service.update_product(product_id, data)
    return jsonify(response), 200 if "message" in response else 404

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    response = product_service.delete_product(product_id)
    return jsonify(response), 200 if "message" in response else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
