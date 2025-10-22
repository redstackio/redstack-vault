---
id: 84ee1e3a-c843-441a-b4f8-8b1136445018
name: Unsecured Credentials
type: technique
mitre_id: T1552
mitre_url: null
created_at: '2023-04-06T00:31:26.009948+00:00'
updated_at: '2023-05-24T20:13:51.754141+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[AWS API Gateway Stage Enumeration]]'
- '[[AWS CLI Configuration]]'
- '[[AWS Console Access via API Keys]]'
- '[[AWS IAM Access Key Enumeration]]'
- '[[AWS KMS Key Listing]]'
- '[[AWS Secret Manager Listing]]'
- '[[AWS Secrets Manager - Describe Secret]]'
- '[[AWS Secrets Manager Resource-Based Policy Exfiltration]]'
- '[[Azure Access Token Retrieval for Management and Graph APIs using Python]]'
- '[[Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell]]'
- '[[Azure Managed Identity Token Theft via Environment Variables]]'
- '[[Credential Harvesting from DynamoDB]]'
- '[[Domain Takeover via Certifried CVE-2022-26923]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Exploiting IIS Machine Keys to Generate ViewState for RCE]]'
- '[[Extracting Network Credentials using Powershell]]'
- '[[Facebook Access Token Leakage]]'
- '[[Facebook Access Token Leakage]]'
- '[[Facebook Access Token Leakage]]'
- '[[Git Index File Recovery]]'
- '[[Git Repository Secrets Harvesting with Trufflehog]]'
- '[[Gitrob Secret Harvesting]]'
- '[[Git Source Code Leakage]]'
- '[[Golden SAML Attack via ADFS]]'
- '[[Golden SAML Attack with Shimit Installation and Configuration]]'
- '[[IIS Machine Key Exploitation]]'
- '[[IIS Machine Key Exploitation]]'
- '[[IIS Machine Key Exploitation]]'
- '[[IIS Machine Key Exploitation via API Key Leaks]]'
- '[[IIS Machine Key Exploitation via API Key Leaks]]'
- '[[IIS Machine Key Exploitation via API Key Leaks]]'
- '[[Kerberos Unconstrained Delegation via SpoolService Abuse]]'
- '[[Linux Privilege Escalation via SSH Key]]'
- '[[Mapbox API Token Leakage]]'
- '[[Mapbox API Token Leakage]]'
- '[[Mapbox API Token Leakage]]'
- '[[MS-EFSRPC Abuse with Unconstrained Delegation and PetitPotam Attack]]'
- '[[Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[Shadow Credentials for Windows Hello]]'
- '[[SSRF Wrapper Credential Access]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Windows - Password Looting via System and Application Logs]]'
- '[[Windows Privilege Escalation - Powershell History Looting]]'
---

# Unsecured Credentials

**MITRE ID**: T1552

## Description

Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Bash History](https://attack.mitre.org/techniques/T1552/003)), operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)), or other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (55)

- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[API Key Leaks Detection with TruffleHog]]
- [[API Key Leaks Detection with TruffleHog]]
- [[API Key Leaks Detection with TruffleHog]]
- [[AWS API Gateway Stage Enumeration]]
- [[AWS CLI Configuration]]
- [[AWS Console Access via API Keys]]
- [[AWS IAM Access Key Enumeration]]
- [[AWS KMS Key Listing]]
- [[AWS Secret Manager Listing]]
- [[AWS Secrets Manager - Describe Secret]]
- [[AWS Secrets Manager Resource-Based Policy Exfiltration]]
- [[Azure Access Token Retrieval for Management and Graph APIs using Python]]
- [[Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell]]
- [[Azure Managed Identity Token Theft via Environment Variables]]
- [[Credential Harvesting from DynamoDB]]
- [[Domain Takeover via Certifried CVE-2022-26923]]
- [[Exploiting IIS Machine Keys to Generate ViewState for RCE]]

*...and 35 more*
