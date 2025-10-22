---
id: ae54b0b0-b344-4682-8361-0b265233980c
name: Credentials from Web Browsers
type: technique
mitre_id: T1503
mitre_url: null
created_at: '2023-04-06T00:31:26.028343+00:00'
updated_at: '2023-04-06T00:31:27.808114+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Credentials from Web Browsers

**MITRE ID**: T1503

## Description

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.  (Citation: Talos Olympic Destroyer 2018) 

Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers.

For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, <code>AppData\Local\Google\Chrome\User Data\Default\Login Data</code> and executing a SQL query: <code>SELECT action_url, username_value, password_value FROM logins;</code>. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function <code>CryptUnprotectData</code>, which uses the victim’s cached logon credentials as the decryption key. (Citation: Microsoft CryptUnprotectData April 2018)

Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc. (Citation: Proofpoint Vega Credential Stealer May 2018)(Citation: FireEye HawkEye Malware July 2017)

Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials.(Citation: GitHub Mimikittenz July 2016)

After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
