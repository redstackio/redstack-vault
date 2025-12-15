---
id: ac-uuid-001
tags:
  - oauth
  - twitter
  - account-takeover
  - phishing
  - auth-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Twitter-OAuth-Flow-as-Attacker]]'
  - '[[procedures/Extract-Twitter-OAuth-Authenticate-URL]]'
  - '[[procedures/Phish-Victim-to-Authorize-OAuth-Token]]'
  - '[[procedures/Complete-OAuth-Flow-to-Hijack-Access]]'
  - '[[procedures/Perform-Actions-on-Hijacked-Account]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:35.387Z'
description: >-
  A multi-stage attack exploiting Twitter's OAuth implementation flaw to hijack
  a victim's account access on third-party applications via shared request
  tokens.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Phishing]]'
---
# Twitter OAuth Request Token Hijacking for Third-Party Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an improper OAuth token binding in Twitter's authentication flow, allowing an attacker to hijack a victim's account on third-party services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate OAuth Flow] --> B[Extract Auth URL]
    B --> C[Victim Authorization]
    C --> D[Complete Flow]
    D --> E[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based)

### Target Environment

- Web platform with Twitter OAuth integration (e.g., unfollowerstats.com)
- Required services: Twitter API, OAuth 1.0
- Network access: Internet connectivity

### Initial Access Requirements

- Attacker Twitter account
- Victim Twitter account
- Social engineering capability to share URL with victim

## Detailed Attack Procedures

### Step 1: Initiate OAuth Flow
procedure: [[procedures/Initiate-Twitter-OAuth-Flow-as-Attacker]]

**Objective**: Start the OAuth authorization process on the third-party site using the attacker's Twitter account to generate a request token.

**Instructions**: Log in to your Twitter account (e.g., TwitterAccount01) in a web browser. Navigate to a vulnerable third-party site like unfollowerstats.com, which will redirect to Twitter's OAuth endpoint (https://api.twitter.com/oauth/authorize) to generate a unique oauth_token.

**Expected Output**: Redirection to Twitter's authorization page with a generated oauth_token.

**Success Indicators**:
- OAuth token generated
- Authorization page loaded

### Step 2: Extract Authenticate URL
procedure: [[procedures/Extract-Twitter-OAuth-Authenticate-URL]]

**Objective**: Capture the OAuth authenticate URL containing the request token for sharing with the victim.

**Instructions**: From the third-party site's callback or authorization page, copy the full authenticate URL, which includes the oauth_token parameter (e.g., https://api.twitter.com/oauth/authenticate?oauth_token=xpXP21WOzwvsocu7yjQBafl8BKRtKdeH).

**Expected Output**: A URL string with the embedded oauth_token.

**Success Indicators**:
- URL extracted successfully
- Token visible in URL

### Step 3: Phish Victim to Authorize
procedure: [[procedures/Phish-Victim-to-Authorize-OAuth-Token]]

**Objective**: Trick the victim into authorizing the shared OAuth token with their own Twitter account, binding it to their credentials.

**Instructions**: Share the extracted URL with the victim (e.g., via email or message) while they are logged into their Twitter account (e.g., TwitterAccount02). Instruct them to open the link and authorize the app; they will log in if needed and grant permissions, completing authorization on their end.

**Expected Output**: Victim sees Twitter login/authorization screen and approves the app.

**Success Indicators**:
- Victim authorizes the token
- Third-party app permissions granted by victim

### Step 4: Complete OAuth Flow
procedure: [[procedures/Complete-OAuth-Flow-to-Hijack-Access]]

**Objective**: Return to the original browser session to claim the access token now bound to the victim's account due to the shared token flaw.

**Instructions**: In the attacker's original browser session (still open on unfollowerstats.com and logged in as TwitterAccount01), refresh the page or resume the OAuth flow. The site will detect the pre-authorized token and issue an access token tied to the victim's account, logging the attacker into the victim's dashboard.

**Expected Output**: Attacker gains access to the victim's account dashboard on the third-party app.

**Success Indicators**:
- Login as victim without their credentials
- Victim's data visible

### Step 5: Perform Actions on Account
procedure: [[procedures/Perform-Actions-on-Hijacked-Account]]

**Objective**: Use the hijacked access to execute actions on the victim's Twitter account via the third-party app.

**Instructions**: From the hijacked dashboard, perform actions such as viewing followers, posting tweets, or following/unfollowing users, all executed with the victim's Twitter credentials through the app's API integration.

**Expected Output**: Successful execution of victim-authorized actions (e.g., new tweet posted).

**Success Indicators**:
- Actions completed on victim's behalf
- No additional authentication required

## Attack Chain Summary

### Key Achievements

1. Generated and shared OAuth request token
2. Induced victim authorization for token hijacking
3. Achieved account takeover on third-party app
4. Performed unauthorized actions on victim's Twitter

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2024-10-01T00:00:00Z*
