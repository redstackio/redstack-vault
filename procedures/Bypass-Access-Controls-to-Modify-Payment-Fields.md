---
id: proc-bypass-access-001
tags:
  - access-control-bypass
  - improper-authorization
  - api-modification
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/patch-payment-method-xss-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-13T23:55:38.327Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass Access Controls to Modify Payment Fields

## Summary

This procedure exploits insufficient access controls in the 8x8 API to unauthorizedly modify fields like isPrimary and savePaymentMethod via the patch endpoint.

## Description

The /api/patchPaymentMethod/ID endpoint lacks proper authorization checks, allowing authenticated users to alter fields they shouldn't, such as setting another method as primary or enabling saves without ownership verification.

## Requirements

1. Authenticated session
2. Knowledge of target payment method IDs
3. Ability to craft JSON payloads for field updates

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on all API mutations
- Validate user ownership of resources before updates
- Audit logs for field changes and alert on anomalies

## Objectives

1. Modify unauthorized payment attributes
2. Demonstrate privilege escalation potential
3. Highlight broken object-level authorization

## Instructions

### Step 1: Identify Target Fields

**Context**: From code analysis, note fields like isPrimary and savePaymentMethod.

No command; review API docs or prior analysis.

> Fields are updatable without checks.

### Step 2: Send Modification Request

**Context**: Use a similar PATCH request to update the fields.

**Command** ([[commands/patch-payment-method-xss-injection]] adapted):
```bash
curl -X POST https://example.8x8.com/api/patchPaymentMethod/ID \
  -H "Content-Type: application/json" \
  -H "Cookie: [session]" \
  -d '{"isPrimary": true, "savePaymentMethod": true}'
```

> Request succeeds, altering the fields without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/patch-payment-method-xss-injection]]

## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[access-control-bypass]]
- [[improper-authorization]]
