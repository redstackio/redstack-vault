---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - oauth
  - signup
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.131Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Create-Reddit-Account-via-Gmail-OAuth

## Summary

This procedure creates a new Reddit account using Gmail OAuth, linking it to a specified email address. It sets up the initial condition for exploiting OAuth email collision vulnerabilities.

## Description

In the context of Reddit's OAuth implementation, this step initiates the signup flow where the attacker uses the victim's Gmail address to create an account. The OAuth provider (Google) authenticates the email ownership, but Reddit does not enforce unique email checks during signup, allowing multiple associations. This is performed via the web interface on reddit.com, requiring no special tools beyond a browser.

## Requirements

1. Access to a web browser with internet connectivity
2. Valid Gmail account with the target email address
3. No existing Reddit session for the email

## Defense

Defensive measures and detection strategies:

- Enforce unique email validation during OAuth signup
- Implement secondary verification (e.g., email code) for OAuth logins
- Monitor for multiple OAuth associations per email and flag anomalies

## Objectives

1. Link the target email to a new Reddit account via OAuth
2. Establish session for subsequent logout
3. Prepare for account collision exploitation

## Instructions

### Step 1: Initiate Signup

**Context**: Start the account creation process on Reddit's signup page.

Navigate to https://www.reddit.com/register/ and select the "Continue with Google" option for OAuth signup.

> Enter the Gmail credentials when prompted by Google, ensuring the email matches the victim's.

### Step 2: Complete OAuth Flow

**Context**: Authorize and finalize account creation.

Follow Google's OAuth prompts to grant Reddit access, then complete any required profile setup on Reddit.

> Upon success, you are logged into the new account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- signup
- auth

---
