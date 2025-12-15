---
id: 123e4567-e89b-12d3-a456-426614174000
tags:
  - api-token
  - misconfiguration
  - mapbox
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.142Z'
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
# Create-Mapbox-No-Scope-API-Token

## Summary

This procedure creates an API access token in Mapbox Studio with no explicit scopes, exploiting the UI's implicit granting of public scopes (styles:read, styles:tiles, fonts:read) to enable unauthorized read access to public resources.

## Description

In Mapbox, selecting 'No scopes' during token creation does not restrict access to zero permissions; instead, it defaults to a public token with read access to all public endpoints. This misconfiguration allows token holders to access user public map styles without intending to grant such permissions, violating least privilege. The procedure targets the Mapbox Studio UI and is used in scenarios testing API token security or demonstrating scope enforcement flaws. Expected outcome: A functional public token that can read styles data.

## Requirements

1. Valid Mapbox account with Studio access
2. Web browser with JavaScript enabled
3. Network connectivity to studio.mapbox.com

## Defense

Defensive measures and detection strategies:

- Update UI and docs to clarify 'No scopes' implies public read access (as Mapbox did post-fix)
- Enforce explicit scope selection during token creation
- Monitor API logs for unexpected read requests from public tokens
- Use token scoping tools to audit permissions

## Objectives

1. Generate a token that implicitly gains public read access
2. Set up for unauthorized API queries
3. Expose potential information disclosure risks

## Instructions

### Step 1: Access Mapbox Studio and Navigate to Token Creation

**Context**: Log in and reach the token management interface to create a new token.

**Instructions**: Open https://studio.mapbox.com in your browser, log in with your Mapbox credentials, click your avatar, select 'Account', then 'Access tokens' in the sidebar.

> No command executed; this is UI-based. Expected: Token creation page loads.

### Step 2: Generate Token with No Scopes

**Context**: Create the token without selecting any scopes to trigger implicit public permissions.

**Instructions**: Click 'New token', enter a name (e.g., 'Test No Scope'), in the 'Scopes' dropdown select 'No scopes', ensure 'Public' token type, then click 'Create token'. Copy the generated token.

> Expected: Token string provided, labeled as public with implicit scopes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-token
- misconfiguration
