---
id: 8372b69c-7030-4d3a-8768-b4e098a62173
name: Pass the Hash
type: sub-technique
mitre_id: T1550.002
mitre_url: null
created_at: '2023-04-06T00:31:27.102893+00:00'
updated_at: '2023-04-06T00:31:27.102893+00:00'
parent_technique: '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication
  Material]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[PrivExchange Attack with NTLM Relay]]'
---

# Pass the Hash

**MITRE ID**: T1550.002

**Parent Technique**: [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

This is a sub-technique of T1550 - Use Alternate Authentication Material.

## Summary

Adversaries may “pass the hash” using stolen password hashes to move laterally within an environment, bypassing normal system access controls. Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authenticat

## Description

Adversaries may “pass the hash” using stolen password hashes to move laterally within an environment, bypassing normal system access controls. Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash.

When performing PtH, valid password hashes for the account being used are captured using a [Credential Access](https://attack.mitre.org/tactics/TA0006) technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems.

Adversaries may also use stolen password hashes to "overpass the hash." Similar to PtH, this involves using a password hash to authenticate as a user but also uses the password hash to create a valid Kerberos ticket. This ticket can then be used to perform [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003) attacks.(Citation: Stealthbits Overpass-the-Hash)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[PrivExchange Attack with NTLM Relay]]
