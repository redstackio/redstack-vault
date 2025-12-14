---
tags:
  - csrf
  - oauth
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.685Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 071a3474-c430-4160-a603-ac0aca813dd7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate Attacker Pinterest Connection

## Summary

This procedure starts the OAuth flow from the attacker's Shopify store to prepare for code generation in the CSRF attack.

## Description

The attacker logs into their own Shopify admin and begins the Pinterest connection process, which lacks CSRF protection due to no state parameter. This sets up the redirect chain exploitable by the victim. Target is Shopify's web app with Pinterest integration.

## Requirements

1. Attacker's Shopify admin access
2. Attacker's Pinterest account credentials
3. No existing Pinterest connection on attacker's store

## Defense

Defensive measures and detection strategies:

- Implement OAuth state parameters to bind requests to sessions
- Log all OAuth initiations for anomaly detection

## Objectives

1. Trigger OAuth redirect to Pinterest
2. Ensure clean state for code capture
3. Prepare for interception

## Instructions

### Step 1: Log In to Attacker Shopify

**Context**: Access the admin panel.

Navigate to attacker's store admin dashboard.

> Expected: Successful login.

### Step 2: Start Connection

**Context**: Initiate the integration.

Go to Apps > Search for Pinterest > Click 'Connect' or 'Add app'.

> Expected: Redirect to https://www.pinterest.com/oauth/ or similar authorization URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[shopify]]
