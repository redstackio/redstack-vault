---
id: 9b538e2f-25ef-42a7-a1f6-2cdb4e1e18dd
name: Search Open Technical Databases
type: technique
mitre_id: T1596
mitre_url: null
created_at: '2023-04-06T00:31:26.153722+00:00'
updated_at: '2023-04-06T03:56:25.846335+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Azure Reconnaissance]]'
- '[[DNS Reconnaissance with ADIDNS Search Commands]]'
- '[[Subdomain Enumeration and Takeover using SubOver]]'
- '[[Subdomain Enumeration and Takeover with tko-subs]]'
- '[[Subdomain Enumeration using Subfinder]]'
- '[[Subdomain Enumeration with Aquatone Scan]]'
- '[[Subdomain Enumeration with DNS Dumpster]]'
- '[[Subdomain Enumeration with Google Dorks]]'
- '[[Subdomain Enumeration with MassDNS]]'
---

# Search Open Technical Databases

**MITRE ID**: T1596

## Description

Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS)(Citation: Medium SSL Cert)(Citation: SSLShopper Lookup)(Citation: DigitalShadows CDN)(Citation: Shodan)

Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (9)

- [[Azure Reconnaissance]]
- [[DNS Reconnaissance with ADIDNS Search Commands]]
- [[Subdomain Enumeration and Takeover using SubOver]]
- [[Subdomain Enumeration and Takeover with tko-subs]]
- [[Subdomain Enumeration using Subfinder]]
- [[Subdomain Enumeration with Aquatone Scan]]
- [[Subdomain Enumeration with DNS Dumpster]]
- [[Subdomain Enumeration with Google Dorks]]
- [[Subdomain Enumeration with MassDNS]]
