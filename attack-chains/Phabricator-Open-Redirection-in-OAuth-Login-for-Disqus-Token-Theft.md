---
tags:
  - open-redirect
  - oauth
  - phishing
  - token-theft
  - phabricator
type: attack_chain
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Launch-Incognito-Session-in-Browser]]'
  - '[[procedures/Open-Crafted-Vulnerable-OAuth-URL]]'
  - '[[procedures/Initiate-OAuth-Login-with-Provider]]'
  - '[[procedures/Complete-Authentication-and-Follow-Redirection]]'
step_count: 4
techniques:
  - '[[T1566.002]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.083Z'
description: >-
  A phishing attack exploiting an open redirection vulnerability in
  Phabricator's OAuth login flow to steal Disqus access tokens by redirecting
  authenticated users to a malicious site.
skill_level: intermediate
impact_level: high
id: 93917128-a842-456b-9190-ed9f2099847a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Drive-by Compromise]]'
---
# Phabricator Open Redirection in OAuth Login for Disqus Token Theft

Multi-stage attack chain demonstrating a phishing workflow that exploits an open redirection vulnerability in Phabricator's OAuth login on secure.phabricator.com to steal Disqus access tokens.

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
    A[Prepare Clean Session] --> B[Access Phishing Link]
    B --> C[Initiate OAuth Login]
    C --> D[Authenticate and Redirect to Malicious Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Chrome]]

### Target Environment

- Web platform
- OAuth services (Disqus, Facebook)
- Phabricator instance (PHP-based)

### Initial Access Requirements

- Valid Disqus or Facebook account for testing
- Access to a crafted phishing URL exploiting the redirect
- No prior credentials needed for Phabricator

## Detailed Attack Procedures

### Step 1: Prepare Clean Session
procedure: [[procedures/Launch-Incognito-Session-in-Browser]]

**Objective**: Simulate a fresh user session without cached data to mimic a real phishing victim.

**Instructions**: Launch Google Chrome in incognito mode to ensure no existing cookies or sessions interfere with the OAuth flow.

**Expected Output**: A new incognito window ready for navigation.

**Success Indicators**:
- Incognito window opens without prior Phabricator session
- No cached login state present

### Step 2: Access Phishing Link
procedure: [[procedures/Open-Crafted-Vulnerable-OAuth-URL]]

**Objective**: Direct the victim to the vulnerable OAuth endpoint using a specially crafted URL that bypasses redirect validation.

**Instructions**: Obtain the crafted URL from the source (e.g., https://www.dropbox.com/s/e8r08b52hawc65c/OAuth.txt) which uses backslashes to replace forward slashes in the redirect parameter, then paste and navigate to it in the incognito window.

**Expected Output**: The Phabricator login page loads with the manipulated redirect parameter.

**Success Indicators**:
- Login page appears without errors
- URL bar shows the crafted redirect parameter

### Step 3: Initiate OAuth Login
procedure: [[procedures/Initiate-OAuth-Login-with-Provider]]

**Objective**: Trick the user into selecting an OAuth provider to begin the authentication process.

**Instructions**: On the loaded login page, select an OAuth provider such as Disqus to proceed with external authentication.

**Expected Output**: Redirection to the OAuth provider's login page (e.g., Disqus).

**Success Indicators**:
- OAuth provider selection works
- User is prompted for credentials on the provider site

### Step 4: Authenticate and Redirect
procedure: [[procedures/Complete-Authentication-and-Follow-Redirection]]

**Objective**: Complete login to trigger the open redirect, sending the user to a malicious site where tokens can be intercepted.

**Instructions**: Enter credentials on the OAuth provider site and authorize the app, observing the post-authentication redirect.

**Expected Output**: After approval, the browser redirects to the attacker-controlled malicious website instead of Phabricator.

**Success Indicators**:
- Successful OAuth approval
- Redirection to arbitrary malicious domain
- Potential capture of Disqus access token on the malicious site

## Attack Chain Summary

### Key Achievements

1. Bypassed Phabricator's redirect validation using backslash manipulation
2. Enabled phishing via OAuth flow to steal Disqus tokens
3. Demonstrated impact on secure.phabricator.com without affecting Facebook tokens

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T12:00:00Z*
