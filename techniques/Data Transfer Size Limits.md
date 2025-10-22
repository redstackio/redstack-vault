---
id: b142a09f-3aec-4654-a223-2ca7cf448d42
name: Data Transfer Size Limits
type: technique
mitre_id: T1030
mitre_url: null
created_at: '2019-08-28T21:17:23.941621+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[EBS Volume Attachment]]'
- '[[MYSQL Injection with Out of Band DNS Exfiltration]]'
- '[[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]'
---

# Data Transfer Size Limits

**MITRE ID**: T1030

## Description

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

# Detection

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). If a process maintains a long connection during which it consistently sends fixed size data packets or a process opens connections and sends fixed sized data packets at regular intervals, it may be performing an aggregate data transfer. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [6]

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [6]

# Footnotes

[1] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[2] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[3] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[4] Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.

[5] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[6] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (3)

- [[EBS Volume Attachment]]
- [[MYSQL Injection with Out of Band DNS Exfiltration]]
- [[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]
