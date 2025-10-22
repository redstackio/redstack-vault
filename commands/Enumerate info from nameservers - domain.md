---
id: 63ae88e3-cf7e-4d75-a569-661a7a869a14
name: Enumerate info from nameservers / domain
type: command
executor: bash
data: 'host -t mx domain.com

  host -t ns domain.com

  '
output: null
created_at: '2020-07-14T18:14:45.647931+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate info from nameservers / domain

```bash
host -t mx domain.com
host -t ns domain.com

```
