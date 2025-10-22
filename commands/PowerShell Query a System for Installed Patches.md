---
id: 11bdb499-96f7-40b2-ae8c-40cde2548b89
name: PowerShell Query a System for Installed Patches
type: command
executor: powershell
data: Get-HotFix | Sort-Object HotFixID
output: 'PS C:\ > Get-HotFix | Sort-Object HotFixID

  Source        Description      HotFixID      InstalledBy          InstalledOn

  ------        -----------      --------      -----------          -----------

  BOB-PC        Security Update  KB4503308                          7/9/2019 12:00:00
  AM

  BOB-PC        Update           KB4506472                          7/9/2019 12:00:00
  AM

  BOB-PC        Security Update  KB4509096                          7/9/2019 12:00:00
  AM

  BOB-PC        Security Update  KB4515383     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00
  AM

  BOB-PC        Update           KB4515871     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00
  AM

  BOB-PC        Security Update  KB4516115     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00
  AM

  BOB-PC        Update           KB4517389     NT AUTHORITY\SYSTEM  10/21/2019 12:00:00
  AM

  BOB-PC        Security Update  KB4520390     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00
  AM

  BOB-PC        Security Update  KB4521863     NT AUTHORITY\SYSTEM  10/14/2019 12:00:00
  AM'
created_at: '2020-01-28T04:36:44.473064+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Query a System for Installed Patches

```powershell
Get-HotFix | Sort-Object HotFixID
```

## Expected Output

```
PS C:\ > Get-HotFix | Sort-Object HotFixID

Source        Description      HotFixID      InstalledBy          InstalledOn
------        -----------      --------      -----------          -----------
BOB-PC        Security Update  KB4503308                          7/9/2019 12:00:00 AM
BOB-PC        Update           KB4506472                          7/9/2019 12:00:00 AM
BOB-PC        Security Update  KB4509096                          7/9/2019 12:00:00 AM
BOB-PC        Security Update  KB4515383     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00 AM
BOB-PC        Update           KB4515871     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00 AM
BOB-PC        Security Update  KB4516115     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00 AM
BOB-PC        Update           KB4517389     NT AUTHORITY\SYSTEM  10/21/2019 12:00:00 AM
BOB-PC        Security Update  KB4520390     NT AUTHORITY\SYSTEM  10/5/2019 12:00:00 AM
BOB-PC        Security Update  KB4521863     NT AUTHORITY\SYSTEM  10/14/2019 12:00:00 AM
```
