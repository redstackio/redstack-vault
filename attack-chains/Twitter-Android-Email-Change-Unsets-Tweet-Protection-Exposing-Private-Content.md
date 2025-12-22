---
id: ac-twitter-email-unprotect-001
tags:
  - privacy-violation
  - twitter
  - android
  - logic-error
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Log-In-to-Twitter-Android-App]]'
  - '[[procedures/Configure-Twitter-App-Link-Handling]]'
  - '[[procedures/Change-Email-Address-in-Twitter-App]]'
  - '[[procedures/Verify-Email-Change-and-Check-Exposure]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:45.339Z'
description: >-
  A logic error in the Twitter Android app that automatically disables tweet
  protection when changing the email address, leading to unintended public
  exposure of private tweets, potentially exploited via phishing.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.001]]'
---
# Twitter Android Email Change Unsets Tweet Protection Exposing Private Content

Multi-stage attack chain demonstrating a complete attack workflow exploiting a logic error in the Twitter Android app.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Protected Account] --> B[Configure App Link Handling]
    B --> C[Initiate Email Change]
    C --> D[Verify and Confirm Exposure]
    D --> E[Private Tweets Now Public]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Twitter Android app (latest version at time of discovery)
- Valid email address for change

### Target Environment

- Android mobile device
- Twitter service
- Protected Twitter account (tweets set to private)

### Initial Access Requirements

- Valid credentials for a protected Twitter account
- Physical access to Android device or remote access via phishing
- No special network position required; standard internet access

## Detailed Attack Procedures

### Step 1: Log In to Twitter Android App
procedure: [[procedures/Log-In-to-Twitter-Android-App]]

**Objective**: Authenticate to a protected Twitter account to access settings.

**Instructions**: Open the Twitter Android app and enter credentials for an account with 'Protect your Tweets' enabled.

**Expected Output**: Successful login with private tweet visibility restricted.

**Success Indicators**:
- Account dashboard loads with protected status visible in settings
- Tweets are not publicly searchable

### Step 2: Configure Twitter App Link Handling
procedure: [[procedures/Configure-Twitter-App-Link-Handling]]

**Objective**: Ensure the app handles twitter.com links internally to maintain session control.

**Instructions**: In Android settings, set the Twitter app as the default handler for twitter.com URLs.

**Expected Output**: Links to twitter.com open directly in the app.

**Success Indicators**:
- Test link opens in app without browser redirect
- Seamless navigation within app confirmed

### Step 3: Change Email Address in Twitter App
procedure: [[procedures/Change-Email-Address-in-Twitter-App]]

**Objective**: Trigger the logic error by initiating an email change, which unsets tweet protection.

**Instructions**: Navigate to Settings > Account > Email, enter a new valid email, and tap 'Next' to submit.

**Expected Output**: Email change initiated; 'Protect your Tweets' option automatically disabled without prompt.

**Success Indicators**:
- Confirmation screen shows email update in progress
- Settings reflect unprotected status immediately

### Step 4: Verify Email Change and Check Exposure
procedure: [[procedures/Verify-Email-Change-and-Check-Exposure]]

**Objective**: Complete the email verification and confirm private tweets are now public.

**Instructions**: Check the new email for verification link, tap it on the same device, then search for previously private tweets from another account or incognito browser.

**Expected Output**: Email verified; private tweets visible publicly.

**Success Indicators**:
- Verification successful
- Previously private tweets appear in public searches

## Attack Chain Summary

### Key Achievements

1. Bypassed user consent to unprotect tweets via email change logic flaw
2. Exposed private user content to public view
3. Demonstrated phishing potential to trick users into this action

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.001]] Phishing: Spearphishing Attachment (adapted for mobile app trickery)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
