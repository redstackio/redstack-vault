---
id: 4b0c85b3-4e07-49ae-8c49-9c37acd8ad03
name: Keychain
type: sub-technique
mitre_id: T1555.001
mitre_url: null
created_at: '2023-04-06T00:31:25.688072+00:00'
updated_at: '2023-04-06T00:31:25.688072+00:00'
parent_technique: '[[Credentials from Password Stores|T1555 - Credentials from Password
  Stores]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[HTTP Request Smuggling Detection and Exploitation]]'
---

# Keychain

**MITRE ID**: T1555.001

**Parent Technique**: [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

This is a sub-technique of T1555 - Credentials from Password Stores.

## Summary

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychai

## Description

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. 

Keychains can be viewed and edited through the Keychain Access application or using the command-line utility <code>security</code>. Keychain files are located in <code>~/Library/Keychains/</code>, <code>/Library/Keychains/</code>, and <code>/Network/Library/Keychains/</code>.(Citation: Keychain Services Apple)(Citation: Keychain Decryption Passware)(Citation: OSX Keychain Schaumann)

Adversaries may gather user credentials from Keychain storage/memory. For example, the command <code>security dump-keychain –d</code> will dump all Login Keychain credentials from <code>~/Library/Keychains/login.keychain-db</code>. Adversaries may also directly read Login Keychain credentials from the <code>~/Library/Keychains/login.keychain</code> file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.(Citation: External to DA, the OS X Way)(Citation: Empire Keychain Decrypt)  

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[HTTP Request Smuggling Detection and Exploitation]]
