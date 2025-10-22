---
id: ad034f1e-de8d-4b55-bad7-384abcd11670
name: DLL Side-Loading
type: technique
mitre_id: T1073
mitre_url: null
created_at: '2019-08-28T21:17:36.637350+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Command Execution via xp_cmdshell - MSSQL Server]]'
---

# DLL Side-Loading

**MITRE ID**: T1073

## Description

Programs may specify DLLs that are loaded at runtime. Programs that improperly or vaguely specify a required DLL may be open to a vulnerability in which an unintended DLL is loaded. Side-loading vulnerabilities specifically occur when Windows Side-by-Side (WinSxS) manifests [1] are not explicit enough about characteristics of the DLL to be loaded. Adversaries may take advantage of a legitimate program that is vulnerable to side-loading to load a malicious DLL. [2]Adversaries likely use this technique as a means of masking actions they perform under a legitimate, trusted system or software process.

# Detection

Monitor processes for unusual activity (e.g., a process that does not use the network begins to do so). Track DLL metadata, such as a hash, and compare DLLs that are loaded at process execution time against previous executions to detect differences that do not correlate with patching or updates.

# Mitigation

Update software regularly. Install software in write-protected locations. Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software.

# Footnotes

[1] Microsoft. (n.d.). Manifests. Retrieved June 3, 2016.

[2] Stewart, A. (2014). DLL SIDE-LOADING: A Thorn in the Side of the Anti-Virus Industry. Retrieved November 12, 2014.

[3] Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.

[4] Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.

[5] Scott, M.. (2014, June 10). Clandestine Fox, Part Deux. Retrieved January 14, 2016.

[6] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[7] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[8] Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.

[9] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[10] Levene, B. et al.. (2018, March 7). Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent. Retrieved March 31, 2018.

[11] Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.

[12] FinFisher. (n.d.). Retrieved December 20, 2017.

[13] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[14] Sabo, S. (2018, February 15). Musical Chairs Playing Tetris. Retrieved February 19, 2018.

[15] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[16] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[17] Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.

[18] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[19] Lancaster, T. and Idrizovic, E.. (2017, June 27). Paranoid PlugX. Retrieved July 13, 2017.

[20] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, July 30). Sakula Malware Family. Retrieved January 26, 2016.

[21] Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.

[22] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[23] Legezo, D. (2018, June 13). LuckyMouse hits national data center to organize country-level waterholing campaign. Retrieved August 18, 2018.

[24] Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.

[25] Microsoft. (2017, November 9). Backdoor:Win32/Wingbird.A!dha. Retrieved November 27, 2017.

[26] Axel F. (2017, April 27). APT Targets Financial Analysts with CVE-2017-0199. Retrieved February 15, 2018.

[27] Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.

## Defense

Update software regularly. Install software in write-protected locations. Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (1)

- [[Command Execution via xp_cmdshell - MSSQL Server]]
