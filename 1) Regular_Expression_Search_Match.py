import re

text = "Hello, my email is user@example.com and phone is 123-456-7890"

email_pattern = r'\b[A-Za-z0-9_]+@[A-Za-z0-9]+.[A-Za-z]{2,}\b'
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

email_match = re.search(email_pattern, text)
if email_match:
    print("Email : ", email_match.group())
else:
    print("Email not found")

phone_match = re.search(phone_pattern, text)
if phone_match:
    print("Phone : ", phone_match.group())
else:
    print("No phone found")
