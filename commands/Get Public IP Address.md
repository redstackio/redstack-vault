---
id: 0c85dcf4-87a3-4783-ba0b-38ffb6756ac1
name: Get Public IP Address
type: command
executor: bash
data: http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text
output: null
created_at: '2023-04-06T03:56:38.548449+00:00'
updated_at: '2023-04-10T20:23:56.681624+00:00'
---

# Get Public IP Address

```bash
http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text
```


