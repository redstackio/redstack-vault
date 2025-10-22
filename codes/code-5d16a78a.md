---
id: 5d16a78a-9411-498f-8ee7-01bcf4e9bdf7
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:10.827187+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5d16a78a

**Language**: Bash

```bash

$SSN_Regex = " [0-9]{3}[-| ][0-9]{2}[-| ][0-9]{4}" ; Get-ChildItem . -Recurse -exclude *.exe,*.dll| Select-String -Pattern $SSN_Regex | Select-String -Pattern $SSN_Regex| Select-Object Path,Filename,Matches |ft -auto|out-string -width 200; "[*] SSN Search Complete!"

```
