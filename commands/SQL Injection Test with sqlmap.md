---
id: 7de45e0f-3a57-455c-8ebf-71348145a503
name: SQL Injection Test with sqlmap
type: command
executor: bash
data: sqlmap -u "http://example.com/" --crawl=1 --random-agent --batch --forms --threads=5
  --level=5 --risk=3
output: null
created_at: '2023-04-06T03:56:36.369227+00:00'
updated_at: '2023-04-10T20:24:17.691223+00:00'
---

# SQL Injection Test with sqlmap

```bash
sqlmap -u "http://example.com/" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3
```


