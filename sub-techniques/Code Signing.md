---
id: 5e712b06-19b9-4491-81e5-4cfb4508fdcd
name: Code Signing
type: sub-technique
mitre_id: T1553.002
mitre_url: null
created_at: '2023-04-06T00:31:25.864310+00:00'
updated_at: '2023-04-06T00:31:25.864310+00:00'
parent_technique: '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[AWS API Gateway Resource Enumeration]]'
- '[[AWS Lambda Function Enumeration]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[CRLF Injection and Cookie Stealing]]'
- '[[Kubernetes Pentest with BishopFox BadPods]]'
- '[[Kubernetes Service Account Token Theft]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Log4Shell Scanning Procedure]]'
- '[[Open URL Redirection Filter Bypass]]'
- '[[PHP Juggling Type and Magic Hashes]]'
---

# Code Signing

**MITRE ID**: T1553.002

**Parent Technique**: [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

This is a sub-technique of T1553 - Subvert Trust Controls.

## Summary

Adversaries may create, acquire, or steal code signing materials to sign their malware or tools. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. (Citation: Wikipedia Code Signing) The certificates used during an

## Description

Adversaries may create, acquire, or steal code signing materials to sign their malware or tools. Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. (Citation: Wikipedia Code Signing) The certificates used during an operation may be created, acquired, or stolen by the adversary. (Citation: Securelist Digital Certificates) (Citation: Symantec Digital Certificates) Unlike [Invalid Code Signature](https://attack.mitre.org/techniques/T1036/001), this activity will result in a valid signature.

Code signing to verify software on first run can be used on modern Windows and macOS systems. It is not used on Linux due to the decentralized nature of the platform. (Citation: Wikipedia Code Signing)(Citation: EclecticLightChecksonEXECodeSigning)

Code signing certificates may be used to bypass security policies that require signed code to execute on a system. 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 12 procedures using this sub-technique:

- [[AWS API Gateway Resource Enumeration]]
- [[AWS Lambda Function Enumeration]]
- [[CRLF Injection and Cookie Stealing]]
- [[CRLF Injection and Cookie Stealing]]
- [[CRLF Injection and Cookie Stealing]]
- [[Kubernetes Pentest with BishopFox BadPods]]
- [[Kubernetes Service Account Token Theft]]
- [[Log4Shell Scanning Procedure]]
- [[Log4Shell Scanning Procedure]]
- [[Log4Shell Scanning Procedure]]
- [[Open URL Redirection Filter Bypass]]
- [[PHP Juggling Type and Magic Hashes]]
