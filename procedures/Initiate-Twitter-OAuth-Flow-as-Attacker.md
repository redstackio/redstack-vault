---
id: proc-uuid-001
tags:
  - oauth
  - twitter
  - initiation
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
updated_at: '2025-12-14T17:24:35.384Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Twitter OAuth Flow as Attacker

## Summary

This procedure starts the OAuth 1.0 authorization process on a third-party Twitter-integrated site using the attacker's credentials to generate a reusable request token.

## Description

In the context of exploiting Twitter's OAuth flaw, the attacker logs into their own Twitter account and initiates the sign-in flow on a vulnerable third-party application, such as unfollowerstats.com. This generates a unique oauth_token that is not session-bound, setting up the hijacking vector. Prerequisites include an active Twitter account for the attacker and access to a site using Twitter OAuth for authentication.

## Requirements

1. Attacker's Twitter account (e.g., TwitterAccount01)
2. Web browser with internet access
3. Target third-party site with Twitter OAuth integration

## Defense

Defensive measures and detection strategies:

- Implement state parameters in OAuth flows to bind tokens to sessions
- Monitor for unusual OAuth token authorizations from mismatched user agents
- Educate users on verifying app permissions before authorizing

## Objectives

1. Generate a unique OAuth request token
2. Prepare for token sharing with victim
3. Establish the initial session for later hijacking

## Instructions

### Step 1: Log In to Twitter

**Context**: Ensure the attacker is authenticated on Twitter to initiate the flow.

Open a web browser and log in to Twitter using the attacker's credentials (e.g., TwitterAccount01).

### Step 2: Navigate to Third-Party Site

**Context**: Trigger the OAuth redirection to generate the token.

Visit the target site (e.g., https://unfollowerstats.com), which will redirect to https://api.twitter.com/oauth/authorize, prompting authorization and generating an oauth_token.

**Expected Output**: Redirection to Twitter's OAuth endpoint with token in the URL.

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
