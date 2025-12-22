---
tags:
  - csrf
  - oauth
  - shopify
  - pinterest
  - account-hijacking
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-05T12:00:00Z'
procedures:
  - '[[procedures/Verify-Victim-Pinterest-Connection]]'
  - '[[procedures/Initiate-Attacker-Pinterest-Connection]]'
  - '[[procedures/Authorize-Attacker-OAuth-Flow]]'
  - '[[procedures/Intercept-OAuth-Callback-URL]]'
  - '[[procedures/Trick-Victim-to-Load-Callback]]'
  - '[[procedures/Verify-Account-Replacement]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.690Z'
description: >-
  Exploits missing state parameter in Shopify's Pinterest OAuth flow to perform
  CSRF, allowing an attacker to replace the victim's connected Pinterest account
  with their own via a tricked callback load.
skill_level: intermediate
impact_level: high
id: 65790024-5fae-48df-ba08-f6af40eb1582
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# CSRF in Shopify Pinterest OAuth to Hijack Victim's Account Integration

Multi-stage attack chain demonstrating a complete CSRF exploitation in Shopify's Pinterest account connection feature, where the lack of a state parameter allows an attacker to hijack the victim's integration by tricking them into completing the OAuth callback in their session.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Verify Victim Setup] --> B[Attacker Initiates Connection]
    B --> C[Authorize Attacker OAuth]
    C --> D[Intercept Callback]
    D --> E[Trick Victim Load]
    E --> F[Account Replacement]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify store with admin access for victim and attacker
- Pinterest accounts for both
- Web browser and proxy tool for interception

### Initial Access Requirements

- Attacker must have their own Shopify store
- Victim must have an active Shopify store with Pinterest integration
- Ability to communicate with victim (e.g., via phishing link)

## Detailed Attack Procedures

### Step 1: Verify Victim Pinterest Connection
procedure: [[procedures/Verify-Victim-Pinterest-Connection]]

**Objective**: Confirm the victim has an existing Pinterest account connected to their Shopify store, setting up the integration to be hijacked.

**Instructions**: Log in to the victim's Shopify admin as an observer or assume prior knowledge. Navigate to the integrations section and check for active Pinterest connection. No specific commands needed; manual verification via UI.

**Expected Output**: Confirmation of existing Pinterest integration in victim's store settings.

**Success Indicators**:
- Victim's store shows connected Pinterest account
- Integration status is active

### Step 2: Initiate Attacker Pinterest Connection
procedure: [[procedures/Initiate-Attacker-Pinterest-Connection]]

**Objective**: Start the OAuth flow from the attacker's Shopify store to generate a valid authorization code.

**Instructions**: Log in to the attacker's Shopify admin. Navigate to Apps > Pinterest and click to connect a Pinterest account. This redirects to Pinterest's OAuth authorization page.

**Expected Output**: Redirect to Pinterest login/authorization page.

**Success Indicators**:
- OAuth initiation successful
- No prior connection exists on attacker's store

### Step 3: Authorize Attacker OAuth Flow
procedure: [[procedures/Authorize-Attacker-OAuth-Flow]]

**Objective**: Complete authorization on the attacker's side to obtain a fresh authorization code.

**Instructions**: On the Pinterest authorization page, log in with attacker's Pinterest credentials and grant permissions to Shopify. This triggers the callback redirect.

**Expected Output**: Attempted redirect to callback URL with code parameter.

**Success Indicators**:
- Permissions granted
- Authorization code generated

### Step 4: Intercept OAuth Callback URL
procedure: [[procedures/Intercept-OAuth-Callback-URL]]

**Objective**: Capture the full callback URL containing the authorization code without completing the flow.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy for the browser. During the redirect after authorization, intercept the request to https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=... and drop it to prevent completion, copying the full URL.

**Expected Output**: Captured URL like https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback?code=d0c18854a3359866774d479614081453d235962f.

**Success Indicators**:
- URL with valid code captured
- Request dropped, flow not completed on attacker side

### Step 5: Trick Victim to Load Callback
procedure: [[procedures/Trick-Victim-to-Load-Callback]]

**Objective**: Use social engineering to make the victim load the intercepted URL in their authenticated Shopify session.

**Instructions**: Craft a phishing email or link (e.g., disguised as a Shopify update) pointing to the captured callback URL. Ensure the victim is logged into their Shopify admin when clicking.

**Expected Output**: Victim's browser loads the URL, processing the code in their session.

**Success Indicators**:
- Victim visits the URL
- No CSRF token challenge due to missing state parameter

### Step 6: Verify Account Replacement
procedure: [[procedures/Verify-Account-Replacement]]

**Objective**: Confirm the victim's Pinterest integration now points to the attacker's account.

**Instructions**: After victim loads the URL, check the victim's Shopify integrations. The connected Pinterest account should now be the attacker's.

**Expected Output**: Victim's store settings show attacker's Pinterest account as connected, overriding the original.

**Success Indicators**:
- Original connection replaced
- Attacker gains control over victim's Pinterest integration

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF protection via missing OAuth state parameter
2. Hijacked victim's Pinterest integration without direct access
3. Enabled potential data exfiltration or control over victim's marketing integrations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-05T12:00:00Z*
