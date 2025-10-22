---
id: 8480841e-c634-498f-b76b-fe7be0b53680
name: Remote Desktop Protocol
type: technique
mitre_id: T1076
mitre_url: null
created_at: '2019-08-28T21:17:41.007926+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Azure VM RunCommand Execution]]'
- '[[RDP Remote Code Execution]]'
- '[[Windows - Elevated RDP Backdoor with Sticky Keys]]'
- '[[Windows - RDP Backdoor using utilman.exe]]'
- '[[Windows RDP Credential Usage]]'
- '[[Windows - Remote Desktop Services Shadowing Persistence]]'
---

# Remote Desktop Protocol

**MITRE ID**: T1076

## Description

Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS). [1] There are other implementations and third-party tools that provide graphical access Remote Services similar to RDS.Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the Accessibility Features technique for Persistence. [2]Adversaries may also perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session and prompted with a question. With System permissions and using Terminal Services Console, c:\windows\system32\tscon.exe [session number to be stolen], an adversary can hijack a session without the need for credentials or prompts to the user. [3] This can be done remotely or locally and with active or disconnected sessions. [4] It can also lead to Remote System Discovery and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in RedSnarf. [5]

# Detection

Use of RDP may be legitimate, depending on the network environment and how it is used. Other factors, such as access patterns and activity that occurs after a remote login, may indicate suspicious or malicious behavior with RDP. Monitor for user accounts logged into systems they would not normally access or access patterns to multiple systems over a relatively short period of time.

Also, set up process monitoring for tscon.exe usage and monitor service creation that uses cmd.exe /k or cmd.exe /c in its arguments to prevent RDP session hijacking.

# Mitigation

Disable the RDP service if it is unnecessary, remove unnecessary accounts and groups from Remote Desktop Users groups, and enable firewall rules to block RDP traffic between network security zones. Audit the Remote Desktop Users group membership regularly. Remove the local Administrators group from the list of groups allowed to log in through RDP. Limit remote user permissions if remote access is necessary. Use remote desktop gateways and multifactor authentication for remote logins. [37] Do not leave RDP accessible from the internet. Change GPOs to define shorter timeouts sessions and maximum amount of time any single session can be active. Change GPOs to specify the maximum amount of time that a disconnected session stays active on the RD session host server. [38]

# Footnotes

[1] Microsoft. (n.d.). Remote Desktop Services. Retrieved June 1, 2016.

[2] Alperovitch, D. (2014, October 31). Malware-Free Intrusions. Retrieved November 4, 2014.

[3] Korznikov, A. (2017, March 17). Passwordless RDP Session Hijacking Feature All Windows versions. Retrieved December 11, 2017.

[4] Beaumont, K. (2017, March 19). RDP hijacking — how to hijack RDS and RemoteApp sessions transparently to move through an organisation. Retrieved December 11, 2017.

[5] NCC Group PLC. (2016, November 1). Kali Redsnarf. Retrieved December 11, 2017.

[6] FireEye Labs. (2014, May 20). The PLA and the 8:00am-5:00pm Work Day: FireEye Confirms DOJ’s Findings on APT1 Intrusion Activity. Retrieved November 4, 2014.

[7] valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.

[8] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[9] Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.

[10] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[11] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[12] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[13] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[14] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[15] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[16] FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved June 25, 2017.

[17] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[18] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[19] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[20] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[21] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[22] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[23] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.

[24] Plan, F., et all. (2019, March 4). APT40: Examining a China-Nexus Espionage Actor. Retrieved March 18, 2019.

[25] PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.

[26] United States District Court Southern District of New York (USDC SDNY) . (2018, December 17). United States of America v. Zhu Hua and Zhang Shilong. Retrieved April 17, 2019.

[27] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[28] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[29] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[30] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[31] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[32] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[33] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[34] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[35] Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved March 25, 2019.

[36] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[37] Berkeley Security, University of California. (n.d.). Securing Remote Desktop for System Administrators. Retrieved November 4, 2014.

[38] Microsoft. (n.d.). Configure Timeout and Reconnection Settings for Remote Desktop Services Sessions. Retrieved December 11, 2017.

## Defense

Disable the RDP service if it is unnecessary, remove unnecessary accounts and groups from Remote Desktop Users groups, and enable firewall rules to block RDP traffic between network security zones. Audit the Remote Desktop Users group membership regularly

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (6)

- [[Azure VM RunCommand Execution]]
- [[RDP Remote Code Execution]]
- [[Windows - Elevated RDP Backdoor with Sticky Keys]]
- [[Windows - RDP Backdoor using utilman.exe]]
- [[Windows RDP Credential Usage]]
- [[Windows - Remote Desktop Services Shadowing Persistence]]
