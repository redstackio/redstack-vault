---
id: f26bb0e4-7d90-492a-aab5-15e9425411c1
name: amass db list previous scans
type: command
executor: bash
data: amass db -dir $_OUTPUT_DIRECTORY -list
output: 'root@kali ~# amass db -dir owasp.org/ -list

  1) 06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT: owasp.org, 2.ip6.arpa, 178.in-addr.arpa,
  159.in-addr.arpa

  2) 06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT: owasp.org, 178.in-addr.arpa,
  2.ip6.arpa, 159.in-addr.arpa

  3) 06/29 13:22:13 2020 EDT -> 06/29 13:24:55 2020 EDT: 159.in-addr.arpa, 2.ip6.arpa,
  178.in-addr.arpa, owasp.org'
created_at: '2020-06-29T18:05:44.399891+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass db list previous scans

```bash
amass db -dir $_OUTPUT_DIRECTORY -list
```

## Expected Output

```
root@kali ~# amass db -dir owasp.org/ -list
1) 06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT: owasp.org, 2.ip6.arpa, 178.in-addr.arpa, 159.in-addr.arpa

2) 06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT: owasp.org, 178.in-addr.arpa, 2.ip6.arpa, 159.in-addr.arpa

3) 06/29 13:22:13 2020 EDT -> 06/29 13:24:55 2020 EDT: 159.in-addr.arpa, 2.ip6.arpa, 178.in-addr.arpa, owasp.org
```
