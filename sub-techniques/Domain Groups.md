---
id: fea9a8a6-9eae-464a-8472-173eea432ca6
name: Domain Groups
type: sub-technique
mitre_id: T1069.002
mitre_url: null
created_at: '2023-04-06T00:31:25.788052+00:00'
updated_at: '2023-04-06T00:31:25.788052+00:00'
parent_technique: '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory ACL Scanning for User]]'
- '[[AWS IAM User Inline Policies Enumeration]]'
---

# Domain Groups

**MITRE ID**: T1069.002

**Parent Technique**: [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

This is a sub-technique of T1069 - Permission Groups Discovery.

## Summary

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated per

## Description

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

Commands such as <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility,  <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain-level groups.

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Active Directory ACL Scanning for User]]
- [[AWS IAM User Inline Policies Enumeration]]
