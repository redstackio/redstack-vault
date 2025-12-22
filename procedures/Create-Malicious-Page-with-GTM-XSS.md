---
tags:
  - xss
  - gtm-exploit
type: procedure
tools:
  - '[[tools/Google-Tag-Manager]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/open-appleid-authorize]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 57ec29ad-eaee-46a1-9531-afb0dc230bf9
created_at: '2025-12-14T00:11:25.337Z'
updated_at: '2025-12-14T00:11:25.337Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Malicious Page with GTM XSS

## Summary

This procedure creates a malicious web page that exploits XSS via arbitrary GTM IDs on www.redditmedia.com to inject scripts and tamper with OAuth parameters.

## Description

By loading an iframe with a custom GTM ID, the attacker injects JavaScript that modifies the OAuth response_type and response_mode, setting up token leakage in the URL fragment.

## Requirements

1. Google Tag Manager account
2. HTML/JS development environment
3. Encoded state from previous step

## Defense

Defensive measures and detection strategies:

- Restrict allowed GTM IDs
- Sanitize iframe sources and scripts

## Objectives

1. Inject malicious JS via XSS
2. Tamper with OAuth flow
3. Prepare for token extraction

## Instructions

### Step 1: Set Up GTM Container

**Context**: Create a custom GTM ID for injection.

Use [[tools/Google-Tag-Manager]] to configure a container with ID like GTM-N3HH8D6, including scripts to modify OAuth parameters.

### Step 2: Build Malicious Page

**Context**: Create HTML page with iframe and injected script.

Load iframe src='https://www.redditmedia.com/gtm/jail?id=GTM-N3HH8D6&state=[encoded_state]'. Use [[commands/open-appleid-authorize]] to open the tainted authorization URL:

```javascript
b=window.open('https://appleid.apple.com/auth/authorize?client_id=com.reddit.RedditAppleSSO&redirect_uri=https%3A%2F%2Fwww.reddit.com&response_type=code+id_token&state='+ state +'&scope=&response_mode=fragment&m=12&v=1.5.4');
```

> This injects the tainted link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/open-appleid-authorize]]

## Tools Used

- [[tools/Google-Tag-Manager]]

## Tags

- xss
- gtm-exploit
