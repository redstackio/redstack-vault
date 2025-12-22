---
tags:
  - sso-bypass
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 08399c00-ce67-4fdb-ac73-20e50bbb8383
created_at: '2025-12-13T09:01:26.364Z'
updated_at: '2025-12-13T09:01:26.364Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Craft Zendesk SSO URL

## Summary

This procedure constructs a URL using the obtained JWT to bypass Zendesk SSO and log in as an organization member.

## Description

By appending the JWT to the access/jwt endpoint, the attacker can authenticate without proper verification, exploiting the trust in Trint-issued tokens.

## Requirements

1. Valid Zendesk JWT from previous step
2. Browser access to trintsupport.zendesk.com

## Defense

Defensive measures and detection strategies:

- Validate token issuance against verified users
- Monitor SSO login attempts from untrusted sources

## Objectives

1. Bypass SSO authentication
2. Gain logged-in session
3. Enable access to protected resources

## Instructions

### Step 1: Construct URL

**Context**: Build the login URL.

Format: https://trintsupport.zendesk.com/access/jwt?jwt=<JWT_TOKEN>

> Replace <JWT_TOKEN> with the actual token.

### Step 2: Access URL

**Context**: Load the URL to initiate login.

Open the constructed URL in a browser.

> This logs you in automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso-bypass]]
- [[url-crafting]]
