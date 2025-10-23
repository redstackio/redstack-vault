---
id: b9e9873d-7ed3-49d3-98b0-5ff2e3a8d8ba
name: Windows Add a User to the Local Administrators Group
type: command
executor: command_prompt
data: net localgroup Administrators $_USERNAME /add
output: 'C:\Windows\system32> net localgroup Administrators hacker /add

  The command completed successfully.'
created_at: '2019-11-14T00:19:34.666164+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Windows Add a User to the Local Administrators Group

```command_prompt
net localgroup Administrators $_USERNAME /add
```

## Expected Output

```
C:\Windows\system32> net localgroup Administrators hacker /add
The command completed successfully.
```


