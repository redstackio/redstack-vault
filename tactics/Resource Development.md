---
id: c0a779c0-b23a-4feb-91fe-93b18008f0e5
name: Resource Development
type: tactic
mitre_id: TA0042
mitre_url: null
created_at: '2023-04-06T00:31:25.391284+00:00'
updated_at: '2023-04-06T00:31:27.695000+00:00'
techniques:
- '[[Acquire Infrastructure|T1583 - Acquire Infrastructure]]'
- '[[Compromise Accounts|T1586 - Compromise Accounts]]'
- '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
- '[[Develop Capabilities|T1587 - Develop Capabilities]]'
- '[[Establish Accounts|T1585 - Establish Accounts]]'
- '[[Obtain Capabilities|T1588 - Obtain Capabilities]]'
- '[[Stage Capabilities|T1608 - Stage Capabilities]]'
procedures:
- '[[Docker Security Assessment]]'
- '[[Gopher SMTP Email Spoofing via SSRF]]'
- '[[RDS Enumeration - Listing Subnets by VPC-id]]'
- '[[SSL Certificate Discovery with Spyse and Microsoft]]'
- '[[Subdomain Enumeration and Takeover using SubOver]]'
---

# Resource Development

**MITRE ID**: TA0042

## Description

The adversary is trying to establish resources they can use to support operations.

Resource Development consists of techniques that involve adversaries creating, purchasing, or compromising/stealing resources that can be used to support targeting. Such resources include infrastructure, accounts, or capabilities. These resources can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using purchased domains to support Command and Control, email accounts for phishing as a part of Initial Access, or stealing code signing certificates to help with Defense Evasion.

## Techniques

This tactic includes 7 techniques:

- [[Acquire Infrastructure|T1583 - Acquire Infrastructure]]
- [[Compromise Accounts|T1586 - Compromise Accounts]]
- [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]
- [[Develop Capabilities|T1587 - Develop Capabilities]]
- [[Establish Accounts|T1585 - Establish Accounts]]
- [[Obtain Capabilities|T1588 - Obtain Capabilities]]
- [[Stage Capabilities|T1608 - Stage Capabilities]]

## Related Procedures

There are 5 procedures implementing this tactic:

- [[Docker Security Assessment]]
- [[Gopher SMTP Email Spoofing via SSRF]]
- [[RDS Enumeration - Listing Subnets by VPC-id]]
- [[SSL Certificate Discovery with Spyse and Microsoft]]
- [[Subdomain Enumeration and Takeover using SubOver]]
