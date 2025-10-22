---
id: 2dcab9d7-c636-4597-8cf6-78068743486f
name: wfuzz fuzz a single url
type: command
executor: bash
data: 'wfuzz -c -f re -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://domain.htb"
  -H "Host: FUZZ.domain.htb" --hh 311\

  '
output: null
created_at: '2020-07-24T17:11:40.367567+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# wfuzz fuzz a single url

```bash
wfuzz -c -f re -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://domain.htb" -H "Host: FUZZ.domain.htb" --hh 311\

```
