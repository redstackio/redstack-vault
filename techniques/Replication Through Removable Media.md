---
id: 96bef649-a04f-446a-b772-a1f980a247a5
name: Replication Through Removable Media
type: technique
mitre_id: T1091
mitre_url: null
created_at: '2019-08-28T21:17:21.622258+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[Drop the MIC - Resource Based Constrained Delegation Attack]]'
- '[[LFI to RCE via Apache and Nginx Log Files]]'
- '[[SSH Local Port Forwarding]]'
- '[[Windows - Restore Service Account Privileges via Impersonation]]'
---

# Replication Through Removable Media

**MITRE ID**: T1091

## Description

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

# Detection

Monitor file access on removable media. Detect processes that execute from removable media after it is mounted or when initiated by a user. If a remote access tool is used in this manner to move laterally, then additional actions are likely to occur after execution, such as opening network connections for Command and Control and system and network information Discovery.

# Mitigation

Disable Autorun if it is unnecessary. [11] Disallow or restrict removable media at an organizational policy level if it is not required for business operations. [12]

Identify potentially malicious software that may be used to infect removable media or may result from tainted removable media, and audit and/or block it by using whitelisting [13] tools, like AppLocker, [14] [15] or Software Restriction Policies [16] where appropriate. [17]

# Footnotes

[1] Shevchenko, S.. (2008, November 30). Agent.btz - A Threat That Hit Pentagon. Retrieved April 8, 2016.

[2] Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.

[3] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[4] Kaspersky Lab's Global Research and Analysis Team. (2014, November). The Darkhotel APT A Story of Unusual Hospitality. Retrieved November 12, 2014.

[5] ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.

[6] Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.

[7] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[8] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[9] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[10] Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.

[11] Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.

[12] Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.

[13] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[14] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[15] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[16] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[17] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Disable Autorun if it is unnecessary. (Citation: Microsoft Disable Autorun) Disallow or restrict removable media at an organizational policy level if it is not required for business operations. (Citation: TechNet Removable Media Control)

Identify potenti

## Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (4)

- [[Drop the MIC - Resource Based Constrained Delegation Attack]]
- [[LFI to RCE via Apache and Nginx Log Files]]
- [[SSH Local Port Forwarding]]
- [[Windows - Restore Service Account Privileges via Impersonation]]
