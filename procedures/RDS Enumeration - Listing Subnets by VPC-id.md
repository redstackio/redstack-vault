---
id: aebb8591-3729-45ae-9bf1-cf5648a617e5
name: RDS Enumeration - Listing Subnets by VPC-id
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.330540+00:00'
updated_at: '2023-04-10T20:20:08.351850+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Resource Development|TA0042 - Resource Development]]'
techniques:
- '[[Acquire Infrastructure|T1583 - Acquire Infrastructure]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Enumeration]]'
- '[[Listing subnet''s by VPC-id]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe Subnets]]'
---

# RDS Enumeration - Listing Subnets by VPC-id

## Summary

RDS Enumeration - Listing Subnets by VPC-id is a technique used by attackers to identify subnets associated with a particular VPC-id. Attackers can use this information to identify potential targets for further attacks. This technique involves using the EC2 Describe Subnets command to list all subn

## Description

# Description

RDS Enumeration - Listing Subnets by VPC-id is a technique used by attackers to identify subnets associated with a particular VPC-id. Attackers can use this information to identify potential targets for further attacks. This technique involves using the EC2 Describe Subnets command to list all subnets associated with a particular VPC-id. This information can be used to identify potential targets for further attacks, such as identifying vulnerable databases or other resources.

From a technical perspective, this technique is relatively simple. Attackers can use the AWS CLI or other tools to execute the EC2 Describe Subnets command and obtain a list of subnets associated with a particular VPC-id. Attackers can then use this information to identify potential targets for further attacks.

From a business perspective, this technique can be used by attackers to identify potential targets for further attacks. By identifying vulnerable databases or other resources, attackers can gain access to sensitive data or disrupt critical business operations.

 

## Requirements

1. Access to AWS CLI or other tools

1. Access to EC2 Describe Subnets command

1. Access to VPC-id

 

## Defense

1. Ensure that VPCs are properly configured and secured

1. Implement network segmentation to limit access to sensitive resources

1. Monitor network traffic for signs of suspicious activity

 

## Objectives

1. Identify subnets associated with a particular VPC-id

1. Identify potential targets for further attacks

 

# Instructions

1. This command is used to describe the subnets in an Amazon Virtual Private Cloud (VPC).

 

The `aws ec2 describe-subnets` command is used to retrieve information about the subnets in a specified VPC. The `--filters` option is used to filter the results based on certain criteria. In this case, we are filtering by the VPC ID with the value `ID`. This command will return a JSON object containing information about each subnet, including its ID, availability zone, CIDR block, and more.



**Command** ([[Describe Subnets]]):

```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=ID"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Resource Development|TA0042 - Resource Development]]

### Techniques

- [[Acquire Infrastructure|T1583 - Acquire Infrastructure]]
- [[External Remote Services|T1133 - External Remote Services]]

## Commands Used

- [[Describe Subnets]]

## Tags

- [[Enumeration]]
- [[Listing subnet's by VPC-id]]
- [[RDS - Relational Database Service]]


