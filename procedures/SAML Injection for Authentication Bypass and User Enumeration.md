---
id: 3364c676-2cb1-4fe1-8260-f017d5b89dc2
name: SAML Injection for Authentication Bypass and User Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.194997+00:00'
updated_at: '2023-04-10T20:23:27.529518+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Compromise Client Software Binary|T1554 - Compromise Client Software Binary]]'
tags:
- '[[Authentication Bypass]]'
- '[[SAML Injection]]'
- '[[XML Comment Handling]]'
---

# SAML Injection for Authentication Bypass and User Enumeration

## Summary

SAML Injection is a technique used to manipulate SAML-based authentication systems to bypass authentication, impersonate users, or enumerate user information. This technique takes advantage of vulnerabilities in the parsing of SAML messages that allow an attacker to insert malicious XML content int

## Description

# Description

SAML Injection is a technique used to manipulate SAML-based authentication systems to bypass authentication, impersonate users, or enumerate user information. This technique takes advantage of vulnerabilities in the parsing of SAML messages that allow an attacker to insert malicious XML content into the SAML response. By doing so, an attacker can bypass the authentication process and gain access to sensitive resources or obtain user information. 

From an offensive perspective, SAML Injection can be used to gain access to sensitive systems and data, or to perform reconnaissance on the target environment. In technical terms, this technique involves crafting a SAML response with malicious XML content that can be used to bypass authentication or enumerate user information. 

The business value of this technique is that it can be used to gain access to sensitive data and systems without the need for valid credentials, which can reduce the time and effort required to perform targeted attacks.

## Requirements

1. Access to a vulnerable SAML-based authentication system

1. Knowledge of the target system's SAML implementation

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use SAML assertions to verify user identities instead of relying solely on SAML responses

1. Monitor SAML logs for suspicious activity such as multiple failed authentication attempts or abnormal user behavior

## Objectives

1. Bypass authentication mechanisms

1. Impersonate legitimate users

1. Enumerate user information

# Instructions

1. To prevent SAML Response Spoofing, it is recommended to implement SAML response signature verification and to validate the Assertion Consumer Service (ACS) URL of the SAML response.

**Code**: [[<SAMLResponse>
    <Issuer>https://idp.com/</Issue]]

> The SAML protocol is used for exchanging authentication and authorization data between parties, in particular, between an identity provider (IdP) and a service provider (SP). SAML Response Spoofing occurs when a threat actor intercepts a SAML response and modifies its content to impersonate another user. This can happen when the SAML response is not properly validated by the service provider. The vulnerability can be exploited to gain unauthorized access to sensitive information or resources.

2. Use the following command to lookup a user's email address: 'lookup email user@user.com'

**Code**: [[user@user.com]]

> This command will search the database for the email address associated with the given username. If the email address is found, it will be returned as the result of the command. If the username is not found, an error message will be returned.

3. Use this domain to create a username for a malicious account.

**Code**: [[.evil.com]]

> This field provides a specific domain that can be used to create a username for a malicious account. The username can be used for various purposes such as phishing, spamming, or other malicious activities. The user can append any string before the domain to create a fake email or username to deceive the victims. It is important to note that the use of such usernames is illegal and unethical.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Compromise Client Software Binary|T1554 - Compromise Client Software Binary]]

## Tags

- [[Authentication Bypass]]
- [[SAML Injection]]
- [[XML Comment Handling]]
