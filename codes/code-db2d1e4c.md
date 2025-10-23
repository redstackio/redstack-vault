---
id: db2d1e4c-4f12-494d-8370-6d16823892b3
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:42.768697+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
---

# Code Snippet db2d1e4c

**Language**: JavaScript

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


