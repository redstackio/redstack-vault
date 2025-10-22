---
id: 904562f6-b9a6-4bb0-b6c4-8cda642bf42b
name: NTFS File Attributes
type: sub-technique
mitre_id: T1564.004
mitre_url: null
created_at: '2023-04-06T00:31:27.173427+00:00'
updated_at: '2023-04-06T00:31:27.173427+00:00'
parent_technique: '[[Hide Artifacts|T1564 - Hide Artifacts]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# NTFS File Attributes

**MITRE ID**: T1564.004

**Parent Technique**: [[Hide Artifacts|T1564 - Hide Artifacts]]

This is a sub-technique of T1564 - Hide Artifacts.

## Summary

Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. (Citation: SpectorOps Host-Based Jul 20

## Description

Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. (Citation: SpectorOps Host-Based Jul 2017) Within MFT entries are file attributes, (Citation: Microsoft NTFS File Attributes Aug 2010) such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files). (Citation: SpectorOps Host-Based Jul 2017) (Citation: Microsoft File Streams) (Citation: MalwareBytes ADS July 2015) (Citation: Microsoft ADS Mar 2014)

Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done to evade some defenses, such as static indicator scanning tools and anti-virus. (Citation: Journey into IR ZeroAccess NTFS EA) (Citation: MalwareBytes ADS July 2015)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
