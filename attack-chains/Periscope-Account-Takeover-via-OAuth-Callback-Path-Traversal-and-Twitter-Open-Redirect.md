---
tags:
  - oauth
  - account-takeover
  - open-redirect
  - path-traversal
  - token-theft
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Mobile
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-Twitter-Credentials-from-Periscope-App]]'
  - '[[procedures/Generate-OAuth-Request-Token-with-Leaked-Credentials]]'
  - '[[procedures/Trick-Victim-into-Authorizing-OAuth-Request]]'
  - >-
    [[procedures/Bypass-OAuth-Callback-Locking-with-Path-Traversal-and-Open-Redirect]]
  - '[[procedures/Capture-OAuth-Token-and-Exchange-for-Access-Token]]'
step_count: 5
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:34.363Z'
description: >-
  A multi-stage attack exploiting insufficient OAuth callback validation in the
  Periscope mobile app combined with a Twitter open redirect to steal OAuth
  tokens and achieve full account takeover.
skill_level: intermediate
impact_level: high
id: ad5ac49d-bc12-4fc6-bef7-44052679ec1e
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Drive-by Compromise]]'
---
# Periscope Account Takeover via OAuth Callback Path Traversal and Twitter Open Redirect

Multi-stage attack chain demonstrating a complete attack workflow exploiting Periscope's OAuth misconfiguration and Twitter's open redirect to steal tokens and takeover linked accounts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Extract Credentials] --> B[Generate Request Token]
    B --> C[Victim Authorization]
    C --> D[Bypass Callback with Traversal & Redirect]
    D --> E[Capture & Exchange Token]
    E --> F[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Reverse engineering tools (e.g., APKTool, Jadx for Android app analysis)
- Twitter API access (using leaked credentials)
- Attacker-controlled domain for redirect fallback

### Target Environment

- Periscope mobile app (iOS/Android)
- Twitter web login (twitter.com)
- Services: Twitter OAuth API, Periscope API
- Tech stack: OAuth 1.0a, Mobile app embedding webviews

### Initial Access Requirements

- Access to Periscope app binary for reverse engineering
- Victim must have a Periscope account linked to Twitter and be logged in
- Social engineering to direct victim to authorization URL
- No prior credentials needed, but victim interaction required

## Detailed Attack Procedures

### Step 1: Extract Credentials
procedure: [[procedures/Extract-Twitter-Credentials-from-Periscope-App]]

**Objective**: Recover the embedded Twitter consumer key and secret from the Periscope app to initiate OAuth flows.

**Instructions**: Reverse engineer the Periscope mobile app binary to locate and deobfuscate the hardcoded Twitter API credentials. Use tools like APKTool to unpack the APK, then Jadx or similar to decompile and search for OAuth-related strings.

**Expected Output**: Twitter consumer key (e.g., a 25-character alphanumeric string) and consumer secret (e.g., a 50-character base64-like string).

**Success Indicators**:
- Credentials successfully extracted and validated by making a test API call to Twitter's request token endpoint.
- No errors in deobfuscation process.

### Step 2: Generate Request Token
procedure: [[procedures/Generate-OAuth-Request-Token-with-Leaked-Credentials]]

**Objective**: Use the leaked credentials to obtain an OAuth request token from Twitter's API, setting the stage for victim authorization.

**Instructions**: Construct an OAuth 1.0a signed request to Twitter's `/oauth/request_token` endpoint using the extracted consumer key and secret. Specify a callback URL that will be manipulated later (initially set to a partial path for traversal).

**Expected Output**: A request token and token secret returned in the API response (e.g., `oauth_token=ABC123&oauth_token_secret=XYZ789`).

**Success Indicators**:
- HTTP 200 response from Twitter API with valid request token.
- Token can be used to build the authorization URL.

### Step 3: Victim Authorization
procedure: [[procedures/Trick-Victim-into-Authorizing-OAuth-Request]]

**Objective**: Socially engineer the victim to visit and authorize the fake Periscope OAuth request, leveraging the app's 'Login with Twitter' feature.

**Instructions**: Craft an authorization URL using the request token, directing the victim to it via phishing email, SMS, or malicious link. If the victim is already logged into Periscope/Twitter, the app may auto-authorize without additional prompts.

**Expected Output**: Victim completes authorization, triggering the callback redirect with the oauth_verifier.

**Success Indicators**:
- Victim reports or is observed authorizing the request.
- Callback is initiated (monitored via network interception if possible).

### Step 4: Bypass Callback and Redirect
procedure: [[procedures/Bypass-OAuth-Callback-Locking-with-Path-Traversal-and-Open-Redirect]]

**Objective**: Evade Periscope's callback URL restrictions using path traversal to inject a Twitter open redirect, preserving the token in the URL fragment.

**Instructions**: In the initial request token generation, set the callback URL to a traversable path like `a/../../login?redirect_after_login=https://cards.twitter.com/card_id`, where `card_id` points to a Twitter card with fallback to `http://attacker.com`. Periscope's validation only checks protocols (blocking http/https) but allows partial paths, enabling traversal to prepend the scheme.

**Expected Output**: Redirect chain: Periscope → Twitter login → cards.twitter.com → attacker site with `#&oauth_token=...&oauth_verifier=...` in fragment.

**Success Indicators**:
- Redirect successfully bypasses Periscope checks.
- Token appears in attacker's site URL fragment.

### Step 5: Capture and Takeover
procedure: [[procedures/Capture-OAuth-Token-and-Exchange-for-Access-Token]]

**Objective**: Intercept the OAuth token from the redirect and exchange it for an access token to takeover the victim's Periscope account.

**Instructions**: On the attacker-controlled site, parse the URL fragment to extract `oauth_token` and `oauth_verifier`. Use these with the consumer credentials to request an access token from Twitter's `/oauth/access_token` endpoint. Then, authenticate to Periscope API with the access token to perform actions like renaming the account.

**Expected Output**: Access token and secret; successful API call to Periscope (e.g., account details or rename confirmation).

**Success Indicators**:
- Access token obtained without errors.
- Victim's account renamed or other changes applied stealthily.

## Attack Chain Summary

### Key Achievements

1. Extraction of embedded Twitter credentials from Periscope app via reverse engineering.
2. Bypassing OAuth callback locking using path traversal to chain with Twitter's open redirect.
3. Stealthy token theft via URL fragment on attacker site, leading to full Periscope account takeover.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
