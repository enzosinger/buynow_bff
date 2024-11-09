import requests

class UserService:
    BASE_URL = "https://buynow-users.blackcliff-7d1a3af3.eastus2.azurecontainerapps.io/api/users"  # URL do microsserviço de usuários

    def create_user(self, data):
        response = requests.post(f"{self.BASE_URL}", json=data)
        return response.json()

    def get_all_users(self):
        response = requests.get(f"{self.BASE_URL}")
        return response.json()

    def update_user(self, user_id, data):
        response = requests.put(f"{self.BASE_URL}/{user_id}", json=data)
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.BASE_URL}/{user_id}")
        return response.json()

    def register_purchase(self, user_id, product_id):
        response = requests.post(f"{self.BASE_URL}/{user_id}/comprar", json={"product_id": product_id})
        return response.json()
