---
id: aaa1ed44-fb7f-4711-bba9-50d5e03793bc
name: AWS Metadata Key Grabbing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.373872+00:00'
updated_at: '2023-04-10T20:19:58.599948+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[AWS Metadata]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Grabbing the keys in metadata version 2]]'
- '[[Remote code execution]]'
commands:
- '[[Get EC2 Metadata with Token]]'
---

# AWS Metadata Key Grabbing

## Summary

AWS metadata is a service that provides information about an instance running on AWS. This includes sensitive information such as access keys, secret keys, and security group IDs. An attacker can exploit a vulnerability in metadata version 2 to retrieve these keys and use them to access other AWS r

## Description

# Description

AWS metadata is a service that provides information about an instance running on AWS. This includes sensitive information such as access keys, secret keys, and security group IDs. An attacker can exploit a vulnerability in metadata version 2 to retrieve these keys and use them to access other AWS resources. This can lead to data theft, data modification, and other malicious activities. To exploit this vulnerability, an attacker can use the 'Retrieve EC2 Instance Metadata with Token Authentication' command. This command allows an attacker to retrieve the access and secret keys from the metadata service.

## Requirements

1. Valid AWS authentication credentials

1. Access to a vulnerable instance running metadata version 2

## Defense

1. Ensure that instances are running the latest version of metadata

1. Limit access to instances and metadata service

1. Use IAM roles instead of access and secret keys

## Objectives

1. Retrieve AWS access and secret keys

1. Gain access to other resources within the AWS environment

# Instructions

1. To retrieve EC2 instance metadata with token authentication, follow these steps:
1. Execute the command to retrieve a token: 
curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"
2. Use the token to retrieve the metadata: 
curl -H "X-aws-ec2-metadata-token: <TOKEN>" http://169.254.169.254/latest/meta-data/

**Code**: [[TOKEN=`curl
X PUT "http://169.254.169.254/latest/ ]]

> This command retrieves metadata about the EC2 instance that the command is executed on. The first command retrieves a token that is valid for 6 hours (-H "X-aws-ec2-metadata-token-ttl-seconds: 21600"). The second command uses this token to retrieve the metadata. The metadata is returned in plain text format and includes information such as the instance ID, instance type, and public IP address. This command can be useful for troubleshooting and debugging issues on EC2 instances.

**Command** ([[Get EC2 Metadata with Token]]):

```bash
TOKEN=`curl
X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/meta-data/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Get EC2 Metadata with Token]]

## Tags

- [[AWS Metadata]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Grabbing the keys in metadata version 2]]
- [[Remote code execution]]
