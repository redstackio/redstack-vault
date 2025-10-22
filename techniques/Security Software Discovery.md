---
id: c36f5f16-17c0-47ad-88f8-b95fbe0b9b81
name: Security Software Discovery
type: technique
mitre_id: T1063
mitre_url: null
created_at: '2019-08-28T21:17:23.716846+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Antivirus Enumeration - Windows Privilege Escalation]]'
- '[[Check PowerShell Session Language Mode]]'
- '[[Enumerate AppLocker Rules]]'
- '[[PrintNightmare WebDAV Attack]]'
- '[[Reflection Method with WMF5 Autologging Bypass]]'
- '[[Windows Defender Antivirus Overview and Configuration]]'
- '[[Windows Defender Firewall Configuration Dump and Blocked Ports Listing]]'
---

# Security Software Discovery

**MITRE ID**: T1063

## Description

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on the system. This may include things such as local firewall rules and anti-virus. These checks may be built into early-stage remote access tools.WindowsExample commands that can be used to obtain security software information are netsh, reg query with Reg, dir with cmd, and Tasklist, but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for.MacIt's becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about local security software, and audit and/or block them by using whitelisting [50] tools, like AppLocker, [51] [52] or Software Restriction Policies [53] where appropriate. [54]

# Footnotes

[1] Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved April 17, 2019.

[2] Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.

[3] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[4] Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.

[5] Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.

[6] F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.

[7] Huss, D.. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.

[8] Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.

[9] ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.

[10] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[11] Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.

[12] Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.

[13] Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.

[14] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[15] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[16] FinFisher. (n.d.). Retrieved December 20, 2017.

[17] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[18] Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.

[19] Gostev, A. (2012, May 30). Flame: Bunny, Frog, Munch and BeetleJuice…. Retrieved March 1, 2017.

[20] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[21] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[22] Sharma, R. (2018, August 15). Revamped jRAT Uses New Anti-Parsing Techniques. Retrieved September 21, 2018.

[23] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[24] Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.

[25] Rascagneres, P., Mercer, W. (2017, June 19). Delphi Used To Score Against Palestine. Retrieved November 13, 2018.

[26] Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.

[27] Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.

[28] ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.

[29] Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.

[30] Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.

[31] Microsoft. (n.d.). Using Netsh. Retrieved February 13, 2017.

[32] Microsoft. (2009, June 3). Netsh Commands for Windows Firewall. Retrieved April 20, 2016.

[33] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[34] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[35] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[36] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[37] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[38] Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.

[39] Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.

[40] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[41] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[42] Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.

[43] Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.

[44] Microsoft. (n.d.). Tasklist. Retrieved December 23, 2015.

[45] Ray, V. (2016, November 22). Tropic Trooper Targets Taiwanese Government and Fossil Fuel Provider With Poison Ivy. Retrieved November 9, 2018.

[46] Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.

[47] Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.

[48] Brumaghin, E., et al. (2017, November 02). Poisoning the Well: Banking Trojan Targets Google Search Results. Retrieved November 5, 2018.

[49] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[50] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[51] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[52] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[53] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[54] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about local security software, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Win

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (7)

- [[Antivirus Enumeration - Windows Privilege Escalation]]
- [[Check PowerShell Session Language Mode]]
- [[Enumerate AppLocker Rules]]
- [[PrintNightmare WebDAV Attack]]
- [[Reflection Method with WMF5 Autologging Bypass]]
- [[Windows Defender Antivirus Overview and Configuration]]
- [[Windows Defender Firewall Configuration Dump and Blocked Ports Listing]]
