---
id: c562c864-1009-4a0a-8e6a-70525df7d968
name: ' xcopy Download Files from a Remote SMB'
type: command
executor: command_prompt
data: xcopy \\$_REMOTE_IP\$_SHARE\$_FILENAME .
output: 'C:\>xcopy \\10.10.10.100\files\secrets .

  \\10.10.10.100\files\secrets

  1 File(s) copied

  '
created_at: '2019-11-25T23:00:09.678942+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[xcopy]]'
---

#  xcopy Download Files from a Remote SMB

```command_prompt
xcopy \\$_REMOTE_IP\$_SHARE\$_FILENAME .
```

## Expected Output

```
C:\>xcopy \\10.10.10.100\files\secrets .
\\10.10.10.100\files\secrets
1 File(s) copied

```


