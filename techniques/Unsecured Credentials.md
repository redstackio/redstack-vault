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
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[api-key-leaks-detection-with-trufflehog]]'
- '[[AWS-API-Gateway-Stage-Enumeration]]'
- '[[AWS-CLI-Configuration]]'
- '[[AWS-Console-Access-via-API-Keys]]'
- '[[AWS-IAM-Access-Key-Enumeration]]'
- '[[Describe-AWS-KMS-Key]]'
- '[[List-Secrets-in-AWS-Secrets-Manager]]'
- '[[Describe-AWS-Secrets-Manager-Secret]]'
- '[[aws-secretsmanager-resource-based-policy-exfiltration]]'
- '[[Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python]]'
- '[[Extract-Azure-Access-Tokens-and-Service-Principal-Secrets-from-CLI-and-PowerShell]]'
- '[[Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]'
- '[[Scan-DynamoDB-Table-for-Credentials]]'
- '[[Domain-Takeover-via-Certifried-CVE-2022-26923]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Extract-Credentials-from-SecureString-PowerShell]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Git-Index-File-Recovery]]'
- '[[Git-Repository-Secrets-Harvesting-with-TruffleHog]]'
- '[[Gitrob-Secret-Harvesting]]'
- '[[Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]'
- '[[Golden-SAML-Attack-via-ADFS]]'
- '[[Golden-SAML-Attack-Using-Shimit]]'
- '[[IIS-Machine-Key-Exploitation]]'
- '[[IIS-Machine-Key-Exploitation]]'
- '[[IIS-Machine-Key-Exploitation]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[abuse-kerberos-unconstrained-delegation-via-spoolservice]]'
- '[[Linux-Privilege-Escalation-via-SSH-Key]]'
- '[[Mapbox-API-Token-Leakage]]'
- '[[Mapbox-API-Token-Leakage]]'
- '[[Mapbox-API-Token-Leakage]]'
- '[[MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]'
- '[[Extract-and-Decrypt-GPP-Passwords-from-SYSVOL]]'
- '[[Shadow-Credentials-for-Windows-Hello]]'
- '[[Exploit-SSRF-to-Access-AWS-Instance-Metadata-Credentials]]'
- '[[Exploit-Leaked-Twilio-API-Credentials]]'
- '[[Exploit-Leaked-Twilio-API-Credentials]]'
- '[[Exploit-Leaked-Twilio-API-Credentials]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Windows-Password-Looting-via-System-and-Application-Logs]]'
- '[[Windows-Privilege-Escalation-via-Powershell-History-Looting]]'
---

# Unsecured Credentials

**MITRE ID**: T1552

## Description

Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Bash History](https://attack.mitre.org/techniques/T1552/003)), operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)), or other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).



## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (55)

- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[Exploit-Leaked-Algolia-API-Key-for-Highlight-Pre-Tag-Injection]]
- [[api-key-leaks-detection-with-trufflehog]]
- [[api-key-leaks-detection-with-trufflehog]]
- [[api-key-leaks-detection-with-trufflehog]]
- [[AWS-API-Gateway-Stage-Enumeration]]
- [[AWS-CLI-Configuration]]
- [[AWS-Console-Access-via-API-Keys]]
- [[AWS-IAM-Access-Key-Enumeration]]
- [[Describe-AWS-KMS-Key]]
- [[List-Secrets-in-AWS-Secrets-Manager]]
- [[Describe-AWS-Secrets-Manager-Secret]]
- [[aws-secretsmanager-resource-based-policy-exfiltration]]
- [[Azure-Access-Token-Retrieval-for-Management-and-Graph-APIs-using-Python]]
- [[Extract-Azure-Access-Tokens-and-Service-Principal-Secrets-from-CLI-and-PowerShell]]
- [[Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]
- [[Scan-DynamoDB-Table-for-Credentials]]
- [[Domain-Takeover-via-Certifried-CVE-2022-26923]]
- [[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]

*...and 35 more*


