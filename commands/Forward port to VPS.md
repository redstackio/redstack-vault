---
id: 8de9130a-21f7-4aeb-8225-bf4c6ac7f70e
name: Forward port to VPS
type: command
executor: bash
data: plink -R [Port to forward to on your VPS]:localhost:[Port to forward on your
  local machine] [VPS IP]
output: null
created_at: '2023-04-06T03:56:23.000085+00:00'
updated_at: '2023-04-10T20:25:11.704574+00:00'
---

# Forward port to VPS

```bash
plink -R [Port to forward to on your VPS]:localhost:[Port to forward on your local machine] [VPS IP]
```


