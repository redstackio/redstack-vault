---
id: 4bc3d461-280e-46bd-9354-6fefcb3efbb9
name: Credential Access
type: tactic
mitre_id: TA0006
mitre_url: null
created_at: '2019-08-28T21:17:32.817028+00:00'
updated_at: '2023-05-29T16:48:53.579491+00:00'
techniques:
- '[[Account Manipulation|T1098 - Account Manipulation]]'
- '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
- '[[Bash History|T1139 - Bash History]]'
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Credentials from Web Browsers]]'
- '[[Credentials from Web Browsers|T1503 - Credentials from Web Browsers]]'
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Credentials in Registry|T1214 - Credentials in Registry]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Forced Authentication|T1187 - Forced Authentication]]'
- '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
- '[[Hooking|T1179 - Hooking]]'
- '[[Input Capture|T1056 - Input Capture]]'
- '[[Input Prompt|T1141 - Input Prompt]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Keychain|T1142 - Keychain]]'
- '[[LLMNR/NBT-NS Poisoning and Relay|T1171 - LLMNR/NBT-NS Poisoning and Relay]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[Multi-Factor Authentication Request Generation|T1621 - Multi-Factor Authentication
  Request Generation]]'
- '[[Network Sniffing|T1040 - Network Sniffing]]'
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
- '[[Private Keys|T1145 - Private Keys]]'
- '[[Securityd Memory|T1167 - Securityd Memory]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
- '[[Steal or Forge Authentication Certificates|T1649 - Steal or Forge Authentication
  Certificates]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
- '[[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
procedures:
- '[[2FA Bypass via Force Browsing]]'
- '[[2FA Bypass via Response Manipulation]]'
- '[[2FA Bypass with Array of OTPs]]'
- '[[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]'
- '[[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active Directory Assessment and Privilege Escalation]]'
- '[[Active Directory Certificate Services ESC9 Attack]]'
- '[[Active Directory Credential Dumping via Vssadmin]]'
- '[[Active Directory Recon using BloodHound and Certipy]]'
- '[[Active Directory Trust Ticket Forgery with Mimikatz]]'
- '[[AD CS Relay Attack with Rubeus and PetitPotam]]'
- '[[Add DCSync Rights with WriteDACL Active Directory Permissions]]'
- '[[Add SPN to a Domain User and Kerberoast for NTLMv2 Hash]]'
- '[[Add User to Active Directory Domain Group]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[ASCII Conversion XSS Filter Bypass]]'
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[AWS API Gateway Stage Enumeration]]'
- '[[AWS CLI Configuration]]'
- '[[AWS Configuration Exploitation for Credential Access]]'
- '[[AWS Console Access via API Keys]]'
- '[[AWS Credential Export]]'
- '[[AWS Credential Testing]]'
- '[[AWS EC2 IAM Instance Profile Enumeration]]'
- '[[AWS EC2 Instance Profile Privilege Escalation]]'
- '[[AWS ECR Repository Enumeration]]'
- '[[AWS ECR Repository Policy Enumeration]]'
- '[[AWS ECS Task Enumeration]]'
- '[[AWS IAM Access Key Enumeration]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[AWS IAM User Enumeration and Credential Checking]]'
- '[[AWS Instance Profile Enumeration]]'
- '[[AWS KMS Key Listing]]'
- '[[AWS KMS Key Listing]]'
- '[[AWS Lambda Backdoor Persistence]]'
- '[[AWS Lambda Event Source Mapping Enumeration]]'
- '[[AWS Lambda Layer Enumeration]]'
- '[[AWS Managed Policies Enumeration]]'
- '[[AWS Metadata Credential Theft]]'
- '[[AWS Privilege Escalation via Attached User Policies]]'
- '[[AWS Privilege Escalation via Default Policy Information]]'
- '[[AWS Secret Manager Listing]]'
- '[[AWS Secrets Manager - Describe Secret]]'
- '[[AWS Secrets Manager Resource-Based Policy Exfiltration]]'
- '[[Azure Access Token Retrieval for Management and Graph APIs using Python]]'
- '[[Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell]]'
- '[[Azure AD Connect Monitoring Disable and Password Reset]]'
- '[[Azure AD Connect - Password Extraction via AD Sync Account DCSync]]'
- '[[Azure AD Connect - Silver Ticket Attack]]'
- '[[Azure AD Password Spray]]'
- '[[Azure Device Management and Token Generation with SharpAzToken]]'
- '[[Azure Graph API Refresh Token]]'
- '[[Azure Key Vault Access and Query with PowerShell]]'
- '[[Azure Managed Identity Token Theft via Environment Variables]]'
- '[[Azure Pass The PRT with Mimikatz]]'
- '[[Azure Password Spraying]]'
- '[[Azure Resource Management and Privilege Checking with PowerShell]]'
- '[[Azure Retrieving Passwords using Microburst]]'
- '[[Azure Token Generation and Authentication with SharpAzToken]]'
- '[[Basic Jinja2 Server Side Template Injection]]'
- '[[BigQuery SQL Injection Attack]]'
- '[[Blind NoSQL Injection via Brute Force]]'
- '[[Breaking JWT Secrets]]'
- '[[Brute Force and Mount a LUKS1 Encrypted File System (EFS)]]'
- '[[Brute Force a Password Hash using John the Ripper]]'
- '[[Brute Force a Password Protected XLSX File]]'
- '[[Brute Force a Web Login Form]]'
- '[[Brute Force MongoDB Password via POST with urlencoded body]]'
- '[[Brute Force Password Hashes (Hashcat)]]'
- '[[Brute Force Private SSH Key Password]]'
- '[[Brute Force Shadow Hashes]]'
- '[[Brute Force SMB Usernames and Passwords]]'
- '[[Brute Force SMB Users Using RID (Authenticated)]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
- '[[Brute Force Valid Users from a Forgotten Password Form]]'
- '[[Build a Password List for Online Dictionary Attack]]'
- '[[CCACHE Ticket Reuse from Keyring with Tickey]]'
- '[[CCACHE Ticket Reuse from Keytab]]'
- '[[CCACHE Ticket Reuse from SSSD KCM and Android Devices]]'
- '[[CCACHE Ticket Reuse from /tmp]]'
- '[[Change an AD Domain User''s Password]]'
- '[[Checksum Validation Exploitation for Active Directory]]'
- '[[Cloud Instance SSRF through OpenStack Metadata URL]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[CLR Assembly Creation and Execution]]'
- '[[CL.TE Request Smuggling]]'
- '[[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[CORS Misconfiguration Exploitation via Wildcard Origin `*` without Credentials]]'
- '[[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]'
- '[[Credential Harvesting from DynamoDB]]'
---

# Credential Access

**MITRE ID**: TA0006

## Description

Credential access represents techniques resulting in access to or control over system, domain, or service credentials that are used within an enterprise environment. Adversaries will likely attempt to obtain legitimate credentials from users or administrator accounts (local system administrator or domain users with administrator access) to use within the network. This allows the adversary to assume the identity of the account, with all of that account's permissions on the system and network, and makes it harder for defenders to detect the adversary. With sufficient access within a network, an adversary can create accounts for later use within the environment.

## Techniques

This tactic includes 32 techniques:

- [[Account Manipulation|T1098 - Account Manipulation]]
- [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]
- [[Bash History|T1139 - Bash History]]
- [[Brute Force|T1110 - Brute Force]]
- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Credentials from Web Browsers]]
- [[Credentials from Web Browsers|T1503 - Credentials from Web Browsers]]
- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Credentials in Registry|T1214 - Credentials in Registry]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Forced Authentication|T1187 - Forced Authentication]]
- [[Forge Web Credentials|T1606 - Forge Web Credentials]]
- [[Hooking|T1179 - Hooking]]
- [[Input Capture|T1056 - Input Capture]]
- [[Input Prompt|T1141 - Input Prompt]]
- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Keychain|T1142 - Keychain]]
- [[LLMNR/NBT-NS Poisoning and Relay|T1171 - LLMNR/NBT-NS Poisoning and Relay]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[Multi-Factor Authentication Request Generation|T1621 - Multi-Factor Authentication Request Generation]]
- [[Network Sniffing|T1040 - Network Sniffing]]
- [[Password Filter DLL|T1174 - Password Filter DLL]]
- [[Private Keys|T1145 - Private Keys]]
- [[Securityd Memory|T1167 - Securityd Memory]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]
- [[Steal or Forge Authentication Certificates|T1649 - Steal or Forge Authentication Certificates]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]
- [[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Related Procedures

There are 100 procedures implementing this tactic:

- [[2FA Bypass via Force Browsing]]
- [[2FA Bypass via Response Manipulation]]
- [[2FA Bypass with Array of OTPs]]
- [[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]
- [[Active Directory ACL Abuse via Kerberoasting and AS-REP Roasting]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active Directory Assessment and Privilege Escalation]]
- [[Active Directory Certificate Services ESC9 Attack]]
- [[Active Directory Credential Dumping via Vssadmin]]
- [[Active Directory Recon using BloodHound and Certipy]]
- [[Active Directory Trust Ticket Forgery with Mimikatz]]
- [[AD CS Relay Attack with Rubeus and PetitPotam]]
- [[Add DCSync Rights with WriteDACL Active Directory Permissions]]
- [[Add SPN to a Domain User and Kerberoast for NTLMv2 Hash]]
- [[Add User to Active Directory Domain Group]]
- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[API Key Leaks Detection with TruffleHog]]
- [[API Key Leaks Detection with TruffleHog]]

*...and 80 more*
