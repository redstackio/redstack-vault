---
id: e65c4b3a-1440-4b53-b868-bf58a05a3eb1
name: Cloud Instance SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.287620+00:00'
updated_at: '2023-04-10T20:23:57.942289+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for AWS Elastic Beanstalk]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Access Key ID]]'
- '[[Generate Access Token]]'
- '[[List S3 bucket contents]]'
- '[[Region]]'
- '[[Retrieve Account ID]]'
- '[[Retrieve AWS IAM Security Credentials]]'
- '[[Retrieve EC2 Instance Identity Document]]'
- '[[Retrieve Security Credentials]]'
---

# Cloud Instance SSRF

## Summary

Cloud Instance SSRF is a technique used to exploit a vulnerability in web applications that allows attackers to send crafted requests from the server to other resources on the network. Attackers can use this technique to bypass firewalls and access sensitive resources in the cloud environment, such

## Description

# Description

Cloud Instance SSRF is a technique used to exploit a vulnerability in web applications that allows attackers to send crafted requests from the server to other resources on the network. Attackers can use this technique to bypass firewalls and access sensitive resources in the cloud environment, such as AWS Elastic Beanstalk. The technical explanation of this technique is that the attacker sends a crafted request to the server, which in turn sends a request to the targeted resource with a manipulated URL. The response from the targeted resource is then returned to the attacker. The business value of this attack is that it can lead to data theft, unauthorized access, and disruption of services.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the vulnerable parameter

## Defense

1. Implement input validation and sanitization to prevent crafted requests

1. Restrict access to sensitive resources

1. Monitor network traffic for suspicious activity

## Objectives

1. Gain unauthorized access to cloud resources

1. Steal sensitive data

1. Disrupt cloud services

# Instructions

1. Use the account id to retrieve the account information

**Code**: [[accountId]]

> The accountId field should be filled with the unique identifier of the account you want to retrieve. This command will return the account information associated with the provided accountId.

**Command** ([[Retrieve Account ID]]):

```bash
accountId
```

2. Use this command to concatenate the 'region' field with the provided 'text' field.

**Code**: [[region]]

> The 'region' field will be combined with the 'text' field provided in the command. The resulting string will be used in further processing or display. Make sure to provide a valid 'text' field to avoid unexpected results.

**Command** ([[Region]]):

```bash
us-west-2
```

3. To retrieve AWS instance identity and security credentials, run the following commands:

**Code**: [[http://169.254.169.254/latest/dynamic/instance-ide]]

> The first URL, http://169.254.169.254/latest/dynamic/instance-identity/document, will return a JSON document containing information about the instance's identity, such as the instance ID, region, and account ID. The second URL, http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role, will return the security credentials for the IAM role associated with the instance. These credentials can be used to make AWS API calls from within the instance.

**Command** ([[Retrieve EC2 Instance Identity Document]]):

```bash
http://169.254.169.254/latest/dynamic/instance-identity/document
```

**Command** ([[Retrieve AWS IAM Security Credentials]]):

```bash
http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role
```

4. To retrieve the Access Key ID, you will need to navigate to the AWS Management Console and go to the IAM service. From there, select the user whose Access Key ID you want to retrieve and click on the 'Security credentials' tab. Under the 'Access keys' section, you will find the Access Key ID.

**Code**: [[AccessKeyId]]

> The Access Key ID is a unique identifier that is used to access AWS services programmatically. It is a combination of an access key and a secret access key, which are used to sign programmatic requests to AWS services.

**Command** ([[Access Key ID]]):

```bash
AccessKeyId
```

5. To use AWS services, you need to provide your Access Key ID and Secret Access Key to authenticate your requests.

**Code**: [[SecretAccessKey]]

> The Secret Access Key is a secret part of the key pair used to sign requests to AWS services. Keep this value confidential to protect your account. Do not share it with anyone and do not store it in a publicly accessible location such as a GitHub repository or a client-side web application.

6. Use this command to concatenate multiple tokens together into a single string.

**Code**: [[Token]]

> This command takes in multiple tokens as input and concatenates them together into a single string, separated by the text specified in the 'text' field. The resulting string is then returned as output. The 'data' field should contain an array of tokens to be concatenated. The 'text' field should contain the separator text to be used between each token. For example, if the 'data' field contains ['hello', 'world'] and the 'text' field contains ', ', the output of this command would be 'hello, world'.

**Command** ([[Generate Access Token]]):

```bash
Run command: generate_token
```

7. To retrieve the credentials of an EC2 instance role, use the following command:

**Code**: [[http://169.254.169.254/latest/meta-data/iam/securi]]

> This command retrieves the temporary security credentials for an EC2 instance role. The credentials are stored in the metadata of the instance and can be accessed using the provided URL. These credentials are used to access AWS services from the instance without having to store long-term access keys on the instance itself. The 'aws-elasticbeanorastalk-ec2-role' in the URL is the default name of the instance profile assigned to the EC2 instance when launched through Elastic Beanstalk. Replace it with the name of the instance profile assigned to your EC2 instance if it is different. The credentials retrieved using this command are valid for a short period of time and will automatically expire. It is recommended to retrieve new credentials periodically to ensure uninterrupted access to AWS services.

**Command** ([[Retrieve Security Credentials]]):

```bash
http://169.254.169.254/latest/meta-data/iam/security-credentials/aws-elasticbeanorastalk-ec2-role
```

8. To list the contents of an S3 bucket, use the `aws s3 ls` command followed by the S3 bucket path. In this case, the command is `aws s3 ls s3://elasticbeanstalk-us-east-2-[ACCOUNT_ID]/`. Replace `[ACCOUNT_ID]` with the actual account ID.

**Code**: [[aws s3 ls s3://elasticbeanstalk-us-east-2-[ACCOUNT]]

> The `aws s3 ls` command is used to list the contents of an S3 bucket. The command takes the following arguments:

- `s3://bucket/path`: The S3 bucket path to list the contents of. Replace `bucket/path` with the actual path to the bucket.

This command requires AWS credentials to be configured on the machine running the command. The credentials can be configured using the `aws configure` command or by setting the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

**Command** ([[List S3 bucket contents]]):

```bash
aws s3 ls s3://elasticbeanstalk-us-east-2-[ACCOUNT_ID]/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Access Key ID]]
- [[Generate Access Token]]
- [[List S3 bucket contents]]
- [[Region]]
- [[Retrieve Account ID]]
- [[Retrieve AWS IAM Security Credentials]]
- [[Retrieve EC2 Instance Identity Document]]
- [[Retrieve Security Credentials]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for AWS Elastic Beanstalk]]
- [[SSRF URL for Cloud Instances]]
