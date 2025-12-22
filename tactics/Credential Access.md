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
- '[[cme-smb-enable-rdp|T1208 - Kerberoasting]]'
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
- '[[Bypass-2FA-via-Force-Browsing]]'
- '[[2FA-Bypass-via-Response-Manipulation]]'
- '[[Bypass-2FA-with-OTP-Array]]'
- '[[Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]'
- '[[Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active-Directory-Assessment-and-Privilege-Escalation]]'
- '[[Active-Directory-Certificate-Services-ESC9-Attack]]'
- '[[Active-Directory-Credential-Dumping-via-Vssadmin]]'
- '[[Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]'
- '[[Forge-AD-Trust-Ticket-with-Mimikatz]]'
- '[[AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]'
- '[[Add-DCSync-Rights-via-WriteDACL-Permissions]]'
- '[[Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash]]'
- '[[Add-User-to-Active-Directory-Domain-Group]]'
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[ASCII-Conversion-XSS-Filter-Bypass]]'
- '[[Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[AWS-CLI-Configuration]]'
- '[[AWS Configuration Exploitation for Credential Access]]'
- '[[AWS-Console-Access-via-API-Keys]]'
- '[[Export-AWS-Credentials-to-Environment]]'
- '[[AWS-Credential-Testing]]'
- '[[AWS-EC2-IAM-Instance-Profile-Enumeration]]'
- '[[AWS-EC2-Instance-Profile-Privilege-Escalation]]'
- '[[Enumerate-AWS-ECR-Repositories]]'
- '[[AWS-ECR-Repository-Policy-Enumeration]]'
- '[[aws-ecs-task-enumeration]]'
- '[[AWS-IAM-Access-Key-Enumeration]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[Retrieve-AWS-IAM-Policy-Version]]'
- '[[AWS-IAM-User-Enumeration-and-Credential-Checking]]'
- '[[AWS-Instance-Profile-Enumeration]]'
- '[[Describe-AWS-KMS-Key]]'
- '[[Describe-AWS-KMS-Key]]'
- '[[aws-lambda-backdoor-persistence]]'
- '[[AWS-Lambda-Event-Source-Mapping-Enumeration]]'
- '[[AWS-Lambda-Layer-Enumeration]]'
- '[[Enumerate-AWS-Managed-Policies-for-IAM-User]]'
- '[[Retrieve-AWS-EC2-Instance-Credentials-via-Metadata-Service]]'
- '[[AWS-Privilege-Escalation-via-Attached-User-Policies]]'
- '[[AWS-Privilege-Escalation-via-Creating-Admin-Policy]]'
- '[[List-Secrets-in-AWS-Secrets-Manager]]'
- '[[Describe-AWS-Secrets-Manager-Secret]]'
- '[[aws-secretsmanager-resource-based-policy-exfiltration]]'
- '[[Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python]]'
- '[[Extract-Azure-Access-Tokens-and-Service-Principal-Secrets-from-CLI-and-PowerShell]]'
- '[[Disable-Azure-AD-Connect-Monitoring-and-Reset-On-Premises-Admin-Password]]'
- '[[azure-ad-connect-password-extraction-via-ad-sync-dcsync]]'
- '[[Azure-AD-Connect-Silver-Ticket-Attack]]'
- '[[Azure-AD-Password-Spray]]'
- '[[azure-device-management-and-token-generation-with-sharpaztoken]]'
- '[[Device-Code-Flow-Authentication-to-Microsoft-Graph-API-in-PowerShell]]'
- '[[Access-Azure-Key-Vault-Using-Managed-Identity]]'
- '[[Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]'
- '[[Azure-Pass-The-PRT-with-Mimikatz]]'
- '[[Azure-Password-Spraying]]'
- '[[Azure-Resource-Management-and-Privilege-Checking-with-PowerShell]]'
- '[[Retrieve-Azure-Passwords-Using-Microburst]]'
- '[[Generate-Azure-Tokens-with-SharpAzToken]]'
- '[[Basic-Jinja2-Server-Side-Template-Injection]]'
- '[[BigQuery-Boolean-Based-SQL-Injection]]'
- '[[Blind-NoSQL-Injection-via-Brute-Force]]'
- '[[Brute-Force-JWT-Signing-Secret]]'
- '[[Brute-Force-and-Mount-LUKS1-Encrypted-Filesystem]]'
- '[[Brute-Force-Password-Hash-with-John-the-Ripper]]'
- '[[Brute-Force-Password-Protected-XLSX-File]]'
- '[[Brute-Force-Web-Login-Form-with-Hydra]]'
- '[[Brute-Force-MongoDB-Login-via-NoSQL-Regex-Injection]]'
- '[[brute-force-hashes-with-hashcat-dictionary]]'
- '[[Brute-Force-Private-SSH-Key-Password]]'
- '[[Brute-Force-Shadow-Hashes]]'
- '[[find-interesting-strings-in-raw-memory-dump]]'
- '[[build-user-list-from-public-webpage]]'
- '[[Brute-Force-Users-Without-Kerberos-Preauthentication]]'
- '[[Brute-Force-Valid-Users-via-Forgotten-Password-Form]]'
- '[[Build-Custom-Password-List-for-Dictionary-Attack]]'
- '[[extract-ccache-tickets-from-linux-keyring-with-tickey]]'
- '[[Extract-and-Reuse-Kerberos-Tickets-from-Keytab]]'
- '[[CCACHE-Ticket-Reuse-from-SSSD-KCM-and-Android-Devices]]'
- '[[CCACHE Ticket Reuse from /tmp]]'
- '[[Change an AD Domain User''s Password]]'
- '[[Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]'
- '[[Exploit-SSRF-to-Access-OpenStack-Metadata]]'
- '[[aws-cloud-security-assessment-and-auditing]]'
- '[[CLR Assembly Creation and Execution]]'
- '[[Perform-CL.TE-HTTP-Request-Smuggling]]'
- '[[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]'
- '[[Exploit-CORS-Misconfiguration-with-Wildcard-Origin-without-Credentials]]'
- '[[Exploit-CORS-Misconfiguration-with-Wildcard-Origin-without-Credentials]]'
- '[[Exploit-CORS-Misconfiguration-with-Wildcard-Origin-without-Credentials]]'
- '[[Exploit-CORS-Misconfiguration-with-Wildcard-Origin-without-Credentials]]'
- '[[Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]'
- '[[Scan-DynamoDB-Table-for-Credentials]]'
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
- [[cme-smb-enable-rdp|T1208 - Kerberoasting]]
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

- [[Bypass-2FA-via-Force-Browsing]]
- [[2FA-Bypass-via-Response-Manipulation]]
- [[Bypass-2FA-with-OTP-Array]]
- [[Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[Active-Directory-ACL-Abuse-via-Kerberoasting-and-AS-REP-Roasting]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active-Directory-Assessment-and-Privilege-Escalation]]
- [[Active-Directory-Certificate-Services-ESC9-Attack]]
- [[Active-Directory-Credential-Dumping-via-Vssadmin]]
- [[Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[Forge-AD-Trust-Ticket-with-Mimikatz]]
- [[AD-CS-Relay-Attack-with-Rubeus-and-PetitPotam]]
- [[Add-DCSync-Rights-via-WriteDACL-Permissions]]
- [[Add-SPN-to-Domain-User-and-Kerberoast-for-NTLMv2-Hash]]
- [[Add-User-to-Active-Directory-Domain-Group]]
- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[api-key-leaks-detection-with-trufflehog]]
- [[api-key-leaks-detection-with-trufflehog]]

*...and 80 more*


