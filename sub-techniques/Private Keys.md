---
id: 3ff7fb9b-ee88-4ff3-b20b-d9ed6eaccd36
name: Private Keys
type: sub-technique
mitre_id: T1552.004
mitre_url: null
created_at: '2023-04-06T00:31:26.208891+00:00'
updated_at: '2023-04-06T00:31:26.208891+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[Algolia API Key Leak Exploit]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[API Key Leaks Detection with TruffleHog]]'
- '[[AWS CLI Configuration]]'
- '[[AWS Console Access via API Keys]]'
- '[[AWS Secret Manager Listing]]'
- '[[Facebook Access Token Leakage]]'
- '[[Facebook Access Token Leakage]]'
- '[[Facebook Access Token Leakage]]'
- '[[Git Index File Recovery]]'
- '[[Golden SAML Attack via ADFS]]'
- '[[Golden SAML Attack with Shimit Installation and Configuration]]'
- '[[Mapbox API Token Leakage]]'
- '[[Mapbox API Token Leakage]]'
- '[[Mapbox API Token Leakage]]'
- '[[Shadow Credentials for Windows Hello]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twilio API Key Leakage]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
---

# Private Keys

**MITRE ID**: T1552.004

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures.(Citation: Wikipedia Public Key Crypto) Common key and certificate

## Description

Adversaries may search for private key certificate files on compromised systems for insecurely stored credentials. Private cryptographic keys and certificates are used for authentication, encryption/decryption, and digital signatures.(Citation: Wikipedia Public Key Crypto) Common key and certificate file extensions include: .key, .pgp, .gpg, .ppk., .p12, .pem, .pfx, .cer, .p7b, .asc. 

Adversaries may also look in common key directories, such as <code>~/.ssh</code> for SSH keys on * nix-based systems or <code>C:&#92;Users&#92;(username)&#92;.ssh&#92;</code> on Windows. These private keys can be used to authenticate to [Remote Services](https://attack.mitre.org/techniques/T1021) like SSH or for use in decrypting other collected files such as email.

Adversary tools have been discovered that search compromised systems for file extensions relating to cryptographic keys and certificates.(Citation: Kaspersky Careto)(Citation: Palo Alto Prince of Persia)

Some private keys require a password or passphrase for operation, so an adversary may also use [Input Capture](https://attack.mitre.org/techniques/T1056) for keylogging or attempt to [Brute Force](https://attack.mitre.org/techniques/T1110) the passphrase off-line.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 25 procedures using this sub-technique:

- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[Algolia API Key Leak Exploit]]
- [[API Key Leaks Detection with TruffleHog]]
- [[API Key Leaks Detection with TruffleHog]]
- [[API Key Leaks Detection with TruffleHog]]
- [[AWS CLI Configuration]]
- [[AWS Console Access via API Keys]]
- [[AWS Secret Manager Listing]]
- [[Facebook Access Token Leakage]]
- [[Facebook Access Token Leakage]]
- [[Facebook Access Token Leakage]]
- [[Git Index File Recovery]]
- [[Golden SAML Attack via ADFS]]
- [[Golden SAML Attack with Shimit Installation and Configuration]]
- [[Mapbox API Token Leakage]]
- [[Mapbox API Token Leakage]]
- [[Mapbox API Token Leakage]]
- [[Shadow Credentials for Windows Hello]]
- [[Twilio API Key Leakage]]

*...and 5 more*
