---
id: 2ea133ce-c10c-4468-be91-b5db2e7745fa
name: RDS Network ACL Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.411030+00:00'
updated_at: '2023-04-10T20:20:08.702450+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Enumeration]]'
- '[[Listing Network ACL''s]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe Network ACLs]]'
---

# RDS Network ACL Enumeration

## Summary

The RDS Network ACL Enumeration procedure involves listing the Network ACL's associated with an RDS instance. This technique can be used by an attacker to discover the network topology of a target environment, and identify potential targets for further exploitation. To perform this procedure, the a

## Description

# Description

The RDS Network ACL Enumeration procedure involves listing the Network ACL's associated with an RDS instance. This technique can be used by an attacker to discover the network topology of a target environment, and identify potential targets for further exploitation. To perform this procedure, the attacker would need to have valid credentials or access to an instance with appropriate permissions.

From a technical perspective, this procedure involves making API calls to the AWS RDS service to obtain information about the network ACL's associated with an RDS instance. This information can then be used to identify potential targets for further exploitation.

From a business perspective, this technique can be used to identify potential vulnerabilities in an organization's AWS environment, and can help inform decisions around security investments and risk management.

## Requirements

1. Valid AWS credentials or access to an instance with appropriate permissions

## Defense

1. Limit access to the AWS console and API to authorized personnel only

1. Implement least privilege access controls to limit the scope of potential attacks

1. Monitor network traffic for suspicious activity, such as repeated failed login attempts

## Objectives

1. Identify the network ACL's associated with an RDS instance

1. Discover the network topology of the target environment

1. Identify potential targets for further exploitation

# Instructions

1. This command retrieves the details of all the network ACLs in your AWS account.

The `describe-network-acls` command is used to retrieve the details of all the network access control lists (ACLs) in your AWS account. Network ACLs are an optional layer of security for your VPC that act as a firewall for controlling traffic in and out of one or more subnets. The command returns a JSON object that contains information such as the ID, name, and rules associated with each network ACL. You can use this information to troubleshoot network issues or to verify the configuration of your network ACLs.

**Command** ([[Describe Network ACLs]]):

```bash
aws ec2 describe-network-acls
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Describe Network ACLs]]

## Tags

- [[Enumeration]]
- [[Listing Network ACL's]]
- [[RDS - Relational Database Service]]
