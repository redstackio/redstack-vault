---
id: 1bbb15fd-72f0-45a2-9ec3-01b1c051e638
name: Software Packing
type: technique
mitre_id: T1045
mitre_url: null
created_at: '2019-08-28T21:17:36.211712+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt]]'
- '[[VBA-AMSI Bypass]]'
---

# Software Packing

**MITRE ID**: T1045

## Description

Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techniques decompress the executable code in memory.Utilities used to perform software packing are called packers. Example packers are MPRESS and UPX. A more comprehensive list of known packers is available, [1] but adversaries may create their own packing techniques that do not leave the same artifacts as well-known packers to evade defenses.

# Detection

Use file scanning to look for known software packers or artifacts of packing techniques. Packing is not a definitive indicator of malicious activity, because legitimate software may use packing techniques to reduce binary size or to protect proprietary code.

# Mitigation

Ensure updated virus definitions. Create custom signatures for observed malware. Employ heuristic-based malware detection.

Identify and prevent execution of potentially malicious software that may have been packed by using whitelisting [31] tools like AppLocker [32] [33] or Software Restriction Policies [34] where appropriate. [35]

# Footnotes

[1] Executable compression. (n.d.). Retrieved December 4, 2014.

[2] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[3] Korban, C, et al. (2017, September). APT3 Adversary Emulation Plan. Retrieved January 16, 2018.

[4] Dumont, R.. (2019, April 9). OceanLotus: macOS malware update. Retrieved April 15, 2019.

[5] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[6] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[7] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[8] Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.

[9] Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.

[10] Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.

[11] Chen, J. and Hsieh, M. (2017, November 7). REDBALDKNIGHT/BRONZE BUTLER’s Daserf Backdoor Now Using Steganography. Retrieved December 27, 2017.

[12] O'Gorman, G., and McDonald, G.. (2012, September 6). The Elderwood Project. Retrieved February 15, 2018.

[13] Trend Micro. (2019, January 16). Exploring Emotet's Activities . Retrieved March 25, 2019.

[14] FinFisher. (n.d.). Retrieved December 20, 2017.

[15] Kaspersky Lab's Global Research & Analysis Team. (2017, October 16). BlackOasis APT and new targeted attacks leveraging zero-day exploit. Retrieved February 15, 2018.

[16] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[17] Scott-Railton, J., et al. (2016, August 2). Group5: Syria and the Iranian Connection. Retrieved September 26, 2016.

[18] Reynolds, J.. (2016, September 13). H1N1: Technical analysis reveals new capabilities. Retrieved September 26, 2016.

[19] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[20] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[21] Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.

[22] Kaspersky Lab's Global Research & Analysis Team. (2016, July 8). The Dropping Elephant – aggressive cyber-espionage in the Asian region. Retrieved August 3, 2016.

[23] Grunzweig, J.. (2015, July 14). Unit 42 Technical Analysis: Seaduke. Retrieved August 3, 2016.

[24] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[25] Symantec Security Response. (2014, July 7). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.

[26] Symantec. (2015, January 26). The Waterbug attack group. Retrieved April 10, 2015.

[27] Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.

[28] Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.

[29] Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.

[30] Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.

[31] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[32] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[33] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[34] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[35] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Ensure updated virus definitions. Create custom signatures for observed malware. Employ heuristic-based malware detection.

Identify and prevent execution of potentially malicious software that may have been packed by using whitelisting (Citation: Beechey

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (2)

- [[ASR Bypass Create Child Process Rule 5 and Open PowerShell from Command Prompt]]
- [[VBA-AMSI Bypass]]
