---
id: f9e34fc8-6ce5-463a-90b3-29752fb26c9f
name: httprobe scan domains for active HTTP/HTTPS servers on custom ports
type: command
executor: bash
data: 'cat domains.txt | httprobe -p http:81 -p https:8443

  '
output: null
created_at: '2020-07-24T17:11:22.868604+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# httprobe scan domains for active HTTP/HTTPS servers on custom ports

```bash
cat domains.txt | httprobe -p http:81 -p https:8443

```
