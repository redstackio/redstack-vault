---
id: 55063317-1a6c-47ba-87c7-c902dbd24d06
name: Install socat and forward traffic to team server
type: command
executor: bash
data: 'sudo apt install socat

  socat TCP4-LISTEN:80,fork TCP4:[TEAM SERVER]:80'
output: null
created_at: '2023-04-06T03:56:16.271092+00:00'
updated_at: '2023-04-10T20:36:24.222219+00:00'
---

# Install socat and forward traffic to team server

```bash
sudo apt install socat
socat TCP4-LISTEN:80,fork TCP4:[TEAM SERVER]:80
```


