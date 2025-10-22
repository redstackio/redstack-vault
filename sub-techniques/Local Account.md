---
id: 2c0e2346-2ed8-4bd8-b541-63596b64d7bb
name: Local Account
type: sub-technique
mitre_id: T1136.001
mitre_url: null
created_at: '2023-04-06T00:31:26.241481+00:00'
updated_at: '2023-04-06T00:31:26.241481+00:00'
parent_technique: '[[Create Account|T1136 - Create Account]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Basic Directory Traversal Exploitation]]'
- '[[XXE File Retrieval via XInclude Attack]]'
---

# Local Account

**MITRE ID**: T1136.001

**Parent Technique**: [[Create Account|T1136 - Create Account]]

This is a sub-technique of T1136 - Create Account.

## Summary

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. With a sufficient level of access, the <code>net user /add</code> comma

## Description

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. With a sufficient level of access, the <code>net user /add</code> command can be used to create a local account. On macOS systems the <code>dscl -create</code> command can be used to create a local account.

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Basic Directory Traversal Exploitation]]
- [[XXE File Retrieval via XInclude Attack]]
