---
id: 95d56cb3-5e2e-4b8a-a9c3-cb9882ce12cb
name: Permission Groups Discovery
type: technique
mitre_id: T1069
mitre_url: null
created_at: '2019-08-28T21:17:46.292151+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]'
- '[[Active Directory ACL Scanning for User]]'
- '[[Add user to group using ADModule (credentials)]]'
- '[[Analyze BloodHound Data for Relationships]]'
- '[[AWS IAM User Inline Policies Enumeration]]'
- '[[Enumerate GenericAll rights on AD Object for specific user (credentials)]]'
- '[[Enumerate GPO with LAPS (Credentials)]]'
- '[[Enumerate LAPS artifacts local machine]]'
- '[[Enumerate Linux Privilege Escalation Paths (LinEnum)]]'
- '[[Enumerate Linux Privilege Escalation Paths (linPEAS)]]'
- '[[Enumerate OU with LAPS (credentials)]]'
- '[[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]'
- '[[Enumerate Windows for Privilege Escalation (JAWS)]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Enumerate Windows for Privilege Escalation (SharpUp)]]'
- '[[Enumerate Windows for Privilege Escalation (winPEAS)]]'
- '[[Map an Active Directory Environment (SharpHound)]]'
- '[[Query an Active Directory User for DCSync Rights]]'
---

# Permission Groups Discovery

**MITRE ID**: T1069

## Description

Adversaries may attempt to find local system or domain-level groups and permissions settings. WindowsExamples of commands that can list groups are net group /domain and net localgroup using the Net utility.MacOn Mac, this same thing can be accomplished with the dscacheutil -q group for the domain, or dscl . -list /Groups for local groups.LinuxOn Linux, local groups can be enumerated with the groups command and domain groups via the ldapsearch command.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about groups and permissions, and audit and/or block them by using whitelisting [18] tools, like AppLocker, [19] [20] or Software Restriction Policies [21] where appropriate. [22]

# Footnotes

[1] FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.

[2] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[3] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[4] Microsoft. (n.d.). Dsquery. Retrieved April 18, 2016.

[5] Falcone, R. and Miller-Osborn, J.. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.

[6] Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.

[7] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[8] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[9] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[10] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[11] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[12] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[13] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[14] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[15] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[16] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[17] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[18] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[19] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[20] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[21] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[22] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about groups and permissions, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Wind

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (18)

- [[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]
- [[Active Directory ACL Scanning for User]]
- [[Add user to group using ADModule (credentials)]]
- [[Analyze BloodHound Data for Relationships]]
- [[AWS IAM User Inline Policies Enumeration]]
- [[Enumerate GenericAll rights on AD Object for specific user (credentials)]]
- [[Enumerate GPO with LAPS (Credentials)]]
- [[Enumerate LAPS artifacts local machine]]
- [[Enumerate Linux Privilege Escalation Paths (LinEnum)]]
- [[Enumerate Linux Privilege Escalation Paths (linPEAS)]]
- [[Enumerate OU with LAPS (credentials)]]
- [[Enumerate Windows for Missing Patches and Hotfixes (Sherlock)]]
- [[Enumerate Windows for Privilege Escalation (JAWS)]]
- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Enumerate Windows for Privilege Escalation (SharpUp)]]
- [[Enumerate Windows for Privilege Escalation (winPEAS)]]
- [[Map an Active Directory Environment (SharpHound)]]
- [[Query an Active Directory User for DCSync Rights]]
