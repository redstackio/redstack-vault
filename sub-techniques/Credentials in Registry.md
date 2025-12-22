---
id: ab273122-6d7d-49d8-8cbd-9399071d5ed3
name: Credentials in Registry
type: sub-technique
mitre_id: T1552.002
mitre_url: null
created_at: '2023-04-06T00:31:25.873824+00:00'
updated_at: '2023-04-06T00:31:25.873824+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AWS-CLI-Configuration]]'
- '[[AWS-IAM-Access-Key-Enumeration]]'
- '[[Describe-AWS-KMS-Key]]'
- '[[Describe-AWS-Secrets-Manager-Secret]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Debug-Facebook-Access-Token]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]'
- '[[Exploit-SSRF-to-Access-AWS-Instance-Metadata-Credentials]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]'
- '[[Windows-Privilege-Escalation-via-Powershell-History-Looting]]'
---

# Credentials in Registry

**MITRE ID**: T1552.002

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may search the Registry on compromised systems for insecurely stored credentials. The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use

## Description

Adversaries may search the Registry on compromised systems for insecurely stored credentials. The Windows Registry stores configuration information that can be used by the system or other programs. Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services. Sometimes these credentials are used for automatic logons.

Example commands to find Registry keys related to password information: (Citation: Pentestlab Stored Credentials)

* Local Machine Hive: <code>reg query HKLM /f password /t REG_SZ /s</code>
* Current User Hive: <code>reg query HKCU /f password /t REG_SZ /s</code>

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 18 procedures using this sub-technique:

- [[AWS-CLI-Configuration]]
- [[AWS-IAM-Access-Key-Enumeration]]
- [[Describe-AWS-KMS-Key]]
- [[Describe-AWS-Secrets-Manager-Secret]]
- [[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]
- [[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]
- [[Generate-Malicious-ViewState-for-IIS-RCE-Using-Machine-Keys]]
- [[Debug-Facebook-Access-Token]]
- [[Debug-Facebook-Access-Token]]
- [[Debug-Facebook-Access-Token]]
- [[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]
- [[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]
- [[Exploit-IIS-Machine-Key-via-API-Key-Leaks]]
- [[Exploit-SSRF-to-Access-AWS-Instance-Metadata-Credentials]]
- [[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]
- [[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]
- [[Authenticate-with-Twitter-API-Using-Leaked-Key-and-Secret]]
- [[Windows-Privilege-Escalation-via-Powershell-History-Looting]]
