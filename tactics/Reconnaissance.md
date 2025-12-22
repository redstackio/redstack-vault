---
id: 140dc60c-c5c1-497d-ba7d-0b0d3cb02352
name: Reconnaissance
type: tactic
mitre_id: TA0043
mitre_url: null
created_at: '2023-04-06T00:31:25.394943+00:00'
updated_at: '2023-04-06T00:31:27.693685+00:00'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Gather Victim Host Information|T1592 - Gather Victim Host Information]]'
- '[[Gather Victim Identity Information|T1589 - Gather Victim Identity Information]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
- '[[Gather Victim Org Information|T1591 - Gather Victim Org Information]]'
- '[[Phishing for Information|T1598 - Phishing for Information]]'
- '[[Search Closed Sources|T1597 - Search Closed Sources]]'
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
- '[[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]'
- '[[Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]'
procedures:
- '[[active-directory-recon-using-ad-module]]'
- '[[Active-Directory-Recon-with-PowerView]]'
- '[[Enumerate-Valid-Emails-in-Azure-O365-Tenant]]'
- '[[Azure-Reconnaissance]]'
- '[[Enumerate-Azure-Subdomains-with-MicroBurst]]'
- '[[dns-reconnaissance-using-standin-adidns-queries]]'
- '[[Spyse-Reverse-IP-Lookup-for-Domain-Discovery]]'
- '[[Exploit-OAuth-CSRF-Vulnerability]]'
- '[[passive-reconnaissance-information-gathering]]'
- '[[Enumerate-DNS-Records-with-Spyse]]'
- '[[Spyse-Subdomain-Enumeration]]'
- '[[SSRF-Enumeration-via-HTTP-URL-Scheme]]'
- '[[Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer]]'
- '[[Subdomain-Enumeration-and-Takeover-Detection-using-SubOver]]'
- '[[Subdomain-Enumeration-and-Takeover-with-tko-subs]]'
- '[[Subdomain-Enumeration-using-AltDNS]]'
- '[[Subdomain-Enumeration-using-Nmap-CRTsh-Script]]'
- '[[Subdomain-Enumeration-with-Subfinder]]'
- '[[Subdomain-Enumeration-with-Aquatone]]'
- '[[Subdomain-Enumeration-and-Scan-with-Aquatone]]'
- '[[Subdomain-Enumeration-Using-DNS-Dumpster]]'
- '[[Subdomain-Enumeration-with-Findomain]]'
- '[[Subdomain-Enumeration-with-Google-Dorks]]'
- '[[Subdomain-Enumeration-with-Knockpy-and-EyeWitness]]'
- '[[Subdomain-Enumeration-with-MassDNS]]'
- '[[Subdomain-Enumeration-Using-Subbrute]]'
- '[[Sublist3r-Subdomain-Enumeration]]'
- '[[Web-Enumeration-and-Backup-File-Discovery]]'
---

# Reconnaissance

**MITRE ID**: TA0043

## Description

The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.



## Techniques

This tactic includes 10 techniques:

- [[Active Scanning|T1595 - Active Scanning]]
- [[Gather Victim Host Information|T1592 - Gather Victim Host Information]]
- [[Gather Victim Identity Information|T1589 - Gather Victim Identity Information]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]
- [[Gather Victim Org Information|T1591 - Gather Victim Org Information]]
- [[Phishing for Information|T1598 - Phishing for Information]]
- [[Search Closed Sources|T1597 - Search Closed Sources]]
- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]
- [[Search Open Websites/Domains|T1593 - Search Open Websites/Domains]]
- [[Search Victim-Owned Websites|T1594 - Search Victim-Owned Websites]]

## Related Procedures

There are 28 procedures implementing this tactic:

- [[active-directory-recon-using-ad-module]]
- [[Active-Directory-Recon-with-PowerView]]
- [[Enumerate-Valid-Emails-in-Azure-O365-Tenant]]
- [[Azure-Reconnaissance]]
- [[Enumerate-Azure-Subdomains-with-MicroBurst]]
- [[dns-reconnaissance-using-standin-adidns-queries]]
- [[Spyse-Reverse-IP-Lookup-for-Domain-Discovery]]
- [[Exploit-OAuth-CSRF-Vulnerability]]
- [[passive-reconnaissance-information-gathering]]
- [[Enumerate-DNS-Records-with-Spyse]]
- [[Spyse-Subdomain-Enumeration]]
- [[SSRF-Enumeration-via-HTTP-URL-Scheme]]
- [[Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer]]
- [[Subdomain-Enumeration-and-Takeover-Detection-using-SubOver]]
- [[Subdomain-Enumeration-and-Takeover-with-tko-subs]]
- [[Subdomain-Enumeration-using-AltDNS]]
- [[Subdomain-Enumeration-using-Nmap-CRTsh-Script]]
- [[Subdomain-Enumeration-with-Subfinder]]
- [[Subdomain-Enumeration-with-Aquatone]]
- [[Subdomain-Enumeration-and-Scan-with-Aquatone]]

*...and 8 more*


