---
id: e5440740-c347-4b44-b145-13d779c2dc1b
name: XSS via OAuth Authorization Endpoint Misconfiguration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.643287+00:00'
updated_at: '2023-04-10T20:23:04.573323+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Executing XSS via redirect_uri]]'
- '[[OAuth Misconfiguration]]'
---

# XSS via OAuth Authorization Endpoint Misconfiguration

## Summary

This procedure involves exploiting a misconfigured OAuth Authorization Endpoint that allows for an attacker to inject a malicious redirect_uri parameter. By doing so, the attacker can execute a cross-site scripting (XSS) attack on unsuspecting victims. This attack can be used to steal sensitive inf

## Description

# Description

This procedure involves exploiting a misconfigured OAuth Authorization Endpoint that allows for an attacker to inject a malicious redirect_uri parameter. By doing so, the attacker can execute a cross-site scripting (XSS) attack on unsuspecting victims. This attack can be used to steal sensitive information such as session cookies or credentials, or to perform other malicious actions on the victim's behalf. From a technical perspective, the attacker would need to identify a vulnerable OAuth Authorization Endpoint and craft a malicious redirect_uri that would trigger the XSS payload. From a business value perspective, this attack can lead to unauthorized access to sensitive information or systems, reputational damage, or financial loss.

 

## Requirements

1. Access to the vulnerable OAuth Authorization Endpoint

1. Ability to craft a malicious redirect_uri

1. Knowledge of XSS payloads and injection techniques

 

## Defense

1. Ensure that OAuth Authorization Endpoints are properly configured and validated

1. Implement input validation and sanitization mechanisms to prevent XSS attacks

1. Monitor network traffic and user activity for suspicious behavior or unauthorized access

 

## Objectives

1. Exploit the misconfigured OAuth Authorization Endpoint to inject a malicious redirect_uri

1. Execute a cross-site scripting (XSS) attack on unsuspecting victims

1. Steal sensitive information such as session cookies or credentials

1. Perform other malicious actions on the victim's behalf

 

# Instructions

1. Use this endpoint to initiate the OAuth authorization process. The 'redirect_uri' parameter is set to a data URI that contains an XSS payload in the 'state' parameter. This vulnerability can be exploited by an attacker to execute arbitrary JavaScript code in the victim's browser.

 



**Code**: [[https://example.com/oauth/v1/authorize?[...]&redir]]



> The OAuth authorization endpoint is used to initiate the authorization process for a user. The endpoint takes several parameters, including 'client_id', 'redirect_uri', and 'state'. The 'redirect_uri' parameter specifies the URI that the user will be redirected to after they have granted or denied access. In this case, the 'redirect_uri' parameter is set to a data URI that contains an XSS payload in the 'state' parameter. This vulnerability can be exploited by an attacker to execute arbitrary JavaScript code in the victim's browser. To mitigate this vulnerability, the 'state' parameter should be properly encoded to prevent XSS attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Executing XSS via redirect_uri]]
- [[OAuth Misconfiguration]]


