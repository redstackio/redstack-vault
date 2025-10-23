---
id: e4f7aca1-c140-41ee-9dd0-f7f5b83c2602
name: HTTP DoS (Slowloris)
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T18:17:44.970363+00:00'
updated_at: '2023-05-26T01:23:52.034781+00:00'
platforms:
- Web
tags:
- '[[DOS]]'
- '[[Web Applications]]'
commands:
- '[[Clone slowloris]]'
- '[[Slowloris]]'
---

# HTTP DoS (Slowloris)

**Status**: ✓ Verified

## Summary

Description Slowloris DoS techniques involves a techniques where it opens multiple socket connections to the target and keep them open as long as possible. It will send partial HTTP requests which are never completed.The server opens multiple connections waiting for each connection to be completed,

## Description

Description

Slowloris DoS techniques involves a techniques where it opens multiple socket connections to the target and keep them open as long as possible. It will send partial HTTP requests which are never completed.The server opens multiple connections waiting for each connection to be completed, thus exhausting the resources of the server.





Instructions





1. Slowloris can be installed with the follwoing command on linux machine uaing git clone.







**Command** ([[Clone slowloris]]):

```bash
git clone https://github.com/gkbrk/slowloris.git
```









2. Once installed run the following command 









**Command** ([[Slowloris]]):

```bash
python3 slowloris.py [website url] -s [number of sockets]
```



 3. Notice that the application's load time increases and significantly leads to DoS



## Platforms

- Web

## Commands Used

- [[Clone slowloris]]
- [[Slowloris]]

## Tags

- [[DOS]]
- [[Web Applications]]


