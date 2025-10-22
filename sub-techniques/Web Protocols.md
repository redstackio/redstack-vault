---
id: 00669413-803d-44bc-8411-1db538a0c0ac
name: Web Protocols
type: sub-technique
mitre_id: T1071.001
mitre_url: null
created_at: '2023-04-06T00:31:27.054231+00:00'
updated_at: '2023-04-06T00:31:27.054231+00:00'
parent_technique: '[[Standard Application Layer Protocol|T1071 - Standard Application
  Layer Protocol]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[DNS Beacon Payload with Cobalt Strike]]'
- '[[Golang Reverse Shell Cheat Sheet]]'
- '[[PHP Bind Shell]]'
- '[[Python Bind Shell]]'
- '[[Python Reverse Shell Cheat Sheet]]'
- '[[SSH Tunneling and SOCKS Proxy]]'
- '[[Windows Staged Reverse TCP Meterpreter Shell]]'
- '[[XXE File Retrieval via XInclude Attack]]'
---

# Web Protocols

**MITRE ID**: T1071.001

**Parent Technique**: [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

This is a sub-technique of T1071 - Standard Application Layer Protocol.

## Summary

Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client

## Description

Adversaries may communicate using application layer protocols associated with web traffic to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as HTTP and HTTPS that carry web traffic may be very common in environments. HTTP/S packets have many fields and headers in which data can be concealed. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures

There are 8 procedures using this sub-technique:

- [[DNS Beacon Payload with Cobalt Strike]]
- [[Golang Reverse Shell Cheat Sheet]]
- [[PHP Bind Shell]]
- [[Python Bind Shell]]
- [[Python Reverse Shell Cheat Sheet]]
- [[SSH Tunneling and SOCKS Proxy]]
- [[Windows Staged Reverse TCP Meterpreter Shell]]
- [[XXE File Retrieval via XInclude Attack]]
