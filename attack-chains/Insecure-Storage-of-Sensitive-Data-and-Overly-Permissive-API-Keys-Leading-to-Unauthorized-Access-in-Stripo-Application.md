---
tags:
  - insecure-storage
  - api-misconfiguration
  - sensitive-data-exposure
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Lateral Movement]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Overly-Permissive-API-Keys]]'
  - '[[procedures/Access-Unencrypted-Sensitive-Data-Storage]]'
step_count: 2
techniques:
  - '[[External Remote Services]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:10.800Z'
description: >-
  A vulnerability chain exploiting misconfigured API keys to gain unauthorized
  access to unencrypted sensitive data stored in the Stripo Inc application,
  potentially exposing user information.
skill_level: intermediate
impact_level: high
id: 4c074b33-2816-4a6c-bbb1-1a153a994b75
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[External Remote Services]]'
  - '[[Credentials In Files]]'
---
# Insecure Storage of Sensitive Data and Overly Permissive API Keys Leading to Unauthorized Access in Stripo Application

Multi-stage attack chain demonstrating exploitation of misconfigurations in Stripo Inc's web application, where overly permissive API keys allow unauthorized access to unencrypted sensitive data storage, leading to potential exposure of user information.

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
    A[API Key Exploitation] --> B[Data Storage Access]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web application platform (Stripo Inc)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the application's API endpoints

### Initial Access Requirements

- No prior credentials needed; relies on publicly accessible or leaked API keys
- Network position: External attacker
- Prior access needed: None, but knowledge of API endpoints

## Detailed Attack Procedures

### Step 1: Exploit Overly Permissive API Keys
procedure: [[procedures/Exploit-Overly-Permissive-API-Keys]]

**Objective**: Use misconfigured API keys to gain unauthorized access to application functionalities and resources.

**Instructions**: Identify and test the permissive API key by sending requests to the application's API endpoints using [[commands/curl-api-test]] to verify excessive permissions, such as listing user data or accessing internal resources.

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/resources
```

Then, enumerate available endpoints with broader access using [[commands/curl-api-enumerate]]:

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/endpoints
```

**Expected Output**: JSON response listing accessible resources or endpoints beyond intended scope.

**Success Indicators**:
- API responds with data not intended for the key's scope
- Access to restricted functionalities confirmed

### Step 2: Access Unencrypted Sensitive Data Storage
procedure: [[procedures/Access-Unencrypted-Sensitive-Data-Storage]]

**Objective**: Retrieve sensitive data from the application's storage, which lacks encryption, leading to direct exposure.

**Instructions**: Once API access is gained, query the storage endpoints for sensitive information using [[commands/curl-data-retrieve]] to fetch unencrypted data files or records.

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/storage/sensitive-data
```

Validate the data exposure by checking for plaintext sensitive fields using [[commands/curl-data-validate]]:

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/storage/user-info | jq '.data'
```

**Expected Output**: Plaintext sensitive data such as user credentials or personal information in JSON format.

**Success Indicators**:
- Retrieval of unencrypted sensitive data
- Confirmation of data exposure without decryption needed

## Attack Chain Summary

### Key Achievements

1. Gained unauthorized API access via permissive keys
2. Accessed and exfiltrated unencrypted sensitive data
3. Demonstrated medium-severity impact on data confidentiality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[External Remote Services]]
- [[Credentials In Files]]

### MITRE ATT&CK Tactics

- [[Lateral Movement]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
