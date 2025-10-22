---
id: c064f88a-085e-4bc5-bb1a-4e5a40ed0c54
name: PowerView Add Active Directory Group Privileges
type: command
executor: powershell
data: Add-DomainGroupMember -Identity '$_GROUP' -Members '$_USER'
output: PS C:\> Add-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS' -Members
  'bob'
created_at: '2020-03-16T01:01:25.836298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Add Active Directory Group Privileges

```powershell
Add-DomainGroupMember -Identity '$_GROUP' -Members '$_USER'
```

## Expected Output

```
PS C:\> Add-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS' -Members 'bob'
```
