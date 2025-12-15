---
id: proc-uuid-002
tags:
  - oauth
  - twitter
  - extraction
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
updated_at: '2025-12-14T17:24:35.379Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Extract Twitter OAuth Authenticate URL

## Summary

This procedure captures the OAuth authenticate URL containing the request token from the third-party site's flow, enabling it to be shared for hijacking.

## Description

After initiating the OAuth flow, the third-party app provides or redirects to an authenticate URL with the oauth_token parameter. The attacker extracts this URL, which can be authorized by any user due to the vulnerability. This step is crucial for the social engineering phase and requires no special tools, just URL inspection.

## Requirements

1. Active OAuth session from previous step
2. Web browser developer tools or URL bar access
3. Knowledge of OAuth URL format

## Defense

Defensive measures and detection strategies:

- Bind OAuth tokens to user sessions via nonces or state parameters
- Log and alert on token extractions or shares
- Use short-lived request tokens

## Objectives

1. Obtain the full authenticate URL with token
2. Prepare URL for phishing delivery
3. Ensure token is valid for authorization

## Instructions

### Step 1: Inspect the Redirect

**Context**: Locate the generated URL during the OAuth handshake.

In the browser, note the URL after redirection, such as https://api.twitter.com/oauth/authenticate?oauth_token=xxxxxxxx.

### Step 2: Copy the URL

**Context**: Secure the token for sharing without altering it.

Copy the entire URL string, verifying the oauth_token parameter (e.g., FUwCQhzh2zNJv7VKC1b1bWLVJUdHrs7x) is intact.

**Expected Output**: Copied URL ready for distribution.

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
- twitter
