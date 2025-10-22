---
id: 6eca2d60-0c30-409e-bdbe-864b7c62f2a5
name: Look up ACL ACE from PowerView
type: command
executor: ''
data: "Get-DomainObjectACL -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_\
  \ | Add-Member NoteProperty 'IdentityName' $(Convert\x02SidToName $_.SecurityIdentifier);$_}\
  \ | ?{$_.IdentityName -match $GROUP_NAME1}\n"
output: null
created_at: '2023-01-12T07:34:23.268830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Look up ACL ACE from PowerView

```bash
Get-DomainObjectACL -Identity $GROUP_NAME2 -ResolveGUIDs | ForEach-Object {$_ | Add-Member NoteProperty 'IdentityName' $(ConvertSidToName $_.SecurityIdentifier);$_} | ?{$_.IdentityName -match $GROUP_NAME1}

```
