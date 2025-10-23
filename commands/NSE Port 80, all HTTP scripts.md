---
id: bb129ee0-02db-47b2-bed5-422df8e91ac2
name: NSE Port 80, all HTTP scripts
type: command
executor: bash
data: 'nmap --script=http-* -p 80 $ip

  '
output: null
created_at: '2020-07-14T18:15:19.608393+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# NSE Port 80, all HTTP scripts

```bash
nmap --script=http-* -p 80 $ip

```


