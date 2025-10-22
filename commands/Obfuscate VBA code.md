---
id: 4e5f3876-c347-44ec-a363-51895fc89d49
name: Obfuscate VBA code
type: command
executor: bash
data: $ cat example_macro/download_payload.vba | docker run -i --rm bonnetn/vba-obfuscator
  /dev/stdin
output: null
created_at: '2023-04-06T03:56:23.756736+00:00'
updated_at: '2023-04-10T20:36:59.136282+00:00'
---

# Obfuscate VBA code

```bash
$ cat example_macro/download_payload.vba | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin
```
