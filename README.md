# API Automation with Pytest & AssertPy

## Overview
This project tests the public API: https://jsonplaceholder.typicode.com/posts

### Features
- Uses `pytest` for test execution
- Uses `assertpy` for fluent, readable assertions
- Includes positive & negative tests
- Parametrized test cases (no hard-coded duplication)
- Setup & teardown with fixtures

## Install
```bash
pip install -r requirements.txt
```

## Run Tests
```bash
pytest -v
```

## Run Specific Test File
```bash
pytest tests/test_posts_api.py -v
```
