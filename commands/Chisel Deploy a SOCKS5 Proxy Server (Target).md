---
id: 806f4c36-f7d6-46c7-863e-9d9b21467e6c
name: Chisel Deploy a SOCKS5 Proxy Server (Target)
type: command
executor: ''
data: chisel server -p $_LISTEN_PORT --socks5
output: "bob@ubuntu18x64:~$ ./chisel server -p 9001 --socks5 \n2019/10/02 01:08:13\
  \ server: SOCKS5 server enabled\n2019/10/02 01:08:13 server: Fingerprint 79:03:39:25:50:c4:72:48:b3:80:35:1f:5f:9d:50:09\n\
  2019/10/02 01:08:13 server: Listening on 0.0.0.0:9001..."
created_at: '2019-10-02T01:17:50.993800+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Chisel]]'
---

# Chisel Deploy a SOCKS5 Proxy Server (Target)

```bash
chisel server -p $_LISTEN_PORT --socks5
```

## Expected Output

```
bob@ubuntu18x64:~$ ./chisel server -p 9001 --socks5 
2019/10/02 01:08:13 server: SOCKS5 server enabled
2019/10/02 01:08:13 server: Fingerprint 79:03:39:25:50:c4:72:48:b3:80:35:1f:5f:9d:50:09
2019/10/02 01:08:13 server: Listening on 0.0.0.0:9001...
```


