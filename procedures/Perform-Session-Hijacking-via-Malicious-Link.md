---
id: proc-uuid-003
tags:
  - session-hijacking
  - phishing
  - web
type: procedure
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.388Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Valid Accounts]]'
---
# Perform-Session-Hijacking-via-Malicious-Link

## Summary

This procedure forces a victim's browser session to switch from their current user to a targeted user by sending a crafted GET link exploiting the authentication bypass.

## Description

Leveraging the 'signin' parameter vulnerability, attackers create malicious links that, when clicked by a logged-in victim, cause an automatic logout and re-authentication as the specified user. This enables session hijacking in web applications with SSO, impacting user privacy and access control. The attack relies on social engineering to get victims to click links.

## Requirements

1. Valid crafted URL with ?signin= parameter
2. Victim logged into the application
3. Delivery method for the link (e.g., email, chat)

## Defense

Defensive measures and detection strategies:

- Warn users against clicking unsolicited links
- Implement CSRF tokens and validate referer headers on sensitive endpoints
- Monitor for sudden session changes and logouts in user sessions

## Objectives

1. Hijack the victim's active session
2. Impersonate the targeted user through the victim's browser
3. Gain unauthorized access to victim-controlled resources

## Instructions

### Step 1: Prepare Malicious Link

**Context**: Build the link using the bypass parameter for the desired target user.

Create a URL like ███?signin=targetuser, ensuring it points to the vulnerable endpoint.

> This link will trigger the bypass upon access.

### Step 2: Deliver and Execute

**Context**: Send the link to the victim and observe the session switch.

Share the link with the victim (e.g., via phishing email). When clicked, their session as user A ends, and they authenticate as user B.

> Expected output: Victim accesses resources as the targeted user; attacker can verify via application behavior or logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[Phishing]]
- [[web]]
