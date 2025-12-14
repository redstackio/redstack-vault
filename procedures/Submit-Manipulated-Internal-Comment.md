---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - parameter-tampering
  - authorization-bypass
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-post-manipulated-hackerone-comment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.372Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Submit-Manipulated-Internal-Comment

## Summary

This procedure exploits improper parameter validation in HackerOne's comment endpoint by appending a comma to the 'is_internal' value, tricking the backend into creating a public comment despite user restrictions.

## Description

Targeted at the comment submission form in HackerOne reports, this involves intercepting the POST request and modifying 'is_internal=' to 'is_internal=,', causing the backend to parse it as non-internal. This leads to minor privilege escalation, making internal-only comments visible to all participants. Prerequisites include a restricted session and access to a report.

## Requirements

1. Active session with restricted 'Post internal comments' permission
2. Access to report ID (e.g., 107329)
3. Browser dev tools or proxy for request interception; optionally curl for scripted testing
4. Knowledge of form parameters from the platform

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all input parameters server-side, rejecting malformed values like trailing commas
- Enforce strict permission checks independent of client-submitted flags
- Log and monitor anomalous comment creations from restricted users
- Implement input whitelisting for boolean-like parameters

## Objectives

1. Bypass internal comment restriction
2. Create a publicly visible comment
3. Demonstrate potential for sensitive data exposure

## Instructions

### Step 1: Intercept Comment Submission

**Context**: Prepare the request by opening the comment form on the target report and using dev tools to capture the POST.

No command; inspect network tab in browser.

> Expected output: Captured form data including 'is_internal=true' or similar.

### Step 2: Modify and Submit

**Context**: Tamper with the 'is_internal' parameter by appending a comma.

**Command** ([[commands/curl-post-manipulated-hackerone-comment]]):
```bash
curl -X POST 'https://hackerone.com/reports/107329/comments' \
  -H 'Cookie: your_session_cookie_here' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'message=test&substate=&is_internal=,&reference=&add_reporter_to_original=false&reply_action=add-comment&reports_count=1&report_ids%5B%5D=107329'
```

> This sends the manipulated POST; replace cookie with your session. Expected output: JSON response {"flash":"Comment was created successfully."} without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-manipulated-hackerone-comment]]

## Tools Used


## Tags

- [[parameter-tampering]]
- [[authorization-bypass]]

---
