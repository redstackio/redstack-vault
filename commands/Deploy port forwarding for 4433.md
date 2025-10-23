---
id: ed7cb3fa-ba02-4351-8624-d28a9b74a93d
name: Deploy port forwarding for 4433
type: command
executor: bash
data: './ngrok http 4433

  ./ngrok tcp 4433'
output: null
created_at: '2023-04-06T03:56:23.038395+00:00'
updated_at: '2023-04-10T20:25:15.147150+00:00'
---

# Deploy port forwarding for 4433

```bash
./ngrok http 4433
./ngrok tcp 4433
```


