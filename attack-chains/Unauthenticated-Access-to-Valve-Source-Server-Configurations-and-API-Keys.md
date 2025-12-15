---
tags:
  - information-disclosure
  - access-control
  - valve
  - srcds
  - api-keys
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Leaked-Valve-Server-Configurations]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.207Z'
description: >-
  A simple information disclosure attack exploiting insufficient access controls
  on Valve's public-facing endpoint to retrieve sensitive server configurations
  and API keys without authentication.
skill_level: beginner
impact_level: high
id: e67a76bc-8694-4625-8bed-d7b9c1f47107
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthenticated Access to Valve Source Server Configurations and API Keys

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-fetch-endpoint]]

### Target Environment

- Target Platform: Web
- Required Services: Source Dedicated Server (srcds)
- Network Access: Public internet access to https://srcds.valve.net

### Initial Access Requirements

- No credentials required
- Direct public access to the endpoint
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access Leaked Endpoint
procedure: [[procedures/Access-Leaked-Valve-Server-Configurations]]

**Objective**: Retrieve sensitive server configurations and API keys from the unauthenticated /find/ endpoint.

**Instructions**: Use [[commands/curl-fetch-endpoint]] to directly query the endpoint and capture the response containing leaked data:

```bash
curl https://srcds.valve.net/find/
```

**Expected Output**: JSON or text response exposing server configs, including API keys and configuration details for Source game servers.

**Success Indicators**:
- Response contains sensitive data such as API keys or server configurations
- No authentication prompt or error denying access

## Attack Chain Summary

### Key Achievements

1. Unauthenticated retrieval of high-value credentials and configs
2. Exposure of Source Dedicated Server (srcds) internal details
3. Potential for further exploitation of leaked API keys

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
