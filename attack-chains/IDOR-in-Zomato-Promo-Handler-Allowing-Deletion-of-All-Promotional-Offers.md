---
id: d3d1f4aa-349c-493f-ae1a-ff1d6d446a68
name: IDOR in Zomato Promo Handler Allowing Deletion of All Promotional Offers
type: attack_chain
description: >-
  An Insecure Direct Object Reference vulnerability in Zomato's promo data
  handler enables unauthorized users to delete or deactivate any promotional
  offers platform-wide by manipulating POST request parameters.
verified: false
submitted: true
step_count: 1
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.139Z'
procedures:
  - '[[procedures/Exploit-IDOR-to-Delete-Promotional-Offers]]'
techniques:
  - '[[Account Discovery]]'
tactics:
  - '[[Discovery]]'
tags:
  - idor
  - web
  - php
  - access-control
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# IDOR in Zomato Promo Handler Allowing Deletion of All Promotional Offers

Multi-stage attack chain demonstrating a complete attack workflow targeting Zomato's promotional system via an IDOR vulnerability.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Exploit IDOR in Promo Handler] --> B[Delete or Deactivate Promos]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or proxy tool like Burp Suite for request manipulation

### Target Environment

- Web platform (PHP-based)
- Access to https://www.zomato.com
- Authenticated session as a Zomato user (e.g., merchant or partner with basic access)

### Initial Access Requirements

- Valid Zomato account credentials
- Network access to the internet
- No prior elevated privileges needed; basic authentication suffices due to IDOR

## Detailed Attack Procedures

### Step 1: Exploit IDOR to Access and Delete Promos
procedure: [[procedures/Exploit-IDOR-to-Delete-Promotional-Offers]]

**Objective**: Manipulate POST request parameters in the promoDataHandler.php endpoint to reference and delete promotional offers outside the user's authorized scope, disrupting platform-wide deals.

**Instructions**: Authenticate to Zomato and navigate to the promo management section. Intercept the POST request to /clients/promoDataHandler.php using a proxy. Modify the promo identifier parameter (e.g., 'promo_id') to target any promo ID, then submit a delete or deactivate action. Use [[commands/curl-idor-promo-delete]] to simulate the request:

```bash
curl -X POST -H "Cookie: session=your_session_cookie" -d "action=delete&promo_id=TARGET_PROMO_ID" https://www.zomato.com/clients/promoDataHandler.php
```

Repeat for multiple promo IDs to affect all offers.

**Expected Output**: Server response indicating successful deletion (e.g., JSON {"status":"success"}), and verification by checking the Zomato platform for removed promos.

**Success Indicators**:
- Promo offers disappear from the platform
- No authorization error in response
- Ability to target arbitrary promo IDs without ownership

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to any promotional offer data via IDOR
2. Deletion or deactivation of platform-wide promos, impacting business operations
3. Demonstration of missing authorization checks in PHP endpoint

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
