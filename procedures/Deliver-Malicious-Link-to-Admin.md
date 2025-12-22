---
id: proc-expressionengine-phish-delivery
tags:
  - phishing
  - social-engineering
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T03:15:47.211Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Deliver-Malicious-Link-to-Admin

## Summary

This procedure uses social engineering to deliver a crafted URL containing a Base64-encoded SQL query to an authenticated ExpressionEngine admin, executing the query in their session for data extraction.

## Description

By tricking the admin into clicking a phishing link, the attack leverages their session to run arbitrary SQL via the unvalidated `thequery` parameter. This is effective in web environments where admins have database access, leading to unauthorized data reads without direct authentication bypass.

## Requirements

1. Target admin's contact info (email, chat)
2. Crafted URL from prior procedure
3. No technical tools beyond email client
4. Admin must be logged in to ExpressionEngine

## Defense

Defensive measures and detection strategies:

- Train admins on phishing recognition and link verification
- Implement URL allowlisting in admin interfaces
- Log and alert on unusual utility/query accesses
- Use multi-factor for admin sessions

## Objectives

1. Convince admin to access malicious URL
2. Execute SQL in admin context
3. Observe data extraction

## Instructions

### Step 1: Prepare Phishing Message

**Context**: Craft a convincing pretext to get the admin to click.

**Command** ([[No specific command]]):

Email: "Urgent: Review this query log - http://target.com/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw=="

> Use social engineering to build trust.

### Step 2: Verify Execution

**Context**: Test the link yourself if possible, or monitor for admin response.

**Command** ([[commands/curl-send-query]]):
```bash
curl "http://target.com/admin.php?/cp/utilities/query/run-query&thequery=c2VsZWN0ICogZnJvbSBleHBfbWVtYmVycw==" -v
```

> Expected: Response with query results if authenticated; check for member data dump.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used

- [[commands/curl-send-query]]

## Tools Used


## Tags

- phishing
- social-engineering
