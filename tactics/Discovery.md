---
id: e5ca8fae-2313-4432-bd46-ba203397de1b
name: Discovery
type: tactic
mitre_id: TA0007
mitre_url: null
created_at: '2019-08-28T21:17:31.551553+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Application Window Discovery|T1010 - Application Window Discovery]]'
- '[[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]'
- '[[Cloud Infrastructure Discovery|T1580 - Cloud Infrastructure Discovery]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Cloud Storage Object Discovery|T1619 - Cloud Storage Object Discovery]]'
- '[[Container and Resource Discovery|T1613 - Container and Resource Discovery]]'
- '[[Debugger Evasion|T1622 - Debugger Evasion]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Group Policy Discovery|T1615 - Group Policy Discovery]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
- '[[Network Sniffing|T1040 - Network Sniffing]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
- '[[Peripheral Device Discovery|T1120 - Peripheral Device Discovery]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
- '[[Process Discovery|T1057 - Process Discovery]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
- '[[Software Discovery|T1518 - Software Discovery]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
- '[[System Location Discovery|T1614 - System Location Discovery]]'
- '[[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]'
- '[[System Network Connections Discovery|T1049 - System Network Connections Discovery]]'
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
- '[[System Service Discovery|T1007 - System Service Discovery]]'
- '[[System Time Discovery|T1124 - System Time Discovery]]'
- '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]'
- '[[Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]'
- '[[Active-Directory-Machine-Account-Enumeration-using-CrackMapExec]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active-Directory-ACL-Scanning-for-User]]'
- '[[Active-Directory-Assessment-and-Privilege-Escalation]]'
- '[[Active-Directory-Domain-Controller-Lookup]]'
- '[[Active-Directory-Integrated-DNS-Enumeration]]'
- '[[active-directory-recon-using-ad-module]]'
- '[[Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]'
- '[[Active-Directory-Recon-Using-BloodHound-Custom-Queries]]'
- '[[Active-Directory-Recon-with-PowerView]]'
- '[[Active-Directory-SCCM-Loot-Inventory-and-Download]]'
- '[[Active-Directory-User-Enumeration]]'
- '[[DNS-Zone-Transfer-Enumeration]]'
- '[[Add-Domain-Admin-to-RODC-Password-Replication-Group]]'
- '[[Add-User-to-Group-Using-ADModule-With-Credentials]]'
- '[[AdminCount-Abuse]]'
- '[[Enumerate-AMSI-Providers-via-Registry]]'
- '[[Analyze-BloodHound-Data-for-AD-Relationships]]'
- '[[Enumerate-Installed-Antivirus-Products-Windows]]'
- '[[Application-Escape-and-Breakout-via-Context-Menues-and-File-Search-Command]]'
- '[[Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]'
- '[[AWS-Account-Identity-Check]]'
- '[[AWS-Account-Identity-Enumeration]]'
- '[[AWS-Account-Identity-Enumeration]]'
- '[[AWS-Account-Identity-Enumeration]]'
- '[[AWS-Account-ID-Retrieval-with-STS-Get-Caller-Identity]]'
- '[[AWS-API-Gateway-Information-Gathering]]'
- '[[Enumerate-AWS-API-Gateway-Methods]]'
- '[[aws-api-gateway-resource-enumeration]]'
- '[[aws-api-gateway-resource-enumeration]]'
- '[[AWS-API-Gateway-Resource-Listing]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[Enumerate-AWS-API-Gateway-Stages]]'
- '[[AWS-API-Key-Enumeration]]'
- '[[AWS-API-Key-Enumeration]]'
- '[[List-AWS-CloudFront-Distributions]]'
- '[[Enumerate-Kubernetes-Service-Account-Secrets-via-Pod-RCE]]'
- '[[Export-AWS-Credentials-to-Environment]]'
- '[[AWS-DynamoDB-Table-Enumeration]]'
- '[[AWS-EC2-IAM-Instance-Profile-Enumeration]]'
- '[[Enumerate-AWS-EC2-Instances]]'
- '[[Enumerate-AWS-EC2-Instances]]'
- '[[Exploit-AWS-EC2-Metadata-SSRF-for-Credential-Extraction]]'
- '[[Enumerate-AWS-ECR-Images]]'
- '[[Enumerate-AWS-ECR-Images]]'
- '[[Enumerate-AWS-ECR-Images]]'
- '[[AWS ECR Repositories Enumeration]]'
- '[[Enumerate-AWS-ECR-Repositories]]'
- '[[aws-ecr-repository-image-enumeration]]'
- '[[AWS-ECR-Repository-Policy-Enumeration]]'
- '[[Enumerate-AWS-ECS-Clusters]]'
- '[[aws-ecs-cluster-information-gathering]]'
- '[[Enumerate-ECS-Container-Instances]]'
- '[[aws-ecs-service-enumeration]]'
- '[[aws-ecs-services-enumeration]]'
- '[[aws-ecs-task-enumeration]]'
- '[[AWS-ECS-Task-Information-Gathering]]'
- '[[aws-eks-cluster-enumeration]]'
- '[[AWS-EKS-Cluster-Information-Gathering]]'
- '[[AWS-EKS-Fargate-Enumeration]]'
- '[[AWS-EKS-Node-Group-Enumeration]]'
- '[[Enumerate-AWS-EKS-Node-Group-Information]]'
- '[[AWS-Extract-EBS-Backup-to-EC2-Instance]]'
- '[[AWS-Extract-EBS-Backup-to-EC2-Instance]]'
- '[[AWS-IAM-Group-Enumeration]]'
- '[[AWS-IAM-Group-Inline-Policies-Enumeration]]'
- '[[AWS-IAM-Group-Managed-Policies-Enumeration]]'
- '[[Enumerate-AWS-IAM-Inline-Policies]]'
- '[[List-AWS-IAM-Access-Keys]]'
- '[[AWS-IAM-Permissions-Enumeration]]'
- '[[AWS-IAM-Policy-Enumeration]]'
- '[[AWS-IAM-Policy-Information-Gathering]]'
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
- '[[AWS-IAM-User-Enumeration]]'
- '[[AWS-IAM-User-Enumeration-and-Credential-Checking]]'
- '[[aws-iam-list-groups-for-user]]'
- '[[AWS-IAM-User-Inline-Policies-Enumeration]]'
- '[[AWS-IAM-Attach-Inline-Policy-to-User]]'
- '[[Enumerate-IAM-User-Attached-Policies]]'
- '[[AWS-IAM-Inline-Policy-Enumeration]]'
- '[[AWS-Instance-Profile-Enumeration]]'
- '[[Enumerate-AWS-Key-Owner-and-Gain-Initial-Access]]'
- '[[aws-kms-enumerate-key-policies]]'
- '[[AWS-KMS-Key-Enumeration]]'
- '[[AWS-KMS-Key-Policy-Enumeration]]'
---

# Discovery

**MITRE ID**: TA0007

## Description

Discovery consists of techniques that allow the adversary to gain knowledge about the system and internal network. When adversaries gain access to a new system, they must orient themselves to what they now have control of and what benefits operating from that system give to their current objective or overall goals during the intrusion. The operating system provides many native tools that aid in this post-compromise information-gathering phase.



## Techniques

This tactic includes 31 techniques:

- [[Account Discovery|T1087 - Account Discovery]]
- [[Application Window Discovery|T1010 - Application Window Discovery]]
- [[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]
- [[Cloud Infrastructure Discovery|T1580 - Cloud Infrastructure Discovery]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Cloud Storage Object Discovery|T1619 - Cloud Storage Object Discovery]]
- [[Container and Resource Discovery|T1613 - Container and Resource Discovery]]
- [[Debugger Evasion|T1622 - Debugger Evasion]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Group Policy Discovery|T1615 - Group Policy Discovery]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]
- [[Network Sniffing|T1040 - Network Sniffing]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]
- [[Peripheral Device Discovery|T1120 - Peripheral Device Discovery]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]
- [[Process Discovery|T1057 - Process Discovery]]
- [[Query Registry|T1012 - Query Registry]]
- [[Remote System Discovery|T1018 - Remote System Discovery]]
- [[Security Software Discovery|T1063 - Security Software Discovery]]
- [[Software Discovery|T1518 - Software Discovery]]
- [[System Information Discovery|T1082 - System Information Discovery]]
- [[System Location Discovery|T1614 - System Location Discovery]]
- [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]
- [[System Network Connections Discovery|T1049 - System Network Connections Discovery]]
- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]
- [[System Service Discovery|T1007 - System Service Discovery]]
- [[System Time Discovery|T1124 - System Time Discovery]]
- [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

## Related Procedures

There are 100 procedures implementing this tactic:

- [[Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords]]
- [[Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[Active-Directory-Machine-Account-Enumeration-using-CrackMapExec]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active-Directory-ACL-Scanning-for-User]]
- [[Active-Directory-Assessment-and-Privilege-Escalation]]
- [[Active-Directory-Domain-Controller-Lookup]]
- [[Active-Directory-Integrated-DNS-Enumeration]]
- [[active-directory-recon-using-ad-module]]
- [[Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[Active-Directory-Recon-Using-BloodHound-Custom-Queries]]
- [[Active-Directory-Recon-with-PowerView]]
- [[Active-Directory-SCCM-Loot-Inventory-and-Download]]
- [[Active-Directory-User-Enumeration]]
- [[DNS-Zone-Transfer-Enumeration]]
- [[Add-Domain-Admin-to-RODC-Password-Replication-Group]]
- [[Add-User-to-Group-Using-ADModule-With-Credentials]]
- [[AdminCount-Abuse]]
- [[Enumerate-AMSI-Providers-via-Registry]]
- [[Analyze-BloodHound-Data-for-AD-Relationships]]

*...and 80 more*


