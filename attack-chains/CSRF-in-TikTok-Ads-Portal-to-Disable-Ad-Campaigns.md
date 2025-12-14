---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - csrf
  - web
  - ads
  - tiktok
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-CSRF-to-Disable-Ad-Campaigns]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.971Z'
description: >-
  A Cross-Site Request Forgery attack on the TikTok Ads Portal that allows an
  attacker to trick authenticated users into disabling their ad campaigns
  without consent.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# CSRF in TikTok Ads Portal to Disable Ad Campaigns

Multi-stage attack chain demonstrating a complete CSRF workflow to unauthorizedly disable ad campaigns in the TikTok Ads Portal.

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
    A[Trick User into Visiting Malicious Page] --> B[Forge Request to Disable Campaigns]
    B --> C[Campaigns Disabled Without Consent]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specific; uses standard web technologies (HTML/JS)

### Target Environment

- Web platform
- TikTok Ads Portal (authenticated session required)

### Initial Access Requirements

- Victim must be authenticated to TikTok Ads Portal
- Attacker needs a way to lure victim (e.g., phishing link)
- No prior network access beyond public web

## Detailed Attack Procedures

### Step 1: Prepare Malicious Page
procedure: [[procedures/Exploit-CSRF-to-Disable-Ad-Campaigns]]

**Objective**: Create a webpage that automatically submits a forged request to the vulnerable endpoint when visited by an authenticated user.

**Instructions**: Host a simple HTML page on an attacker-controlled server that includes an auto-submitting form targeting the TikTok Ads Portal's campaign disable endpoint. For example, use a form with hidden fields mimicking the disable action:

```html
<form action="https://ads.tiktok.com/campaign/disable" method="POST" id="csrf-form">
    <input type="hidden" name="campaign_id" value="TARGET_CAMPAIGN_ID">
    <input type="hidden" name="action" value="disable">
</form>
<script>document.getElementById('csrf-form').submit();</script>
```

Replace `TARGET_CAMPAIGN_ID` with the ID of the victim's campaign (if known via social engineering or prior recon).

**Expected Output**: The form submits silently upon page load.

**Success Indicators**:
- Page loads and form submits without user interaction
- No CSRF token validation blocks the request

### Step 2: Lure and Execute
procedure: [[procedures/Exploit-CSRF-to-Disable-Ad-Campaigns]]

**Objective**: Trick the authenticated user into visiting the malicious page, triggering the forged request and disabling campaigns.

**Instructions**: Distribute the malicious URL via phishing email, social media, or malicious link (e.g., "Check this urgent ad update: [malicious-link]"). When the victim clicks while logged into TikTok Ads Portal, the browser sends the forged POST request using the session cookies.

**Expected Output**: Ad campaigns are disabled on the victim's account.

**Success Indicators**:
- Victim's ad campaigns status changes to disabled
- No alerts or confirmations required due to missing protections

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication via session hijacking through CSRF
2. Performed unauthorized action (campaign disable) without direct access
3. Caused business disruption by halting ad campaigns

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
