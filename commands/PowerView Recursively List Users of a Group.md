---
id: 3e5b763e-487a-4c9a-aad5-bfdfd93cb3e6
name: PowerView Recursively List Users of a Group
type: command
executor: powershell
data: Get-DomainGroupMember -Identity "$_GROUP" -Recurse
output: 'PS C:\> Get-DomainGroupMember -Identity "Domain Admins" -Recurse



  GroupDomain             : DEV.TESLA.LOCAL

  GroupName               : Domain Admins

  GroupDistinguishedName  : CN=Domain Admins,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  MemberDomain            : DEV.TESLA.LOCAL

  MemberName              : dave

  MemberDistinguishedName : CN=dave,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  MemberObjectClass       : user

  MemberSID               : S-1-5-21-1576920733-1301476157-954876328-1107


  GroupDomain             : DEV.TESLA.LOCAL

  GroupName               : Domain Admins

  GroupDistinguishedName  : CN=Domain Admins,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  MemberDomain            : DEV.TESLA.LOCAL

  MemberName              : Administrator

  MemberDistinguishedName : CN=Administrator,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  MemberObjectClass       : user

  MemberSID               : S-1-5-21-1576920733-1301476157-954876328-500'
created_at: '2020-07-01T22:54:44.508232+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[PowerView]]'
- '[[ps]]'
---

# PowerView Recursively List Users of a Group

```powershell
Get-DomainGroupMember -Identity "$_GROUP" -Recurse
```

## Expected Output

```
PS C:\> Get-DomainGroupMember -Identity "Domain Admins" -Recurse


GroupDomain             : DEV.TESLA.LOCAL
GroupName               : Domain Admins
GroupDistinguishedName  : CN=Domain Admins,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
MemberDomain            : DEV.TESLA.LOCAL
MemberName              : dave
MemberDistinguishedName : CN=dave,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
MemberObjectClass       : user
MemberSID               : S-1-5-21-1576920733-1301476157-954876328-1107

GroupDomain             : DEV.TESLA.LOCAL
GroupName               : Domain Admins
GroupDistinguishedName  : CN=Domain Admins,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
MemberDomain            : DEV.TESLA.LOCAL
MemberName              : Administrator
MemberDistinguishedName : CN=Administrator,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
MemberObjectClass       : user
MemberSID               : S-1-5-21-1576920733-1301476157-954876328-500
```


