import os

import requests


class AmazonService:
    DEFAULT_BASE_URL = "https://www.mercadolibre.com.ar"

    def __init__(self):
        self.service_base_url = os.getenv("BOOK_SERVICE_BASE_URL", AmazonService.DEFAULT_BASE_URL)

    def get_departments(self):
        return requests.get(f"{self.service_base_url}/menu/departments")
