import requests


class NeuralLoveAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.neural.love/v1/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def _post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def generate_art(self, prompt, style, layout, amount, is_hd, is_public):
        data = {
            "prompt": prompt,
            "style": style,
            "layout": layout,
            "amount": amount,
            "isHd": is_hd,
            "isPublic": is_public
        }

        return self._post("ai-art/generate", data)

    def get_order_status(self, order_id):
        return self._get(f"ai-art/orders/{order_id}")

    def estimate_cost(self, prompt, style, layout, amount, is_hd, is_public):
        data = {
            "prompt": prompt,
            "style": style,
            "layout": layout,
            "amount": amount,
            "isHd": is_hd,
            "isPublic": is_public
        }

        return self._post("ai-art/estimate", data)
