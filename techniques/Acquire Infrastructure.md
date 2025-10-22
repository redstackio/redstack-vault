---
id: 3ff2ff6a-4d72-4e01-9a8b-b8e62a32028e
name: Acquire Infrastructure
type: technique
mitre_id: T1583
mitre_url: null
created_at: '2023-04-06T00:31:25.431556+00:00'
updated_at: '2023-04-06T03:56:25.846335+00:00'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
procedures:
- '[[RDS Enumeration - Listing Subnets by VPC-id]]'
- '[[SSL Certificate Discovery with Spyse and Microsoft]]'
- '[[Subdomain Enumeration and Takeover using SubOver]]'
---

# Acquire Infrastructure

**MITRE ID**: T1583

## Description

Adversaries may buy, lease, or rent infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services.(Citation: TrendmicroHideoutsLease) Additionally, botnets are available for rent or purchase.

Use of these infrastructure solutions allows an adversary to stage, launch, and execute an operation. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contact to third-party web services. Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

## Tactics

- [[Resource Development|TA0042 - Resource Development]]

## Related Procedures (3)

- [[RDS Enumeration - Listing Subnets by VPC-id]]
- [[SSL Certificate Discovery with Spyse and Microsoft]]
- [[Subdomain Enumeration and Takeover using SubOver]]
