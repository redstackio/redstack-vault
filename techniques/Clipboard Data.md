---
id: 03ed0eb2-86a7-4001-85dd-e9877cd76103
name: Clipboard Data
type: technique
mitre_id: T1115
mitre_url: null
created_at: '2019-08-28T21:17:25.401729+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
---

# Clipboard Data

**MITRE ID**: T1115

## Description

Adversaries may collect data stored in the Windows clipboard from users copying information within or between applications. WindowsApplications can access clipboard data by using the Windows API. [1] MacOSX provides a native command, pbpaste, to grab clipboard contents  [2].

# Detection

Access to the clipboard is a legitimate function of many applications on a Windows system. If an organization chooses to monitor for this behavior, then the data will likely need to be correlated against other suspicious or non-user-driven activity.

# Mitigation

Instead of blocking software based on clipboard capture behavior, identify potentially malicious software that may contain this functionality, and audit and/or block it by using whitelisting [25] tools, like AppLocker, [26] [27] or Software Restriction Policies [28] where appropriate. [29]

# Footnotes

[1] Microsoft. (n.d.). About the Clipboard. Retrieved March 29, 2016.

[2] rvrsh3ll. (2016, May 18). Operating with EmPyre. Retrieved July 12, 2017.

[3] Brumaghin, E., et al. (2018, October 15). Old dog, new tricks - Analysing new RTF-based campaign distributing Agent Tesla, Loki with PyREbox. Retrieved November 5, 2018.

[4] Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.

[5] Zhang, X. (2017, June 28). In-Depth Analysis of A New Variant of .NET Malware AgentTesla. Retrieved November 5, 2018.

[6] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[7] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[8] Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved July 10, 2018.

[9] F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.

[10] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[11] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[12] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[13] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[14] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[15] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[16] Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.

[17] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[18] Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.

[19] Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.

[20] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[21] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[22] Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.

[23] Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.

[24] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[25] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[26] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[27] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[28] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[29] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Instead of blocking software based on clipboard capture behavior, identify potentially malicious software that may contain this functionality, and audit and/or block it by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windo

## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (1)

- [[Linux Privilege Escalation - Writable Files Escalation]]
