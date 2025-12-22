---
tags:
  - auth-bypass
  - parameter-tampering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-invite-with-coc-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.623Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c4b8db25-d8bc-4686-b1c4-e1fc6a19739d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Invite-Validation-with-coc-Parameter

## Summary

This procedure exploits a client-side validation flaw in the Gratipay Slack invite system by tampering with the 'coc' parameter in the POST request, allowing duplicate or unauthorized invites to proceed without checks.

## Description

The vulnerability occurs in the /invite endpoint on gratipay-slackin.herokuapp.com, where client-side JavaScript prevents resending invites by checking a 'coc' flag. By inspecting network requests from inside.gratipay.com/appendices/chat and setting 'coc' to 1 in the JSON payload, the server-side logic is bypassed, enabling forced processing. This is an improper authentication issue, as the server does not re-validate the parameter, leading to unintended invite sending. The target environment is a web application hosted on Heroku using Express and Cowboy servers, integrated with Slack.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome DevTools) or a proxy like Burp Suite
2. Public access to inside.gratipay.com/appendices/chat
3. Ability to craft and send custom HTTP POST requests

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all parameters, ignoring client-set flags like 'coc'
- Rate-limit invite requests per IP or email to prevent spam
- Monitor for anomalous 400 responses followed by invite emails in Slack logs

## Objectives

1. Bypass client-side duplicate invite prevention
2. Force the server to process unauthorized invite requests
3. Enable subsequent spam or enumeration attacks

## Instructions

### Step 1: Inspect Normal Invite Request

**Context**: Load the chat appendices page and attempt a legitimate invite to capture the baseline request structure.

Navigate to inside.gratipay.com/appendices/chat, enter an email, and submit. In DevTools Network tab, locate the POST to /invite and note the JSON payload with 'coc' likely set to 0.

**Expected Output**: Baseline request visible, e.g., {"coc":0,"email":"legit@example.com"}.

### Step 2: Modify and Send Tampered Request

**Context**: Alter the 'coc' value to 1 to bypass validation and send to an arbitrary email.

**Command** ([[commands/curl-post-invite-with-coc-bypass]]):
```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"test@example.com"}'
```

> This command sends the tampered payload. Expected output: HTTP/1.1 400 Bad Request with JSON {'msg':'You have already been invited to Slack. Check for an email from feedback@slack.com.'}, but validation is bypassed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-invite-with-coc-bypass]]

## Tools Used


## Tags

- auth-bypass
- parameter-tampering
- web-exploit
