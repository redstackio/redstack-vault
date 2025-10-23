---
id: ea9edc75-ade5-4c9d-85ae-e145585d6b55
name: Sniff Unencrypted LDAP Queries via the Loopback
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T21:17:13.602531+00:00'
updated_at: '2023-05-25T19:46:39.379615+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Sniffing|T1040 - Network Sniffing]]'
platforms:
- Linux
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[tcpdump Intercept Packets on Loopback Interface]]'
- '[[Tshark Extract Hex and ASCII Dump from a Pcap]]'
---

# Sniff Unencrypted LDAP Queries via the Loopback

**Status**: ✓ Verified

## Summary

Some versions of LDAP send unencrypted queries over the loopback address. If an attacker is able to sniff traffic locally while LDAP requests are being generated, it may be possible to intercept plaintext credentials. 

## Description

# Description

Some versions of LDAP send unencrypted queries over the loopback address. If an attacker is able to sniff traffic locally while LDAP requests are being generated, it may be possible to intercept plaintext credentials.



# Instructions

1. Set up tcpdump to sniff for LDAP requests (port 389) on the loopback interface.





**Command** ([[tcpdump Intercept Packets on Loopback Interface]]):

```bash
tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
```



2. Trigger and/or wait for an LDAP query to be intercepted.

3. Review the pcap file for plaintext passwords.





**Command** ([[Tshark Extract Hex and ASCII Dump from a Pcap]]):

```bash
tshark -r $_DUMP.pcap -x
```





4. Analyze the results for credentials.

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Sniffing|T1040 - Network Sniffing]]

## Commands Used

- [[tcpdump Intercept Packets on Loopback Interface]]
- [[Tshark Extract Hex and ASCII Dump from a Pcap]]

## Tags

- [[data exposure]]
- [[Network]]


