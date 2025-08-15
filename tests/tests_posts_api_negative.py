import pytest
from assertpy import assert_that
from utils import api_client


class TestApiClientNegative:
    """Test suite for negative JSONPlaceholder /posts endpoint"""

    @pytest.mark.parametrize("invalid_id", [999999, -1, "abc"])
    def test_get_single_post_invalid(self, invalid_id):
        response = api_client.get_single_post(invalid_id)

        assert_that(response.status_code).described_as("Status is not 404").is_equal_to(404)
        data = response.json()
        assert_that(data).is_equal_to({}) or assert_that(data.get("id")).described_as("id is equal to invalid id")\
            .is_not_equal_to(invalid_id)
