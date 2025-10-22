---
id: 54525dea-2a18-4acd-af86-0114efd5e1b0
name: TCP Redirection (socat)
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:06.545825+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# TCP Redirection (socat)

**Command** ([[Simple TCP Port Redirection]]):

```bash
socat TCP-LISTEN:80,fork TCP::80

```

**Command** ([[UDP Port Redirection]]):

```bash
socat udp4-recvfrom:53,reuseaddr,fork udp4-sendto:; echo -ne

```
