---
id: 3e4a130a-44b2-4783-963a-d398ee5c5d74
name: Combine Custom DNS Wordlist
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:30.913532+00:00'
updated_at: '2023-05-26T00:48:53.058161+00:00'
commands:
- '[[dnsgen combine domain names from the provided input]]'
---

# Combine Custom DNS Wordlist

**Status**: ✓ Verified

## Summary

Generate a combination of domain names from the provided input. dnsgen 

## Description

# Description

Generate a combination of domain names from the provided input.

[dnsgen](https://github.com/ProjectAnte/dnsgen)





**Command** ([[dnsgen combine domain names from the provided input]]):

```bash
cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J --flush 2>/dev/null

```





## Commands Used

- [[dnsgen combine domain names from the provided input]]


