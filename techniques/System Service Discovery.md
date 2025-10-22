---
id: 19e32846-d131-43ef-9b5d-b8e6b706e331
name: System Service Discovery
type: technique
mitre_id: T1007
mitre_url: null
created_at: '2019-08-28T21:17:43.838168+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[AWS API Gateway Version Enumeration]]'
- '[[AWS REST API Enumeration]]'
- '[[AWS S3 Bucket Listing Exploitation]]'
- '[[Brute Force an SNMP Community String]]'
- '[[CL.TE Request Smuggling]]'
- '[[Enumerate Linux Privilege Escalation Paths (LinEnum)]]'
- '[[Enumerate Linux Privilege Escalation Paths (linPEAS)]]'
- '[[Enumerate Windows for Privilege Escalation (JAWS)]]'
- '[[Enumerate Windows for Privilege Escalation (SharpUp)]]'
- '[[Enumerate Windows for Privilege Escalation (winPEAS)]]'
- '[[Kubernetes API Address Enumeration via kubelet]]'
- '[[Monitor Processes and Commands]]'
- '[[MYSQL Time Based Injection using SLEEP in a subselect]]'
---

# System Service Discovery

**MITRE ID**: T1007

## Description

Adversaries may try to get information about registered services. Commands that may obtain information about services using operating system utilities are "sc," "tasklist /svc" using Tasklist, and "net start" using Net, but adversaries may also use other tools as well.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system information related to services. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about services, and audit and/or block them by using whitelisting [31] tools, like AppLocker, [32] [33] or Software Restriction Policies [34] where appropriate. [35]

# Footnotes

[1] FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.

[2] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[3] Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.

[4] Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.

[5] Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.

[6] Falcone, R. and Miller-Osborn, J.. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.

[7] Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.

[8] F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.

[9] Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.

[10] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[11] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[12] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[13] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[14] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[15] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[16] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[17] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[18] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[19] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[20] Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.

[21] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[22] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[23] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[24] Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.

[25] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[26] Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.

[27] Microsoft. (n.d.). Tasklist. Retrieved December 23, 2015.

[28] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[29] US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.

[30] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[31] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[32] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[33] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[34] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[35] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about services, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands J

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (13)

- [[AWS API Gateway Version Enumeration]]
- [[AWS REST API Enumeration]]
- [[AWS S3 Bucket Listing Exploitation]]
- [[Brute Force an SNMP Community String]]
- [[CL.TE Request Smuggling]]
- [[Enumerate Linux Privilege Escalation Paths (LinEnum)]]
- [[Enumerate Linux Privilege Escalation Paths (linPEAS)]]
- [[Enumerate Windows for Privilege Escalation (JAWS)]]
- [[Enumerate Windows for Privilege Escalation (SharpUp)]]
- [[Enumerate Windows for Privilege Escalation (winPEAS)]]
- [[Kubernetes API Address Enumeration via kubelet]]
- [[Monitor Processes and Commands]]
- [[MYSQL Time Based Injection using SLEEP in a subselect]]
