---
id: b34b3453-5907-48b8-99dd-68c147018f4d
name: File Transfer Protocols
type: sub-technique
mitre_id: T1071.002
mitre_url: null
created_at: '2023-04-06T00:31:26.610084+00:00'
updated_at: '2023-04-06T00:31:26.610084+00:00'
parent_technique: '[[Standard Application Layer Protocol|T1071 - Standard Application
  Layer Protocol]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# File Transfer Protocols

**MITRE ID**: T1071.002

**Parent Technique**: [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

This is a sub-technique of T1071 - Standard Application Layer Protocol.

## Summary

Adversaries may communicate using application layer protocols associated with transferring files to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the

## Description

Adversaries may communicate using application layer protocols associated with transferring files to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as FTP, FTPS, and TFTP that transfer files may be very common in environments.  Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the transferred files. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
