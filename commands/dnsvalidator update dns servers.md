---
id: 2a348104-5b4e-4c74-a8ae-005d4285c876
name: dnsvalidator update dns servers
type: command
executor: bash
data: dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS
  -o $_OUTPUT_FILE
output: "root@kali ~# dnsvalidator -tL https://public-dns.info/nameservers.txt -threads\
  \ 20 -o resolvers.txt\n=======================================================\n\
  dnsvalidator v0.1\tby James McLean (@vortexau) \n                \t& Michael Skelton\
  \ (@codingo_)\n=======================================================\n[22:10:53]\
  \ [INFO] [1.1.1.1] resolving baseline\n[22:10:53] [INFO] [8.8.8.8] resolving baseline\n\
  [22:10:54] [INFO] [9.9.9.9] resolving baseline\n... [CUT] ..."
created_at: '2020-06-30T02:34:45.156623+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
tools:
- '[[dnsvalidator]]'
---

# dnsvalidator update dns servers

```bash
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_FILE
```

## Expected Output

```
root@kali ~# dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o resolvers.txt
=======================================================
dnsvalidator v0.1	by James McLean (@vortexau) 
                	& Michael Skelton (@codingo_)
=======================================================
[22:10:53] [INFO] [1.1.1.1] resolving baseline
[22:10:53] [INFO] [8.8.8.8] resolving baseline
[22:10:54] [INFO] [9.9.9.9] resolving baseline
... [CUT] ...
```


