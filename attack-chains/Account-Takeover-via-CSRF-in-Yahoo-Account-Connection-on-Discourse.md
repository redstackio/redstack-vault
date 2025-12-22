---
tags:
  - csrf
  - account-takeover
  - discourse
  - yahoo
  - openid
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Initiate-Yahoo-Account-Connection]]'
  - '[[procedures/Intercept-and-Capture-Callback-Request]]'
  - '[[procedures/Craft-and-Deliver-CSRF-Payload]]'
  - '[[procedures/Verify-Account-Takeover]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
description: >-
  Exploits lack of CSRF protection in Discourse's Yahoo account connection
  workflow to force victim account linkage to attacker's Yahoo credentials,
  enabling full takeover.
skill_level: intermediate
impact_level: high
id: 5c4ba837-9ad7-4cc5-8b71-dc0bbd63b534
created_at: '2025-12-14T17:33:24.599Z'
updated_at: '2025-12-14T17:33:24.599Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
# Account Takeover via CSRF in Yahoo Account Connection on Discourse

Multi-stage attack chain demonstrating a complete attack workflow exploiting CSRF in the Yahoo account connection on try.discourse.org, leading to full victim account takeover by linking it to the attacker's Yahoo credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Connection] --> B[Intercept Callback]
    B --> C[Deliver CSRF]
    C --> D[Takeover Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Discourse instance like try.discourse.org)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Attacker must have browser access to the target site

### Initial Access Requirements

- No prior credentials needed for discovery, but attacker needs a Yahoo account
- Victim must be authenticated on Discourse
- Network position: Direct internet access to try.discourse.org

## Detailed Attack Procedures

### Step 1: Initiate Yahoo Account Connection
procedure: [[procedures/Initiate-Yahoo-Account-Connection]]

**Objective**: Start the Yahoo authentication workflow to prepare for interception of the vulnerable callback.

**Instructions**: Navigate to the account preferences page on the target Discourse instance and trigger the Yahoo connection process.

**Expected Output**: Authentication workflow begins, redirecting to Yahoo for login.

**Success Indicators**:
- Access to preferences page loaded
- 'Connect Yahoo account' option visible and clickable

### Step 2: Intercept and Capture Callback Request
procedure: [[procedures/Intercept-and-Capture-Callback-Request]]

**Objective**: Use Burp Suite to capture the vulnerable GET callback request containing the Yahoo auth token.

**Instructions**: Enable Burp interceptor, complete the Yahoo login, and forward requests until the /auth/yahoo/callback is intercepted. Copy the request details including OpenID parameters and the auth token, then drop the request to prevent completion on attacker's side.

**Expected Output**: Full HTTP GET request captured with parameters like openid.claimed_id, openid.ax.value.email, and the auth token.

**Success Indicators**:
- Callback request intercepted in Burp Suite
- Auth token extracted and saved

### Step 3: Craft and Deliver CSRF Payload
procedure: [[procedures/Craft-and-Deliver-CSRF-Payload]]

**Objective**: Modify the captured request into a deliverable form (URL or HTML form) and trick the victim into processing it while authenticated.

**Instructions**: Transform the GET request into an HTML form or direct URL with the captured parameters. Deliver to the victim via phishing or malicious link, ensuring they are logged into Discourse.

**Expected Output**: Victim visits the URL/form, sees 'authentication complete', and is redirected to /?authComplete=true.

**Success Indicators**:
- Victim account connects to attacker's Yahoo
- No CSRF token validation blocks the request

### Step 4: Verify Account Takeover
procedure: [[procedures/Verify-Account-Takeover]]

**Objective**: Confirm the linkage by logging in with Yahoo and accessing the victim's account.

**Instructions**: Attempt login to Discourse using the attacker's Yahoo account, follow redirects, and navigate to the main site to check control over the victim's profile.

**Expected Output**: Successful login and access to victim's Discourse account.

**Success Indicators**:
- Redirect to /auth/yahoo/null after login
- Full access to victim's posts, settings, and actions

## Attack Chain Summary

### Key Achievements

1. Captured Yahoo auth token via intercepted callback
2. Forced victim account connection without CSRF protection
3. Achieved full account takeover on Discourse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Credential Access]]

---
*Last updated: 2023-10-01*
