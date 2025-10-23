---
id: 7c2d16a9-ee2e-4533-afb6-cb41d0383bd8
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:30.990650+00:00'
updated_at: '2023-04-10T20:38:05.082755+00:00'
---

# Code Snippet 7c2d16a9

**Language**: Bash

```bash
%COMSPEC% /Q /c echo dir &gt; \\127.0.0.1\C$\__output 2&gt;&amp;1 &gt; %TEMP%\execute.bat &amp; %COMSPEC% /Q /c %TEMP%\execute.bat &amp; del %TEMP%\execute.bat
```


