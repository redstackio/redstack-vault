---
id: 62a3e709-7ef4-409b-8ea9-dd8372d90c8c
name: Steal Web Session Cookie
type: technique
mitre_id: T1539
mitre_url: null
created_at: '2023-04-06T00:31:25.562649+00:00'
updated_at: '2023-04-06T03:56:41.707478+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AWS IAM User Enumeration and Credential Checking]]'
- '[[Azure AD Connect - Silver Ticket Attack]]'
- '[[Azure Graph API Refresh Token]]'
- '[[Cloud Security Assessment and Auditing]]'
- '[[TE Header Obfuscation]]'
- '[[UI Redressing with Fake Login Form Injection]]'
---

# Steal Web Session Cookie

**MITRE ID**: T1539

## Description

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.(Citation: Pass The Cookie)

There are several examples of malware targeting cookies from web browsers on the local system.(Citation: Kaspersky TajMahal April 2019)(Citation: Unit 42 Mac Crypto Cookies January 2019) There are also open source frameworks such as Evilginx 2 and Muraena that can gather session cookies through a malicious proxy (ex: [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)) that can be set up by an adversary and used in phishing campaigns.(Citation: Github evilginx2)(Citation: GitHub Mauraena)

After an adversary acquires a valid cookie, they can then perform a [Web Session Cookie](https://attack.mitre.org/techniques/T1550/004) technique to login to the corresponding web application.

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (6)

- [[AWS IAM User Enumeration and Credential Checking]]
- [[Azure AD Connect - Silver Ticket Attack]]
- [[Azure Graph API Refresh Token]]
- [[Cloud Security Assessment and Auditing]]
- [[TE Header Obfuscation]]
- [[UI Redressing with Fake Login Form Injection]]
