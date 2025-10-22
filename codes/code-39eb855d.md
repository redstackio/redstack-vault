---
id: 39eb855d-a993-46d4-8323-d4739bf0ab83
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:23.551855+00:00'
updated_at: '2023-04-10T20:36:53.088799+00:00'
---

# Code Snippet 39eb855d

**Language**: Bash

```bash
r = GetObject(&quot;winmgmts:\\.\root\cimv2:Win32_Process&quot;).Create(&quot;calc.exe&quot;, null, null, intProcessID)
```
