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
- '[[Account-Takeover-via-Password-Reset-and-IDOR-on-API-Parameters]]'
- '[[Active-Directory-Assessment-and-Privilege-Escalation]]'
- '[[Active-Directory-Integrated-DNS-Enumeration]]'
- '[[Active-Directory-MitM-and-Password-Cracking]]'
- '[[Forge-AD-Trust-Ticket-with-Mimikatz]]'
- '[[AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]'
- '[[Add-Domain-Admin-to-RODC-Password-Replication-Group]]'
- '[[Enumerate-AWS-API-Gateway-REST-APIs]]'
- '[[AWS-API-Gateway-Method-Enumeration]]'
- '[[AWS-EBS-Snapshot-Volume-Creation]]'
- '[[AWS-EKS-Service-Account-Token-Theft]]'
- '[[AWS-Fargate-Container-Credentials-Theft]]'
- '[[AWS-IAM-Group-Managed-Policies-Enumeration]]'
- '[[Enumerate-AWS-IAM-Inline-Policies]]'
- '[[Retrieve-AWS-IAM-Policy-Version-Details]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[AWS-IAM-Role-Inline-Policy-Enumeration]]'
- '[[Enumerate-IAM-User-Attached-Policies]]'
- '[[aws-lambda-backdoor-persistence]]'
- '[[AWS-Lambda-Function-Invocation-for-Privilege-Escalation]]'
- '[[Retrieve-AWS-EC2-Instance-Credentials-via-Metadata-Service]]'
- '[[Configure-AWS-CLI-for-S3-Access]]'
- '[[Configure-AWS-CLI-for-S3-Access]]'
- '[[Create-AWS-Glue-Development-Endpoint]]'
- '[[aws-ssm-command-execution-ec2-shell-script]]'
- '[[AWS-User-Policy-Enumeration]]'
- '[[Azure-AD-Connect-Silver-Ticket-Attack]]'
- '[[Generate-Azure-Blob-Storage-SAS-URLs]]'
- '[[Azure - Illicit Consent Grant Prevention]]'
- '[[Retrieve-Access-Tokens-from-Azure-Managed-Identity]]'
- '[[azure-pass-the-certificate-ad-cert-request-and-rce]]'
- '[[Azure-Pass-The-PRT-with-Mimikatz]]'
- '[[Azure-Resource-Management-and-Privilege-Checking-with-PowerShell]]'
- '[[Exploit-Azure-SSRF-to-Access-VM-Metadata-Service]]'
- '[[azure-vm-runcommand-execution]]'
- '[[azure-web-apps-remote-ssh-connection]]'
- '[[Establish-Bash-TCP-Reverse-Shell]]'
- '[[Basic-Directory-Traversal-Exploitation]]'
- '[[BITSAdmin-Download-and-Execute-Payload]]'
- '[[Perform-Blind-XPath-Injection-for-Data-Extraction]]'
- '[[Browse-FTP-Site-with-Interactive-Session]]'
- '[[browse-smb-share-using-ntlm-hash]]'
- '[[Bypass-SSRF-Filters-with-IPv6-Loopback-Addresses]]'
- '[[Cassandra-Login-Bypass-via-SQL-Injection]]'
- '[[Cloudflare-Tunnel-Pivoting-for-Lateral-Movement]]'
- '[[aws-cloud-security-assessment-and-auditing]]'
- '[[psexec-authenticated-remote-shell]]'
- '[[Query-LDAP-and-Enumerate-Base-DN-with-Nmap]]'
- '[[Copy-File-to-Remote-Windows-Host-Using-WinRS-and-BitsAdmin]]'
- '[[Copy-File-to-Remote-Windows-Machine-via-Xcopy]]'
- '[[Copy-EC2-Instance-via-AMI-Creation-in-AWS]]'
- '[[Create-Golden-Ticket-and-Launch-Windows-Shell]]'
- '[[Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]'
- '[[Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]'
- '[[Perform-CSRF-Attack-via-File-Upload]]'
- '[[Perform-CSRF-Attack-via-File-Upload]]'
- '[[Inject-PHP-Code-into-Image-Metadata-for-RCE]]'
- '[[DB2-Configuration-Parameters-Retrieval]]'
- '[[DB2-Current-Server-Query]]'
- '[[Enumerate-DB2-Databases-and-Schemas]]'
- '[[DB2-SQL-Injection-Using-ASCII-Concatenation]]'
- '[[DB2-SQL-Injection-ASCII-Value-Extraction]]'
- '[[DB2 Injection - Bitwise AND Operation]]'
- '[[DB2-SQL-Injection-Using-ASCII-Function]]'
- '[[DB2-SQL-Injection-to-Find-Tables-by-Column-Name]]'
- '[[List-Tables-via-DB2-SQL-Injection]]'
- '[[Retrieve-DB2PATH-via-SQL-Injection]]'
- '[[DB2-SQL-Injection-Using-Comments]]'
- '[[DB2-Integer-Conversion-SQL-Injection]]'
- '[[DB2-List-DBA-Accounts-via-SQL-Injection]]'
- '[[Extract-DB2-Database-Version-Information]]'
- '[[DBMS-Fingerprinting-via-SQL-Injection]]'
- '[[DBMS-Magic-Functions-Injection]]'
- '[[DCOM-DCE-RPC-Relay-using-RemotePotato0]]'
- '[[dcom-lateral-movement]]'
- '[[DCOM-Office-Remote-Code-Execution]]'
- '[[dcom-shellbrowserwindow-calculator-execution]]'
- '[[DCOM-Shell-Command-Execution-via-MMC-Application-Class]]'
- '[[dcom-shellexecute-calculator-execution]]'
- '[[Disable-CloudTrail-on-Specific-Regions]]'
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[Disable-CloudTrail-Logging-via-Trail-Deletion]]'
- '[[DNS-Rebinding-Protection-Bypass-via-CNAME]]'
- '[[DNS-Rebinding-for-SSRF-Bypass]]'
- '[[Exploit-Open-Docker-API-for-Container-Management]]'
- '[[Drop-the-MIC-NTLM-Relay-Attack]]'
- '[[resource-based-constrained-delegation-via-printerbug]]'
- '[[EKS-Fargate-Profile-Enumeration]]'
- '[[Bypass-SSRF-Filters-Using-Enclosed-Alphanumerics]]'
- '[[Establish-and-Enumerate-PAM-Trust-Between-Domains]]'
- '[[execute-command-on-remote-system-with-winrm]]'
- '[[Execute-Commands-with-an-Active-Directory-Machine-Account]]'
- '[[Execute-NET-Assembly-via-Cobalt-Strike-Beacon]]'
- '[[Exploit-Backdoor-in-UnrealIRCd-3.2.8]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Exploit-PrintNightmare-for-SYSTEM-Shell-on-Domain-Controller]]'
- '[[Exploit-PrintNightmare-for-SYSTEM-Access-on-Domain-Controller]]'
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

- [[Account-Takeover-via-Password-Reset-and-IDOR-on-API-Parameters]]
- [[Active-Directory-Assessment-and-Privilege-Escalation]]
- [[Active-Directory-Integrated-DNS-Enumeration]]
- [[Active-Directory-MitM-and-Password-Cracking]]
- [[Forge-AD-Trust-Ticket-with-Mimikatz]]
- [[AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[Add-Domain-Admin-to-RODC-Password-Replication-Group]]
- [[Enumerate-AWS-API-Gateway-REST-APIs]]
- [[AWS-API-Gateway-Method-Enumeration]]
- [[AWS-EBS-Snapshot-Volume-Creation]]
- [[AWS-EKS-Service-Account-Token-Theft]]
- [[AWS-Fargate-Container-Credentials-Theft]]
- [[AWS-IAM-Group-Managed-Policies-Enumeration]]
- [[Enumerate-AWS-IAM-Inline-Policies]]
- [[Retrieve-AWS-IAM-Policy-Version-Details]]
- [[Retrieve-AWS-IAM-Policy-Version]]
- [[AWS-IAM-Role-Inline-Policy-Enumeration]]
- [[Enumerate-IAM-User-Attached-Policies]]
- [[aws-lambda-backdoor-persistence]]
- [[AWS-Lambda-Function-Invocation-for-Privilege-Escalation]]

*...and 80 more*


e*


