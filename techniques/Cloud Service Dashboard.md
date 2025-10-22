---
id: 92dd2fdd-2629-46e0-823f-c0eaefc2be50
name: Cloud Service Dashboard
type: technique
mitre_id: T1538
mitre_url: null
created_at: '2023-04-06T00:31:27.085332+00:00'
updated_at: '2023-04-06T03:56:16.002960+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[AWS Account Identity Enumeration]]'
- '[[AWS Credential Export]]'
- '[[AWS EC2 IAM Instance Profile Enumeration]]'
- '[[AWS ECR Repository Enumeration]]'
- '[[AWS ECS Task Enumeration]]'
- '[[AWS IAM Policy Information Gathering]]'
- '[[AWS IAM User Enumeration]]'
- '[[AWS IAM User Enumeration and Credential Checking]]'
- '[[AWS IAM User Policy Attachment]]'
- '[[AWS Key Owner Enumeration and Initial Compromise]]'
- '[[AWS Lambda Event Source Mapping Enumeration]]'
- '[[AWS Lambda Function Details Enumeration]]'
- '[[AWS Lambda Function Enumeration]]'
- '[[AWS Lambda Function Enumeration]]'
- '[[AWS Lambda Function Policy Enumeration]]'
- '[[AWS Lambda Function Privilege Escalation via IAM Policy Attachment]]'
- '[[AWS Lambda Layer Enumeration]]'
- '[[AWS Managed Policies Enumeration]]'
- '[[AWS Metadata Key Grabbing]]'
- '[[AWS S3 Bucket Public Access Block Enumeration]]'
- '[[Azure Access Token Retrieval for Management and Graph APIs using Python]]'
- '[[Azure AD Enumeration with AzureAD Powershell (Creds)]]'
- '[[Azure Conditional Access Device Joining]]'
- '[[Azure Managed Identity Token Retrieval]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[Disable CloudTrail on AWS]]'
---

# Cloud Service Dashboard

**MITRE ID**: T1538

## Description

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, findings of potential security risks, and to run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This allows the adversary to gain information without making any API requests.

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (26)

- [[AWS Account Identity Enumeration]]
- [[AWS Credential Export]]
- [[AWS EC2 IAM Instance Profile Enumeration]]
- [[AWS ECR Repository Enumeration]]
- [[AWS ECS Task Enumeration]]
- [[AWS IAM Policy Information Gathering]]
- [[AWS IAM User Enumeration]]
- [[AWS IAM User Enumeration and Credential Checking]]
- [[AWS IAM User Policy Attachment]]
- [[AWS Key Owner Enumeration and Initial Compromise]]
- [[AWS Lambda Event Source Mapping Enumeration]]
- [[AWS Lambda Function Details Enumeration]]
- [[AWS Lambda Function Enumeration]]
- [[AWS Lambda Function Enumeration]]
- [[AWS Lambda Function Policy Enumeration]]
- [[AWS Lambda Function Privilege Escalation via IAM Policy Attachment]]
- [[AWS Lambda Layer Enumeration]]
- [[AWS Managed Policies Enumeration]]
- [[AWS Metadata Key Grabbing]]
- [[AWS S3 Bucket Public Access Block Enumeration]]

*...and 6 more*
