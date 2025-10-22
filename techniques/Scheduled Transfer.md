---
id: df9a9b24-6c0a-4dda-8e80-48f231657bae
name: Scheduled Transfer
type: technique
mitre_id: T1029
mitre_url: null
created_at: '2019-08-28T21:17:20.571522+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[Local DTD Injection in Citrix XenMobile Server]]'
- '[[Node Deserialization Exploit using Funcster]]'
- '[[Python Pickle Deserialization]]'
- '[[YAML Deserialization in Ruby]]'
- '[[YAML Deserialization via SnakeYAML]]'
---

# Scheduled Transfer

**MITRE ID**: T1029

## Description

Data exfiltration may be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over Command and Control Channel and Exfiltration Over Alternative Protocol.

# Detection

Monitor process file access patterns and network behavior. Unrecognized processes or scripts that appear to be traversing file systems and sending network traffic may be suspicious. Network connections to the same destination that occur at the same time of day for multiple days are suspicious.

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [8]

# Footnotes

[1] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[2] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[3] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[4] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[5] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[6] Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.

[7] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[8] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (5)

- [[Local DTD Injection in Citrix XenMobile Server]]
- [[Node Deserialization Exploit using Funcster]]
- [[Python Pickle Deserialization]]
- [[YAML Deserialization in Ruby]]
- [[YAML Deserialization via SnakeYAML]]
