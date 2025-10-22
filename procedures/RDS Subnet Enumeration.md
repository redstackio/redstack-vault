---
id: ff123c96-1bc0-4fb0-9c37-edfd5a3e9ad0
name: RDS Subnet Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.302623+00:00'
updated_at: '2023-04-10T20:20:22.878774+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing subnet''s]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[List Subnets]]'
---

# RDS Subnet Enumeration

## Summary

RDS is a managed database service offered by AWS. Attackers can use the 'EC2 Describe Subnets' command to enumerate subnets in the target environment that are used by RDS instances. This can be used to identify potential targets for further attacks. 

The attacker can use this technique to gain a b

## Description

# Description

RDS is a managed database service offered by AWS. Attackers can use the 'EC2 Describe Subnets' command to enumerate subnets in the target environment that are used by RDS instances. This can be used to identify potential targets for further attacks. 

The attacker can use this technique to gain a better understanding of the target environment and identify potential attack paths. By identifying the subnets used by RDS instances, the attacker can focus their efforts on exploiting those subnets and the instances within them. This technique can be used as a precursor to other attacks, such as lateral movement or data exfiltration.

From a business perspective, this technique can help identify potential security weaknesses in the target environment and allow for proactive mitigation before an actual attack occurs.

## Requirements

1. Access to the AWS CLI

1. Permissions to run the 'EC2 Describe Subnets' command

## Defense

1. Limit access to the AWS CLI and restrict permissions for running the 'EC2 Describe Subnets' command

1. Implement network segmentation to reduce the attack surface for RDS instances

1. Monitor network traffic for unusual activity related to RDS instances

## Objectives

1. Identify subnets used by RDS instances in the target environment

1. Gain a better understanding of the target environment

# Instructions

1. The `aws ec2 describe-subnets` command is used to retrieve information about all subnets in a VPC. This command requires the `ec2:DescribeSubnets` permission.

The `aws ec2 describe-subnets` command returns a JSON object containing information about all subnets in a VPC. This includes the subnet ID, VPC ID, availability zone, CIDR block, and any associated tags. You can filter the results by specifying one or more subnet IDs, VPC IDs, or CIDR blocks. For example, to retrieve information about a specific subnet, you can use the `--subnet-ids` parameter followed by the subnet ID. You can also use the `--filters` parameter to specify multiple filters.

**Command** ([[List Subnets]]):

```bash
aws ec2 describe-subnets
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[List Subnets]]

## Tags

- [[Enumeration]]
- [[Listing subnet's]]
- [[RDS - Relational Database Service]]
