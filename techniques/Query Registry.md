---
id: 84f7d79b-8fc9-41be-a8c9-db4c8c5bd16e
name: Query Registry
type: technique
mitre_id: T1012
mitre_url: null
created_at: '2019-08-28T21:17:25.411425+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory Integrated DNS Enumeration]]'
- '[[DB2 Current User Information Retrieval]]'
- '[[DB2 Injection - List Columns]]'
- '[[Domain Trust Enumeration]]'
- '[[Enumerate Database Users for a MSSQL Server Database]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Extracting Database Information using MySQL Union Based Injection]]'
- '[[Impersonation Credential Check]]'
- '[[Linked Database Column Extraction]]'
- '[[Linked Database Top 5 Columns Extraction]]'
- '[[MSSQL Database Name Enumeration]]'
- '[[MSSQL Injection - List Permissions]]'
- '[[MSSQL Read File via INI Disclosure]]'
- '[[MSSQL Server Effective Permissions Query]]'
- '[[MSSQL Server - Identify Sensitive Information - Gather Top 5 Entries from a Specific
  Table]]'
- '[[MSSQL Server Linked Database Enumeration]]'
- '[[MSSQL UNC Path Out-of-Band Data Retrieval]]'
- '[[MYSQL Out of Band UNC Path Hash Stealing]]'
- '[[MYSQL Union-Based Injection to Extract Column Names]]'
- '[[Oracle SQL Database Enumeration]]'
- '[[Oracle SQL List Tables and Columns]]'
---

# Query Registry

**MITRE ID**: T1012

## Description

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.The Registry contains a significant amount of information about the operating system, configuration, software, and security. [1] Some of the information may help adversaries to further their operation within a network.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Interaction with the Windows Registry may come from the command line using utilities such as Reg or through running malware that may interact with the Registry through an API. Command-line invocation of utilities used to query the Registry may be detected through process and command-line monitoring. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information within the Registry, and audit and/or block them by using whitelisting [51] tools, like AppLocker, [52] [53] or Software Restriction Policies [54] where appropriate. [55]

# Footnotes

[1] Wikipedia. (n.d.). Windows Registry. Retrieved February 2, 2015.

[2] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[3] Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.

[4] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[5] Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.

[6] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[7] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[8] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[9] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[10] ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.

[11] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[12] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[13] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[14] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[15] ClearSky Cyber Security. (2017, December). Charming Kitten. Retrieved December 27, 2017.

[16] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[17] Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.

[18] Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved July 31, 2018.

[19] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[20] FinFisher. (n.d.). Retrieved December 20, 2017.

[21] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[22] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[23] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[24] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[25] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[26] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[27] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[28] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved March 2, 2016.

[29] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[30] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[31] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[32] Vasilenko, R. (2013, December 17). An Analysis of PlugX Malware. Retrieved November 24, 2015.

[33] Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.

[34] Brumaghin, E. and Grady, C.. (2017, March 2). Covert Channels and Poor Decisions: The Tale of DNSMessenger. Retrieved March 8, 2017.

[35] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[36] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[37] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[38] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[39] Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.

[40] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[41] Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.

[42] Microsoft. (2012, April 17). Reg. Retrieved May 1, 2015.

[43] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[44] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[45] Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.

[46] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[47] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[48] US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.

[49] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[50] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[51] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[52] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[53] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[54] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[55] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information within the Registry, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Comma

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (21)

- [[Active Directory Integrated DNS Enumeration]]
- [[DB2 Current User Information Retrieval]]
- [[DB2 Injection - List Columns]]
- [[Domain Trust Enumeration]]
- [[Enumerate Database Users for a MSSQL Server Database]]
- [[Enumerate Windows for Privilege Escalation (PowerUp)]]
- [[Extracting Database Information using MySQL Union Based Injection]]
- [[Impersonation Credential Check]]
- [[Linked Database Column Extraction]]
- [[Linked Database Top 5 Columns Extraction]]
- [[MSSQL Database Name Enumeration]]
- [[MSSQL Injection - List Permissions]]
- [[MSSQL Read File via INI Disclosure]]
- [[MSSQL Server Effective Permissions Query]]
- [[MSSQL Server - Identify Sensitive Information - Gather Top 5 Entries from a Specific Table]]
- [[MSSQL Server Linked Database Enumeration]]
- [[MSSQL UNC Path Out-of-Band Data Retrieval]]
- [[MYSQL Out of Band UNC Path Hash Stealing]]
- [[MYSQL Union-Based Injection to Extract Column Names]]
- [[Oracle SQL Database Enumeration]]

*...and 1 more*
