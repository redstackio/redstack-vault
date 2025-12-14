---
tags:
  - google-oauth
  - external-auth
  - backdoor-linking
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
  - '[[External Remote Services]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.998Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: ea60973b-5efc-4759-a31d-e93a53433abb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
  - '[[Valid Accounts]]'
---
# Authenticate-with-External-Provider

## Summary

This procedure completes the OAuth authentication with an external provider like Google to link it to the unverified Shopify account, establishing the backdoor without email verification.

## Description

After injection, the OAuth flow redirects to Google's login page. Authenticating with a controlled Google account binds it to the Shopify profile, exploiting the lack of verification checks for new accounts. This occurs in a web environment, with outcomes including a linked external login visible in the profile.

## Requirements

1. Redirect from Shopify to Google OAuth
2. Controlled Google account credentials
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Require email verification before allowing external provider linking
- Audit OAuth callbacks for unverified accounts and block suspicious ones
- Implement multi-factor prompts during external auth for new accounts

## Objectives

1. Successfully link Google to the unverified Shopify account
2. Redirect back to profile with linked credentials
3. Enable future logins via external provider

## Instructions

### Step 1: Handle OAuth Redirect

**Context**: Respond to the Google login prompt after link click.

No command; the browser redirects automatically.

> Expected: Google sign-in page loads.

### Step 2: Log In to Google

**Context**: Authenticate with a Google account to complete linking.

Enter credentials for an existing or new Google account on the OAuth page.

> Upon success, redirect to Shopify profile.

### Step 3: Confirm Linking

**Context**: Verify the external login is now associated.

Check the profile page for the Google login option.

> Expected: Profile shows linked Google without email verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[google-oauth]]
- [[external-auth]]
- [[backdoor-linking]]
