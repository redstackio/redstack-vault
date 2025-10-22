---
id: f28be3d0-3c98-490f-868f-b58303292c5d
name: Credentials from Web Browsers
type: sub-technique
mitre_id: T1555.003
mitre_url: null
created_at: '2023-04-06T00:31:26.178756+00:00'
updated_at: '2023-04-06T00:31:26.178756+00:00'
parent_technique: '[[Credentials from Password Stores|T1555 - Credentials from Password
  Stores]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[Credential Harvesting from DynamoDB]]'
- '[[Extracting Service Principal Keys from /etc/krb5.keytab]]'
- '[[HTTP Request Smuggling Detection and Exploitation]]'
- '[[Insecure Source Code Management with Bazaar using bzr_dumper]]'
- '[[Linux Password Looting]]'
- '[[Shadow Credentials for Windows Hello]]'
- '[[Windows DPAPI Credential Retrieval with Mimikatz]]'
- '[[Windows - Retail Credential Theft]]'
---

# Credentials from Web Browsers

**MITRE ID**: T1555.003

**Parent Technique**: [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

This is a sub-technique of T1555 - Credentials from Password Stores.

## Summary

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.(Citation: Talos Olympic Destroyer 2018) Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers ty

## Description

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.(Citation: Talos Olympic Destroyer 2018) Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers.

For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, <code>AppData\Local\Google\Chrome\User Data\Default\Login Data</code> and executing a SQL query: <code>SELECT action_url, username_value, password_value FROM logins;</code>. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function <code>CryptUnprotectData</code>, which uses the victim’s cached logon credentials as the decryption key.(Citation: Microsoft CryptUnprotectData April 2018)

Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc.(Citation: Proofpoint Vega Credential Stealer May 2018)(Citation: FireEye HawkEye Malware July 2017) Windows stores Internet Explorer and Microsoft Edge credentials in Credential Lockers managed by the [Windows Credential Manager](https://attack.mitre.org/techniques/T1555/004).

Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials.(Citation: GitHub Mimikittenz July 2016)

After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 9 procedures using this sub-technique:

- [[Automated Password Extraction from SYSVOL and Group Policy Preferences]]
- [[Credential Harvesting from DynamoDB]]
- [[Extracting Service Principal Keys from /etc/krb5.keytab]]
- [[HTTP Request Smuggling Detection and Exploitation]]
- [[Insecure Source Code Management with Bazaar using bzr_dumper]]
- [[Linux Password Looting]]
- [[Shadow Credentials for Windows Hello]]
- [[Windows DPAPI Credential Retrieval with Mimikatz]]
- [[Windows - Retail Credential Theft]]
