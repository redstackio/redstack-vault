---
id: proc-uuid-2
tags:
  - privilege-escalation
  - data-manipulation
  - dust-app
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/post-dust-app-secrets]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:46.836Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
---
---

# Overwrite-or-Create-Secrets-as-Builder-User

## Summary

This procedure demonstrates privilege escalation by allowing Builder users to create new secrets or overwrite existing ones in Dust's secret management via unprotected POST requests, enabling tampering with app configurations and injection of malicious values like compromised API keys.

## Description

The POST endpoint at /api/w/[workspace_id]/dust_app_secrets in Dust lacks validation for Builder role permissions, which should not allow modifications. An authenticated Builder can send JSON payloads with 'name' and 'value' to silently overwrite existing secrets or create new ones. This can lead to supply chain attacks by altering secrets used in apps, compromising accounts, or exfiltrating data. Prerequisites include a valid Builder session and workspace_id; the operation succeeds without warnings.

## Requirements

1. Valid Builder role authentication and appSession cookie
2. Target workspace_id and a secret name (from enumeration)
3. HTTP client like curl
4. Malicious value to inject (e.g., attacker-controlled API key)

## Defense

Defensive measures and detection strategies:

- Enforce strict RBAC on POST operations, limiting modifications to Admin roles only
- Audit and alert on all secret creation/overwrite events, correlating with user roles
- Implement secret versioning and immutable references to detect tampering

## Objectives

1. Tamper with existing secrets to inject malicious configurations
2. Create new secrets for persistence or escalation
3. Compromise apps relying on modified secrets, enabling further attacks

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Select a target secret name (e.g., from enumeration) and craft a JSON body with a malicious value.

Ensure headers include Host, Content-Type, and Cookie.

### Step 2: Send POST Request to Modify Secret

**Context**: Execute the POST to overwrite or create, exploiting the lack of checks.

**Command** ([[commands/post-dust-app-secrets]]):
```bash
curl -X POST "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" \
  -H "Host: dust.tt" \
  -H "Content-Type: application/json" \
  -H "Cookie: [appSession]" \
  -d '{"name":"API_KEY","value":"malicious-value"}'
```

> Command sends the payload. Expected output: 200 OK with no body or error, indicating success. If the name exists, it overwrites silently; otherwise, creates new.

### Step 3: Verify Modification

**Context**: Confirm the change by re-enumerating secrets.

**Command** ([[commands/get-dust-app-secrets]]):
```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]" | jq '.secrets[] | select(.name == "API_KEY") .value'
```

> Should show masked "•••••••" for the updated secret, confirming tampering without direct value exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/post-dust-app-secrets]]
- [[commands/get-dust-app-secrets]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[data-manipulation]]
- [[dust-app]]
