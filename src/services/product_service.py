import requests

class ProductService:
    BASE_URL = "https://buynow-nodefunctions.azurewebsites.net/api/products"  # URL do Azure Functions de produtos

    def create_product(self, data):
        response = requests.post(f"{self.BASE_URL}", json=data)
        return response.json()

    def get_all_products(self):
        response = requests.get(f"{self.BASE_URL}")
        return response.json()

    def update_product(self, product_id, data):
        response = requests.put(f"{self.BASE_URL}/{product_id}", json=data)
        return response.json()

    def delete_product(self, product_id):
        response = requests.delete(f"{self.BASE_URL}/{product_id}")
        return response.json()
