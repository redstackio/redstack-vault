---
id: b72270d9-c049-4af4-ac4e-7f01ecca511d
name: Port Knocking
type: sub-technique
mitre_id: T1205.001
mitre_url: null
created_at: '2023-04-06T00:31:26.528824+00:00'
updated_at: '2023-04-06T00:31:26.528824+00:00'
parent_technique: '[[Port Knocking|T1205 - Port Knocking]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Port Knocking

**MITRE ID**: T1205.001

**Parent Technique**: [[Port Knocking|T1205 - Port Knocking]]

This is a sub-technique of T1205 - Port Knocking.

## Summary

Adversaries may use port knocking to hide open ports used for persistence or command and control. To enable a port, an adversary sends a series of attempted connections to a predefined sequence of closed ports. After the sequence is completed, opening a port is often accomplished by the host based f

## Description

Adversaries may use port knocking to hide open ports used for persistence or command and control. To enable a port, an adversary sends a series of attempted connections to a predefined sequence of closed ports. After the sequence is completed, opening a port is often accomplished by the host based firewall, but could also be implemented by custom software.

This technique has been observed both for the dynamic opening of a listening port as well as the initiating of a connection to a listening server on a different system.

The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r (Citation: Hartrell cd00r 2002), is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
