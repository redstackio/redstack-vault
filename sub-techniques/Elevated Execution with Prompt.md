---
id: ed44f7ff-d70c-4613-b8e8-595b84f35684
name: Elevated Execution with Prompt
type: sub-technique
mitre_id: T1548.004
mitre_url: null
created_at: '2023-04-06T00:31:26.799837+00:00'
updated_at: '2023-04-06T00:31:26.799837+00:00'
parent_technique: '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control
  Mechanism]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD]]'
- '[[Linux - Suid Binary Persistence]]'
---

# Elevated Execution with Prompt

**MITRE ID**: T1548.004

**Parent Technique**: [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

This is a sub-technique of T1548 - Abuse Elevation Control Mechanism.

## Summary

Adversaries may leverage the <code>AuthorizationExecuteWithPrivileges</code> API to escalate privileges by prompting the user for credentials.(Citation: AppleDocs AuthorizationExecuteWithPrivileges) The purpose of this API is to give application developers an easy way to perform operations with root

## Description

Adversaries may leverage the <code>AuthorizationExecuteWithPrivileges</code> API to escalate privileges by prompting the user for credentials.(Citation: AppleDocs AuthorizationExecuteWithPrivileges) The purpose of this API is to give application developers an easy way to perform operations with root privileges, such as for application installation or updating. This API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously modified. 

Although this API is deprecated, it still fully functions in the latest releases of macOS. When calling this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior with elevated privileges.

Adversaries may abuse <code>AuthorizationExecuteWithPrivileges</code> to obtain root privileges in order to install malicious software on victims and install persistence mechanisms.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019)(Citation: OSX Coldroot RAT) This technique may be combined with [Masquerading](https://attack.mitre.org/techniques/T1036) to trick the user into granting escalated privileges to malicious code.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019) This technique has also been shown to work by modifying legitimate programs present on the machine that make use of this API.(Citation: Death by 1000 installers; it's all broken!)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Linux - Privilege Escalation via LD_PRELOAD and NOPASSWD]]
- [[Linux - Suid Binary Persistence]]
