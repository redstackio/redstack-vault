---
id: d4156ed3-ea0f-4f40-82a1-a597bf93fb31
name: Install Root Certificate
type: sub-technique
mitre_id: T1553.004
mitre_url: null
created_at: '2023-04-06T00:31:26.902384+00:00'
updated_at: '2023-04-06T00:31:26.902384+00:00'
parent_technique: '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Open URL Redirection Filter Bypass]]'
- '[[PHP Juggling Type and Magic Hashes]]'
- '[[Subdomain Enumeration and Takeover with tko-subs]]'
---

# Install Root Certificate

**MITRE ID**: T1553.004

**Parent Technique**: [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

This is a sub-technique of T1553 - Subvert Trust Controls.

## Summary

Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers. Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or applicati

## Description

Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers. Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or application will trust certificates in the root's chain of trust that have been signed by the root certificate.(Citation: Wikipedia Root Certificate) Certificates are commonly used for establishing secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security settings, the browser may not allow the user to establish a connection to the website.

Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that system. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.(Citation: Operation Emmental)

Atypical root certificates have also been pre-installed on systems by the manufacturer or in the software supply chain and were used in conjunction with malware/adware to provide [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) capability for intercepting information transmitted over secure TLS/SSL communications.(Citation: Kaspersky Superfish)

Root certificates (and their associated chains) can also be cloned and reinstalled. Cloned certificate chains will carry many of the same metadata characteristics of the source and can be used to sign malicious code that may then bypass signature validation tools (ex: Sysinternals, antivirus, etc.) used to block execution and/or uncover artifacts of Persistence.(Citation: SpectorOps Code Signing Dec 2017)

In macOS, the Ay MaMi malware uses <code>/usr/bin/security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /path/to/malicious/cert</code> to install a malicious certificate as a trusted root certificate into the system keychain.(Citation: objective-see ay mami 2018)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Open URL Redirection Filter Bypass]]
- [[PHP Juggling Type and Magic Hashes]]
- [[Subdomain Enumeration and Takeover with tko-subs]]
