---
id: dd4da0e2-3f65-4f9d-a251-c4f08976768a
name: S3 Bucket File Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:52.778863+00:00'
updated_at: '2023-04-06T03:55:52.802689+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[Basic tests]]'
- '[[Listing files]]'
commands:
- '[[List contents of S3 bucket flaws.cloud]]'
- '[[List contents of S3 bucket targetbucket]]'
- '[[Query flaws.cloud DNS record]]'
- '[[Reverse lookup for IP address 52.218.192.11]]'
---

# S3 Bucket File Listing

## Summary

This procedure involves listing files within an Amazon S3 bucket. This can be useful for reconnaissance purposes, as it allows an attacker to gain a better understanding of the contents of the bucket. To list the files, the 'aws s3 ls' command is used with the appropriate bucket name and region. Th

## Description

# Description

This procedure involves listing files within an Amazon S3 bucket. This can be useful for reconnaissance purposes, as it allows an attacker to gain a better understanding of the contents of the bucket. To list the files, the 'aws s3 ls' command is used with the appropriate bucket name and region. This technique can be used to identify sensitive data within the bucket, such as configuration files, credentials, and other valuable information. The business value of this procedure lies in its ability to help organizations identify and mitigate potential security risks associated with their cloud storage infrastructure.

## Requirements

1. Valid AWS credentials or access to an unsecured S3 bucket

1. Network access to the S3 bucket

1. AWS CLI installed on the attacker's machine

## Defense

1. Ensure that S3 buckets are properly secured with appropriate access controls and permissions

1. Implement network security measures such as firewalls and intrusion detection systems to monitor and block unauthorized access to S3 buckets

1. Monitor S3 bucket activity for suspicious or unauthorized access

## Objectives

1. List files within an Amazon S3 bucket

1. Identify sensitive data within the bucket

# Instructions

1. Replace 'targetbucket' with the name of the bucket you want to list files from. Replace 'insert-region-here' with the appropriate region for the bucket. Alternatively, you can list files from a known insecure bucket such as 'flaws.cloud'.

**Code**: [[aws s3 ls s3://targetbucket --no-sign-request --re]]

> This command uses the AWS CLI to list the files within the specified S3 bucket. The '--no-sign-request' flag is used to bypass authentication and access the bucket anonymously. The '--region' flag specifies the region where the bucket is located. This command can be used to identify sensitive data within the bucket, such as configuration files, credentials, and other valuable information.

**Command** ([[List contents of S3 bucket targetbucket]]):

```bash
aws s3 ls s3://targetbucket --no-sign-request --region insert-region-here
```

**Command** ([[List contents of S3 bucket flaws.cloud]]):

```bash
aws s3 ls s3://flaws.cloud/ --no-sign-request --region us-west-2
```

2. Replace 'flaws.cloud' with the name of the bucket you want to get the region for.

**Code**: [[$ dig flaws.cloud
;; ANSWER SECTION:
flaws.cloud. ]]

> This command uses the 'dig' and 'nslookup' utilities to determine the region of an S3 bucket. First, the 'dig' command is used to retrieve the IP address associated with the bucket. Then, the 'nslookup' command is used to perform a reverse DNS lookup on the IP address, which returns the hostname of the bucket in the format 's3-website-{region}.amazonaws.com'. The region can then be extracted from the hostname.

**Command** ([[Query flaws.cloud DNS record]]):

```bash
$ dig flaws.cloud
;; ANSWER SECTION:
flaws.cloud.    5    IN    A    52.218.192.11

```

**Command** ([[Reverse lookup for IP address 52.218.192.11]]):

```bash
$ nslookup 52.218.192.11
Non-authoritative answer:
11.192.218.52.in-addr.arpa name = s3-website-us-west-2.amazonaws.com.
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[List contents of S3 bucket flaws.cloud]]
- [[List contents of S3 bucket targetbucket]]
- [[Query flaws.cloud DNS record]]
- [[Reverse lookup for IP address 52.218.192.11]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[Basic tests]]
- [[Listing files]]
