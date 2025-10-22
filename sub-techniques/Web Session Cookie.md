---
id: c0da9069-6e14-439e-9767-132538b2531a
name: Web Session Cookie
type: sub-technique
mitre_id: T1550.004
mitre_url: null
created_at: '2023-04-06T00:31:26.886390+00:00'
updated_at: '2023-04-06T00:31:26.886390+00:00'
parent_technique: '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication
  Material]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Extracting Service Principal Keys from /etc/krb5.keytab]]'
- '[[SAML Injection for Authentication Bypass]]'
---

# Web Session Cookie

**MITRE ID**: T1550.004

**Parent Technique**: [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

This is a sub-technique of T1550 - Use Alternate Authentication Material.

## Summary

Adversaries can use stolen session cookies to authenticate to web applications and services. This technique bypasses some multi-factor authentication protocols since the session is already authenticated.(Citation: Pass The Cookie)

Authentication cookies are commonly used in web applications, includ

## Description

Adversaries can use stolen session cookies to authenticate to web applications and services. This technique bypasses some multi-factor authentication protocols since the session is already authenticated.(Citation: Pass The Cookie)

Authentication cookies are commonly used in web applications, including cloud-based services, after a user has authenticated to the service so credentials are not passed and re-authentication does not need to occur as frequently. Cookies are often valid for an extended period of time, even if the web application is not actively used. After the cookie is obtained through [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539) or [Web Cookies](https://attack.mitre.org/techniques/T1606/001), the adversary may then import the cookie into a browser they control and is then able to use the site or application as the user for as long as the session cookie is active. Once logged into the site, an adversary can access sensitive information, read email, or perform actions that the victim account has permissions to perform.

There have been examples of malware targeting session cookies to bypass multi-factor authentication systems.(Citation: Unit 42 Mac Crypto Cookies January 2019)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Extracting Service Principal Keys from /etc/krb5.keytab]]
- [[SAML Injection for Authentication Bypass]]
