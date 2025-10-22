---
id: 36ce0aaa-4a2c-4f62-9a08-51ca58cf6bbc
name: Web Cookies
type: sub-technique
mitre_id: T1606.001
mitre_url: null
created_at: '2023-04-06T00:31:26.522100+00:00'
updated_at: '2023-04-06T00:31:26.522100+00:00'
parent_technique: '[[Forge Web Credentials|T1606 - Forge Web Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Web Cookies

**MITRE ID**: T1606.001

**Parent Technique**: [[Forge Web Credentials|T1606 - Forge Web Credentials]]

This is a sub-technique of T1606 - Forge Web Credentials.

## Summary

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

Adversaries may generate these coo

## Description

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

Adversaries may generate these cookies in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539) and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces.(Citation: Pass The Cookie) The generation of web cookies often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.

Once forged, adversaries may use these web cookies to access resources ([Web Session Cookie](https://attack.mitre.org/techniques/T1550/004)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Volexity SolarWinds)(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
