---
tags:
  - csrf
  - xss
  - token-theft
  - exfiltration
  - socialclub
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:49.527Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 674bac2e-41c2-4936-9575-7c4ec8ee7e7a
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Combine-Flash-XSS-with-CSRF-to-Steal-Tokens

## Summary

This procedure chains a Flash-based XSS vulnerability with a CSRF flaw to force authenticated users' browsers to make unauthorized requests to the SocialClub GetTokens endpoint, stealing private tokens without user knowledge.

## Description

By leveraging Flash XSS to inject code that triggers a forged request to the unprotected CSRF endpoint, attackers can exfiltrate sensitive tokens from victims who visit a malicious site while logged into SocialClub. This bypasses normal secure calling mechanisms, as Flash allows cross-origin execution. The attack targets web sessions and results in token theft, enabling further account compromise.

## Requirements

1. Malicious SWF file from prior XSS discovery
2. Hosted external site for luring victims
3. Authenticated victim session to SocialClub
4. Server to receive exfiltrated tokens (e.g., via POST to attacker domain)

## Defense

Defensive measures and detection strategies:

- Remove Flash dependencies and migrate to secure alternatives like HTML5
- Add comprehensive CSRF protections and validate all cross-origin requests
- Use browser security features like sandboxing for embeds
- Monitor for token access logs and anomalous Flash loads

## Objectives

1. Force unauthorized token retrieval via chained exploits
2. Exfiltrate tokens to attacker control
3. Demonstrate full impact on user accounts

## Instructions

### Step 1: Prepare Malicious Site

**Context**: Set up a lure site hosting the Flash XSS payload configured to trigger CSRF.

Host an HTML page embedding the malicious SWF. In the SWF, include ActionScript to make a request to https://socialclub.rockstargames.com/profileedit/GetTokens upon load, using the victim's cookies.

Example SWF integration (inline):

```html
<object data="malicious.swf" type="application/x-shockwave-flash"></object>
```

**Expected Output**: Site ready for victim visit.

### Step 2: Trigger Exploitation

**Context**: Lure the victim to the site to execute the chain.

Send a phishing link to the victim. Upon loading, Flash XSS executes, forcing the CSRF request in the background.

**Expected Output**: Request sent to GetTokens endpoint.

### Step 3: Exfiltrate Tokens

**Context**: Capture and send the response to attacker.

Modify the SWF to POST the token response to an attacker endpoint, e.g., via URLLoader in ActionScript.

**Expected Output**: Tokens received on attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[Exfiltration]]
