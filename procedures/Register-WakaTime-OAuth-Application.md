---
id: proc-uuid-1
name: Register WakaTime OAuth Application
tags:
  - oauth
  - app-registration
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
updated_at: '2025-12-14T17:30:18.749Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Register WakaTime OAuth Application

## Summary

This procedure registers a malicious OAuth application on WakaTime's developer portal to obtain a client ID and configure scopes for the clickjacking attack, enabling later token exchange for victim access.

## Description

In the context of the double clickjacking attack, the attacker first creates an OAuth app at https://wakatime.com/apps/new. This provides a client_id (e.g., joUNHCTnWqQ9hsmrWS5CTokR) and sets a redirect_uri (e.g., https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead) for code capture. Scopes like read_orgs and write_orgs are requested to gain broad access to organizations upon authorization. This step is prerequisite for embedding credentials in the malicious OAuth URL.

## Requirements

1. Access to WakaTime account (free signup if needed)
2. A controlled redirect URI (e.g., webhook.site instance)
3. Browser for portal navigation

## Defense

Defensive measures and detection strategies:

- Monitor for suspicious app registrations with broad scopes
- Implement app review processes for OAuth clients
- Rate-limit or audit new app creations

## Objectives

1. Obtain client credentials for OAuth flow
2. Configure redirect for code interception
3. Request scopes for maximum impact

## Instructions

### Step 1: Access Developer Portal

**Context**: Navigate to the WakaTime app registration page to begin setup.

No command required; use browser to visit https://wakatime.com/apps/new and fill in app details like name, description, and redirect URI.

> Enter redirect_uri as https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead and scopes as read_orgs,write_orgs.

### Step 2: Submit and Verify Registration

**Context**: Complete registration to receive client_id.

No command; submit the form and note the generated client_id (e.g., joUNHCTnWqQ9hsmrWS5CTokR).

> Successful registration shows client_id and confirms redirect_uri.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[app-registration]]
