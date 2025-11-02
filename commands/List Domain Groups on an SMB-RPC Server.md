---
id: 00953fbf-5f04-46e5-8bc5-21478a28af6d
name: List Domain Groups on an SMB/RPC Server
type: command
executor: default
data: enumdomgroups
output: "rpcclient $> enumdomgroups \ngroup:[Enterprise Read-only Domain Controllers]\
  \ rid:[0x1f2]\ngroup:[Domain Admins] rid:[0x200]\ngroup:[Domain Users] rid:[0x201]\n\
  group:[Domain Guests] rid:[0x202]\ngroup:[Domain Computers] rid:[0x203]\ngroup:[Domain\
  \ Controllers] rid:[0x204]\ngroup:[Schema Admins] rid:[0x206]\ngroup:[Enterprise\
  \ Admins] rid:[0x207]\n..."
created_at: '2020-03-26T05:23:16.576629+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[rpcclient]]'
---

# List Domain Groups on an SMB/RPC Server

```default
enumdomgroups
```

## Expected Output

```
rpcclient $> enumdomgroups 
group:[Enterprise Read-only Domain Controllers] rid:[0x1f2]
group:[Domain Admins] rid:[0x200]
group:[Domain Users] rid:[0x201]
group:[Domain Guests] rid:[0x202]
group:[Domain Computers] rid:[0x203]
group:[Domain Controllers] rid:[0x204]
group:[Schema Admins] rid:[0x206]
group:[Enterprise Admins] rid:[0x207]
...
```


