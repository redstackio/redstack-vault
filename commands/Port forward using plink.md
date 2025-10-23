---
id: a5320f30-150e-4c53-9e47-2586cc36eba3
name: Port forward using plink
type: command
executor: bash
data: 'plink.exe -l username -pw password target-ip -R 8080:127.0.0.1:8080

  '
output: null
created_at: '2020-07-14T18:14:31.061496+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Port forward using plink

```bash
plink.exe -l username -pw password target-ip -R 8080:127.0.0.1:8080

```


