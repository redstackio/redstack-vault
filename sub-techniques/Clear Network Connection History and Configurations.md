---
id: e6564f98-84a1-4ad1-9a64-0b6b41675ba4
name: Clear Network Connection History and Configurations
type: sub-technique
mitre_id: T1070.007
mitre_url: null
created_at: '2023-04-06T00:31:25.929837+00:00'
updated_at: '2023-04-06T00:31:25.929837+00:00'
parent_technique: '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Clear Network Connection History and Configurations

**MITRE ID**: T1070.007

**Parent Technique**: [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

This is a sub-technique of T1070 - Indicator Removal on Host.

## Summary

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system from behaviors that require network connections, such as [Remote

## Description

Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system from behaviors that require network connections, such as [Remote Services](https://attack.mitre.org/techniques/T1021) or [External Remote Services](https://attack.mitre.org/techniques/T1133). Defenders may use these artifacts to monitor or otherwise analyze network connections created by adversaries.

Network connection history may be stored in various locations on a system. For example, RDP connection history may be stored in Windows Registry values under (Citation: Microsoft RDP Removal):

* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code>
* <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code>

Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code> and `C:\Users\%username%\AppData\Local\Microsoft\Terminal
Server Client\Cache\`.(Citation: Moran RDPieces) Similarly, macOS and Linux hosts may store information highlighting connection history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`).(Citation: Apple Culprit Access)(Citation: FreeDesktop Journal)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)

Malicious network connections may also require changes to network configuration settings, such as [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1562/004) or tampering to enable [Proxy](https://attack.mitre.org/techniques/T1090). Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
