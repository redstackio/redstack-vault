---
id: proc-periscope-oauth-victim-auth
tags:
  - phishing
  - oauth
  - social-engineering
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:33:34.235Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Send-OAuth-URL-to-Victim-for-Authorization

## Summary

This procedure involves delivering the captured OAuth URL to the victim, prompting them to authorize the Periscope app with their Twitter credentials, which redirects tokens to the attacker.

## Description

The captured URL from Twitter's OAuth authenticate endpoint is sent to the victim via email, link, or other means. Upon visiting, the victim sees a legitimate-looking Twitter authorization prompt for Periscope. Authorization completes the flow, redirecting to the poisoned domain with tokens. This relies on social engineering and assumes the victim has or wants a Periscope account.

## Requirements

1. Captured OAuth URL with valid token
2. Method to deliver link to victim (e.g., phishing email)
3. Victim's interaction within token validity period

## Defense

Defensive measures and detection strategies:

- Educate users on OAuth prompts and verify app legitimacy
- Implement OAuth consent screens with clear app details
- Monitor for unusual authorization spikes or from suspicious IPs

## Objectives

1. Deliver URL to victim
2. Obtain victim authorization
3. Trigger redirect to attacker domain

## Instructions

### Step 1: Deliver the URL

**Context**: Send the captured https://twitter.com/oauth/authenticate?oauth_token=... URL to the victim.

No specific command; use email or messaging to share the link.

> Victim visits and authorizes; expected output is post-auth redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- phishing
- oauth
- social-engineering
