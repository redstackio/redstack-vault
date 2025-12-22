---
type: command
executor: cmd
data: |
  \\<DOMAIN_DNS>\SYSVOL\<DOMAIN_DNS>\Policies\<{GPONAME_OR_GUID}>\
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - gpo
verified: true
validated: true
---

# access-sysvol-gpo-folder

## Command

```cmd
\\<DOMAIN_DNS>\SYSVOL\<DOMAIN_DNS>\Policies\<{GPONAME_OR_GUID}>\
```

## Description

This UNC path accesses the SYSVOL share for a specific Group Policy Object (GPO) folder, allowing browsing and modification of GPO files like Scheduled Tasks Preferences. Use in Windows Explorer, `net use`, or `dir` to list contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <DOMAIN_DNS> | FQDN of the Active Directory domain (e.g., example.com) | Yes |
| <GPONAME_OR_GUID> | Name or GUID of the target GPO (e.g., {31B2F340-016D-11D2-945F-00C04FB984F9}) | Yes |

## Examples

### Basic Usage

Open in Explorer:

```cmd
explorer \\example.com\SYSVOL\example.com\Policies\{GUID}
```

### List Contents

```cmd
dir \\example.com\SYSVOL\example.com\Policies\{GUID}
```

## Expected Output

Directory listing of GPO files:

Volume in drive \\example.com\SYSVOL is SYSVOL
Volume Serial Number is XXXX-XXXX

Directory of \\example.com\SYSVOL\example.com\Policies\{GUID}

[date] <DIR>          .
[date] <DIR>          ..
[date]     <DIR>          Machine
[date]     <DIR>          User

## Related

- [[procedures/Exploit-GPO-Scheduled-Tasks-Preferences]]
- [[commands/gpupdate-force-policy-update]]
