---
id: 1fffd502-c988-4518-a28d-265052190fca
name: Mail Protocols
type: sub-technique
mitre_id: T1071.003
mitre_url: null
created_at: '2023-04-06T00:31:26.145224+00:00'
updated_at: '2023-04-06T00:31:26.145224+00:00'
parent_technique: '[[Standard Application Layer Protocol|T1071 - Standard Application
  Layer Protocol]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Mail Protocols

**MITRE ID**: T1071.003

**Parent Technique**: [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

This is a sub-technique of T1071 - Standard Application Layer Protocol.

## Summary

Adversaries may communicate using application layer protocols associated with electronic mail delivery to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic betwe

## Description

Adversaries may communicate using application layer protocols associated with electronic mail delivery to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. 

Protocols such as SMTP/S, POP3/S, and IMAP that carry electronic mail may be very common in environments.  Packets produced from these protocols may have many fields and headers in which data can be concealed. Data could also be concealed within the email messages themselves. An adversary may abuse these protocols to communicate with systems under their control within a victim network while also mimicking normal, expected traffic. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
