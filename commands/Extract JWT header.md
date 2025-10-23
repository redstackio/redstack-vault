---
id: 64bd01de-04c7-42bb-8953-4cdafc47ebe9
name: Extract JWT header
type: command
executor: bash
data: python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
output: null
created_at: '2023-04-06T03:56:00.787256+00:00'
updated_at: '2023-04-10T20:22:34.479056+00:00'
---

# Extract JWT header

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
```


