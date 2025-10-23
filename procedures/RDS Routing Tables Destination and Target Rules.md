---
id: 1889f531-e49c-4eab-984b-95f56ecd5500
name: RDS Routing Tables Destination and Target Rules
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.208798+00:00'
updated_at: '2023-04-10T20:20:48.819458+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[RDS - Relational Database Service]]'
- '[[Routing Tables]]'
commands:
- '[[Destination Target]]'
---

# RDS Routing Tables Destination and Target Rules

## Summary

The RDS Routing Tables Destination and Target Rules procedure is used to redirect traffic to a specific target. This can be used to bypass network security controls and gain access to sensitive data stored in RDS instances. By modifying the destination and target rules in the routing table, an atta

## Description

# Description

The RDS Routing Tables Destination and Target Rules procedure is used to redirect traffic to a specific target. This can be used to bypass network security controls and gain access to sensitive data stored in RDS instances. By modifying the destination and target rules in the routing table, an attacker can redirect traffic to their own malicious server, allowing them to capture data in transit. This technique can be used to gain access to credentials, sensitive data, and other resources.

 

## Requirements

1. Access to the RDS instance

1. Knowledge of the routing table

 

## Defense

1. Implement strict network segmentation to prevent lateral movement

1. Monitor network traffic for suspicious activity

1. Enforce strong authentication mechanisms to prevent unauthorized access to RDS instances

 

## Objectives

1. Redirect traffic to a malicious server

1. Capture sensitive data in transit

 

# Instructions

1. To use these rules, specify the destination and target for each traffic flow. The available destinations are: local, igw, nat, pcx, vpce, vgw, and eni. The available targets depend on the destination selected.

 

When traffic enters a VPC, it needs to be directed to its destination. This is done using destination and target rules. The destination specifies where the traffic is going, while the target specifies how the traffic will get there. For example, if the destination is 'local', the target will be the VPC's internal IP addresses. If the destination is 'igw', the target will be the Internet Gateway. These rules are used to determine how traffic flows within a VPC network.



**Command** ([[Destination Target]]):

```bash
IP          local -> VPC Internal
IP          igw   -> Internet Gateway
IP          nat   -> NAT Gateway
IP          pcx   -> VPC Peering
IP          vpce  -> VPC Endpoint
IP          vgw   -> VPN Gateway
IP          eni   -> Network Interface
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Destination Target]]

## Tags

- [[RDS - Relational Database Service]]
- [[Routing Tables]]


