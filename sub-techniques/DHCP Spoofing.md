---
id: b867a123-7b57-4731-8661-44bf96b414b7
name: DHCP Spoofing
type: sub-technique
mitre_id: T1557.003
mitre_url: null
created_at: '2023-04-06T00:31:26.189327+00:00'
updated_at: '2023-04-06T00:31:26.189327+00:00'
parent_technique: '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
---

# DHCP Spoofing

**MITRE ID**: T1557.003

**Parent Technique**: [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]

This is a sub-technique of T1557 - Adversary-in-the-Middle.

## Summary

Adversaries may redirect network traffic to adversary-owned systems by spoofing Dynamic Host Configuration Protocol (DHCP) traffic and acting as a malicious DHCP server on the victim network. By achieving the adversary-in-the-middle (AiTM) position, adversaries may collect network communications, in

## Description

Adversaries may redirect network traffic to adversary-owned systems by spoofing Dynamic Host Configuration Protocol (DHCP) traffic and acting as a malicious DHCP server on the victim network. By achieving the adversary-in-the-middle (AiTM) position, adversaries may collect network communications, including passed credentials, especially those sent over insecure, unencrypted protocols. This may also enable follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040) or [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002).

DHCP is based on a client-server model and has two functionalities: a protocol for providing network configuration settings from a DHCP server to a client and a mechanism for allocating network addresses to clients.(Citation: rfc2131) The typical server-client interaction is as follows: 

1. The client broadcasts a `DISCOVER` message.

2. The server responds with an `OFFER` message, which includes an available network address. 

3. The client broadcasts a `REQUEST` message, which includes the network address offered. 

4. The server acknowledges with an `ACK` message and the client receives the network configuration parameters.

Adversaries may spoof as a rogue DHCP server on the victim network, from which legitimate hosts may receive malicious network configurations. For example, malware can act as a DHCP server and provide adversary-owned DNS servers to the victimized computers.(Citation: new_rogue_DHCP_serv_malware)(Citation: w32.tidserv.g) Through the malicious network configurations, an adversary may achieve the AiTM position, route client traffic through adversary-controlled systems, and collect information from the client network.

DHCPv6 clients can receive network configuration information without being assigned an IP address by sending a <code>INFORMATION-REQUEST (code 11)</code> message to the <code>All_DHCP_Relay_Agents_and_Servers</code> multicast address.(Citation: rfc3315) Adversaries may use their rogue DHCP server to respond to this request message with malicious network configurations.

Rather than establishing an AiTM position, adversaries may also abuse DHCP spoofing to perform a DHCP exhaustion attack (i.e, [Service Exhaustion Flood](https://attack.mitre.org/techniques/T1499/002)) by generating many broadcast DISCOVER messages to exhaust a network’s DHCP allocation pool. 

## Tactics

This sub-technique is used in the following tactics:

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
