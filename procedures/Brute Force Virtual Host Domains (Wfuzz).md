---
id: 1420675d-0263-4f2f-9a8e-cdbd0407e5e0
name: Brute Force Virtual Host Domains (Wfuzz)
type: procedure
verified: true
submitted: true
created_at: '2019-10-17T21:12:56.080002+00:00'
updated_at: '2023-05-26T01:15:16.104150+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
platforms:
- Web
tags:
- '[[Brute Force]]'
- '[[Web Applications]]'
commands:
- '[[Wfuzz Brute Force DNS with the Host Parameter]]'
---

# Brute Force Virtual Host Domains (Wfuzz)

**Status**: ✓ Verified

## Summary

Some web applications use virtual hosts (vhosts) to serve different web sites depending on the domain being requested. These web apps can be fuzzed using the "Host" parameter of the header. 

## Description

# Description

Some web applications use virtual hosts (vhosts) to serve different web sites depending on the domain being requested. These web apps can be fuzzed using the "Host" parameter of the header.



# Instructions

Brute force subdomains using the header field.





**Command** ([[Wfuzz Brute Force DNS with the Host Parameter]]):

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP -H 'Host: FUZZ.$_DOMAIN'
```





## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Wfuzz Brute Force DNS with the Host Parameter]]

## Tags

- [[Brute Force]]
- [[Web Applications]]


