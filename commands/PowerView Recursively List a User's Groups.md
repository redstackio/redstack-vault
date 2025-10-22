---
id: 124ef92e-2968-4c9d-a2e0-dc3e508a18fb
name: PowerView Recursively List a User's Groups
type: command
executor: powershell
data: Get-DomainGroup -MemberIdentity $_USER
output: 'PS C:\> Get-DomainGroup -MemberIdentity dave

  grouptype              : DOMAIN_LOCAL_SCOPE, SECURITY

  iscriticalsystemobject : True

  samaccounttype         : ALIAS_OBJECT

  samaccountname         : Denied RODC Password Replication Group

  whenchanged            : 7/1/2020 9:39:46 PM

  objectsid              : S-1-5-21-1576920733-1301476157-954876328-572

  objectclass            : {top, group}

  cn                     : Denied RODC Password Replication Group

  ...'
created_at: '2020-07-01T22:54:44.510303+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Recursively List a User's Groups

```powershell
Get-DomainGroup -MemberIdentity $_USER
```

## Expected Output

```
PS C:\> Get-DomainGroup -MemberIdentity dave

grouptype              : DOMAIN_LOCAL_SCOPE, SECURITY
iscriticalsystemobject : True
samaccounttype         : ALIAS_OBJECT
samaccountname         : Denied RODC Password Replication Group
whenchanged            : 7/1/2020 9:39:46 PM
objectsid              : S-1-5-21-1576920733-1301476157-954876328-572
objectclass            : {top, group}
cn                     : Denied RODC Password Replication Group
...
```
