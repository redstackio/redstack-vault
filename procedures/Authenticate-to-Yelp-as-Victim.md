---
id: proc-yelp-auth-001
tags:
  - authentication
  - web
  - yelp
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[User Execution]]'
updated_at: '2025-12-14T17:28:51.954Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Authenticate-to-Yelp-as-Victim

## Summary

This procedure simulates logging into a victim's Yelp account to prepare for clickjacking exploitation, ensuring saved credit card details are available for unauthorized transactions.

## Description

In a clickjacking attack on Yelp, the victim must be authenticated to enable seamless checkout using pre-saved payment methods. This step uses an incognito browser to mimic the victim's session without interfering with their real login. It sets the stage for embedding the checkout page in an iframe, where clicks can trigger purchases invisibly. Prerequisites include valid Yelp credentials; in a real attack, this relies on the victim being logged in elsewhere.

## Requirements

1. Valid Yelp account credentials (username/email and password)
2. Modern web browser with incognito mode (e.g., Chrome, Firefox)
3. Internet access to https://www.yelp.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) on accounts to prevent unauthorized logins
- Monitor for unusual login locations or devices via account activity logs
- Educate users on phishing risks leading to credential compromise

## Objectives

1. Establish an authenticated session with access to saved payment info
2. Verify payment methods are enabled for quick checkout
3. Prepare browser state for iframe embedding without session conflicts

## Instructions

### Step 1: Launch Incognito Browser

**Context**: Use incognito mode to isolate the session and simulate a fresh victim login without cookies from prior sessions.

Navigate to https://www.yelp.com in an incognito window.

### Step 2: Enter Credentials and Login

**Context**: Provide the victim's credentials to authenticate and access the account dashboard.

Enter email/username and password on the login form, then submit. Upon success, navigate to account settings to confirm saved credit cards.

### Step 3: Verify Payment Setup

**Context**: Ensure credit card details are saved to allow one-click purchases in the checkout flow.

Go to Account Settings > Payments and verify at least one card is added and set as default.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[web]]
- [[yelp]]
