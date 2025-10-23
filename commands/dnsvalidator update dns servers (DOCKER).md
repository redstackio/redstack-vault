---
id: 8b07685e-9f19-4168-9801-e334c5822830
name: dnsvalidator update dns servers (DOCKER)
type: command
executor: bash
data: docker run -v $(pwd):$_OUTPUT_DIRECTORY -t dnsvalidator -tL https://public-dns.info/nameservers.txt
  -threads $_THREADS -o $_OUTPUT_DIRECTORY/$_OUTPUT_RESULTS
output: "root@kali ~# docker run -v $(pwd):/dnsvalidator/output -t dnsvalidator -tL\
  \ https://public-dns.info/nameservers.txt -threads 20 -o /dnsvalidator/output/resolvers.txt\n\
  ... [CUT DOCKER INFO] ...\n=======================================================\n\
  dnsvalidator v0.1\tby James McLean (@vortexau) \n                \t& Michael Skelton\
  \ (@codingo_)\n=======================================================\n[22:10:53]\
  \ [INFO] [1.1.1.1] resolving baseline\n[22:10:53] [INFO] [8.8.8.8] resolving baseline\n\
  [22:10:54] [INFO] [9.9.9.9] resolving baseline\n... [CUT] ..."
created_at: '2020-06-30T02:34:45.156833+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
---

# dnsvalidator update dns servers (DOCKER)

```bash
docker run -v $(pwd):$_OUTPUT_DIRECTORY -t dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_DIRECTORY/$_OUTPUT_RESULTS
```

## Expected Output

```
root@kali ~# docker run -v $(pwd):/dnsvalidator/output -t dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 20 -o /dnsvalidator/output/resolvers.txt
... [CUT DOCKER INFO] ...
=======================================================
dnsvalidator v0.1	by James McLean (@vortexau) 
                	& Michael Skelton (@codingo_)
=======================================================
[22:10:53] [INFO] [1.1.1.1] resolving baseline
[22:10:53] [INFO] [8.8.8.8] resolving baseline
[22:10:54] [INFO] [9.9.9.9] resolving baseline
... [CUT] ...
```


