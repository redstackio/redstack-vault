---
id: c8aa8259-2575-4064-9d33-0aa5fad92eac
name: Chisel Deploy a SOCKS5 Client (Attacker)
type: command
executor: ''
data: chisel client $_TARGET_IP:$_TARGET_PORT socks
output: 'root@kali:~# ./chisel client 10.10.10.10:9001 socks

  2019/10/01 21:08:14 client: Connecting to ws://10.10.10.10:9001

  2019/10/01 21:08:14 client: proxy#1:127.0.0.1:1080=>socks: Listening

  2019/10/01 21:08:14 client: Fingerprint 79:03:39:25:50:c4:72:48:b3:80:35:1f:5f:9d:50:09

  2019/10/01 21:08:14 client: Connected (Latency 393.56µs)'
created_at: '2019-10-02T01:17:50.994902+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Chisel]]'
---

# Chisel Deploy a SOCKS5 Client (Attacker)

```bash
chisel client $_TARGET_IP:$_TARGET_PORT socks
```

## Expected Output

```
root@kali:~# ./chisel client 10.10.10.10:9001 socks
2019/10/01 21:08:14 client: Connecting to ws://10.10.10.10:9001
2019/10/01 21:08:14 client: proxy#1:127.0.0.1:1080=>socks: Listening
2019/10/01 21:08:14 client: Fingerprint 79:03:39:25:50:c4:72:48:b3:80:35:1f:5f:9d:50:09
2019/10/01 21:08:14 client: Connected (Latency 393.56µs)
```


