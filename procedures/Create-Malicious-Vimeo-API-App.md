---
id: proc-create-vimeo-app
tags:
  - oauth
  - api-registration
  - vimeo
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
updated_at: '2025-12-14T17:31:11.122Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Vimeo-API-App

## Summary

This procedure involves registering a new application on Vimeo's API developer portal to obtain a client_id, which is essential for crafting malicious OAuth flows in subsequent attack stages.

## Description

In the context of exploiting Vimeo's OAuth integration with Facebook, an attacker first needs a legitimate-looking app on Vimeo's platform. Vimeo's API allows open registration without strict verification, providing a client_id that can be used to initiate OAuth authorization requests. This step sets up the foundation for chaining redirects and stealing codes, targeting users who authorize via Facebook to access Vimeo features.

## Requirements

1. Access to the internet and a web browser
2. Basic knowledge of API registration processes
3. No credentials required for initial app creation

## Defense

Defensive measures and detection strategies:

- Enforce app review processes before issuing client_ids
- Monitor for unusual app registrations from suspicious IPs
- Implement rate limiting on API registrations

## Objectives

1. Obtain a valid client_id for the malicious app
2. Establish a foothold in the Vimeo ecosystem for OAuth exploitation
3. Enable subsequent redirect chaining without detection

## Instructions

### Step 1: Access Vimeo Developer Portal

**Context**: Navigate to Vimeo's API documentation and developer signup to begin app creation.

Visit https://developer.vimeo.com/apps/new and provide basic app details such as name, description, and callback URL (can be placeholder at this stage).

> Upon submission, Vimeo generates and displays the client_id immediately.

### Step 2: Note Client ID

**Context**: Securely record the issued client_id for use in URL construction.

Example client_id: `9f3bb9f9186bc825434330567c99283f6dd57586`.

> Store this in a secure note or script variable; do not expose it publicly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[api-registration]]
- [[vimeo]]
