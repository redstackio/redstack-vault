---
id: 44d65861-c679-47d4-ac7e-fa0a2ab583ec
name: ActiveDirectory List AD Users with SID
type: command
executor: powershell
data: Get-ADUser -Filter * | Select-Object -Property name,sid
output: "PS C:\\> Get-ADUser -Filter * | Select-Object -Property name,sid\n      \
  \                                    \nname                                    \
  \                      sid     \n----                                          \
  \                ---\nAdministrator                                            \
  \     S-1-5-21-3072663084-364016917-1341370565-500\nGuest                      \
  \                                   S-1-5-21-3072663084-364016917-1341370565-501\n\
  DefaultAccount                                                S-1-5-21-3072663084-364016917-1341370565-503\n\
  krbtgt                                                        S-1-5-21-3072663084-364016917-1341370565-502\n\
  Exchange Online-ApplicationAccount                            S-1-5-21-3072663084-364016917-1341370565-1123\n\
  SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}           S-1-5-21-3072663084-364016917-1341370565-1124"
created_at: '2020-03-20T22:38:48.722091+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ActiveDirectory List AD Users with SID

```powershell
Get-ADUser -Filter * | Select-Object -Property name,sid
```

## Expected Output

```
PS C:\> Get-ADUser -Filter * | Select-Object -Property name,sid

name                                                          sid     
----                                                          ---
Administrator                                                 S-1-5-21-3072663084-364016917-1341370565-500
Guest                                                         S-1-5-21-3072663084-364016917-1341370565-501
DefaultAccount                                                S-1-5-21-3072663084-364016917-1341370565-503
krbtgt                                                        S-1-5-21-3072663084-364016917-1341370565-502
Exchange Online-ApplicationAccount                            S-1-5-21-3072663084-364016917-1341370565-1123
SystemMailbox{1f05a927-89c0-4725-adca-4527114196a1}           S-1-5-21-3072663084-364016917-1341370565-1124
```
