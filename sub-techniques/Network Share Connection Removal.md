---
id: 8aa4a8f2-e6ae-47d4-99d5-9bd17f67a4c3
name: Network Share Connection Removal
type: sub-technique
mitre_id: T1070.005
mitre_url: null
created_at: '2023-04-06T00:31:26.692982+00:00'
updated_at: '2023-04-06T00:31:26.692982+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Network Share Connection Removal

**MITRE ID**: T1070.005

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) connections can be removed when no longer needed. [Net](https://attack.mitre.org/softw

## Description

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) connections can be removed when no longer needed. [Net](https://attack.mitre.org/software/S0039) is an example utility that can be used to remove network share connections with the <code>net use \\system\share /delete</code> command. (Citation: Technet Net Use)

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
