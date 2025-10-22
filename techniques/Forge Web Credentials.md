---
id: 22ed5327-9c37-45eb-b2e7-8c533e673cbe
name: Forge Web Credentials
type: technique
mitre_id: T1606
mitre_url: null
created_at: '2023-04-06T00:31:26.588973+00:00'
updated_at: '2023-04-06T03:56:32.274610+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AD CS Relay Attack with Rubeus and PetitPotam]]'
- '[[CL.TE Request Smuggling]]'
- '[[SAML Injection Authentication Bypass]]'
- '[[SAML Injection for Authentication Bypass and XML External Entity Attacks]]'
- '[[SAML Injection with XML Signature Wrapping Attack]]'
- '[[Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)]]'
---

# Forge Web Credentials

**MITRE ID**: T1606

## Description

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

Adversaries may generate these credential materials in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539), [Steal Application Access Token](https://attack.mitre.org/techniques/T1528), and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users. The generation of web credentials often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.(Citation: GitHub AWS-ADFS-Credential-Generator)

Once forged, adversaries may use these web credentials to access resources (ex: [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)(Citation: Microsoft SolarWinds Customer Guidance)

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (6)

- [[AD CS Relay Attack with Rubeus and PetitPotam]]
- [[CL.TE Request Smuggling]]
- [[SAML Injection Authentication Bypass]]
- [[SAML Injection for Authentication Bypass and XML External Entity Attacks]]
- [[SAML Injection with XML Signature Wrapping Attack]]
- [[Windows - Disable Antivirus and Security (Elastic Agent and Cortex XDR)]]
