---
id: 0b68ab3f-b5cc-47cc-8b3f-2c579fa621b0
name: Domains
type: sub-technique
mitre_id: T1584.001
mitre_url: null
created_at: '2023-04-06T00:31:27.224335+00:00'
updated_at: '2023-04-06T00:31:27.224335+00:00'
parent_technique: '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Domains

**MITRE ID**: T1584.001

**Parent Technique**: [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]

This is a sub-technique of T1584 - Compromise Infrastructure.

## Summary

Adversaries may hijack domains and/or subdomains that can be used during targeting. Domain registration hijacking is the act of changing the registration of a domain name without the permission of the original registrant.(Citation: ICANNDomainNameHijacking) Adversaries may gain access to an email ac

## Description

Adversaries may hijack domains and/or subdomains that can be used during targeting. Domain registration hijacking is the act of changing the registration of a domain name without the permission of the original registrant.(Citation: ICANNDomainNameHijacking) Adversaries may gain access to an email account for the person listed as the owner of the domain. The adversary can then claim that they forgot their password in order to make changes to the domain registration. Other possibilities include social engineering a domain registration help desk to gain access to an account or taking advantage of renewal process gaps.(Citation: Krebs DNS Hijack 2019)

Subdomain hijacking can occur when organizations have DNS entries that point to non-existent or deprovisioned resources. In such cases, an adversary may take control of a subdomain to conduct operations with the benefit of the trust associated with that domain.(Citation: Microsoft Sub Takeover 2020)

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
