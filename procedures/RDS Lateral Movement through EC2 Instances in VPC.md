---
id: 379b36c5-484a-441e-9d13-a7e2bf96af7d
name: RDS Lateral Movement through EC2 Instances in VPC
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.511741+00:00'
updated_at: '2023-04-10T20:20:17.683928+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Lateral Movement and Pivoting]]'
- '[[Listing instances on the specified VPC ID]]'
- '[[RDS - Relational Database Service]]'
- '[[Scenario]]'
commands:
- '[[Describe EC2 instances in VPC]]'
---

# RDS Lateral Movement through EC2 Instances in VPC

## Summary

This procedure involves using the EC2 instances in a specified VPC to pivot into the RDS instance. An attacker can use this method to move laterally within the network and gain access to sensitive data stored in the RDS instance. The attacker can use various tools and techniques to discover the VPC

## Description

# Description

This procedure involves using the EC2 instances in a specified VPC to pivot into the RDS instance. An attacker can use this method to move laterally within the network and gain access to sensitive data stored in the RDS instance. The attacker can use various tools and techniques to discover the VPC ID and then list all the EC2 instances within that VPC. Once the EC2 instance has been identified, the attacker can use it to pivot into the RDS instance.

To execute this procedure, the attacker needs to have access to the network and knowledge of the VPC ID. The attacker can use various reconnaissance techniques to discover the VPC ID. Once the VPC ID is known, the attacker can use the AWS CLI or other tools to list all the EC2 instances within that VPC. The attacker can then use the EC2 instance to pivot into the RDS instance.

This procedure can be used by attackers to gain access to sensitive data stored in the RDS instance. It is important to secure the network and limit access to the RDS instance to prevent lateral movement.

## Requirements

1. Access to the network

1. Knowledge of the VPC ID

1. AWS CLI or other tools to list EC2 instances

## Defense

1. Limit access to the RDS instance to prevent lateral movement

1. Implement network segmentation to limit the attacker's ability to move laterally

1. Monitor network traffic for any signs of unauthorized access

## Objectives

1. List all EC2 instances within a specified VPC

1. Pivot into the RDS instance using an EC2 instance

# Instructions

1. To get a list of EC2 instances in a specific VPC, use the following command:

This command uses the AWS CLI to describe EC2 instances in a specific VPC. Replace 'ID' with the actual VPC ID. The command returns a list of instances with their details such as instance ID, instance type, and launch time.

**Command** ([[Describe EC2 instances in VPC]]):

```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=ID"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe EC2 instances in VPC]]

## Tags

- [[Lateral Movement and Pivoting]]
- [[Listing instances on the specified VPC ID]]
- [[RDS - Relational Database Service]]
- [[Scenario]]
