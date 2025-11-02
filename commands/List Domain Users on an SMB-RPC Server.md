---
id: 7fc5c2f5-1018-4a34-94df-fbb78ec1e5b5
name: List Domain Users on an SMB/RPC Server
type: command
executor: default
data: enumdomusers
output: 'rpcclient $> enumdomusers

  user:[games] rid:[0x3f2]

  user:[nobody] rid:[0x1f5]

  user:[bind] rid:[0x4ba]

  user:[proxy] rid:[0x402]

  user:[syslog] rid:[0x4b4

  user:[root] rid:[0x3e8]'
created_at: '2019-09-18T22:53:24.469030+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[rpcclient]]'
---

# List Domain Users on an SMB/RPC Server

```default
enumdomusers
```

## Expected Output

```
rpcclient $> enumdomusers
user:[games] rid:[0x3f2]
user:[nobody] rid:[0x1f5]
user:[bind] rid:[0x4ba]
user:[proxy] rid:[0x402]
user:[syslog] rid:[0x4b4
user:[root] rid:[0x3e8]
```


