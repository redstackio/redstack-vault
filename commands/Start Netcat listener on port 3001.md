---
id: 05b08393-2277-4a4d-b066-bca3943ed944
name: Start Netcat listener on port 3001
type: command
executor: bash
data: stty raw -echo; (stty size; cat) | nc -lvnp 3001
output: null
created_at: '2023-04-06T03:56:25.077213+00:00'
updated_at: '2023-04-10T20:25:27.754209+00:00'
---

# Start Netcat listener on port 3001

```bash
stty raw -echo; (stty size; cat) | nc -lvnp 3001
```


