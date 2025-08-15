import requests
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_posts():
    logging.info(f"GET {BASE_URL}/posts")
    return requests.get(f"{BASE_URL}/posts")


def get_single_post(post_id):
    logging.info(f"GET {BASE_URL}/posts/{post_id}")
    return requests.get(f"{BASE_URL}/posts/{post_id}")


def create_post(payload):
    logging.info(f"POST {BASE_URL}/posts with payload={payload}")
    return requests.post(f"{BASE_URL}/posts", json=payload)
