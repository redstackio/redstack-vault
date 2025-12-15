---
id: proc-identify-oauth-misconfig
tags:
  - oauth
  - misconfiguration
  - recon
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
updated_at: '2025-12-14T17:24:35.601Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Facebook-OAuth-Misconfiguration

## Summary

This procedure involves inspecting a web application's Facebook OAuth integration to detect misconfigurations, such as the absence of valid redirect URIs, which allows arbitrary redirect_uri parameters in authorization requests.

## Description

In the Gratipay vulnerability, attackers observed that the Facebook login flow lacked a dedicated callback endpoint (e.g., /facebook/callback), and the Facebook app console had no specified redirect URIs. This enabled crafting OAuth URLs with unvalidated redirect_uri values pointing to attacker-controlled pages. The procedure targets web apps using OAuth for authentication, focusing on reconnaissance to identify exploitable setup flaws that could lead to token theft.

## Requirements

1. Access to a web browser and network connectivity to the target site
2. Knowledge of the target's OAuth client_id (often discoverable via public endpoints)
3. No authentication required for initial inspection

## Defense

Defensive measures and detection strategies:

- Configure strict redirect URIs in the OAuth provider console (e.g., Facebook App Dashboard)
- Implement server-side validation of redirect_uri parameters
- Monitor for anomalous OAuth authorization requests with unexpected URIs

## Objectives

1. Confirm lack of redirect URI validation in OAuth flow
2. Identify the OAuth client_id and scopes used
3. Establish foundation for crafting exploitable URLs

## Instructions

### Step 1: Inspect OAuth Flow

**Context**: Navigate to the target's login page and observe the Facebook OAuth initiation to check for callback endpoints and parameter handling.

No specific command; use browser developer tools to examine network requests during login attempts. Look for authorization URLs like https://www.facebook.com/dialog/oauth and note if redirect_uri is present and unvalidated.

> Manually test by modifying the redirect_uri in a browser and observing if the flow proceeds without errors.

### Step 2: Verify App Configuration

**Context**: If possible, access the OAuth provider's app management console or infer from public sources.

Search for the client_id in the target's source code or HackerOne reports. Confirm no valid URIs are set, allowing arbitrary values.

> Expected: Flow accepts redirect_uri like https://evil.com without rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[misconfiguration]]
- [[recon]]
