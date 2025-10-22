---
id: ba9baeab-c49b-4a66-a558-db5f79c8bbd8
name: Archive Collected Data
type: technique
mitre_id: T1560
mitre_url: null
created_at: '2023-04-06T00:31:26.128041+00:00'
updated_at: '2023-04-06T03:56:11.677565+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[AWS IAM Policy Information Gathering]]'
---

# Archive Collected Data

**MITRE ID**: T1560

## Description

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network. Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (1)

- [[AWS IAM Policy Information Gathering]]
