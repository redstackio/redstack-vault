---
id: 23ecfcd3-16db-445f-9ad1-81337fe3847d
name: Run Python client with NTLM proxy
type: command
executor: bash
data: python client.py --server-ip [server ip] --server-port 9443 --ntlm-proxy-ip
  [proxy ip] --ntlm-proxy-port 8080 --domain CORP --username jdoe --hashes 986D46921DDE3E58E03656362614DEFE:50C189A98FF73B39AAD3B435B51404EE
output: null
created_at: '2023-04-06T03:56:22.867185+00:00'
updated_at: '2023-04-10T20:25:21.419917+00:00'
---

# Run Python client with NTLM proxy

```bash
python client.py --server-ip [server ip] --server-port 9443 --ntlm-proxy-ip [proxy ip] --ntlm-proxy-port 8080 --domain CORP --username jdoe --hashes 986D46921DDE3E58E03656362614DEFE:50C189A98FF73B39AAD3B435B51404EE
```
