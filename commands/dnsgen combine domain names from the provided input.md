---
id: bbf0de6b-746f-4496-9e2d-3a9c7e3e03a7
name: dnsgen combine domain names from the provided input
type: command
executor: bash
data: 'cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J --flush
  2>/dev/null

  '
output: null
created_at: '2020-07-24T17:11:30.890757+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dnsgen combine domain names from the provided input

```bash
cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J --flush 2>/dev/null

```


