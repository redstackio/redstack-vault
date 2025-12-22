---
id: 8ef679a6-bed1-4a4c-8870-e9950bdd5eae
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.537415+00:00'
updated_at: '2023-04-10T20:21:49.896602+00:00'
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/Filter-Bypass-and-Exotic-Payloads]]'
platforms:
  - Web
validated: true
---

# XSS-Payload-Bypass-Parentheses-with-Template-Literals

## Code

```javascript
alert`1`
setTimeout`alert\u0028document.domain\u0029`;
```

## Description

This JavaScript payload uses ES6 template literals (backticks) to invoke the alert function without parentheses, bypassing filters that block them in string contexts. The first part displays '1' immediately. The second uses setTimeout with a template literal containing a Unicode-escaped opening parenthesis (\u0028) to execute alert(document.domain), revealing the page's domain. It's designed for injection into XSS-vulnerable web pages to confirm execution and demonstrate filter evasion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no variables; it's self-contained for testing. | N/A |

## Usage

Inject this code into a reflected or stored XSS vulnerability, such as a URL parameter or form input that gets executed in a <script> tag. For example, wrap in <script> tags and URL-encode for transmission: <script>alert%601%60%0asetTimeout%60alert%5cu0028document.domain%5cu0029%60;</script>. Used in red team engagements to test XSS filters or during pentests to gain initial script execution for further attacks like cookie theft.

## Detection

- Browser developer tools showing unexpected alert dialogs or domain popups.
- WAF logs for template literal patterns (backticks) or Unicode escapes like \u0028 in input.
- Content Security Policy violations if CSP is misconfigured to allow inline scripts.
- JavaScript error logs or anomaly detection in client-side execution monitoring.

## Related

- [[procedures/Exotic-Payloads-for-Bypassing-Parentheses-in-String-XSS]]
