---
id: fc252100-812d-4f80-9ef4-124e3874d2ae
name: Spearphishing via Service
type: sub-technique
mitre_id: T1566.003
mitre_url: null
created_at: '2023-04-06T00:31:27.205360+00:00'
updated_at: '2023-04-06T00:31:27.205360+00:00'
parent_technique: '[[Phishing|T1566 - Phishing]]'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
procedures:
- '[[Account Takeover Through Password Reset Poisoning]]'
---

# Spearphishing via Service

**MITRE ID**: T1566.003

**Parent Technique**: [[Phishing|T1566 - Phishing]]

This is a sub-technique of T1566 - Phishing.

## Summary

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than dire

## Description

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than directly via enterprise email channels. 

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries send messages through various social media services, personal webmail, and other non-enterprise controlled services. These services are more likely to have a less-strict security policy than an enterprise. As with most kinds of spearphishing, the goal is to generate rapport with the target or get the target's interest in some way. Adversaries will create fake social media accounts and message employees for potential job opportunities. Doing so allows a plausible reason for asking about services, policies, and software that's running in an environment. The adversary can then send malicious links or attachments through these services.

A common example is to build rapport with a target via social media, then send content to a personal webmail service that the target uses on their work computer. This allows an adversary to bypass some email restrictions on the work account, and the target is more likely to open the file since it's something they were expecting. If the payload doesn't work as expected, the adversary can continue normal communications and troubleshoot with the target on how to get it working.

## Tactics

This sub-technique is used in the following tactics:

- [[Initial Access|TA0001 - Initial Access]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Account Takeover Through Password Reset Poisoning]]
