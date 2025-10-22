---
id: 69b1f115-2baf-44c1-aae6-f73f54791783
name: wmic Get a Group's SID from Active Directory
type: command
executor: command_prompt
data: wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain
output: 'C:\>wmic.exe group where name="Enterprise Admins" get name,sid,domain

  Domain  Name               SID

  TESLA   Enterprise Admins  S-1-5-21-3428605742-3005092657-1212549955-519'
created_at: '2023-03-14T05:28:32.527173+00:00'
updated_at: '2023-03-14T06:02:49.008864+00:00'
---

# wmic Get a Group's SID from Active Directory

```command_prompt
wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain
```

## Expected Output

```
C:\>wmic.exe group where name="Enterprise Admins" get name,sid,domain
Domain  Name               SID
TESLA   Enterprise Admins  S-1-5-21-3428605742-3005092657-1212549955-519
```
