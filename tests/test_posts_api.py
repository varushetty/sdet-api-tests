import pytest
from assertpy import assert_that
from utils import api_client
from tests.validators import validate_post_structure


class TestPostsAPI:
    """Test suite for JSONPlaceholder /posts endpoint"""

    def test_get_posts_status_code(self, all_posts):
        assert_that(all_posts.status_code)\
            .described_as(f"Status code is not 200 instead found: {all_posts.status_code} ")\
            .is_equal_to(200)

    def test_get_posts_is_list(self, all_posts):
        data = all_posts.json()
        assert_that(data).described_as(f"{data} is not list").is_instance_of(list)
        assert_that(data).described_as(f"{data} is empty").is_not_empty()

    def test_post_structure(self, all_posts):
        first_post = all_posts.json()[0]
        validate_post_structure(first_post)

    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_get_single_post_valid(self, post_id):
        response = api_client.get_single_post(post_id)
        assert_that(response.status_code).described_as("Status response is not 200").is_equal_to(200)

        data = response.json()
        validate_post_structure(data)
        assert_that(data["id"]).described_as(f"{data['id']} is not equal to {post_id}").is_equal_to(post_id)

    @pytest.mark.parametrize("title, body, user_id", [
        ("Test Title", "Test Body", 1),
        ("Another Post", "Some content", 2)
    ])
    def test_create_post(self, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        response = api_client.create_post(payload)

        assert_that(response.status_code)\
            .described_as(f"status response {response.status_code} is not equal to 201")\
            .is_equal_to(201)
        data = response.json()
        assert_that(data["title"])\
            .described_as(f"{data['title']} title is not matching to expected {title}")\
            .is_equal_to(title)
        assert_that(data["body"])\
            .described_as(f"data['body'] body is not matching to expected {body}")\
            .is_equal_to(body)
        assert_that(data["userId"])\
            .described_as(f"data['userId'] id is not matching to expected {user_id}")\
            .is_equal_to(user_id)



