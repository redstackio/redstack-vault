---
id: cab9440a-5df8-4893-93f4-4f8a0e15b69d
name: Lateral Movement
type: tactic
mitre_id: TA0008
mitre_url: null
created_at: '2019-08-28T21:17:22.541960+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[AppleScript|T1155 - AppleScript]]'
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Application Deployment Software|T1017 - Application Deployment Software]]'
- '[[Distributed Component Object Model|T1175 - Distributed Component Object Model]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
- '[[Lateral Tool Transfer|T1570 - Lateral Tool Transfer]]'
- '[[Logon Scripts|T1037 - Logon Scripts]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
- '[[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
- '[[Remote File Copy|T1105 - Remote File Copy]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]'
- '[[Replication Through Removable Media|T1091 - Replication Through Removable Media]]'
- '[[Shared Webroot|T1051 - Shared Webroot]]'
- '[[SSH Hijacking|T1184 - SSH Hijacking]]'
- '[[Taint Shared Content|T1080 - Taint Shared Content]]'
- '[[Third-party Software|T1072 - Third-party Software]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
- '[[Web Session Cookie|T1506 - Web Session Cookie]]'
- '[[Windows Admin Shares|T1077 - Windows Admin Shares]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
procedures:
- '[[Account Takeover via Password Reset Feature and IDOR on API Parameters]]'
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[Active Directory Integrated DNS Enumeration]]'
- '[[Active Directory Man-in-the-Middle and Password Cracking]]'
- '[[Active Directory Trust Ticket Forgery with Mimikatz]]'
- '[[AD CS Relay Attack with Rubeus and PetitPotam]]'
- '[[Add Domain Admin to RODC Password Replication Group Procedure]]'
- '[[AWS API Enumeration]]'
- '[[AWS API Gateway Method Enumeration]]'
- '[[AWS EBS Snapshot Volume Creation]]'
- '[[AWS EKS Service Account Token Theft]]'
- '[[AWS Fargate Container Credentials Theft]]'
- '[[AWS IAM Group Managed Policies Enumeration]]'
- '[[AWS IAM Inline Policy Enumeration]]'
- '[[AWS IAM Policy Version Information Retrieval]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM Role Inline Policy Enumeration]]'
- '[[AWS IAM User Policy Enumeration]]'
- '[[AWS Lambda Backdoor Persistence]]'
- '[[AWS Lambda Function Invocation for Privilege Escalation]]'
- '[[AWS Metadata Credential Theft]]'
- '[[AWS S3 Bucket Configuration]]'
- '[[AWS S3 Bucket Configuration]]'
- '[[AWS Shadow Admin - Create AWS Glue Development Endpoint]]'
- '[[AWS SSM Command Execution - EC2 Shell Script]]'
- '[[AWS User Policy Enumeration]]'
- '[[Azure AD Connect - Silver Ticket Attack]]'
- '[[Azure Generate Shared Access Signature (SAS) URLs for Blob Storage]]'
- '[[Azure - Illicit Consent Grant Prevention]]'
- '[[Azure Managed Identity Token Retrieval]]'
- '[[Azure Pass the Certificate: AD Cert Request and RCE]]'
- '[[Azure Pass The PRT with Mimikatz]]'
- '[[Azure Resource Management and Privilege Checking with PowerShell]]'
- '[[Azure SSRF for VM Metadata Service]]'
- '[[Azure VM RunCommand Execution]]'
- '[[Azure Web Apps: Remote SSH Connection]]'
- '[[Bash TCP Reverse Shell Connection]]'
- '[[Basic Directory Traversal Exploitation]]'
- '[[BITSAdmin Download and Execute]]'
- '[[Blind XPATH Injection]]'
- '[[Browse an FTP Site with an Interactive Session]]'
- '[[Browse SMB Share (NTLM)]]'
- '[[Bypassing filters with IPv6 Server Ports]]'
- '[[Cassandra Login Bypass via SQL Injection]]'
- '[[Cloudflare Tunnel Exposer Pivoting]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[Connect to Windows using PsExec (Authenticated)]]'
- '[[Connect to WinRM from a Linux System (Pass-the-Hash)]]'
- '[[Copy file from HTTP to remote host WinRS + BitsAdmin]]'
- '[[Copy file to remote machine with xcopy (LOL)]]'
- '[[Copying EC2 Instances using AMI Image in AWS]]'
- '[[Create a Golden Ticket and Launch a Windows Shell (Windows)]]'
- '[[Create a Golden Ticket and Launch a Windows SYSTEM Shell (Linux)]]'
- '[[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]'
- '[[Cross-Site Request Forgery with File Upload]]'
- '[[Cross-Site Request Forgery with File Upload]]'
- '[[Custom Metadata PHP Injection]]'
- '[[DB2 Configuration Parameters Retrieval]]'
- '[[DB2 Current Database Selection]]'
- '[[DB2 Enumeration]]'
- '[[DB2 Injection - ASCII Concatenation]]'
- '[[DB2 Injection - ASCII Value Extraction]]'
- '[[DB2 Injection - Bitwise AND Operation]]'
- '[[DB2 Injection - Char to ASCII Conversion]]'
- '[[DB2 Injection - Find Tables From Column Name]]'
- '[[DB2 Injection - List Tables]]'
- '[[DB2 Injection: Retrieval of DB2PATH]]'
- '[[DB2 Injection with Comment Filtering]]'
- '[[DB2 Integer Conversion Injection]]'
- '[[DB2 List DBA Accounts Procedure]]'
- '[[DB2 Version Information Extraction]]'
- '[[DBMS Identification via SQL Injection Commands]]'
- '[[DBMS Magic Functions Injection]]'
- '[[DCOM DCE RPC Relay using RemotePotato0]]'
- '[[DCOM Lateral Movement]]'
- '[[DCOM Office Remote Code Execution]]'
- '[[DCOM ShellBrowserWindow Calculator Execution]]'
- '[[DCOM Shell Command Execution via MMC Application Class]]'
- '[[DCOM ShellExecute Calculator Execution]]'
- '[[Disable CloudTrail on Specific Regions]]'
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[Disabling CloudTrail Trail]]'
- '[[DNS Rebinding Protection Bypass via CNAME]]'
- '[[DNS Rebinding Server-Side Request Forgery]]'
- '[[Docker API Port Scanning and Container Management]]'
- '[[Drop the MIC Relay Attack]]'
- '[[Drop the MIC - Resource Based Constrained Delegation Attack]]'
- '[[EKS Fargate Profile Enumeration]]'
- '[[Enclosed Alphanumeric Server-Side Request Forgery]]'
- '[[Establishing and Enumerating PAM Trust between lab.local and bastion.local]]'
- '[[Execute a Command on a Remote System with WinRM]]'
- '[[Execute Commands with an Active Directory Machine Account]]'
- '[[Execute .NET Remote Execution with Beacon Post-Exploitation Job]]'
- '[[Exploit a Backdoor in UnrealIRCd 3.2.8]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting PrintNightmare to gain SYSTEM shell on DC]]'
- '[[Exploiting PrintNightmare to gain SYSTEM shell on Domain Controller]]'
- '[[Extracting Service Principal Keys from /etc/krb5.keytab]]'
---

# Lateral Movement

**MITRE ID**: TA0008

## Description

Lateral movement consists of techniques that enable an adversary to access and control remote systems on a network and could, but does not necessarily, include execution of tools on remote systems. The lateral movement techniques could allow an adversary to gather information from a system without needing additional tools, such as a remote access tool.

## Techniques

This tactic includes 23 techniques:

- [[AppleScript|T1155 - AppleScript]]
- [[Application Access Token|T1527 - Application Access Token]]
- [[Application Deployment Software|T1017 - Application Deployment Software]]
- [[Distributed Component Object Model|T1175 - Distributed Component Object Model]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Internal Spearphishing|T1534 - Internal Spearphishing]]
- [[Lateral Tool Transfer|T1570 - Lateral Tool Transfer]]
- [[Logon Scripts|T1037 - Logon Scripts]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]
- [[Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]
- [[Remote File Copy|T1105 - Remote File Copy]]
- [[Remote Services|T1021 - Remote Services]]
- [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]
- [[Replication Through Removable Media|T1091 - Replication Through Removable Media]]
- [[Shared Webroot|T1051 - Shared Webroot]]
- [[SSH Hijacking|T1184 - SSH Hijacking]]
- [[Taint Shared Content|T1080 - Taint Shared Content]]
- [[Third-party Software|T1072 - Third-party Software]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]
- [[Web Session Cookie|T1506 - Web Session Cookie]]
- [[Windows Admin Shares|T1077 - Windows Admin Shares]]
- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Related Procedures

There are 100 procedures implementing this tactic:

- [[Account Takeover via Password Reset Feature and IDOR on API Parameters]]
- [[Active Directory Assessment and Privilege Escalation]]
- [[Active Directory Integrated DNS Enumeration]]
- [[Active Directory Man-in-the-Middle and Password Cracking]]
- [[Active Directory Trust Ticket Forgery with Mimikatz]]
- [[AD CS Relay Attack with Rubeus and PetitPotam]]
- [[Add Domain Admin to RODC Password Replication Group Procedure]]
- [[AWS API Enumeration]]
- [[AWS API Gateway Method Enumeration]]
- [[AWS EBS Snapshot Volume Creation]]
- [[AWS EKS Service Account Token Theft]]
- [[AWS Fargate Container Credentials Theft]]
- [[AWS IAM Group Managed Policies Enumeration]]
- [[AWS IAM Inline Policy Enumeration]]
- [[AWS IAM Policy Version Information Retrieval]]
- [[AWS IAM Policy Version Retrieval]]
- [[AWS IAM Role Inline Policy Enumeration]]
- [[AWS IAM User Policy Enumeration]]
- [[AWS Lambda Backdoor Persistence]]
- [[AWS Lambda Function Invocation for Privilege Escalation]]

*...and 80 more*
