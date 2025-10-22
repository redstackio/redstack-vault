---
id: 146dcb47-57ca-434f-ad7a-0ee228c0ee99
name: OS Exhaustion Flood
type: sub-technique
mitre_id: T1499.001
mitre_url: null
created_at: '2023-04-06T00:31:25.524761+00:00'
updated_at: '2023-04-06T00:31:25.524761+00:00'
parent_technique: '[[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# OS Exhaustion Flood

**MITRE ID**: T1499.001

**Parent Technique**: [[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]

This is a sub-technique of T1499 - Endpoint Denial of Service.

## Summary

Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS). A system's OS is responsible for managing the finite resources as well as preventing the entire system from being overwhelmed by excessive demands on its capacity. These attacks do not need to exha

## Description

Adversaries may launch a denial of service (DoS) attack targeting an endpoint's operating system (OS). A system's OS is responsible for managing the finite resources as well as preventing the entire system from being overwhelmed by excessive demands on its capacity. These attacks do not need to exhaust the actual resources on a system; the attacks may simply exhaust the limits and available resources that an OS self-imposes.

Different ways to achieve this exist, including TCP state-exhaustion attacks such as SYN floods and ACK floods.(Citation: Arbor AnnualDoSreport Jan 2018) With SYN floods, excessive amounts of SYN packets are sent, but the 3-way TCP handshake is never completed. Because each OS has a maximum number of concurrent TCP connections that it will allow, this can quickly exhaust the ability of the system to receive new requests for TCP connections, thus preventing access to any TCP service provided by the server.(Citation: Cloudflare SynFlood)

ACK floods leverage the stateful nature of the TCP protocol. A flood of ACK packets are sent to the target. This forces the OS to search its state table for a related TCP connection that has already been established. Because the ACK packets are for connections that do not exist, the OS will have to search the entire state table to confirm that no match exists. When it is necessary to do this for a large flood of packets, the computational requirements can cause the server to become sluggish and/or unresponsive, due to the work it must do to eliminate the rogue ACK packets. This greatly reduces the resources available for providing the targeted service.(Citation: Corero SYN-ACKflood)

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]
