---
tags:
  - idor
  - unauthenticated-access
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-conversations-view]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.627Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b87e140d-2fcf-4b1d-9aa7-8ee96e858372
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Access-Conversation-via-IDOR-as-Unauthenticated-User

## Summary

This procedure exploits the IDOR vulnerability in the Concrete CMS conversations endpoint by sending an unauthenticated POST request with a specific cnvID, retrieving restricted comment data including PII without authorization checks.

## Description

The /index.php/tools/required/conversations/view_ajax endpoint in Concrete CMS 5.7.5.7 directly uses the cnvID parameter from POST requests without verifying user permissions or authentication. An unauthenticated attacker can supply any integer cnvID to access the corresponding conversation object, bypassing restrictions on administrator-only pages. This leads to disclosure of sensitive comment content. The procedure assumes a known cnvID from prior setup or enumeration.

## Requirements

1. Network access to the target Concrete CMS instance
2. Knowledge of a valid cnvID (e.g., from setup or guessing low integers)
3. HTTP client like curl for POST requests

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all object references (e.g., verify user permissions against the conversation owner)
- Rate-limit requests to the conversations endpoint to prevent enumeration
- Log all access to conversation objects and alert on unauthenticated attempts

## Objectives

1. Gain unauthorized access to a specific restricted comment
2. Confirm lack of authentication and permission enforcement
3. Extract sensitive data like PII from the response

## Instructions

### Step 1: Prepare Unauthenticated Request

**Context**: Ensure no session cookies or auth headers are sent to simulate an unauthenticated user.

Identify the target URL: http://target.com/index.php/tools/required/conversations/view_ajax.

### Step 2: Send POST Request with cnvID

**Context**: Use the known cnvID to fetch the conversation data.

**Command** ([[commands/curl-post-conversations-view]]):
```bash
curl -X POST 'http://target.com/index.php/tools/required/conversations/view_ajax' -d 'cnvID=1'
```

> This command sends a POST request with cnvID=1. Expected output is JSON or HTML containing the comment text, including any PII, without errors.

**Expected Output**: Response body with comment details, e.g., {"comment": "Test PII: user@example.com"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-conversations-view]]

## Tools Used


## Tags

- [[idor]]
- [[unauthenticated-access]]
- [[concrete-cms]]
