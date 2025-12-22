---
id: proc-host-malicious-json
tags:
  - xss
  - payload
  - json
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.185Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-JSON-Payload-for-XSS

## Summary

This procedure involves creating and hosting a malicious JSON file on an attacker-controlled HTTPS server. The JSON crafts a payload in the 'authorize_url' property that breaks out of the Mapbox authorize template by injecting a script tag, enabling reflected XSS when fetched by the vulnerable endpoint.

## Description

In the Mapbox OAuth flow, the /core/oauth/auth endpoint accepts arbitrary redirect_uri values without validation, leading to an open redirect. The authorize page fetches data from this endpoint and inserts the 'authorize_url' from the JSON response directly into a form action attribute without HTML escaping: <form id='oauth' method='post' action='<%=App.api + obj.authorize_url%>' class='col6 modal-body fill-white'>. By hosting JSON with a payload like "><script>alert(document.domain);</script>, the template breaks, injecting executable JavaScript on the www.mapbox.com domain. This requires an HTTPS server to match the secure context.

## Requirements

1. Access to an HTTPS-enabled server for hosting files (e.g., Apache, Nginx, or cloud storage like AWS S3 with HTTPS).
2. Basic knowledge of JSON structure and HTML/JS injection techniques.
3. No target credentials needed, as it's a public-facing vulnerability.

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect_uri parameters to only allow trusted domains.
- Escape all user-controlled data inserted into HTML templates, especially in server-side rendering.
- Implement Content Security Policy (CSP) to block inline scripts on the authorize page.
- Monitor for anomalous fetches to external domains from auth endpoints.

## Objectives

1. Deliver a JSON response that injects malicious HTML/JS into the target's template.
2. Enable cross-origin fetching without CORS blocks.
3. Achieve initial payload delivery for XSS exploitation.

## Instructions

### Step 1: Create the Malicious JSON File

**Context**: Craft the JSON to mimic a legitimate auth response but embed the XSS payload in authorize_url to close the attribute and inject a script.

No command required; manually create the file oauth.json with content:

```json
{
  "authorize_url": "'><script>alert(document.domain);</script>",
  "stage": "authorize",
  "user": {
    "name": "nombre",
    "extraTm2z": 17
  },
  "origin": ""
}
```

> This payload closes the form action quote ("), adds a script tag, and alerts the domain to prove execution. Save as oauth.json.

### Step 2: Host the File on HTTPS Server

**Context**: Upload the JSON to a publicly accessible HTTPS endpoint to allow fetching from the browser context of www.mapbox.com.

Upload the file to your server, ensuring the URL is HTTPS, e.g., https://u00f1.xyz/mapbox/oauth.json.

> Verify accessibility by curling the URL or loading in browser; expect the raw JSON response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- json-payload
- hosting
