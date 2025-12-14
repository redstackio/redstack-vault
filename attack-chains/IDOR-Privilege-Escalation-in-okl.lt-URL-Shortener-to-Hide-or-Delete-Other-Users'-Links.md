---
tags:
  - idor
  - privilege-escalation
  - web
  - url-shortener
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-inspect-link-endpoint]]'
  - '[[commands/curl-hide-link-idor]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-IDOR-in-Link-Management-Endpoints]]'
  - '[[procedures/Exploit-IDOR-to-Manipulate-Other-Users-Links]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  An authenticated attacker exploits an Insecure Direct Object Reference (IDOR)
  vulnerability in the okl.lt URL shortener's dashboard endpoints to hide or
  delete links belonging to other users, achieving privilege escalation and
  disrupting their access.
skill_level: intermediate
impact_level: high
id: 08d91765-4569-42a0-915b-5b49a91b8b3a
created_at: '2025-12-14T17:30:07.428Z'
updated_at: '2025-12-14T17:30:07.428Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR Privilege Escalation in okl.lt URL Shortener to Hide or Delete Other Users' Links

## Overview

This attack chain demonstrates a privilege escalation vulnerability in the okl.lt URL shortener service, where an authenticated user can exploit an IDOR flaw in the dashboard's link management endpoints. By directly referencing user IDs without proper authorization checks, an attacker can hide or delete other users' shortened links from their dashboards, disrupting access and visibility while the links themselves remain functional externally. The attack requires an authenticated account and was discovered through manual testing of API endpoints.

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
    A[Discovery of IDOR] --> B[Exploitation]
    B --> C[Disruption of User Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for request inspection

### Target Environment

- Web platform
- okl.lt URL shortener service
- Authenticated access to dashboard

### Initial Access Requirements

- Valid authenticated account on okl.lt
- Knowledge of target user's ID (e.g., via enumeration or known values)
- Network access to the web application

## Detailed Attack Procedures

### Step 1: Discover IDOR in Link Management
procedure: [[procedures/Discover-IDOR-in-Link-Management-Endpoints]]

**Objective**: Identify the lack of authorization checks in link management endpoints by inspecting requests and testing with modified parameters.

**Instructions**: Log in to the okl.lt dashboard and create a test shortened link. Use browser developer tools to inspect the network requests for hiding or deleting links. Alternatively, use [[commands/curl-inspect-link-endpoint]] to replicate a legitimate hide request:

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id": "YOUR_LINK_ID", "user_id": "YOUR_USER_ID"}'
```

Modify the `user_id` parameter to a different value and resend the request to test for IDOR. Observe if the endpoint processes the request without ownership validation.

**Expected Output**: Successful response indicating the link is hidden, even for non-owned links.

**Success Indicators**:
- Endpoint accepts requests with altered user IDs without error
- Link status changes in the dashboard for the target user

### Step 2: Exploit IDOR to Hide or Delete Links
procedure: [[procedures/Exploit-IDOR-to-Manipulate-Other-Users-Links]]

**Objective**: Target and manipulate other users' links by sending crafted requests with their user IDs to hide or delete entries from their dashboards.

**Instructions**: Obtain the target user's ID (e.g., through prior enumeration or dashboard inspection). Use [[commands/curl-hide-link-idor]] to send a hide request for a specific link owned by the target:

```bash
curl -X POST 'https://okl.lt/api/hide-link' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"link_id": "TARGET_LINK_ID", "user_id": "TARGET_USER_ID"}'
```

For deletion, adapt to the delete endpoint (e.g., `/api/delete-link`) with similar parameters. Repeat for multiple links to fully disrupt the target's dashboard.

**Expected Output**: API response confirming the action (e.g., 200 OK with success message), and verification by logging in as the target (if possible) shows missing links.

**Success Indicators**:
- Target links are hidden or deleted from the victim's dashboard
- No errors related to authorization in API responses

## Attack Chain Summary

### Key Achievements

1. Identified IDOR in link management without ownership checks
2. Achieved privilege escalation to manipulate other users' dashboard content
3. Disrupted user experience by removing access to shortened links in the UI

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2024-01-01T00:00:00Z*
