---
id: proc-test-own-deletion
tags:
  - testing
  - web
  - idor
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-delete-own-draft]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.582Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Own-Draft-Deletion

## Summary

This procedure tests the draft deletion endpoint using a personal draft ID to verify that the mechanism functions correctly for authorized deletions, confirming the endpoint's behavior before exploitation.

## Description

The TopCoder wiki uses a GET parameter discardDraftId in the viewmydrafts.action endpoint for deletions. This step ensures the deletion works for owned drafts, highlighting the lack of robust checks that enables IDOR. Requires authentication and a known own draft ID.

## Requirements

1. Authenticated session with own draft ID
2. HTTP client for request submission
3. Access to the wiki URL

## Defense

Defensive measures and detection strategies:

- Server-side logging of deletion attempts
- Ownership verification before processing deletions

## Objectives

1. Confirm deletion of own draft
2. Validate endpoint response
3. Identify any error patterns

## Instructions

### Step 1: Submit Deletion Request for Own Draft

**Context**: Use the own draft ID in the parameter to test legitimate deletion.

**Command** ([[commands/curl-delete-own-draft]]):
```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=YOUR_OWN_DRAFT_ID" -H "Cookie: JSESSIONID=your_session"
```

> Submits the deletion request. Expected output: Redirect or confirmation page with the draft removed.

### Step 2: Verify Deletion

**Context**: Refresh the drafts page to confirm the draft is gone.

Use the access procedure command to re-fetch drafts and check absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-own-draft]]

## Tools Used


## Tags

- testing
- web
