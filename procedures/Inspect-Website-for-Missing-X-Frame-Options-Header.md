---
id: proc-inspect-xframe-missing
tags:
  - clickjacking
  - x-frame-options
  - web-security
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.719Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Website-for-Missing-X-Frame-Options-Header

## Summary

This procedure involves inspecting HTTP response headers of a website to detect the absence of the X-Frame-Options header, which protects against clickjacking attacks by preventing the site from being embedded in iframes from external origins. It was used to identify a vulnerability on www.glasswire.com, enabling potential UI redressing where attackers could trick users into performing unintended actions like adding tasks.

## Description

Clickjacking, or UI redressing, occurs when an attacker overlays a transparent iframe over legitimate content to capture user clicks on hidden elements. The X-Frame-Options header (e.g., DENY or SAMEORIGIN) mitigates this by instructing browsers not to allow framing. In this scenario, nearly all pages on the GlassWire website lacked this header, as discovered through HTTP response inspection. The attack targets public-facing web applications and requires no authentication, making it a low-barrier initial access vector. Expected outcomes include confirmation of vulnerability and potential for crafting a proof-of-concept malicious page to demonstrate embedding and click hijacking.

## Requirements

1. Internet access to the target website (e.g., www.glasswire.com)
2. Command-line tool like curl installed for header inspection
3. Basic knowledge of HTTP headers and browser developer tools for verification

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server configurations (e.g., via Apache/Nginx headers)
- Use Content-Security-Policy (CSP) with frame-ancestors directive as a modern alternative
- Monitor web server logs for unusual iframe embedding attempts or anomalous user interactions
- Regularly scan websites with tools like securityheaders.com for missing headers

## Objectives

1. Confirm the absence of X-Frame-Options header to validate clickjacking risk
2. Assess impact on user interactions, such as unauthorized actions via tricked clicks
3. Provide remediation guidance to prevent framing from untrusted sites

## Instructions

### Step 1: Fetch HTTP Headers Using Curl

**Context**: Retrieve the response headers from the target URL to check for the presence of X-Frame-Options.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://www.glasswire.com
```

> This command performs a HEAD request to the target, outputting headers like Server, Content-Type, etc. Look for X-Frame-Options; if absent, the site is vulnerable to framing. Expected output includes a 200 OK status without the protective header.

### Step 2: Verify Framing in Browser

**Context**: Test if the site can be embedded in an iframe to confirm exploitability.

**Instructions**: Create a local HTML file with an iframe src pointing to the target:

```html
<!DOCTYPE html>
<html>
<body>
<iframe src="https://www.glasswire.com" width="800" height="600"></iframe>
</body>
</html>
```

Open this file in a browser. If the iframe loads without errors, the vulnerability exists. Overlay a transparent div to simulate clickjacking.

> Successful execution shows the target site loading inside the iframe, allowing potential UI manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[clickjacking]]
- [[x-frame-options]]
- [[web-security]]
