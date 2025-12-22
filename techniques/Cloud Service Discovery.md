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
- '[[AWS-Account-Identity-Enumeration]]'
- '[[AWS-Account-Identity-Enumeration]]'
- '[[Enumerate-AWS-API-Gateway-Methods]]'
- '[[aws-api-gateway-resource-enumeration]]'
- '[[aws-api-gateway-resource-enumeration]]'
- '[[AWS-API-Gateway-Resource-Listing]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[AWS-API-Key-Enumeration]]'
- '[[AWS-API-Key-Enumeration]]'
- '[[Enumerate-Kubernetes-Service-Account-Secrets-via-Pod-RCE]]'
- '[[AWS-DynamoDB-Table-Enumeration]]'
- '[[Enumerate-AWS-EC2-Instances]]'
- '[[Enumerate-AWS-EC2-Instances]]'
- '[[Enumerate-AWS-ECR-Images]]'
- '[[Enumerate-AWS-ECR-Images]]'
- '[[aws-ecr-repositories-enumeration]]'
- '[[aws-ecr-repository-image-enumeration]]'
- '[[AWS-ECR-Repository-Policy-Enumeration]]'
- '[[Enumerate-AWS-ECS-Clusters]]'
- '[[aws-ecs-services-enumeration]]'
- '[[aws-eks-cluster-enumeration]]'
- '[[AWS-EKS-Cluster-Information-Gathering]]'
- '[[AWS-EKS-Fargate-Enumeration]]'
- '[[AWS-EKS-Node-Group-Enumeration]]'
- '[[Enumerate-AWS-EKS-Node-Group-Information]]'
- '[[AWS-IAM-Group-Inline-Policies-Enumeration]]'
- '[[AWS-IAM-Group-Managed-Policies-Enumeration]]'
- '[[Enumerate-AWS-IAM-Inline-Policies]]'
- '[[AWS-IAM-Permissions-Enumeration]]'
- '[[AWS-IAM-Policy-Enumeration]]'
- '[[AWS-IAM-Policy-Information-Retrieval]]'
- '[[aws-iam-policy-version-enumeration]]'
- '[[Gather-AWS-IAM-Policy-Version-Information]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[AWS-IAM-Role-Enumeration]]'
- '[[AWS-IAM-Role-Enumeration]]'
- '[[AWS-IAM-Role-Inline-Policy-Enumeration]]'
- '[[List-Attached-Policies-for-AWS-IAM-Role]]'
- '[[aws-iam-enumerate-attached-role-policies]]'
- '[[Enumerate-AWS-IAM-Role-Trust-Relationships]]'
- '[[Enumerate-AWS-IAM-User-ARNS]]'
- '[[AWS-IAM-User-Inline-Policies-Enumeration]]'
- '[[Enumerate-IAM-User-Attached-Policies]]'
- '[[AWS-IAM-Inline-Policy-Enumeration]]'
- '[[AWS-Instance-Profile-Enumeration]]'
- '[[aws-kms-enumerate-key-policies]]'
- '[[AWS-KMS-Key-Enumeration]]'
- '[[AWS-KMS-Key-Policy-Enumeration]]'
- '[[retrieve-aws-kms-key-policy]]'
- '[[AWS-Lambda-Environment-Variable-Credential-Access]]'
- '[[Enumerate-AWS-Lambda-Function-Details]]'
- '[[AWS-Lambda-Function-Enumeration]]'
- '[[AWS-Lambda-Layer-Enumeration]]'
- '[[List-AWS-API-Gateway-REST-APIs]]'
- '[[Enumerate-AWS-Managed-IAM-Policies]]'
- '[[Enumerate-AWS-IAM-Managed-Policy-Versions]]'
- '[[AWS-Metadata-Information-Retrieval]]'
- '[[AWS-Privilege-Escalation-via-Attached-User-Policies]]'
- '[[aws-s3-object-acl-enumeration]]'
- '[[AWS-S3-Bucket-ACL-Enumeration]]'
- '[[AWS-S3-Bucket-Enumeration]]'
- '[[AWS-S3-Bucket-Object-Enumeration]]'
- '[[Enumerate-AWS-S3-Bucket-Policy]]'
- '[[Enumerate-AWS-S3-Bucket-Public-Access-Block]]'
- '[[Scan-AWS-S3-Buckets-for-Misconfigurations]]'
- '[[Enumerate-AWS-Secrets-Manager-Secrets]]'
- '[[AWS-Secrets-Manager-Resource-Policy-Enumeration]]'
- '[[Gather-AWS-Temporary-Credential-Information]]'
- '[[AWS-User-Policy-Enumeration]]'
- '[[Azure-AD-Administrative-Unit-Management]]'
- '[[azure-application-proxy-enumeration]]'
- '[[azure-pass-the-certificate-ad-cert-request-and-rce]]'
- '[[Azure-Storage-Blob-Enumeration]]'
- '[[Azure-Tenant-Enumeration-with-Az-CLI]]'
- '[[Cloud-Instance-Rancher-Metadata-Retrieval-via-SSRF]]'
- '[[aws-cloud-security-assessment-and-auditing]]'
- '[[List-AWS-CloudTrail-Trails]]'
- '[[DB2-Schema-Enumeration-via-XML-Serialization]]'
- '[[Docker-Security-Assessment]]'
- '[[Enumerate-EBS-Snapshots]]'
- '[[EKS-Fargate-Profile-Enumeration]]'
- '[[Kubernetes-Service-Account-Permissions-Enumeration]]'
- '[[Enumerate-AWS-RDS-VPCs]]'
- '[[Enumerate-AWS-RDS-VPCs]]'
- '[[SSRF-to-Enumerate-Docker-Containers-and-Images]]'
- '[[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]'
- '[[Exploit-Spring-Boot-Actuator-Insecure-Endpoints]]'
- '[[Exploit-SSRF-to-Extract-AWS-ECS-Metadata-Credentials]]'
- '[[Exploit-SSRF-to-Access-Cloud-Metadata]]'
- '[[Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]'
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

- [[AWS-Account-Identity-Enumeration]]
- [[AWS-Account-Identity-Enumeration]]
- [[Enumerate-AWS-API-Gateway-Methods]]
- [[aws-api-gateway-resource-enumeration]]
- [[aws-api-gateway-resource-enumeration]]
- [[AWS-API-Gateway-Resource-Listing]]
- [[AWS-API-Gateway-Stage-Enumeration]]
- [[AWS-API-Key-Enumeration]]
- [[AWS-API-Key-Enumeration]]
- [[Enumerate-Kubernetes-Service-Account-Secrets-via-Pod-RCE]]
- [[AWS-DynamoDB-Table-Enumeration]]
- [[Enumerate-AWS-EC2-Instances]]
- [[Enumerate-AWS-EC2-Instances]]
- [[Enumerate-AWS-ECR-Images]]
- [[Enumerate-AWS-ECR-Images]]
- [[aws-ecr-repositories-enumeration]]
- [[aws-ecr-repository-image-enumeration]]
- [[AWS-ECR-Repository-Policy-Enumeration]]
- [[Enumerate-AWS-ECS-Clusters]]
- [[aws-ecs-services-enumeration]]

*...and 72 more*


