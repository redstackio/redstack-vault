---
id: ee099ee5-9720-4053-bd73-b18aff8ab6f1
name: Generate Encoded Shellcode
type: command
executor: bash
data: $ python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor
output: null
created_at: '2023-04-06T03:56:16.386855+00:00'
updated_at: '2023-04-10T20:36:24.586607+00:00'
---

# Generate Encoded Shellcode

```bash
$ python2 ./shellcode_encoder.py -cpp -cs -py payload.bin MySecretPassword xor
```
