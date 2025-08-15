from assertpy import assert_that


def validate_post_structure(post):
    expected_keys = {"userId", "id", "title", "body"}
    assert_that(post.keys()).contains(*expected_keys)

    assert_that(post["userId"]).is_instance_of(int)
    assert_that(post["id"]).is_instance_of(int)
    assert_that(post["title"]).is_instance_of(str).is_not_empty()
    assert_that(post["body"]).is_instance_of(str).is_not_empty()
