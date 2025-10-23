---
id: 2fa50f66-1199-4678-9dde-5e81471d318a
name: AWS EC2 Metadata SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.266408+00:00'
updated_at: '2023-04-10T20:20:49.560227+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[AWS - Metadata SSRF]]'
- '[[Cloud - AWS]]'
- '[[Method for Elastic Cloud Compute (EC2)]]'
commands:
- '[[List of Instance Metadata]]'
---

# AWS EC2 Metadata SSRF

## Summary

AWS EC2 Metadata SSRF is a technique used to obtain sensitive information from EC2 instances running in the cloud. An attacker can use SSRF (Server-Side Request Forgery) to send a crafted request to the EC2 metadata service, which can result in the disclosure of sensitive information such as AWS te

## Description

# Description

AWS EC2 Metadata SSRF is a technique used to obtain sensitive information from EC2 instances running in the cloud. An attacker can use SSRF (Server-Side Request Forgery) to send a crafted request to the EC2 metadata service, which can result in the disclosure of sensitive information such as AWS temporary access keys. This technique can be used to gain access to other AWS services and resources, leading to further compromise.

To execute this technique, an attacker needs to have network access to the EC2 instance and send a crafted request to the instance metadata service. The attacker can then extract temporary access keys, which can be used to access other AWS resources.

This technique can be used to gain access to sensitive data stored in EC2 instances, as well as other AWS services and resources. It can also be used to pivot to other systems in the cloud environment.

 

## Requirements

1. Access to the EC2 instance's network

1. Ability to send crafted requests

 

## Defense

1. Restrict network access to EC2 instances to trusted sources only

1. Implement network segmentation to limit access to sensitive resources

1. Monitor and analyze network traffic for suspicious activity

 

## Objectives

1. Obtain sensitive information from EC2 instances

1. Gain access to other AWS services and resources

 

# Instructions

1. To access the metadata of an EC2 instance, make a GET request to the following URL: http://169.254.169.254/latest/meta-data. This will return a list of available metadata categories. To retrieve specific metadata, append the category name to the URL.

 



**Code**: [[ami-id
ami-launch-index
ami-manifest-path
block-de]]



> The `ami-id` command returns the ID of the Amazon Machine Image (AMI) used to launch the instance. The `ami-launch-index` command returns the index of this instance in the reservation. The `ami-manifest-path` command returns the path to the AMI manifest file in Amazon S3. The `block-device-mapping/` command returns a list of block device mappings associated with the instance. The `events/` command returns a list of available event categories. The `hostname` command returns the instance hostname. The `iam/` command returns the instance's IAM role. The `identity-credentials/` command returns the temporary security credentials associated with the instance. The `instance-action` command returns the last action performed on the instance. The `instance-id` command returns the ID of the instance.



**Command** ([[List of Instance Metadata]]):

```bash
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hostname
iam/
identity-credentials/
instance-action
instance-id
```



2. To extract the temporary keys for an AWS role, use the following command:

aws ec2 instance-metadata --iam --query 'InstanceProfileArn' --output text | cut -d '/' -f 2

This will return the name of the role that is currently assigned to the EC2 instance. You can then use the following command to extract the temporary keys for that role:

curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>

 



**Code**: [[{
"Code" : "Success",
"LastUpdated" : "2019-07-31T]]



> The AWS Temporary Key Extraction command is used to extract temporary security credentials for an AWS role assigned to an EC2 instance. These credentials are required to access AWS resources using the permissions associated with the role. The command consists of two steps - first, extracting the name of the role assigned to the instance, and second, using that name to extract the temporary keys associated with the role.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[List of Instance Metadata]]

## Tags

- [[AWS - Metadata SSRF]]
- [[Cloud - AWS]]
- [[Method for Elastic Cloud Compute (EC2)]]


