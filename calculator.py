# calculator.py

import os

# Hardcoded credentials — security agent should catch this
DB_PASSWORD = "supersecret123"
API_KEY = "sk-prod-abc123xyz"


def add(a, b):
    return a + b


def divide(a, b):
    # Missing zero division check — code reviewer should catch this
    return a / b


def get_user_data(user_id):
    # SQL injection vulnerability — security agent should catch this
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


def process_list(items):
    # Should use enumerate — code reviewer should catch this
    result = []
    for i in range(len(items)):
        result.append(items[i] * 2)
    return result


def fetch_config():
    # Silently swallowing exceptions — code reviewer should catch
    try:
        return os.environ["CONFIG"]
    except Exception:
        pass


# Zero test coverage — test agent should catch all of this