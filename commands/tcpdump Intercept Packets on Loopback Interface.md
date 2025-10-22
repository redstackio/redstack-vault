---
id: 49050e1d-dc03-4106-91df-bdf554795820
name: tcpdump Intercept Packets on Loopback Interface
type: command
executor: bash
data: tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
output: 'kali:~# tcpdump -i lo -w dump2.pcap -c 10 port 389

  tcpdump: listening on lo, link-type EN10MB (Ethernet), capture size 262144 bytes

  10 packets captured

  22 packets received by filter

  0 packets dropped by kernel'
created_at: '2019-10-09T21:17:13.469264+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# tcpdump Intercept Packets on Loopback Interface

```bash
tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
```

## Expected Output

```
kali:~# tcpdump -i lo -w dump2.pcap -c 10 port 389
tcpdump: listening on lo, link-type EN10MB (Ethernet), capture size 262144 bytes
10 packets captured
22 packets received by filter
0 packets dropped by kernel
```
