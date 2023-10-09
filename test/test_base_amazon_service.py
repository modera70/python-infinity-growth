import random
import string

import pytest

from src.service.amazon_service import AmazonService


class TestBaseService:

    @pytest.fixture()
    def departments_service(self):
        return AmazonService()
