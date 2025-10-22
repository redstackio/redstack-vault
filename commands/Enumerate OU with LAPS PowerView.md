---
id: a9b24e80-3402-4721-81af-e064ea076ae6
name: Enumerate OU with LAPS PowerView
type: command
executor: ''
data: "Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | Where\x02Object {($_.ObjectAceType\
  \ -like 'ms-Mcs-AdmPwd') -and \n($_.ActiveDirectoryRights -match 'ReadProperty')}\
  \ | ForEach-Object {$_ | Add\x02Member NoteProperty 'IdentityName' $(Convert-SidToName\
  \ \n$_.SecurityIdentifier);$_}"
output: '(...)

  ObjectAceType: ms-Mcs-AdmPwd

  (...)'
created_at: '2023-01-12T18:59:53.015414+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate OU with LAPS PowerView

```bash
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | WhereObject {($_.ObjectAceType -like 'ms-Mcs-AdmPwd') -and 
($_.ActiveDirectoryRights -match 'ReadProperty')} | ForEach-Object {$_ | AddMember NoteProperty 'IdentityName' $(Convert-SidToName 
$_.SecurityIdentifier);$_}
```

## Expected Output

```
(...)
ObjectAceType: ms-Mcs-AdmPwd
(...)
```
