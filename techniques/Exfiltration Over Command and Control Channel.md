---
id: ebdefb52-dd55-420b-937a-3b9d2f14acd2
name: Exfiltration Over Command and Control Channel
type: technique
mitre_id: T1041
mitre_url: null
created_at: '2019-08-28T21:17:39.592073+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[Active Directory SCCM Loot Inventory and Download]]'
- '[[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]'
- '[[Mercurial Source Code Extraction with rip-hg.pl]]'
- '[[MYSQL Injection with Out of Band DNS Exfiltration]]'
- '[[PostgreSQL Time Based Injection for Database Dump]]'
- '[[RDS List Instance Details Exfiltration]]'
---

# Exfiltration Over Command and Control Channel

**MITRE ID**: T1041

## Description

Data exfiltration is performed over the Command and Control channel. Data is encoded into the normal communications channel using the same protocol as command and control communications.

# Detection

Detection for command and control applies. Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [23]

# Mitigation

Mitigations for command and control apply. Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [23]

# Footnotes

[1] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[2] Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.

[3] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[4] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[5] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[6] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[7] Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.

[8] Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.

[9] Trend Micro. (2019, January 16). Exploring Emotet's Activities . Retrieved March 25, 2019.

[10] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[11] Kasza, A. and Reichel, D.. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.

[12] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[13] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[14] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[15] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved March 2, 2016.

[16] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[17] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[18] Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.

[19] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[20] Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.

[21] Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.

[22] Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.

[23] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Mitigations for command and control apply. Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for un

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (6)

- [[Active Directory SCCM Loot Inventory and Download]]
- [[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]
- [[Mercurial Source Code Extraction with rip-hg.pl]]
- [[MYSQL Injection with Out of Band DNS Exfiltration]]
- [[PostgreSQL Time Based Injection for Database Dump]]
- [[RDS List Instance Details Exfiltration]]
