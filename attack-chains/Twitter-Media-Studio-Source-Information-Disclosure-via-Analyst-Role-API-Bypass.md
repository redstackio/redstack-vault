---
tags:
  - idor
  - information-disclosure
  - api-bypass
  - twitter-media-studio
  - access-control
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/twitter-ingest-list-get]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Add-Analyst-Account-to-Victim-Twitter-Media-Studio]]'
  - '[[procedures/Switch-to-Victim-Account-and-Verify-UI-Restrictions]]'
  - '[[procedures/Retrieve-Sensitive-Source-Information-via-API]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
description: >-
  Multi-stage attack exploiting inadequate API access controls in Twitter Media
  Studio, allowing an Analyst role user to disclose sensitive producer source
  details belonging to a victim account.
skill_level: intermediate
impact_level: high
id: b5013291-ed53-43ef-a6a0-cbc711f4aef2
created_at: '2025-12-14T17:25:13.102Z'
updated_at: '2025-12-14T17:25:13.102Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Twitter Media Studio Source Information Disclosure via Analyst Role API Bypass

Multi-stage attack chain demonstrating a complete attack workflow exploiting information disclosure and IDOR vulnerabilities in Twitter Media Studio.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Add Analyst Access] --> B[Switch and Verify UI] --> C[API Disclosure]
    C --> D[Exfiltrate Sources]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]

### Target Environment

- Web platform
- Twitter Media Studio service
- Analyst role credentials on victim account

### Initial Access Requirements

- Owner credentials for victim account (Account A)
- Analyst credentials (Account B)
- Network access to studio.twitter.com

## Detailed Attack Procedures

### Step 1: Add Analyst Access
procedure: [[procedures/Add-Analyst-Account-to-Victim-Twitter-Media-Studio]]

**Objective**: Grant Analyst role to the attacker's account on the victim's Twitter Media Studio account to establish initial access.

**Instructions**: Log in as the victim (Account A) and navigate to the account management page to add the analyst account (Account B).

**Expected Output**: Confirmation that Account B has been added with Analyst role.

**Success Indicators**:
- Analyst account listed in account users
- Role confirmed as Analyst

### Step 2: Switch to Victim Account and Verify UI Restrictions
procedure: [[procedures/Switch-to-Victim-Account-and-Verify-UI-Restrictions]]

**Objective**: Use analyst credentials to switch to the victim account and confirm UI-level restrictions on sensitive sections.

**Instructions**: Log in with analyst credentials (Account B), switch to the victim account, and check the producer page for hidden Sources section.

**Expected Output**: Sources section not visible in the UI.

**Success Indicators**:
- Successful account switch
- UI hides Sources section due to role limitations

### Step 3: Retrieve Source Information via API
procedure: [[procedures/Retrieve-Sensitive-Source-Information-via-API]]

**Objective**: Bypass UI restrictions by directly querying the API endpoint to disclose sensitive source details.

**Instructions**: Use [[commands/twitter-ingest-list-get]] with obtained parameters to fetch the ingest list:

```bash
curl -X GET "https://studio.twitter.com/1/live/ingest/list.json?account_id=ACCOUNT_ID&owner_id=OWNER_ID&user_id=USER_ID" -H "Authorization: Bearer TOKEN"
```

**Expected Output**: JSON response with source names, URLs, and keys.

**Success Indicators**:
- API returns sensitive source data
- Sources can be used for unauthorized broadcasts

## Attack Chain Summary

### Key Achievements

1. Bypassed UI restrictions using Analyst role
2. Disclosed victim source names, URLs, and keys via API
3. Enabled creation of unauthorized broadcasts with victim's sources

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01*
