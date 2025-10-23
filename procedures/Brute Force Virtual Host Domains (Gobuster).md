---
id: fca07e91-ed6c-4cf7-becb-eb974b1175ac
name: Brute Force Virtual Host Domains (Gobuster)
type: procedure
verified: true
submitted: true
created_at: '2020-04-27T20:55:00.019928+00:00'
updated_at: '2023-05-26T18:53:14.843649+00:00'
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
- '[[Gobuster Brute Force DNS with the Host Parameter]]'
---

# Brute Force Virtual Host Domains (Gobuster)

**Status**: ✓ Verified

## Summary

Some web applications use virtual hosts (vhosts) to serve different web sites depending on the domain being requested. These web apps can be fuzzed using the "Host" parameter of the header. 

## Description

# Description

Some web applications use virtual hosts (vhosts) to serve different web sites depending on the domain being requested. These web apps can be fuzzed using the "Host" parameter of the header.



# Instructions





**Command** ([[Gobuster Brute Force DNS with the Host Parameter]]):

```bash
gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST
```



Note: Gobuster automatically prepends each guess to the $_TARGET_HOST argument. For example: GUESS.baseurl.com. In some situations, it may be necessary to hard code the IP and FQDN relationship in the /etc/hosts file.



## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Gobuster Brute Force DNS with the Host Parameter]]

## Tags

- [[Brute Force]]
- [[Web Applications]]


