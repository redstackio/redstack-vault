---
id: ae31d4af-afba-48fa-beb4-6558cea8dbcc
name: Port Knocking
type: technique
mitre_id: T1205
mitre_url: null
created_at: '2019-08-28T21:17:35.215791+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[DB2 Injection - Time Delay]]'
---

# Port Knocking

**MITRE ID**: T1205

## Description

Port Knocking is a well-established method used by both defenders and adversaries to hide open ports from access. To enable a port, an adversary sends a series of packets with certain characteristics before the port will be opened. Usually this series of packets consists of attempted connections to a predefined sequence of closed ports, but can involve unusual flags, specific strings or other unique characteristics. After the sequence is completed, opening a port is often accomplished by the host based firewall, but could also be implemented by custom software. This technique has been observed to both for the dynamic opening of a listening port as well as the initiating of a connection to a listening server on a different system.The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r [1], is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.

# Detection

Record network packets sent to and from the system, looking for extraneous packets that do not belong to established flows.

# Mitigation

Mitigation of some variants of this technique could be achieved through the use of stateful firewalls, depending upon how it is implemented.

# Footnotes

[1] Hartrell, Greg. (2002, August). Get a handle on cd00r: The invisible backdoor. Retrieved October 13, 2018.

[2] Sebastian Feldmann. (2018, February 14). Chaos: a Stolen Backdoor Rising Again. Retrieved March 5, 2018.

[3] Fernando Mercês. (2016, September 5). Pokémon-themed Umbreon Linux Rootkit Hits x86, ARM Systems. Retrieved March 5, 2018.

## Defense

Mitigation of some variants of this technique could be achieved through the use of stateful firewalls, depending upon how it is implemented.

## Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (1)

- [[DB2 Injection - Time Delay]]
