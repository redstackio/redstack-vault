---
id: 90af0264-cf90-462c-9a68-fa67700ecd38
name: Find HTTP/HTTPS Servers (HTTProbe)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:22.899720+00:00'
updated_at: '2023-05-25T20:11:58.173791+00:00'
commands:
- '[[httprobe scan domains for active HTTP/HTTPS servers]]'
- '[[httprobe scan domains for active HTTP/HTTPS servers on custom ports]]'
---

# Find HTTP/HTTPS Servers (HTTProbe)

**Status**: ✓ Verified

## Summary

Probe a list of HTTP and HTTPS servers to find the active ones from a list of domains. httprobe 

## Description

# Description

Probe a list of HTTP and HTTPS servers to find the active ones from a list of domains.

[httprobe](https://github.com/tomnomnom/httprobe)





**Command** ([[httprobe scan domains for active HTTP/HTTPS servers]]):

```bash
cat recon/example/domains.txt | httprobe

```







**Command** ([[httprobe scan domains for active HTTP/HTTPS servers on custom ports]]):

```bash
cat domains.txt | httprobe -p http:81 -p https:8443

```





## Commands Used

- [[httprobe scan domains for active HTTP/HTTPS servers]]
- [[httprobe scan domains for active HTTP/HTTPS servers on custom ports]]


