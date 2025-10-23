---
id: 6d7635ae-c7d1-4125-b1e7-1d3e7539821a
name: Chisel Deploy a Reverse Port Forwarding Server
type: command
executor: bash
data: chisel server -p $_LISTEN_PORT --reverse
output: 'root@kali:~# ./chisel server -p 9001 --reverse

  2019/10/01 19:56:38 server: Reverse tunnelling enabled

  2019/10/01 19:56:38 server: Fingerprint 85:91:1f:ed:c1:0b:f4:b5:01:e1:56:8d:d1:fb:d6:71

  2019/10/01 19:56:38 server: Listening on 0.0.0.0:9001...'
created_at: '2019-10-02T01:17:50.992676+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Chisel Deploy a Reverse Port Forwarding Server

```bash
chisel server -p $_LISTEN_PORT --reverse
```

## Expected Output

```
root@kali:~# ./chisel server -p 9001 --reverse
2019/10/01 19:56:38 server: Reverse tunnelling enabled
2019/10/01 19:56:38 server: Fingerprint 85:91:1f:ed:c1:0b:f4:b5:01:e1:56:8d:d1:fb:d6:71
2019/10/01 19:56:38 server: Listening on 0.0.0.0:9001...
```


