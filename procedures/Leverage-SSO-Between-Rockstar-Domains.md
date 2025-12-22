---
id: proc-uuid-2
name: Leverage-SSO-Between-Rockstar-Domains
tags:
  - sso
  - misconfig
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T03:47:12.611Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Leverage-SSO-Between-Rockstar-Domains

## Summary

This procedure exploits single sign-on (SSO) misconfiguration between rockstargames.com and rockstarwarehouse.com to share authentication sessions across domains, escalating access from the XSS-compromised warehouse to the main SocialClub platform.

## Description

The root cause is improper SSO setup allowing unintended cross-domain session propagation. After gaining a foothold via XSS on rockstarwarehouse.com, the injected script triggers SSO flows that authenticate the session on rockstargames.com. This targets web environments with federated identity providers, enabling privilege escalation without additional credentials. Expected outcomes include access to protected endpoints on the primary domain.

## Requirements

1. Active session on rockstarwarehouse.com via prior XSS
2. SSO enabled between the domains (e.g., shared cookies or token exchange)
3. Victim's browser allowing cross-domain requests

## Defense

Defensive measures and detection strategies:

- Configure SSO with strict domain isolation and same-site cookie policies
- Validate session tokens for domain-specific scopes
- Log and alert on cross-domain authentication attempts

## Objectives

1. Propagate session from warehouse subdomain to main domain
2. Gain authenticated access to SocialClub resources
3. Set up for OAuth manipulation

## Instructions

### Step 1: Trigger SSO from Injected Script

**Context**: Use the XSS payload to navigate or submit a form that initiates SSO login to rockstargames.com.

Inject code like `window.location = 'https://rockstargames.com/sso-login?from=warehouse';` to force the SSO handshake.

### Step 2: Inherit Session Across Domains

**Context**: Exploit the misconfiguration to reuse the warehouse session cookie or token on the main domain.

Monitor network requests; the SSO should set or validate shared auth artifacts without re-authentication.

### Step 3: Confirm Escalated Access

**Context**: Test access to rockstargames.com protected pages.

Attempt to load a SocialClub endpoint; success indicates session inheritance.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sso]]
- [[misconfig]]
