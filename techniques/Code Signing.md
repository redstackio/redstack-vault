---
id: c4c5d507-60a0-451a-b740-f5584f9dffe3
name: Code Signing
type: technique
mitre_id: T1116
mitre_url: null
created_at: '2019-08-28T21:17:25.634993+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[DB2 Injection - Time Delay]]'
- '[[ECMAScript6 Filter Bypass Script Injection]]'
- '[[Linux Privilege Escalation - Writable Files Escalation]]'
- '[[MSSQL Read File via INI Disclosure]]'
- '[[MSSQL Server Extended Stored Procedure DLL Injection]]'
- '[[POP Gadget .NET Serialization]]'
- '[[Windows Defender Application Control Device Guard Configuration]]'
- '[[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]'
---

# Code Signing

**MITRE ID**: T1116

## Description

Code signing provides a level of authenticity on a binary from the developer and a guarantee that the binary has not been tampered with. [1] However, adversaries are known to use code signing certificates to masquerade malware and tools as legitimate binaries [2]. The certificates used during an operation may be created, forged, or stolen by the adversary. [3] [4]Code signing to verify software on first run can be used on modern Windows and macOS/OS X systems. It is not used on Linux due to the decentralized nature of the platform. [1]Code signing certificates may be used to bypass security policies that require signed code to execute on a system.

# Detection

Collect and analyze signing certificate metadata on software that executes within the environment to look for unusual certificate characteristics and outliers.

# Mitigation

Process whitelisting and trusted publishers to verify authenticity of software can help prevent signed malicious or untrusted code from executing on a system. [33] [34] [3]

# Footnotes

[1] Wikipedia. (2015, November 10). Code Signing. Retrieved March 31, 2016.

[2] Thomas. (2013, July 15). New signed malware called Janicab. Retrieved July 17, 2017.

[3] Ladikov, A. (2015, January 29). Why You Shouldn’t Completely Trust Files Signed with Digital Certificates. Retrieved March 31, 2016.

[4] Shinotsuka, H. (2013, February 22). How Attackers Steal Private Keys from Digital Certificates. Retrieved March 31, 2016.

[5] Raiu, C., and Ivanov, A. (2016, June 17). Operation Daybreak. Retrieved February 15, 2018.

[6] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[7] Miller-Osborn, J. and Grunzweig, J.. (2017, February 16). menuPass Returns with New Malware and New Attacks Against Japanese Academics and Organizations. Retrieved March 1, 2017.

[8] Nakamura, Y.. (2017, February 17). ChChes - Malware that Communicates with C&C Servers Using Cookie Headers. Retrieved March 1, 2017.

[9] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[10] Kaspersky Lab's Global Research and Analysis Team. (2014, November). The Darkhotel APT A Story of Unusual Hospitality. Retrieved November 12, 2014.

[11] Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.

[12] DiMaggio, J. (2016, April 28). Tick cyberespionage group zeros in on Japan. Retrieved July 16, 2018.

[13] M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.

[14] Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.

[15] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[16] Carr, N., et al. (2018, August 01). On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation. Retrieved August 23, 2018.

[17] ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.

[18] Kaspersky Lab's Global Research & Analysis Team. (2017, August 30). Introducing WhiteBear. Retrieved September 21, 2017.

[19] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[20] ClearSky Cybersecurity. (2017, January 5). Iranian Threat Agent OilRig Delivers Digitally Signed Malware, Impersonates University of Oxford. Retrieved May 3, 2017.

[21] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[22] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[23] Plan, F., et all. (2019, March 4). APT40: Examining a China-Nexus Espionage Actor. Retrieved March 18, 2019.

[24] Villeneuve, N., Haq, H., Moran, N. (2013, August 23). OPERATION MOLERATS: MIDDLE EAST CYBER ATTACKS USING POISON IVY. Retrieved April 1, 2016.

[25] Ladley, F. (2012, May 15). Backdoor.Nerex. Retrieved February 23, 2018.

[26] McAfee. (2015, March 2). Netwire RAT Behind Recent Targeted Attacks. Retrieved February 15, 2018.

[27] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[28] Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.

[29] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[30] Russinovich, M. (2016, July 4). SDelete v2.0. Retrieved February 8, 2018.

[31] DiMaggio, J.. (2016, March 15). Suckfly: Revealing the secret life of your code signing certificates. Retrieved August 3, 2016.

[32] Kaspersky Lab's Global Research and Analysis Team. (2013, April 11). Winnti. More than just a game. Retrieved February 8, 2017.

[33] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[34] Microsoft. (n.d.). Manage Trusted Publishers. Retrieved March 31, 2016.

## Defense

Process whitelisting and trusted publishers to verify authenticity of software can help prevent signed malicious or untrusted code from executing on a system. (Citation: NSA MS AppLocker) (Citation: TechNet Trusted Publishers) (Citation: Securelist Digita

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (8)

- [[DB2 Injection - Time Delay]]
- [[ECMAScript6 Filter Bypass Script Injection]]
- [[Linux Privilege Escalation - Writable Files Escalation]]
- [[MSSQL Read File via INI Disclosure]]
- [[MSSQL Server Extended Stored Procedure DLL Injection]]
- [[POP Gadget .NET Serialization]]
- [[Windows Defender Application Control Device Guard Configuration]]
- [[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]
