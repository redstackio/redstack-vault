---
id: 645c57b5-c693-4c0b-8b5c-0f0b702a228d
name: Password Filter DLL
type: sub-technique
mitre_id: T1556.002
mitre_url: null
created_at: '2023-04-06T00:31:25.913879+00:00'
updated_at: '2023-04-06T00:31:25.913879+00:00'
parent_technique: '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[AWS ECR Repository Policy Enumeration]]'
- '[[Golden SAML Attack via ADFS]]'
- '[[Insecure Docker Registry Pentest]]'
- '[[JWT Token Signing with JWKS Injection]]'
- '[[SSL MITM Network Discovery with OpenSSL]]'
- '[[Web Sockets Authentication Exploitation]]'
---

# Password Filter DLL

**MITRE ID**: T1556.002

**Parent Technique**: [[Modify Authentication Process|T1556 - Modify Authentication Process]]

This is a sub-technique of T1556 - Modify Authentication Process.

## Summary

Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process to acquire user credentials as they are validated. 

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as DLL

## Description

Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process to acquire user credentials as they are validated. 

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as DLLs containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts. Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation. 

Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made.(Citation: Carnal Ownage Password Filters Sept 2013)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 6 procedures using this sub-technique:

- [[AWS ECR Repository Policy Enumeration]]
- [[Golden SAML Attack via ADFS]]
- [[Insecure Docker Registry Pentest]]
- [[JWT Token Signing with JWKS Injection]]
- [[SSL MITM Network Discovery with OpenSSL]]
- [[Web Sockets Authentication Exploitation]]
