---
id: 2e484a39-7aeb-48c7-ae80-a2cafcebfc22
name: Credentials from Password Stores
type: technique
mitre_id: T1555
mitre_url: null
created_at: '2023-04-06T00:31:25.984508+00:00'
updated_at: '2023-04-06T03:56:35.671631+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[Credential Harvesting from DynamoDB]]'
- '[[Credential Harvesting from Task Scheduler using Mimikatz]]'
- '[[Extracting Network Credentials using Powershell]]'
- '[[Extracting Service Principal Keys from /etc/krb5.keytab]]'
- '[[Git Repository Secrets Harvesting with Trufflehog]]'
- '[[HTTP Request Smuggling Detection and Exploitation]]'
- '[[Insecure Source Code Management with Bazaar using bzr_dumper]]'
- '[[Linux Password Looting]]'
- '[[PostgreSQL Database Enumeration]]'
- '[[Shadow Credentials for Windows Hello]]'
- '[[Stealing Chrome Cookies and Credentials with Mimikatz]]'
- '[[Windows DPAPI Credential Retrieval with Mimikatz]]'
- '[[Windows DPAPI Credential Theft]]'
- '[[Windows - Retail Credential Theft]]'
---

# Credentials from Password Stores

**MITRE ID**: T1555

## Description

Adversaries may search for common password storage locations to obtain user credentials. Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications that store passwords to make it easier for users manage and maintain. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (15)

- [[Automated Password Extraction from SYSVOL and Group Policy Preferences]]
- [[Credential Harvesting from DynamoDB]]
- [[Credential Harvesting from Task Scheduler using Mimikatz]]
- [[Extracting Network Credentials using Powershell]]
- [[Extracting Service Principal Keys from /etc/krb5.keytab]]
- [[Git Repository Secrets Harvesting with Trufflehog]]
- [[HTTP Request Smuggling Detection and Exploitation]]
- [[Insecure Source Code Management with Bazaar using bzr_dumper]]
- [[Linux Password Looting]]
- [[PostgreSQL Database Enumeration]]
- [[Shadow Credentials for Windows Hello]]
- [[Stealing Chrome Cookies and Credentials with Mimikatz]]
- [[Windows DPAPI Credential Retrieval with Mimikatz]]
- [[Windows DPAPI Credential Theft]]
- [[Windows - Retail Credential Theft]]
