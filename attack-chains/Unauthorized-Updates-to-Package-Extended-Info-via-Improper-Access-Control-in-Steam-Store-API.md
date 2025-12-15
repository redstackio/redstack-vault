---
id: ac-uuid-001
name: >-
  Unauthorized Updates to Package Extended Info via Improper Access Control in
  Steam Store API
tags:
  - access-control-bypass
  - web-vulnerability
  - steam
  - valve
  - api-exploit
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Exploit-Improper-Access-Control-to-Update-Package-Extended-Info]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.273Z'
description: >-
  This attack chain exploits improper access control in the Steam Store's
  /store/ajaxpackagesave endpoint, allowing authenticated partners to
  unauthorizedly modify extended_info properties of their packages, enabling
  creation of special package types like externally-grantable ones with broader
  security implications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Updates to Package Extended Info via Improper Access Control in Steam Store API

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access control in Valve's Steam Store API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Partner Authentication] --> B[Unauthorized Property Update]
    B --> C[Special Package Creation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or API client (e.g., curl)

### Target Environment

- Steam Store web platform
- Access to partner account with package management permissions
- Network access to Steam API endpoints

### Initial Access Requirements

- Valid partner credentials for Steamworks
- Knowledge of package ID to target

## Detailed Attack Procedures

### Step 1: Exploit Access Control to Update Extended Info
procedure: [[procedures/Exploit-Improper-Access-Control-to-Update-Package-Extended-Info]]

**Objective**: Unauthorizedly modify the 'extended_info' properties of a package to create special types, such as externally-grantable packages, bypassing intended restrictions.

**Instructions**: Authenticate as a partner user, then use [[commands/curl-post-package-update]] to send a POST request to the /store/ajaxpackagesave endpoint with manipulated extended_info data. For example, set properties that enable external granting:

```bash
curl -X POST 'https://store.steampowered.com/store/ajaxpackagesave' \
  -H 'Cookie: steamLogin=partner_session_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'packageid=12345&extended_info={"type":"externally_grantable"}' \
  -v
```

Verify the response for success (e.g., no error and updated package reflected in partner dashboard).

**Expected Output**: HTTP 200 response with confirmation of package save, and subsequent API queries showing modified extended_info.

**Success Indicators**:
- No access denied error in response
- Package properties updated in Steamworks dashboard
- Ability to create or grant special package types

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to update restricted package properties
2. Enabled creation of externally-grantable packages
3. Demonstrated potential for chained security issues, such as unauthorized distribution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
