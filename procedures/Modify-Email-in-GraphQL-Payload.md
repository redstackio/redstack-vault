---
id: proc-modify-graphql-email-001
tags:
  - email-hijack
  - payload-modification
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.860Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: proc-modify-graphql-email-001
name: Modify-Email-in-GraphQL-Payload
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]]
techniques: [[Valid Accounts]], [[Exploit Public-Facing Application]]
sub_techniques: []
tags: email-hijack, payload-modification
commands: []
platforms: Web
tools: [[tools/Browser-Developer-Tools]]
skill_level: intermediate
impact_level: high
detection_risk: medium
---

# Modify-Email-in-GraphQL-Payload

## Summary

This procedure modifies the captured StaffMemberUpdate GraphQL payload to change the target account's email to the attacker's Google Apps email, exploiting lack of authorization checks.

## Description

The GraphQL mutation allows updating the 'email' variable without verifying the updater's permissions over the target. By editing the payload in the CURL export, the attacker sets it to their own Google Apps email from the domain, enabling subsequent linkage. This works on staff or owners without existing Google links and can be chained with XSS for owner escalation.

## Requirements

1. Captured CURL from StaffMemberUpdate mutation
2. Attacker's Google Apps email (must match store's domain)
3. Terminal or tool to execute modified CURL (e.g., curl command)

## Defense

Defensive measures and detection strategies:

- Add authorization checks in GraphQL resolvers for email updates
- Validate that only owners or self can modify emails
- Audit logs for email changes not initiated via UI

## Objectives

1. Successfully update victim's email to attacker's
2. Avoid detection by mimicking legitimate requests
3. Prepare for Google linkage

## Instructions

### Step 1: Paste CURL into Editor

**Context**: Load the captured request for editing.

Copy the CURL command into a text editor or terminal.

### Step 2: Locate and Edit Email Variable

**Context**: Identify the 'email' field in the JSON payload.

In the --data-raw section, find the variables object and change the "email" value to the attacker's Google Apps email, e.g., "attacker@store-domain.com".

### Step 3: Execute Modified Request

**Context**: Replay the altered payload to the endpoint.

Run the edited CURL command in a terminal:

```bash
curl 'https://pos-channel.shopifycloud.com/graphql-proxy/admin' \
  -H 'Authorization: Bearer <token>' \
  --data-raw '{ "query": "mutation StaffMemberUpdate(...) { ... }", "variables": { "input": { "email": "attacker@store-domain.com" } } }'
```

**Expected Output**: JSON response with "data.staffMemberUpdate.staffMember.email" updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- graphql-modify
- email-update
- shopify
