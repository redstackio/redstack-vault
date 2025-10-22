---
id: af05d266-8105-4195-90fd-8cc481dd7ddd
name: Compiled HTML File
type: technique
mitre_id: T1223
mitre_url: null
created_at: '2019-08-28T21:17:21.388761+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
---

# Compiled HTML File

**MITRE ID**: T1223

## Description

Compiled HTML files (.chm) are commonly distributed as part of the Microsoft HTML Help system. CHM files are compressed compilations of various content such as HTML documents, images, and scripting/web related programming languages such VBA, JScript, Java, and ActiveX. [1] CHM content is displayed using underlying components of the Internet Explorer browser [2] loaded by the HTML Help executable program (hh.exe). [3]Adversaries may abuse this technology to conceal malicious code. A custom CHM file containing embedded payloads could be delivered to a victim then triggered by User Execution. CHM execution may also bypass application whitelisting on older and/or unpatched systems that do not account for execution of binaries through hh.exe. [4] [5]

# Detection

Monitor and analyze the execution and arguments of hh.exe. [4] Compare recent invocations of hh.exe with prior history of known good arguments to determine anomalous and potentially adversarial activity (ex: obfuscated and/or malicious commands). Non-standard process execution trees may also indicate suspicious or malicious behavior, such as if hh.exe is the parent process for suspicious processes and activity relating to other adversarial techniques.

Monitor presence and use of CHM files, especially if they are not typically used within an environment.

# Mitigation

Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns, such as CHM files. [10] Also consider using application whitelisting to prevent execution of hh.exe if it is not required for a given system or network to prevent potential misuse by adversaries.

# Footnotes

[1] Microsoft. (2018, May 30). Microsoft HTML Help 1.4. Retrieved October 3, 2018.

[2] Microsoft. (n.d.). HTML Help ActiveX Control Overview. Retrieved October 3, 2018.

[3] Microsoft. (n.d.). About the HTML Help Executable Program. Retrieved October 3, 2018.

[4] Moe, O. (2017, August 13). Bypassing Device guard UMCI using CHM – CVE-2017-8625. Retrieved October 3, 2018.

[5] Microsoft. (2017, August 8). CVE-2017-8625 - Internet Explorer Security Feature Bypass Vulnerability. Retrieved October 3, 2018.

[6] Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved April 17, 2019.

[7] Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.

[8] GReAT. (2017, April 3). Lazarus Under the Hood. Retrieved October 3, 2018.

[9] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[10] Kiwi. (2016, April 6). Breakout Recap: Cybersecurity Best Practices Part 1 - Preventing Opportunistic Attacks. Retrieved October 3, 2018.

## Defense

Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns, such as CHM files. (Citation: PaloAlto Preventing Opportunistic Attacks Apr 2016) Also consider using application whitelisting to

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
