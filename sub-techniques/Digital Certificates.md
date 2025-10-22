---
id: 48a287ca-303c-4a64-841f-5191a711ccc9
name: Digital Certificates
type: sub-technique
mitre_id: T1596.003
mitre_url: null
created_at: '2023-04-06T00:31:25.470448+00:00'
updated_at: '2023-04-06T00:31:25.470448+00:00'
parent_technique: '[[Search Open Technical Databases|T1596 - Search Open Technical
  Databases]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Subdomain Enumeration and Takeover with tko-subs]]'
- '[[Subdomain Enumeration with Aquatone Scan]]'
- '[[Subdomain Enumeration with Google Dorks]]'
- '[[Subdomain Enumeration with MassDNS]]'
---

# Digital Certificates

**MITRE ID**: T1596.003

**Parent Technique**: [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

This is a sub-technique of T1596 - Search Open Technical Databases.

## Summary

Adversaries may search public digital certificate data for information about victims that can be used during targeting. Digital certificates are issued by a certificate authority (CA) in order to cryptographically verify the origin of signed content. These certificates, such as those used for encryp

## Description

Adversaries may search public digital certificate data for information about victims that can be used during targeting. Digital certificates are issued by a certificate authority (CA) in order to cryptographically verify the origin of signed content. These certificates, such as those used for encrypted web traffic (HTTPS SSL/TLS communications), contain information about the registered organization such as name and location.

Adversaries may search digital certificate data to gather actionable information. Threat actors can use online resources and lookup tools to harvest information about certificates.(Citation: SSLShopper Lookup) Digital certificate data may also be available from artifacts signed by the organization (ex: certificates used from encrypted web traffic are served with content).(Citation: Medium SSL Cert) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[Subdomain Enumeration and Takeover with tko-subs]]
- [[Subdomain Enumeration with Aquatone Scan]]
- [[Subdomain Enumeration with Google Dorks]]
- [[Subdomain Enumeration with MassDNS]]
