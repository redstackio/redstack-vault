---
id: 8cfc0d1b-c038-457b-b981-07fef4240769
name: Remote System Discovery
type: technique
mitre_id: T1018
mitre_url: null
created_at: '2019-08-28T21:17:43.174155+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory Domain Controller Lookup]]'
- '[[Active Directory Recon using BloodHound Custom Queries]]'
- '[[Domain SQL Server Discovery]]'
- '[[Kubelet API Address Enumeration]]'
- '[[Kubernetes Endpoint Enumeration]]'
- '[[Linked Database Enumeration]]'
- '[[Ping Sweep a Subnet for Online Hosts]]'
- '[[RDS Enumeration of Routing Tables by VPC-id]]'
- '[[RDS Subnet Enumeration]]'
- '[[RDS Subnet Group Enumeration]]'
- '[[S3 Bucket File Listing]]'
- '[[S3 Bucket File Listing]]'
- '[[SID Enumeration and WMI Query for MS14-068 Checksum Validation]]'
---

# Remote System Discovery

**MITRE ID**: T1018

## Description

Adversaries will likely attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used. Adversaries may also use local host files in order to discover the hostname to IP address mappings of remote systems. WindowsExamples of tools and commands that acquire this information include "ping" or "net view" using Net. The contents of the C:\Windows\System32\Drivers\etc\hosts file can be viewed to gain insight into the existing hostname to IP mappings on the system.MacSpecific to Mac, the bonjour protocol to discover additional Mac-based systems within the same broadcast domain. Utilities such as "ping" and others can be used to gather information about remote systems. The contents of the /etc/hosts file can be viewed to gain insight into existing hostname to IP mappings on the system.LinuxUtilities such as "ping" and others can be used to gather information about remote systems. The contents of the /etc/hosts file can be viewed to gain insight into existing hostname to IP mappings on the system.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events related to legitimate remote system discovery may be uncommon, depending on the environment and how they are used. Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell. 

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information on remotely available systems, and audit and/or block them by using whitelisting [31] tools, like AppLocker, [32] [33] or Software Restriction Policies [34] where appropriate. [35]

# Footnotes

[1] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[2] Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.

[3] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[4] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[5] GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.

[6] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[7] Alperovitch, D. (2014, July 7). Deep in Thought: Chinese Targeting of National Security Think Tanks. Retrieved November 12, 2014.

[8] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[9] Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.

[10] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[11] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[12] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[13] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[14] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[15] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[16] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[17] FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.

[18] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[19] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[20] ss64. (n.d.). NLTEST.exe - Network Location Test. Retrieved February 14, 2019.

[21] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[22] Microsoft. (n.d.). Ping. Retrieved April 8, 2016.

[23] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[24] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[25] FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved January 11, 2017.

[26] Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.

[27] Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.

[28] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[29] Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.

[30] Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.

[31] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[32] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[33] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[34] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[35] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information on remotely available systems, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Win

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (13)

- [[Active Directory Domain Controller Lookup]]
- [[Active Directory Recon using BloodHound Custom Queries]]
- [[Domain SQL Server Discovery]]
- [[Kubelet API Address Enumeration]]
- [[Kubernetes Endpoint Enumeration]]
- [[Linked Database Enumeration]]
- [[Ping Sweep a Subnet for Online Hosts]]
- [[RDS Enumeration of Routing Tables by VPC-id]]
- [[RDS Subnet Enumeration]]
- [[RDS Subnet Group Enumeration]]
- [[S3 Bucket File Listing]]
- [[S3 Bucket File Listing]]
- [[SID Enumeration and WMI Query for MS14-068 Checksum Validation]]
