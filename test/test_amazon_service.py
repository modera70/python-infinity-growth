import requests
from assertpy import assert_that

from test.test_base_amazon_service import TestBaseService


class TestService(TestBaseService):

    def test_get_departments(self, departments_service):
        departments_response = departments_service.get_departments()
        print(f"response_content: {departments_response.json()}\nresponse_code: {departments_response.status_code}")
        departments_json = departments_response.json()
        departments = departments_json['departments']
        assert_that(len(departments)).is_greater_than(0)
