---
id: 36cfabad-156e-4047-a7da-906a98119fa2
name: Windows Add a New User
type: command
executor: command_prompt
data: net user $_USERNAME $_PASSWORD /add
output: 'C:\Windows\system32>net user hacker hacker /add

  The command completed successfully.'
created_at: '2019-11-14T00:19:34.662723+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Windows Add a New User

```command_prompt
net user $_USERNAME $_PASSWORD /add
```

## Expected Output

```
C:\Windows\system32>net user hacker hacker /add
The command completed successfully.
```


