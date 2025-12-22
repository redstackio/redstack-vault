---
id: 3d2c5178-b84f-47c6-8418-948e5a6aa807
name: Brute-Force-Login-via-MongoDB-Query-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.517650+00:00'
updated_at: '2023-04-10T20:23:01.631145+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Blind NoSQL]]'
  - '[[tags/NoSQL Injection]]'
  - '[[tags/POST with JSON body]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Brute-Force-Login-via-MongoDB-Query-Injection

## Summary

This procedure demonstrates how to perform a brute force attack on a login endpoint vulnerable to MongoDB query injection. By injecting specially crafted MongoDB queries into the JSON payload of POST requests, the attacker iteratively guesses the password character by character using regex patterns, bypassing traditional authentication checks and gaining unauthorized access to the application.

## Description

MongoDB query injection in login forms allows attackers to manipulate the backend database queries to validate credentials without knowing the full password upfront. This technique exploits insufficient input sanitization in web applications using MongoDB, where user-supplied data is directly interpolated into queries. The attack constructs payloads that match the username exactly while using a regex to test password prefixes, progressively building the password through trial and error. It is effective against blind NoSQL injection scenarios where no direct error feedback is provided, relying instead on successful login indicators like status codes or response text. This method targets web applications with JSON-based APIs and can lead to full account compromise, enabling further actions such as data theft or privilege escalation. The procedure assumes the target uses MongoDB without parameterized queries and lacks rate limiting on login attempts.

## Requirements

1. Network access to the target's login endpoint (e.g., HTTP/HTTPS reachable).
2. Knowledge of the target username (e.g., 'admin') or ability to enumerate it separately.
3. Python environment with the 'requests' and 'urllib3' libraries installed.
4. Target application vulnerable to MongoDB query injection in the login form.

## Defense

- Implement parameterized queries or use an ORM that escapes inputs to prevent injection.
- Enforce rate limiting on login attempts to thwart brute force attacks.
- Monitor application logs for anomalous query patterns or repeated failed logins from the same IP.
- Validate and sanitize all user inputs in JSON payloads before processing.

## Objectives

1. Bypass authentication by injecting MongoDB queries to validate partial passwords.
2. Iteratively discover the full password character by character.
3. Gain unauthorized access to the target account and application.

## Instructions

### Step 1: Prepare the Environment

**Context**: Set up the Python script with the target details. Identify the login endpoint URL and the username to brute force. Ensure the 'requests' library is available for sending HTTP POST requests.

Install required libraries if needed:

```bash
pip install requests urllib3
```

> This step ensures the scripting environment is ready. Expected output: No errors during installation; libraries imported successfully when testing the script.

### Step 2: Configure and Run the Brute Force Script

**Context**: Use the provided script to send injected payloads. The script loops through printable characters, building the password prefix with regex '^prefix' to check for matches. It continues until the full password is guessed, indicated by a successful login response (e.g., 'OK' in response or 302 redirect).

**Code** ([[codes/MongoDB-Query-Injection-Brute-Force-Script]]):

Embed the script here or execute it directly in a Python interpreter.

> Run the script against the target. Monitor console output for discovered characters. Expected output: Progressive printing of password characters, e.g., "Found one more char : a", until the full password is built and login succeeds.

### Step 3: Verify Access and Extract Credentials

**Context**: Once the password is fully discovered, use it to log in normally and confirm access. This validates the brute force success and allows further exploitation.

Send a standard login request with the discovered credentials:

```python
import requests

payload = {'username': 'admin', 'password': 'full_discovered_password'}
r = requests.post('http://example.org/login', json=payload)
if r.status_code == 200 and 'OK' in r.text:
    print('Login successful')
```

> Expected output: Successful login response, such as a session token or dashboard redirect. If failed, review the script for injection issues or rate limiting.
