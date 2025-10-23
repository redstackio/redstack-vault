---
id: edb80866-fd03-41e1-8319-ac813597dee2
name: RDS Enumeration - Listing VPCs in us-west-1 region
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.256582+00:00'
updated_at: '2023-04-10T20:20:58.012407+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing VPC''s specifing the region]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe VPCs in us-west-1 region]]'
---

# RDS Enumeration - Listing VPCs in us-west-1 region

## Summary

This procedure involves listing all Virtual Private Clouds (VPCs) in the us-west-1 region that are associated with the Amazon RDS service. This information can be used to identify potential targets for further attacks. To accomplish this, the user will need to have access to the AWS console or API 

## Description

# Description

This procedure involves listing all Virtual Private Clouds (VPCs) in the us-west-1 region that are associated with the Amazon RDS service. This information can be used to identify potential targets for further attacks. To accomplish this, the user will need to have access to the AWS console or API credentials. This procedure has the potential to provide valuable information for an attacker, including potentially sensitive data stored in the RDS instances.

Technical Description: The attacker will use the AWS CLI or AWS Management Console to list all VPCs in the us-west-1 region that are associated with the Amazon RDS service. This information could be used to identify potential targets for further attacks or to gain a better understanding of the target's infrastructure.

Business Value: This procedure can provide valuable information to an attacker, allowing them to identify potential targets for further attacks and gain a better understanding of the target's infrastructure. Organizations can take steps to secure their AWS environment by monitoring for unusual activity and limiting access to sensitive data.

 

## Requirements

1. Access to the AWS console or API credentials

 

## Defense

1. Monitor AWS environment for unusual activity

1. Limit access to sensitive data

1. Implement strong authentication measures for AWS console and API access

 

## Objectives

1. Identify potential targets for further attacks

1. Gain a better understanding of the target's infrastructure

 

# Instructions

1. To list all the VPCs in the us-west-1 region, run the following command:

 

This command is used to describe all the VPCs in the specified region. The --region parameter is used to specify the region for which the VPCs are to be listed. This command returns a JSON object containing information about all the VPCs in the specified region.



**Command** ([[Describe VPCs in us-west-1 region]]):

```bash
aws ec2 describe-vpcs --region us-west-1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe VPCs in us-west-1 region]]

## Tags

- [[Enumeration]]
- [[Listing VPC's specifing the region]]
- [[RDS - Relational Database Service]]


