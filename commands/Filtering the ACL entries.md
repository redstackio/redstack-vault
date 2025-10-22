---
id: 9380d669-b3f2-44b5-ba1c-6bdd3c141da7
name: Filtering the ACL entries
type: command
executor: bash
data: Get-DomainObjectAcl -Identity "SuperSecureGPO" -ResolveGUIDs |  Where-Object
  {($_.ActiveDirectoryRights.ToString() -match "GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner")}
output: null
created_at: '2023-04-06T03:56:03.622769+00:00'
updated_at: '2023-04-10T20:25:53.418574+00:00'
---

# Filtering the ACL entries

```bash
Get-DomainObjectAcl -Identity "SuperSecureGPO" -ResolveGUIDs |  Where-Object {($_.ActiveDirectoryRights.ToString() -match "GenericWrite|AllExtendedWrite|WriteDacl|WriteProperty|WriteMember|GenericAll|WriteOwner")}
```
