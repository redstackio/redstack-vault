---
id: 226d731c-5fe5-4bf4-9bf1-ea355aa3b2ed
name: Chain multiple openquery
type: command
executor: bash
data: select version from openquery("link1",'select version from openquery("link2","select
  @@version as version")')
output: null
created_at: '2023-04-06T03:56:34.105354+00:00'
updated_at: '2023-04-10T20:22:42.442119+00:00'
---

# Chain multiple openquery

```bash
select version from openquery("link1",'select version from openquery("link2","select @@version as version")')
```
