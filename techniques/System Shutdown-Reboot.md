---
id: 20cf8f53-aaca-4cc8-8427-546acd61fe73
name: System Shutdown/Reboot
type: technique
mitre_id: T1529
mitre_url: null
created_at: '2023-04-06T00:31:27.243877+00:00'
updated_at: '2023-04-06T03:56:44.273450+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
procedures:
- '[[Billion Laugh Attack to Perform Denial of Service using XML External Entity]]'
- '[[Docker Security Assessment]]'
- '[[Exploiting .NET BinaryFormatter Deserialization]]'
- '[[HTTP/2 Request Smuggling]]'
- '[[Jinja2 Config Information Extraction]]'
- '[[Lessjs Server Side Template Injection via Inline Import]]'
- '[[Linux - Docker Privilege Escalation]]'
---

# System Shutdown/Reboot

**MITRE ID**: T1529

## Description

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) (e.g. <code>reload</code>).(Citation: Microsoft Shutdown Oct 2017)(Citation: alert_TA18_106A) Shutting down or rebooting systems may disrupt access to computer resources for legitimate users.

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) or [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490), to hasten the intended effects on system availability.(Citation: Talos Nyetya June 2017)(Citation: Talos Olympic Destroyer 2018)

## Tactics

- [[Impact|TA0040 - Impact]]

## Related Procedures (7)

- [[Billion Laugh Attack to Perform Denial of Service using XML External Entity]]
- [[Docker Security Assessment]]
- [[Exploiting .NET BinaryFormatter Deserialization]]
- [[HTTP/2 Request Smuggling]]
- [[Jinja2 Config Information Extraction]]
- [[Lessjs Server Side Template Injection via Inline Import]]
- [[Linux - Docker Privilege Escalation]]
