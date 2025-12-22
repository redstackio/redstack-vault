---
type: code
language: HTML
verified: true
tags:
  - xss-payload
  - waf-bypass
  - prompt-injection
platforms:
  - Web
validated: true
---

# Obfuscated-HTML-Details-Tag-for-Prompt-XSS

## Code

```html
<dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>
```

## Description

This obfuscated HTML snippet uses a malformed <details> element with URL-encoded line breaks (%0a) and mixed-case attributes to evade WAF detection. When injected into a vulnerable webpage and rendered, the 'open' attribute triggers the 'ontoggle' event, executing JavaScript that calls prompt() to display a user input dialog. This enables client-side code execution for XSS attacks, bypassing server-side filters focused on direct script injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no variables; customize the prompt message by editing the JS inline if needed (e.g., change 'a=prompt' to 'a=prompt(1)') | N/A |

## Usage

Inject this code into XSS-vulnerable inputs on a webpage protected by Akamai WAF, such as URL parameters, form fields, or stored content. Ensure the victim loads the page to trigger rendering. Ideal for reflected or DOM-based XSS to prompt for credentials or execute further JS chains like data exfiltration.

## Detection

- Browser console logs showing unexpected ontoggle events or prompt executions.
- WAF logs for anomalous HTML patterns if not fully obfuscated; monitor for <details> tags with unusual attributes.
- Client-side monitoring via CSP violations or XSS auditors in modern browsers.
- Network traffic showing post-prompt requests to external domains.

## Related

- [[procedures/Akamai-WAF-Bypass-via-XSS-Prompt-Injection]]
