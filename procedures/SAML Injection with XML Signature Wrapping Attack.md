---
id: 27751b2c-a45f-4aa6-9f7e-c3f3e22e0618
name: SAML Injection with XML Signature Wrapping Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.167694+00:00'
updated_at: '2023-04-10T20:23:26.106551+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
sub_techniques:
- '[[Parent PID Spoofing|T1134.004 - Parent PID Spoofing]]'
tags:
- '[[Authentication Bypass]]'
- '[[SAML Injection]]'
- '[[XML Signature Wrapping Attacks]]'
commands:
- '[[FA conversion]]'
---

# SAML Injection with XML Signature Wrapping Attack

## Summary

The SAML Injection with XML Signature Wrapping Attack procedure is used to bypass authentication measures in SAML-based web applications. This attack involves manipulating the SAML response to inject arbitrary XML content, which can then be used to bypass authentication measures. An attacker can us

## Description

# Description

The SAML Injection with XML Signature Wrapping Attack procedure is used to bypass authentication measures in SAML-based web applications. This attack involves manipulating the SAML response to inject arbitrary XML content, which can then be used to bypass authentication measures. An attacker can use this technique to gain unauthorized access to sensitive data or systems. The attack is performed by exploiting vulnerabilities in the SAML implementation and manipulating the XML signature of the SAML response.

## Requirements

1. Access to a vulnerable SAML-based web application

1. Knowledge of SAML Injection and XML Signature Wrapping Attacks

## Defense

1. Regularly update and patch the SAML implementation to prevent vulnerabilities

1. Implement multi-factor authentication to add an extra layer of security

1. Monitor SAML responses for any signs of tampering or injection

## Objectives

1. Bypass authentication measures in SAML-based web applications

1. Gain unauthorized access to sensitive data or systems

# Instructions

1. To prevent XML Signature Wrapping attacks, ensure that your application checks for valid signatures and matches them to valid assertions, as well as checking for multiple assertions and signatures. Be sure to also ensure that your application behaves consistently regardless of the order of assertions.

**Code**: [[<SAMLResponse>
  <FA ID="evil">
      <Subject>Att]]

> XML Signature Wrapping (XSW) is an attack technique that exploits weaknesses in the way some SAML-based Single Sign-On (SSO) implementations validate digital signatures in XML documents. This can allow an attacker to impersonate a legitimate user or elevate their privileges within the system. To prevent this attack, it is important to implement proper validation and verification of digital signatures and ensure that the application behaves consistently regardless of the order or number of assertions and signatures.

2. To exploit the Github Enterprise vulnerability, the attacker would send this request to the target system. The request would verify the vulnerability and create a session for the attacker.

**Code**: [[Attacker]]

> The Github Enterprise vulnerability allows an attacker to create an arbitrary session on the target system. By sending this request, the attacker can verify the vulnerability and create a session for themselves. This session can then be used to carry out further attacks on the target system.

3. Verify the legitimacy of a user

**Code**: [[Legitimate User]]

> This command is used to verify whether a user is legitimate or not. The command takes in various arguments such as user ID, email address, phone number, etc. and performs a series of checks to ensure that the user is not a bot or a fake account. If the user passes all the checks, the command returns a success message indicating that the user is legitimate. Otherwise, it returns an error message indicating that the user is not legitimate and should be blocked from accessing the system.

4. Please check the authentication credentials provided and ensure they are correct. If you continue to experience issues, please contact support for further assistance.

**Code**: [[FA]]

> This error message indicates that the authentication process has failed. This could be due to incorrect login credentials or expired authentication tokens. Users should double-check their login information and make sure it is up-to-date. If the issue persists, they should contact the support team for further assistance.

**Command** ([[FA conversion]]):

```bash
fa -i input_file.txt -o output_file.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Forge Web Credentials|T1606 - Forge Web Credentials]]

### Sub-Techniques

- [[Parent PID Spoofing|T1134.004 - Parent PID Spoofing]]

## Commands Used

- [[FA conversion]]

## Tags

- [[Authentication Bypass]]
- [[SAML Injection]]
- [[XML Signature Wrapping Attacks]]
