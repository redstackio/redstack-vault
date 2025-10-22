---
id: 78a8a8bc-0434-49ed-bc61-d8eec61b5ffd
name: 'RDS Lateral Movement: List Instances on Specified Subnet'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.536026+00:00'
updated_at: '2023-04-10T20:20:58.371390+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Lateral Movement and Pivoting]]'
- '[[Listing instances on the specified subnet]]'
- '[[RDS - Relational Database Service]]'
- '[[Scenario]]'
commands:
- '[[Describe EC2 instances in a specific subnet]]'
---

# RDS Lateral Movement: List Instances on Specified Subnet

## Summary

This procedure involves listing instances on a specified subnet in order to identify potential targets for lateral movement. An attacker may use this technique to identify instances that can be used to pivot into other areas of the network. By identifying RDS instances on the subnet, an attacker ca

## Description

# Description

This procedure involves listing instances on a specified subnet in order to identify potential targets for lateral movement. An attacker may use this technique to identify instances that can be used to pivot into other areas of the network. By identifying RDS instances on the subnet, an attacker can potentially gain access to sensitive data stored in the databases. 

To execute this procedure, the attacker would use the 'List EC2 Instances in a Subnet' command to identify instances on the subnet. From there, the attacker can use other techniques to gain access to the instances and move laterally through the network. 

The business value of this procedure is that it allows an attacker to gain access to sensitive data stored in RDS instances. This can lead to data theft, data manipulation, and other malicious activities.

## Requirements

1. Access to the AWS console or API

1. Knowledge of the subnet to be targeted

1. Authentication credentials or other means of accessing the instances

## Defense

1. Limit access to the AWS console or API to authorized personnel only

1. Implement network segmentation to limit lateral movement

1. Monitor network traffic for signs of suspicious activity

## Objectives

1. Identify instances on a specified subnet

1. Use identified instances to pivot into other areas of the network

1. Gain access to sensitive data stored in RDS instances

# Instructions

1. To list all the EC2 instances in a specific subnet, use the following command:

This command uses the AWS CLI to describe all EC2 instances that are running in a specific subnet. Replace 'ID' with the ID of the subnet you want to list the instances for. The output will contain detailed information about each EC2 instance, including its ID, instance type, launch time, and more.

**Command** ([[Describe EC2 instances in a specific subnet]]):

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=ID"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Describe EC2 instances in a specific subnet]]

## Tags

- [[Lateral Movement and Pivoting]]
- [[Listing instances on the specified subnet]]
- [[RDS - Relational Database Service]]
- [[Scenario]]
