---
id: 2b962d35-6902-47c4-8636-8c25c58655f3
name: massdns find cnames for online subdomains
type: command
executor: bash
data: 'massdns -r massdns/lists/resolvers.txt -t CNAME -o S -w paypal.massdns.cnames
  paypal.subdomains

  '
output: null
created_at: '2020-07-24T17:11:26.640368+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# massdns find cnames for online subdomains

```bash
massdns -r massdns/lists/resolvers.txt -t CNAME -o S -w paypal.massdns.cnames paypal.subdomains

```
