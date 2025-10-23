---
id: 5e347377-8fd8-4f4d-a8bf-081eb57cf67c
name: Integrate shodan-hq with nmap
type: command
executor: bash
data: nmap --script shodan-hq.nse --script-args 'apikey=<yourShodanAPIKey>,target=<hackme>'
output: null
created_at: '2023-04-06T03:56:21.737230+00:00'
updated_at: '2023-04-10T20:21:17.936731+00:00'
---

# Integrate shodan-hq with nmap

```bash
nmap --script shodan-hq.nse --script-args 'apikey=<yourShodanAPIKey>,target=<hackme>'
```


