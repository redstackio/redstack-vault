---
id: 05d175a2-be96-48f2-8350-8c86ae5db26b
name: Cloud Service Discovery
type: technique
mitre_id: T1526
mitre_url: null
created_at: '2023-04-06T00:31:27.071966+00:00'
updated_at: '2023-04-06T03:56:38.806818+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[AWS Account Identity Enumeration]]'
- '[[AWS Account Identity Enumeration]]'
- '[[AWS API Gateway Method Information Enumeration]]'
- '[[AWS API Gateway Resource Enumeration]]'
- '[[AWS API Gateway Resource Enumeration]]'
- '[[AWS API Gateway Resource Listing]]'
- '[[AWS API Gateway Stage Information Gathering]]'
- '[[AWS API Key Enumeration]]'
- '[[AWS API Key Enumeration]]'
- '[[AWS Cloud - Kubernetes Service Account Secrets Enumeration]]'
- '[[AWS DynamoDB Table Enumeration]]'
- '[[AWS EC2 Instance Enumeration]]'
- '[[AWS EC2 Instance Enumeration]]'
- '[[AWS ECR Image Enumeration]]'
- '[[AWS ECR Image Listing]]'
- '[[AWS ECR Repositories Enumeration]]'
- '[[AWS ECR Repository Image Enumeration]]'
- '[[AWS ECR Repository Policy Enumeration]]'
- '[[AWS ECS Cluster Enumeration]]'
- '[[AWS ECS Services Enumeration]]'
- '[[AWS EKS Cluster Enumeration]]'
- '[[AWS EKS Cluster Information Gathering]]'
- '[[AWS EKS Fargate Enumeration]]'
- '[[AWS EKS Node Group Enumeration]]'
- '[[AWS EKS Node Group Information Enumeration]]'
- '[[AWS IAM Group Inline Policies Enumeration]]'
- '[[AWS IAM Group Managed Policies Enumeration]]'
- '[[AWS IAM Inline Policy Enumeration]]'
- '[[AWS IAM Permissions Enumeration]]'
- '[[AWS IAM Policy Enumeration]]'
- '[[AWS IAM Policy Information Retrieval]]'
- '[[AWS IAM Policy Version Enumeration]]'
- '[[AWS IAM Policy Version Information Gathering]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM Role Enumeration]]'
- '[[AWS IAM Role Enumeration]]'
- '[[AWS IAM Role Inline Policy Enumeration]]'
- '[[AWS IAM Role Policies Enumeration]]'
- '[[AWS IAM Role Policy Enumeration]]'
- '[[AWS IAM Role Trust Relationship Enumeration]]'
- '[[AWS IAM User ARN Enumeration]]'
- '[[AWS IAM User Inline Policies Enumeration]]'
- '[[AWS IAM User Policy Enumeration]]'
- '[[AWS Inline Policy Enumeration]]'
- '[[AWS Instance Profile Enumeration]]'
- '[[AWS Key Policy Enumeration]]'
- '[[AWS KMS Key Enumeration]]'
- '[[AWS KMS Key Policy Enumeration]]'
- '[[AWS KMS Key Policy Listing]]'
- '[[AWS Lambda Environment Variable Credential Access]]'
- '[[AWS Lambda Function Details Enumeration]]'
- '[[AWS Lambda Function Enumeration]]'
- '[[AWS Lambda Layer Enumeration]]'
- '[[AWS Listing Rest APIs]]'
- '[[AWS Managed Policy Enumeration]]'
- '[[AWS Managed Policy Version Enumeration]]'
- '[[AWS Metadata Information Retrieval]]'
- '[[AWS Privilege Escalation via Attached User Policies]]'
- '[[AWS S3 ACL Enumeration]]'
- '[[AWS S3 Bucket ACL Enumeration]]'
- '[[AWS S3 Bucket Enumeration]]'
- '[[AWS S3 Bucket Object Enumeration]]'
- '[[AWS S3 Bucket Policy Enumeration]]'
- '[[AWS S3 Bucket Public Access Block Enumeration]]'
- '[[AWS S3 Bucket Scanner]]'
- '[[AWS Secret Manager Enumeration]]'
- '[[AWS Secret Resource Policy Enumeration]]'
- '[[AWS Temporary Credential Information Gathering]]'
- '[[AWS User Policy Enumeration]]'
- '[[Azure AD Administrative Unit Management]]'
- '[[Azure Application Proxy Enumeration]]'
- '[[Azure Pass the Certificate: AD Cert Request and RCE]]'
- '[[Azure Storage Blob Enumeration]]'
- '[[Azure Tenant Enumeration with az-cli]]'
- '[[Cloud Instance Rancher Metadata Retrieval via SSRF]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[CloudTrail Logs Listing]]'
- '[[DB2 Schema Enumeration via XML Serialization]]'
- '[[Docker Security Assessment]]'
- '[[EBS Snapshot Enumeration]]'
- '[[EKS Fargate Profile Enumeration]]'
- '[[Kubernetes Service Account Permissions Enumeration]]'
- '[[RDS VPC Enumeration]]'
- '[[RDS VPC Enumeration]]'
- '[[Server-Side Request Forgery for Docker Containers and Images Enumeration]]'
- '[[Server-Side Request Forgery on Cloud Instances and HP Helion]]'
- '[[Springboot-Actuator Insecure Management Interface]]'
- '[[SSRF for AWS ECS and Cloud Instances]]'
- '[[SSRF for Cloud Instances]]'
- '[[SSRF URL for Oracle Cloud Instances via AWS Instance Metadata and User Data]]'
---

# Cloud Service Discovery

**MITRE ID**: T1526

## Description

An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Azure AD, etc. 

Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Azure AD Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity.(Citation: Azure - Resource Manager API)(Citation: Azure AD Graph API)

Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.(Citation: Azure - Stormspotter)(Citation: GitHub Pacu)

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (92)

- [[AWS Account Identity Enumeration]]
- [[AWS Account Identity Enumeration]]
- [[AWS API Gateway Method Information Enumeration]]
- [[AWS API Gateway Resource Enumeration]]
- [[AWS API Gateway Resource Enumeration]]
- [[AWS API Gateway Resource Listing]]
- [[AWS API Gateway Stage Information Gathering]]
- [[AWS API Key Enumeration]]
- [[AWS API Key Enumeration]]
- [[AWS Cloud - Kubernetes Service Account Secrets Enumeration]]
- [[AWS DynamoDB Table Enumeration]]
- [[AWS EC2 Instance Enumeration]]
- [[AWS EC2 Instance Enumeration]]
- [[AWS ECR Image Enumeration]]
- [[AWS ECR Image Listing]]
- [[AWS ECR Repositories Enumeration]]
- [[AWS ECR Repository Image Enumeration]]
- [[AWS ECR Repository Policy Enumeration]]
- [[AWS ECS Cluster Enumeration]]
- [[AWS ECS Services Enumeration]]

*...and 72 more*
