---
id: 2481a518-52d0-450a-9c9e-6ee7d873cf47
name: NSE Port 80 CVEs
type: command
executor: bash
data: 'nmap --script=http-vuln-cve* -p80 $ip

  '
output: null
created_at: '2020-07-14T18:15:19.608403+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NSE Port 80 CVEs

```bash
nmap --script=http-vuln-cve* -p80 $ip

```


