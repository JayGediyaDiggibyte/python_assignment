import re

def is_valid_email(email):
    patters = r'^[A-Za-z0-9_.-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return bool(re.match(patters, email))

def filter_valid_emails(emails):
    return sorted(filter(is_valid_email, emails))