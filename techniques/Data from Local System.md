---
id: 975e0d1d-ca2a-4563-9d82-674313474bd0
name: Data from Local System
type: technique
mitre_id: T1005
mitre_url: null
created_at: '2019-08-28T21:17:20.794546+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
procedures:
- '[[Active Directory SCCM Loot Inventory and Download]]'
- '[[Dump a Process''s Memory (PowerShell)]]'
- '[[EBS Snapshot Creation]]'
- '[[Enumerate a MS Access .mdb Database and Tables]]'
- '[[Enumerate Local Users'' PowerShell History]]'
- '[[Extract E-mails and Attachments from MS .PST Files]]'
- '[[Extracting Database Information using MySQL Union Based Injection]]'
- '[[Find Interesting Strings in a Raw Memory Dump]]'
- '[[Git Repository Dumping with GoGitDumper]]'
- '[[Jinja2 Server Side Template Injection - Dump All Used Classes]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[Log4Shell Environment Variables Exfiltration]]'
- '[[MSSQL Server - Identify Sensitive Information - Get Tables and Column Details]]'
- '[[Oracle SQL List Tables and Columns]]'
- '[[Password Looting from SharePoint and SMB Shares]]'
- '[[Unzip an AES Encrypted Zip Archive (Linux)]]'
- '[[XML External Entity Injection to Disclose HTTP Response]]'
- '[[XML External Entity WAF Bypass via Character Encoding]]'
- '[[XML External Entity (XXE) Injection using Various Tools]]'
- '[[XXE in DTD File Contents Extractor]]'
---

# Data from Local System

**MITRE ID**: T1005

## Description

Sensitive data can be collected from local system sources, such as the file system or databases of information residing on the system prior to Exfiltration.Adversaries will often search the file system on computers they have compromised to find files of interest. They may do this using a Command-Line Interface, such as cmd, which has functionality to interact with the file system to gather information. Some adversaries may also use Automated Collection on the local system.

# Detection

Monitor processes and command-line arguments for actions that could be taken to collect files from a system. Remote access tools with built-in features may interact directly with the Windows API to gather data. Data may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to collect data from the local system, and audit and/or block them by using whitelisting [52] tools, like AppLocker, [53] [54] or Software Restriction Policies [55] where appropriate. [56]

# Footnotes

[1] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[2] Guarnieri, C. (2015, June 19). Digital Attack on German Parliament: Investigative Report on the Hack of the Left Party Infrastructure in Bundestag. Retrieved January 22, 2018.

[3] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[4] valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.

[5] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[6] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[7] Levene, B. et al.. (2018, March 7). Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent. Retrieved March 31, 2018.

[8] Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.

[9] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[10] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[11] Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.

[12] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[13] Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.

[14] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[15] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[16] F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.

[17] Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.

[18] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[19] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[20] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[21] Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.

[22] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[23] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[24] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[25] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[26] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[27] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[28] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[29] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved March 2, 2016.

[30] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.

[31] Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.

[32] United States District Court Southern District of New York (USDC SDNY) . (2018, December 17). United States of America v. Zhu Hua and Zhang Shilong. Retrieved April 17, 2019.

[33] Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.

[34] Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.

[35] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[36] F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.

[37] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[38] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[39] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[40] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[41] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[42] Kizhakkinan, D. et al.. (2016, May 11). Threat Actor Leverages Windows Zero-day Exploit in Payment Card Data Attacks. Retrieved February 12, 2018.

[43] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[44] Nesbit, B. and Ackerman, D. (2017, January). Malware Analysis Report - RawPOS Malware: Deconstructing an Intruder’s Toolkit. Retrieved October 4, 2017.

[45] TrendLabs Security Intelligence Blog. (2015, April). RawPOS Technical Brief. Retrieved October 4, 2017.

[46] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[47] Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.

[48] Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.

[49] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[50] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[51] Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.

[52] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[53] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[54] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[55] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[56] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to collect data from the local system, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands J

## Tactics

- [[Collection|TA0009 - Collection]]

## Related Procedures (22)

- [[Active Directory SCCM Loot Inventory and Download]]
- [[Dump a Process's Memory (PowerShell)]]
- [[EBS Snapshot Creation]]
- [[Enumerate a MS Access .mdb Database and Tables]]
- [[Enumerate Local Users' PowerShell History]]
- [[Extract E-mails and Attachments from MS .PST Files]]
- [[Extracting Database Information using MySQL Union Based Injection]]
- [[Find Interesting Strings in a Raw Memory Dump]]
- [[Git Repository Dumping with GoGitDumper]]
- [[Jinja2 Server Side Template Injection - Dump All Used Classes]]
- [[Linux - Privilege Escalation via Writable /etc/passwd]]
- [[Log4Shell Environment Variables Exfiltration]]
- [[Log4Shell Environment Variables Exfiltration]]
- [[Log4Shell Environment Variables Exfiltration]]
- [[MSSQL Server - Identify Sensitive Information - Get Tables and Column Details]]
- [[Oracle SQL List Tables and Columns]]
- [[Password Looting from SharePoint and SMB Shares]]
- [[Unzip an AES Encrypted Zip Archive (Linux)]]
- [[XML External Entity Injection to Disclose HTTP Response]]
- [[XML External Entity WAF Bypass via Character Encoding]]

*...and 2 more*
