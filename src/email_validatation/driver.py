from util import filter_valid_emails

n = int(input())
emails = [input().split() for _ in range(n)]

print(filter_valid_emails(emails))