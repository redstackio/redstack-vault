---
id: proc-twitter-oauth-redirect-victim
tags:
  - phishing
  - oauth
  - victim-engagement
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:35.713Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Redirect-Victim-to-Authorize-Endpoint

## Summary

This procedure involves directing a victim to Twitter's OAuth authorize or authenticate page using a malicious request token, initiating the flow that leads to XSS execution upon permission grant.

## Description

After obtaining the tainted token, construct a URL to https://twitter.com/oauth/authorize?oauth_token=MALICIOUS_TOKEN and deliver it via phishing (email, social engineering). The victim logs in and authorizes, triggering the redirect to the injected callback, where XSS fires. Targets twitter.com; assumes victim has a Twitter account.

## Requirements

1. Malicious oauth_token from prior step
2. Social engineering vector (e.g., email/phishing site)
3. Victim's Twitter access

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious authorization requests
- Rate-limit OAuth requests per IP/user
- Log and alert on unusual oauth_token usages

## Objectives

1. Engage victim in OAuth flow
2. Obtain authorization to trigger redirect
3. Position for payload execution

## Instructions

### Step 1: Construct Authorization URL

**Context**: Build the phishing link with the malicious token.

No command; manually create: https://twitter.com/oauth/authorize?oauth_token=EXTRACTED_TOKEN&force_login=true (optional for fresh login).

> Deliver via email or link shortener.

### Step 2: Monitor Victim Interaction

**Context**: Wait for victim to authorize and observe redirect.

Use browser dev tools or proxy to intercept if testing.

> Expected: Victim sees authorize page, clicks 'Authorize app', redirects to callback executing JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[oauth]]
