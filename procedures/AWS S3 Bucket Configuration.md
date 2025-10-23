---
id: 41e53d08-432e-486e-81ad-855645e15542
name: AWS S3 Bucket Configuration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.520681+00:00'
updated_at: '2023-04-06T03:55:53.547466+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[AWS Configuration]]'
commands:
- '[[Configure AWS credentials]]'
- '[[Configure AWS Profile]]'
- '[[Install AWS CLI]]'
- '[[Set AWS Credentials]]'
---

# AWS S3 Bucket Configuration

## Summary

The AWS S3 bucket is a popular cloud storage service that provides users with the ability to store and retrieve data from anywhere in the world. However, misconfigured S3 buckets can result in data breaches and other security incidents. This procedure provides instructions on how to properly config

## Description

# Description

The AWS S3 bucket is a popular cloud storage service that provides users with the ability to store and retrieve data from anywhere in the world. However, misconfigured S3 buckets can result in data breaches and other security incidents. This procedure provides instructions on how to properly configure the AWS S3 bucket to ensure security and prevent unauthorized access. By properly configuring the S3 bucket, organizations can ensure that their sensitive data is secure and protected from unauthorized access.

 

## Requirements

1. An AWS account

1. awscli installed

 

## Defense

1. Properly configure S3 bucket permissions to prevent unauthorized access

1. Enable AWS CloudTrail to monitor and log all S3 bucket activity

1. Regularly review S3 bucket permissions and access logs to identify and remediate security issues

 

## Objectives

1. To properly configure the AWS S3 bucket

1. To ensure that sensitive data is secure and protected from unauthorized access

 

# Instructions

1. 

 



**Code**: [[sudo apt install awscli]]



> This command installs the AWS command-line interface (CLI) which is used to interact with AWS services from the command line.



**Command** ([[Install AWS CLI]]):

```bash
sudo apt install awscli
```



2. 

 



**Code**: [[aws configure
AWSAccessKeyId=[ENTER HERE YOUR KEY]]]



> This command configures the AWS CLI with the user's access key and secret access key, which are used to authenticate the user's requests to AWS services.



**Command** ([[Configure AWS credentials]]):

```bash
aws configure
AWSAccessKeyId=[ENTER HERE YOUR KEY]
AWSSecretKey=[ENTER HERE YOUR KEY]
```



3. 

 



**Code**: [[aws configure --profile nameofprofile]]



> This command creates an AWS profile, which is a named set of configuration options that can be used when running AWS CLI commands.



**Command** ([[Configure AWS Profile]]):

```bash
aws configure --profile nameofprofile
```



4. 

 



**Code**: [[export AWS_ACCESS_KEY_ID=ASIAZ[...]PODP56
export A]]



> This command exports the AWS access key, secret access key, and session token as environment variables, which can be used to authenticate the user's requests to AWS services.



**Command** ([[Set AWS Credentials]]):

```bash
export AWS_ACCESS_KEY_ID=ASIAZ[...]PODP56
export AWS_SECRET_ACCESS_KEY=fPk/Gya[...]4/j5bSuhDQ
export AWS_SESSION_TOKEN=FQoGZXIvYXdzE[...]8aOK4QU=
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Configure AWS credentials]]
- [[Configure AWS Profile]]
- [[Install AWS CLI]]
- [[Set AWS Credentials]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[AWS Configuration]]


