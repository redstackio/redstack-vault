---
id: 7159b747-083e-4f86-9648-369fe4e37b53
name: RDS Lateral Movement via VPC Peering Connections
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.434883+00:00'
updated_at: '2023-04-10T20:20:49.206858+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Lateral Movement and Pivoting]]'
- '[[Listing VPC peering connections]]'
- '[[RDS - Relational Database Service]]'
- '[[Scenario]]'
commands:
- '[[List VPC Peering Connections]]'
---

# RDS Lateral Movement via VPC Peering Connections

## Summary

RDS is a managed database service provided by AWS. Attackers can use VPC peering connections to pivot from one VPC to another and gain access to RDS instances. By listing VPC peering connections, an attacker can identify which VPCs are connected to the target VPC and attempt to exploit any vulnerab

## Description

# Description

RDS is a managed database service provided by AWS. Attackers can use VPC peering connections to pivot from one VPC to another and gain access to RDS instances. By listing VPC peering connections, an attacker can identify which VPCs are connected to the target VPC and attempt to exploit any vulnerabilities in those VPCs to gain access to RDS instances. This technique can be used for lateral movement within an organization's network.

Technical Explanation: VPC peering connections allow communication between VPCs in different accounts or regions. By listing VPC peering connections, an attacker can identify which VPCs are connected to the target VPC and attempt to exploit any vulnerabilities in those VPCs to gain access to RDS instances. The attacker can use tools such as Nmap to scan for open ports and services in the target VPC and connected VPCs.

Business Value: An attacker who gains access to RDS instances can steal sensitive data such as customer information, financial data, and intellectual property. This can result in reputational damage, loss of revenue, and legal penalties.

 

## Requirements

1. Access to AWS console or API

1. Knowledge of AWS networking and RDS

 

## Defense

1. Implement network segmentation to limit lateral movement

1. Monitor VPC peering connections for suspicious activity

1. Implement least privilege access controls to limit access to RDS instances

 

## Objectives

1. Identify VPC peering connections

1. Gain access to RDS instances

1. Perform lateral movement within the network

 

# Instructions

1. Use this command to describe the VPC peering connections that exist between two VPCs.

 

This command returns information about the specified VPC peering connections, including information about the requester VPC, accepter VPC, connection status, and any tags associated with the connection. You can use this command to troubleshoot connectivity issues between VPCs or to get an overview of the VPC peering connections in your account. Optional arguments include the IDs of the VPC peering connections to describe, filters to apply to the results, and flags to control the output format.



**Command** ([[List VPC Peering Connections]]):

```bash
aws ec2 describe-vpc-peering-connections
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[List VPC Peering Connections]]

## Tags

- [[Lateral Movement and Pivoting]]
- [[Listing VPC peering connections]]
- [[RDS - Relational Database Service]]
- [[Scenario]]


