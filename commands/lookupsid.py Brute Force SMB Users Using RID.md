---
id: fc0ae50f-6c12-4e92-a256-304b6af90dc1
name: lookupsid.py Brute Force SMB Users Using RID
type: command
executor: bash
data: lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
output: 'root@kali:~# lookupsid.py ''bob'':''secretpass''@10.10.10.10

  Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation


  [*] Brute forcing SIDs at 10.10.10.10

  [*] StringBinding ncacn_np:10.10.10.10[\pipe\lsarpc]

  [*] Domain SID is: S-1-5-21-4254423774-1266059056-3197185112

  500: Bob-PC\Administrator (SidTypeUser)

  501: Bob-PC\Guest (SidTypeUser)

  503: Bob-PC\DefaultAccount (SidTypeUser)

  504: Bob-PC\WDAGUtilityAccount (SidTypeUser)

  513: Bob-PC\None (SidTypeGroup)

  1008: Bob-PC\Bob (SidTypeUser)'
created_at: '2019-12-27T22:38:42.675982+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# lookupsid.py Brute Force SMB Users Using RID

```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Expected Output

```
root@kali:~# lookupsid.py 'bob':'secretpass'@10.10.10.10
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[*] Brute forcing SIDs at 10.10.10.10
[*] StringBinding ncacn_np:10.10.10.10[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-4254423774-1266059056-3197185112
500: Bob-PC\Administrator (SidTypeUser)
501: Bob-PC\Guest (SidTypeUser)
503: Bob-PC\DefaultAccount (SidTypeUser)
504: Bob-PC\WDAGUtilityAccount (SidTypeUser)
513: Bob-PC\None (SidTypeGroup)
1008: Bob-PC\Bob (SidTypeUser)
```


