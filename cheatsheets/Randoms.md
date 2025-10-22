---
id: a70b7dce-9ae8-4deb-af3e-803e3b20b459
name: Randoms
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:28.785815+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Randoms

**Command** ([[Start p0f, listent on an interface, and write out a log file]]):

```bash
p0f -i eth0 -p -o /tmp/p0f.log

```

p0f try to determine Host OS based on network packets.

**Command** ([[Split pcaps into multiple tcp connection files]]):

```bash
tcpflow -a -o tcpflow -r pcapvil1.pcap

```
