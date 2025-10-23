---
id: 83634d12-6c01-4018-8622-3719e75fc0f2
name: Provision S3 Website and Upload Payload
type: procedure
verified: false
submitted: false
created_at: '2019-10-10T18:18:30.697830+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Stage Capabilities|TA0026 - Stage Capabilities]]'
techniques:
- '[[Upload, install, and configure software/tools|T1362 - Upload, install, and configure
  software/tools]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
- '[[Network]]'
commands:
- '[[Terraform Apply]]'
- '[[Terraform Destroy]]'
- '[[Terraform Initialization]]'
---

# Provision S3 Website and Upload Payload

## Summary

During a RedTeam engagement it could be useful to host and deliver a file from an internet accessible website. To solve this problem with a quick-to-run solution, here is a Terraform script to create an S3 bucket, enable it as a website with an open policy and upload a payload file. This Terraform 

## Description

# Description

During a RedTeam engagement it could be useful to host and deliver a file from an internet accessible website. To solve this problem with a quick-to-run solution, here is a Terraform script to create an S3 bucket, enable it as a website with an open policy and upload a payload file. This Terraform script will output the URL of the S3 bucket when it is finished.



# Requirements

AWS API Access Key stored in the credentials file. Use an existing IAM users Access Key on your AWS account or generate a new IAM user and an Access Key. It's a good idea to name the key in the credentials file to easily recall which Access Key is for which AWS account. RedStack will always use "hacker" for the attacker systems, and "target" for the targets.





**Code**: [[# ~/.aws/credentials
[hacker]
aws_access_key_id = ]]



## Tools

- awscli

- Terraform



# Instructions

On the hacker system create a new Working Directory "workdir" and you will make 3 files inside:



1. payload.exe file - This is the payload you will deliver to the target system.

- Generate any type of payload, this will be Attack Chain specific



2. Make the tfvars file. This Terraform variables file is required to make the Terraform script reusable. Create S3 bucket names are unique in AWS, so use an md5 hash combined with a site name.

The aws_profile should match that inside the [] brackets of the  ~/.aws/credentials file

If the payload file is in a different directory, an exact directory needs to be used to reference the file in the variable file. This is the file that will be uploaded to the S3 bucket.



**Code**: [[# terraform.tfvars
site_hash = "4a4a8f4331a58e9138]]





3. Next, create the Terraform script. There are a few important sections in this Terraform script, focusing on the most important, it creates two S3 buckets, one bucket is for logs, and one bucket is to convert to a website, apply a policy, and upload a file. The logs are important in a RedTeam engagement to track and keep record of which IP address is accessing the publicly available website and what file the target requests, the logs can confirm a reverse shell is being accessed by the target.







**Code**: [[### AWS Config
provider "aws" {
  region = "us-eas]]





## Guide

With the 3 files inside of the Working Directory, first initialize Terraform to setup the modules and providers needed for the TF script.





**Command** ([[Terraform Initialization]]):

```bash
terraform init
```





Next apply the configuration.

Note: This step will create the buckets on your AWS account and you will be billed for their usage by AWS Amazon.



**Command** ([[Terraform Apply]]):

```bash
terraform apply -auto-approve
```





The Terraform script will output the S3 bucket address and filename of the payload. Now this address can be used in any script or command used to deliver the payload into a system.



When this part of the pentest is complete, destroy the S3 bucket and wipe all of the files

Note: This will also delete the S3 website logs folder, if you wish to retain the logs, download them separately.







**Command** ([[Terraform Destroy]]):

```bash
terraform destroy -auto-approve
```





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Stage Capabilities|TA0026 - Stage Capabilities]]

### Techniques

- [[Upload, install, and configure software/tools|T1362 - Upload, install, and configure software/tools]]

## Commands Used

- [[Terraform Apply]]
- [[Terraform Destroy]]
- [[Terraform Initialization]]

## Tags

- [[AWS]]
- [[Cloud]]
- [[Network]]


