---
id: f9531b85-2692-4842-8a96-40c2c144c086
name: SMBMap list guest access tricks
type: command
executor: ''
data: 'smbmap -U ''%'' -L //$DC_IP

  smbmap -U ''guest%'' -L //$DC_IP'
output: null
created_at: '2023-01-11T20:23:08.317997+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SMBMap list guest access tricks

```bash
smbmap -U '%' -L //$DC_IP
smbmap -U 'guest%' -L //$DC_IP
```


