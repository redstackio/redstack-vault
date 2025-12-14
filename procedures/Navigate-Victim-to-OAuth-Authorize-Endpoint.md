---
tags:
  - oauth
  - csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 09abdf20-b8b2-4471-9228-8b467c11adb3
created_at: '2025-12-13T23:56:03.995Z'
updated_at: '2025-12-13T23:56:03.995Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Navigate Victim to OAuth Authorize Endpoint

## Summary

This procedure navigates the victim to the /admin/oauth/authorize endpoint on the attacker's store to force login using stuffed cookies.

## Description

Leveraging the stuffed cookies, this step triggers the OAuth authorization flow, logging the victim in as the attacker without consent. Part of a Login CSRF chain in web applications. Requires prior cookie stuffing and victim interaction.

## Requirements

1. Stuffed cookies in victim browser
2. Malicious redirect or navigation script
3. Attacker-controlled Shopify store

## Defense

Defensive measures and detection strategies:

- Implement state parameters in OAuth
- Monitor for anomalous logins

## Objectives

1. Trigger OAuth flow
2. Force attacker login
3. Set up session hijack

## Instructions

### Step 1: Prepare URL

**Context**: Construct the /admin/oauth/authorize URL with client_id, redirect_uri, etc.

> Include necessary parameters for the app.

### Step 2: Navigate Victim

**Context**: Redirect or navigate the victim to the prepared URL.

> Use window.location or similar to initiate the flow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- oauth
- csrf
