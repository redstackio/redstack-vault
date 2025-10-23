---
id: 22d72f23-c86e-4338-aca7-fc053c1bcd02
name: pivot via sshuttle
type: command
executor: bash
data: 'sshuttle -vr <via-ssh-server> <Remote-Net-To-Route>

  sshuttle -vr username@target-ip 10.1.1.0/24

  '
output: null
created_at: '2020-07-14T18:14:29.550571+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# pivot via sshuttle

```bash
sshuttle -vr <via-ssh-server> <Remote-Net-To-Route>
sshuttle -vr username@target-ip 10.1.1.0/24

```


