---
id: 52eaa3c9-b844-465f-8321-abbb91e6c070
name: altdns mutate sub domain wordlist and output resolved hosts
type: command
executor: bash
data: 'altdns -i subdomains.txt -o data_output -w words.txt -r -s results_output.txt

  '
output: null
created_at: '2020-07-24T17:11:37.192020+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# altdns mutate sub domain wordlist and output resolved hosts

```bash
altdns -i subdomains.txt -o data_output -w words.txt -r -s results_output.txt

```
