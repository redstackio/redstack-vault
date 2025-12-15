---
tags:
  - idor
  - tiktok
  - ads
  - support-ticket
  - deletion
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-manipulate-draft-order-id]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-IDOR-in-TikTok-Support-Ticket-Deletion]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the TikTok ads platform's support ticket system, allowing
  unauthorized access and deletion of other users' tickets via the
  'draft_order_id' parameter.
skill_level: intermediate
impact_level: high
id: 2ac4f5b1-1907-490b-9be7-e4430e825922
created_at: '2025-12-14T17:25:48.234Z'
updated_at: '2025-12-14T17:25:48.234Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# IDOR in TikTok Ads Support Ticket System for Unauthorized Ticket Deletion

## Overview

This attack chain demonstrates the exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in the TikTok ads platform at ads.tiktok.com. The vulnerability resides in the support ticket system's 'draft_order_id' parameter, which lacks proper authorization checks. By manipulating this parameter with another user's ticket ID, an attacker can access and delete unauthorized support tickets. This disrupts customer support for victims and was reported via HackerOne (Report #1475520) with a severity of 7.5. The chain involves identifying the vulnerability and executing the deletion, requiring authenticated access to the platform.

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
    A[Initial Access] --> B[Exploit IDOR for Deletion]
    B --> C[Impact: Ticket Disruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for parameter manipulation

### Target Environment

- Web platform: ads.tiktok.com
- Required services: Support ticket system
- Network access: Internet connectivity with authenticated session

### Initial Access Requirements

- Valid authenticated account on TikTok Ads platform
- Knowledge of target user's ticket ID (e.g., via enumeration or guessing sequential IDs)
- No prior elevated privileges needed

## Detailed Attack Procedures

### Step 1: Exploit IDOR for Unauthorized Ticket Deletion
procedure: [[procedures/Exploit-IDOR-in-TikTok-Support-Ticket-Deletion]]

**Objective**: Manipulate the 'draft_order_id' parameter to access and delete another user's support ticket without authorization.

**Instructions**: Authenticate to ads.tiktok.com and navigate to the support ticket creation or management interface. Intercept the request using browser dev tools or a proxy. Identify the 'draft_order_id' parameter in the deletion endpoint. Replace it with a target ticket ID (e.g., obtained from other users or sequential guessing). Send the modified request to delete the ticket.

Use [[commands/curl-manipulate-draft-order-id]] to simulate the deletion request (adapt cookies and headers from your session):

```bash
curl -X POST 'https://ads.tiktok.com/support/ticket/delete' \
  -H 'Cookie: session_id=your_session; auth_token=your_token' \
  -H 'Content-Type: application/json' \
  -d '{"draft_order_id": "TARGET_TICKET_ID"}'
```

**Expected Output**: HTTP 200 response indicating successful deletion, or confirmation message in the UI that the ticket is removed.

**Success Indicators**:
- Ticket no longer visible in the system for the target user
- No error returned for unauthorized access
- Server-side confirmation of deletion

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to other users' support tickets via IDOR
2. Successful deletion of arbitrary tickets, disrupting support workflows
3. High-impact demonstration of broken object-level authorization

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data Destruction]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
