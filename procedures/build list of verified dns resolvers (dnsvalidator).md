---
id: b72460ae-da99-459e-a5e2-48753a8a8e80
name: build list of verified dns resolvers (dnsvalidator)
type: procedure
verified: null
submitted: true
created_at: '2020-06-30T02:51:19.652319+00:00'
updated_at: '2023-03-13T19:52:35.078857+00:00'
commands:
- '[[dnsvalidator update dns servers]]'
- '[[dnsvalidator update dns servers (DOCKER)]]'
- '[[sort and tail # of results]]'
---

# build list of verified dns resolvers (dnsvalidator)

**Status**: Submitted for Review

## Summary

You can use this tool to build a list of verified dns servers to be used in conjunction with other tools. This tool can take a while to run so, do it prior to your pentest and use lots of threads (20-200 should be good). This command will store the results in the output file. This file can be used 

## Description

# Description

You can use this tool to build a list of verified dns servers to be used in conjunction with other tools. 

This tool can take a while to run so, do it prior to your pentest and use lots of threads (20-200 should be good).



This command will store the results in the output file. This file can be used with dns enumeration tools like amass.







**Command** ([[dnsvalidator update dns servers]]):

```bash
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_FILE
```







There is a docker version available also, please check he tool page for the instruction to build the dnsvalidator docker container.





**Command** ([[dnsvalidator update dns servers (DOCKER)]]):

```bash
docker run -v $(pwd):$_OUTPUT_DIRECTORY -t dnsvalidator -tL https://public-dns.info/nameservers.txt -threads $_THREADS -o $_OUTPUT_DIRECTORY/$_OUTPUT_RESULTS
```







## Note

You can sort and copy only the number of resolvers you need from this list.





**Command** ([[sort and tail # of results]]):

```bash
cat $_FILE | sort | tail -n 25
```





## Commands Used

- [[dnsvalidator update dns servers]]
- [[dnsvalidator update dns servers (DOCKER)]]
- [[sort and tail # of results]]


