---
id: bcb6daa6-ca19-4413-bbd2-ea87fe957ddf
name: Modify Registry
type: technique
mitre_id: T1112
mitre_url: null
created_at: '2019-08-28T21:17:42.080152+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]'
- '[[DB2 Injection - Select Nth Char Extraction]]'
- '[[Identify Encrypted Databases via MSSQL Server]]'
- '[[Patching AmsiScanBuffer to Bypass AMSI Scanning]]'
---

# Modify Registry

**MITRE ID**: T1112

## Description

Adversaries may interact with the Windows Registry to hide configuration information within Registry keys, remove information as part of cleaning up, or as part of other techniques to aid in Persistence and Execution.Access to specific areas of the Registry depends on account permissions, some requiring administrator-level access. The built-in Windows command-line utility Reg may be used for local or remote Registry modification. [1] Other tools may also be used, such as a remote access tool, which may contain functionality to interact with the Registry through the Windows API (see examples).Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via Reg or other utilities using the Win32 API. [2] Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to establish Persistence. [3] [4]The Registry of a remote system may be modified to aid in execution of files as part of Lateral Movement. It requires the remote Registry service to be running on the target system. [5] Often Valid Accounts are required, along with access to the remote system's Windows Admin Shares for RPC communication.

# Detection

Modifications to the Registry are normal and occur throughout typical use of the Windows operating system. Consider enabling Registry Auditing on specific keys to produce an alertable event (Event ID 4657) whenever a value is changed (though this may not trigger when values are created with Reghide or other evasive methods). [62] Changes to Registry entries that load software on Windows startup that do not correlate with known software, patch cycles, etc., are suspicious, as are additions or changes to files within the startup folder. Changes could also include new services and modification of existing binary paths to point to malicious files. If a change to a service-related entry occurs, then it will likely be followed by a local or remote service start or restart to execute the file.

Monitor processes and command-line arguments for actions that could be taken to change or delete information in the Registry. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell, which may require additional logging features to be configured in the operating system to collect necessary information for analysis.

Monitor for processes, command-line arguments, and API calls associated with concealing Registry keys, such as Reghide. [2] Inspect and cleanup malicious hidden Registry entries using Native Windows API calls and/or tools such as Autoruns [4] and RegDelNull [63].

# Mitigation

Misconfiguration of permissions in the Registry may lead to opportunities for an adversary to execute code, like through Service Registry Permissions Weakness. Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

Identify and block unnecessary system utilities or potentially malicious software that may be used to modify the Registry by using whitelisting [57] tools like AppLocker [58] [59] or Software Restriction Policies [60] where appropriate. [61]

# Footnotes

[1] Microsoft. (2012, April 17). Reg. Retrieved May 1, 2015.

[2] Russinovich, M. & Sharkey, K. (2006, January 10). Reghide. Retrieved August 9, 2018.

[3] Santos, R. (2014, August 1). POWELIKS: Malware Hides In Windows Registry. Retrieved August 9, 2018.

[4] Reitz, B. (2017, July 14). Hiding Registry keys with PSReflect. Retrieved August 9, 2018.

[5] Microsoft. (n.d.). Enable the Remote Registry Service. Retrieved May 1, 2015.

[6] Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.

[7] Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.

[8] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[9] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[10] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[11] US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.

[12] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[13] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[14] Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved July 10, 2018.

[15] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[16] TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.

[17] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[18] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[19] Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.

[20] Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved July 31, 2018.

[21] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[22] Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.

[23] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[24] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[25] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[26] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[27] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[28] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[29] US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.

[30] ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.

[31] Neville, A. (2012, June 15). Trojan.Naid. Retrieved February 22, 2018.

[32] The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.

[33] Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.

[34] Ladley, F. (2012, May 15). Backdoor.Nerex. Retrieved February 23, 2018.

[35] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[36] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[37] Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.

[38] Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.

[39] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[40] Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.

[41] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[42] Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.

[43] Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.

[44] Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.

[45] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[46] FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved January 11, 2017.

[47] Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.

[48] Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.

[49] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[50] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[51] Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.

[52] US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.

[53] US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.

[54] Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.

[55] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[56] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[57] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[58] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[59] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[60] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[61] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[62] Miroshnikov, A. & Hall, J. (2017, April 18). 4657(S): A registry value was modified. Retrieved August 9, 2018.

[63] Russinovich, M. & Sharkey, K. (2016, July 4). RegDelNull v1.11. Retrieved August 10, 2018.

## Defense

Misconfiguration of permissions in the Registry may lead to opportunities for an adversary to execute code, like through [Service Registry Permissions Weakness](https://attack.mitre.org/techniques/T1058). Ensure proper permissions are set for Registry hiv

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (4)

- [[Abusing Active Directory ACLs/ACEs - GenericWrite and Remote Connection Manager]]
- [[DB2 Injection - Select Nth Char Extraction]]
- [[Identify Encrypted Databases via MSSQL Server]]
- [[Patching AmsiScanBuffer to Bypass AMSI Scanning]]
