---
id: ada70e1a-3456-4cd2-8267-0e1dd6f06b01
name: Domain Account
type: sub-technique
mitre_id: T1136.002
mitre_url: null
created_at: '2023-04-06T00:31:26.364566+00:00'
updated_at: '2023-04-06T00:31:26.364566+00:00'
parent_technique: '[[Create Account|T1136 - Create Account]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Filter Bypass using UTF-7 Encoding for XSS Injection]]'
---

# Domain Account

**MITRE ID**: T1136.002

**Parent Technique**: [[Create Account|T1136 - Create Account]]

This is a sub-technique of T1136 - Create Account.

## Summary

Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover user, administrator, and

## Description

Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover user, administrator, and service accounts. With a sufficient level of access, the <code>net user /add /domain</code> command can be used to create a domain account.

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Filter Bypass using UTF-7 Encoding for XSS Injection]]
