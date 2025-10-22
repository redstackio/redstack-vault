---
id: 552f7e88-d9b3-4afa-9147-dda0585239cd
name: Hide Artifacts
type: technique
mitre_id: T1564
mitre_url: null
created_at: '2023-04-06T00:31:25.728854+00:00'
updated_at: '2023-04-06T03:56:41.245756+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Linux - Backdoor MOTD Persistence]]'
- '[[Linux - Startup Service Backdoor with Reverse Shell]]'
- '[[Linux - Text Hiding and Payload Creation]]'
- '[[Malicious HLS playlist inside an AVI video]]'
- '[[Windows - Elevated RDP Backdoor with Sticky Keys]]'
- '[[Windows - Mimikatz Hidden Persistence]]'
- '[[Windows - Simple User File Hidden Persistence]]'
- '[[Zip Slip Basic Exploit - Unix Server Shell Upload]]'
---

# Hide Artifacts

**MITRE ID**: T1564

## Description

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.(Citation: Sofacy Komplex Trojan)(Citation: Cybereason OSX Pirrit)(Citation: MalwareBytes ADS July 2015)

Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.(Citation: Sophos Ragnar May 2020)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (8)

- [[Linux - Backdoor MOTD Persistence]]
- [[Linux - Startup Service Backdoor with Reverse Shell]]
- [[Linux - Text Hiding and Payload Creation]]
- [[Malicious HLS playlist inside an AVI video]]
- [[Windows - Elevated RDP Backdoor with Sticky Keys]]
- [[Windows - Mimikatz Hidden Persistence]]
- [[Windows - Simple User File Hidden Persistence]]
- [[Zip Slip Basic Exploit - Unix Server Shell Upload]]
