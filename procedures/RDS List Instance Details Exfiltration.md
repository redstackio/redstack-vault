---
id: 96f57a27-7aa5-49e7-9c14-218108ae37ab
name: RDS List Instance Details Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.968596+00:00'
updated_at: '2023-04-10T20:19:50.611806+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
tags:
- '[[Data exfiltration]]'
- '[[List instances in RDS]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Describe RDS Instances]]'
---

# RDS List Instance Details Exfiltration

## Summary

The RDS List Instance Details Exfiltration procedure involves an attacker listing instances in the Amazon Web Services (AWS) Relational Database Service (RDS) in order to exfiltrate data. This procedure can be used to identify and exfiltrate sensitive data stored in RDS instances. Attackers can use

## Description

# Description

The RDS List Instance Details Exfiltration procedure involves an attacker listing instances in the Amazon Web Services (AWS) Relational Database Service (RDS) in order to exfiltrate data. This procedure can be used to identify and exfiltrate sensitive data stored in RDS instances. Attackers can use this procedure to gain access to sensitive data such as user credentials, personally identifiable information (PII), and other confidential data.

To execute this procedure, the attacker needs to have access to the AWS console or API credentials. The attacker can use the 'AWS RDS DB Instance Details' command to list all the RDS instances in the targeted AWS account. The output of this command can be used to identify the RDS instances that contain sensitive data. Once the attacker has identified the target RDS instance, they can exfiltrate the data using various methods such as SQL injection or by copying the data to a different location within the same AWS account or to a different AWS account.

The business value of this procedure is that attackers can gain access to sensitive data stored in RDS instances, which can be used for various purposes such as identity theft, financial fraud, and espionage.

## Requirements

1. Access to the AWS console or API credentials

## Defense

1. Limit access to the AWS console and API credentials to authorized personnel only

1. Implement network segmentation to limit access to RDS instances

1. Monitor network traffic for any unusual activity or data exfiltration attempts

## Objectives

1. Identify and list all RDS instances in the targeted AWS account

1. Exfiltrate sensitive data stored in the RDS instances

# Instructions

1. To retrieve details of one or more Amazon RDS DB instances, run the following command:

This command retrieves details of one or more Amazon RDS DB instances. Use this command to get information about DB instances such as engine type, endpoint, instance class, availability zone, and more. The command takes no arguments, but you can use filters to narrow down the results. For example, you can filter by DB instance identifier, engine type, status, and more. For more information about the available filters, see the AWS documentation.

**Command** ([[Describe RDS Instances]]):

```bash
aws rds describe-db-instances
```

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]

## Commands Used

- [[Describe RDS Instances]]

## Tags

- [[Data exfiltration]]
- [[List instances in RDS]]
- [[RDS - Relational Database Service]]
