---
id: 780c1ced-9594-4a59-9042-26adfac12890
name: SSH Tunnels
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:22.731295+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# SSH Tunnels

**Command** ([[Send data over ssh to port 9000 on target]]):

```bash
ssh -L 8090:localhost:9000 james@123.123.123

```

**Command** ([[Send data over ssh to port 80 on target through jumphost]]):

```bash
ssh -A -t -p22 -L 8800:localhost:8800 james@123.001.123.321 -t ssh -L 8800:localhost:80 james@124.123.122

```

**Code**: [[
nano ~/.ssh/config
ControlMaster auto
ControlPath]]
