# calculator.py
import os

# Hardcoded credentials
DB_PASSWORD = "supersecret123"
API_KEY = "sk-prod-abac123xyz"


def divide(a, b):
    return a / b  # missing zero check


def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query


def process_list(items):
    result = []
    for i in range(len(items)):
        result.append(items[i] * 2)
    return result