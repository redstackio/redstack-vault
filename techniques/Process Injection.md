---
id: f05d72f0-73fa-4510-aaa2-017503e53e7b
name: Process Injection
type: technique
mitre_id: T1055
mitre_url: null
created_at: '2019-08-28T21:17:44.532547+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[CLR Assembly Creation and Execution]]'
- '[[Cobalt Strike Elevate Kit with Beacon Command Elevators]]'
- '[[Creating and Importing a CLR Assembly for MSSQL Server]]'
- '[[DirtyPipe Kernel Exploit Privilege Escalation]]'
- '[[Enumerate MSSQL Server Permissions]]'
- '[[Kubernetes RBAC Privilege Escalation via Malicious RoleBinding]]'
- '[[Linux - Docker Privilege Escalation]]'
- '[[Linux - List Capabilities of Executables]]'
- '[[Memory Execution of Calculator and WCE with Meterpreter]]'
- '[[MSSQL Server Extended Stored Procedure DLL Injection]]'
- '[[Upgrade Windows Meterpreter x32 Shell to x64]]'
- '[[Windows - Impersonation Privileges Elevation with Meterpreter]]'
- '[[Windows - Privileged DiagHub Exploit]]'
- '[[Windows Privilege Escalation - Processes and Tasks Enumeration]]'
- '[[Windows - Run Programs with Different Permissions using Runas Command]]'
---

# Process Injection

**MITRE ID**: T1055

## Description

Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process.WindowsThere are multiple approaches to injecting code into a live process. Windows implementations include: [1]Dynamic-link library (DLL) injection involves writing the path to a malicious DLL inside a process then invoking execution by creating a remote thread.Portable executable injection involves writing malicious code directly into the process (without a file on disk) then invoking execution with either additional code or by creating a remote thread. The displacement of the injected code introduces the additional requirement for functionality to remap memory references. Variations of this method such as reflective DLL injection (writing a self-mapping DLL into a process) and memory module (map DLL when writing into process) overcome the address relocation issue. [2]Thread execution hijacking involves injecting malicious code or the path to a DLL into a thread of a process. Similar to Process Hollowing, the thread must first be suspended.Asynchronous Procedure Call (APC) injection involves attaching malicious code to the APC Queue [3] of a process's thread. Queued APC functions are executed when the thread enters an alterable state. A variation of APC injection, dubbed "Early Bird injection", involves creating a suspended process in which malicious code can be written and executed before the process' entry point (and potentially subsequent anti-malware hooks) via an APC. [4]  AtomBombing  [5] is another variation that utilizes APCs to invoke malicious code previously written to the global atom table. [6]Thread Local Storage (TLS) callback injection involves manipulating pointers inside a portable executable (PE) to redirect a process to malicious code before reaching the code's legitimate entry point. [7]Mac and LinuxImplementations for Linux and OS X/macOS systems include: [8] [9]LD_PRELOAD, LD_LIBRARY_PATH (Linux), DYLD_INSERT_LIBRARIES (Mac OS X) environment variables, or the dlfcn application programming interface (API) can be used to dynamically load a library (shared object) in a process which can be used to intercept API calls from the running process. [10]Ptrace system calls can be used to attach to a running process and modify it in runtime. [9]/proc/[pid]/mem provides access to the memory of the process and can be used to read/write arbitrary data to it. This technique is very rare due to its complexity. [9]VDSO hijacking performs runtime injection on ELF binaries by manipulating code stubs mapped in from the linux-vdso.so shared object. [11]Malware commonly utilizes process injection to access system resources through which Persistence and other environment modifications can be made. More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel.

# Detection

Monitoring Windows API calls indicative of the various types of code injection may generate a significant amount of data and may not be directly useful for defense unless collected under specific circumstances for known bad sequences of calls, since benign use of API functions may be common and difficult to distinguish from malicious behavior. API calls such as CreateRemoteThread, SuspendThread/SetThreadContext/ResumeThread, QueueUserAPC/NtQueueApcThread, and those that can be used to modify memory within another process, such as WriteProcessMemory, may be used for this technique. [1]

Monitoring for Linux specific calls such as the ptrace system call, the use of LD_PRELOAD environment variable, or dlfcn dynamic linking API calls, should not generate large amounts of data due to their specialized nature, and can be a very effective method to detect some of the common process injection methods. [87]  [88]  [89]  [90]

Monitor for named pipe creation and connection events (Event IDs 17 and 18) for possible indicators of infected processes with external modules. [91]

Monitor processes and command-line arguments for actions that could be done before or after code injection has occurred and correlate the information with related event information. Code injection may also be performed using PowerShell with tools such as PowerSploit, [92] so additional PowerShell monitoring may be required to cover known implementations of this behavior.

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls will likely have unintended side effects, such as preventing legitimate software (i.e., security products) from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior. [77]

Identify or block potentially malicious software that may contain process injection functionality by using whitelisting [78] tools, like AppLocker, [79] [80] or Software Restriction Policies [81] where appropriate. [82]

Utilize Yama  [83] to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux  [84], grsecurity  [85], and AppAmour  [86].

# Footnotes

[1] Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.

[2] Desimone, J. (2017, June 13). Hunting in Memory. Retrieved December 7, 2017.

[3] Microsoft. (n.d.). Asynchronous Procedure Calls. Retrieved December 8, 2017.

[4] Gavriel, H. & Erbesfeld, B. (2018, April 11). New ‘Early Bird’ Code Injection Technique Discovered. Retrieved May 24, 2018.

[5] Liberman, T. (2016, October 27). ATOMBOMBING: BRAND NEW CODE INJECTION FOR WINDOWS. Retrieved December 8, 2017.

[6] Microsoft. (n.d.). About Atom Tables. Retrieved December 8, 2017.

[7] Vaish, A. & Nemes, S. (2017, November 28). Newly Observed Ursnif Variant Employs Malicious TLS Callback Technique to Achieve Process Injection. Retrieved December 18, 2017.

[8] Turner-Trauring, I. (2017, April 18). “This will only hurt for a moment”: code injection on Linux and macOS with LD_PRELOAD. Retrieved December 20, 2017.

[9] skape. (2003, January 19). Linux x86 run-time process manipulation. Retrieved December 20, 2017.

[10] halflife. (1997, September 1). Shared Library Redirection Techniques. Retrieved December 20, 2017.

[11] O'Neill, R. (2009, May). Modern Day ELF Runtime infection via GOT poisoning. Retrieved December 20, 2017.

[12] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[13] Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.

[14] Symantec Security Response. (2014, July 7). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.

[15] F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.

[16] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[17] ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.

[18] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[19] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[20] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[21] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[22] Perigaud, F. (2015, December 15). Newcomers in the Derusbi family. Retrieved December 20, 2017.

[23] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[24] Symantec Security Response. (2015, June 23). Dyre: Emerging threat on financial fraud landscape. Retrieved August 23, 2018.

[25] Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.

[26] Accenture Security. (2018, January 27). DRAGONFISH DELIVERS NEW FORM OF ELISE MALWARE TARGETING ASEAN DEFENCE MINISTERS’ MEETING AND ASSOCIATES. Retrieved November 14, 2018.

[27] Falcone, R. and Miller-Osborn, J.. (2015, December 18). Attack on French Diplomat Linked to Operation Lotus Blossom. Retrieved February 15, 2016.

[28] Özarslan, S. (2018, December 21). The Christmas Card you never wanted - A new wave of Emotet is back to wreak havoc. Retrieved March 25, 2019.

[29] Salvio, J.. (2014, June 27). New Banking Malware Uses Network Sniffing for Data Theft. Retrieved March 25, 2019.

[30] US-CERT. (2018, July 20). Alert (TA18-201A) Emotet Malware. Retrieved March 25, 2019.

[31] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[32] FinFisher. (n.d.). Retrieved December 20, 2017.

[33] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[34] ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.

[35] Kaspersky Lab's Global Research & Analysis Team. (2017, August 30). Introducing WhiteBear. Retrieved September 21, 2017.

[36] Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.

[37] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[38] ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.

[39] Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.

[40] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[41] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[42] F-Secure. (2015, September 8). Sofacy Recycles Carberp and Metasploit Code. Retrieved August 3, 2016.

[43] Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.

[44] Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.

[45] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[46] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[47] Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.

[48] Minerva Labs LTD and ClearSky Cyber Security. (2015, November 23). CopyKittens Attack Group. Retrieved September 11, 2017.

[49] Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.

[50] FireEye. (2014). POISON IVY: Assessing Damage and Extracting Intelligence. Retrieved November 12, 2014.

[51] Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.

[52] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[53] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[54] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[55] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[56] Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.

[57] Camba, A. (2013, February 27). BKDR_RARSTONE: New RAT to Watch Out For. Retrieved January 8, 2016.

[58] Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.

[59] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[60] Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.

[61] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[62] Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.

[63] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[64] Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.

[65] Trend Micro. (2012). The Taidoor Campaign. Retrieved November 12, 2014.

[66] Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.

[67] Legezo, D. (2018, June 13). LuckyMouse hits national data center to organize country-level waterholing campaign. Retrieved August 18, 2018.

[68] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[69] Antazo, F. (2016, October 31). TSPY_TRICKLOAD.N. Retrieved September 14, 2018.

[70] Pornasdoro, A. (2017, October 12). Trojan:Win32/Totbrick. Retrieved September 14, 2018.

[71] Horejsi, J., et al. (2018, March 14). Tropic Trooper’s New Strategy. Retrieved November 9, 2018.

[72] ESET Research. (2018, May 22). Turla Mosquito: A shift towards more generic tools. Retrieved July 3, 2018.

[73] Rapid7. (2013, November 26). meterpreter/source/extensions/priv/server/elevate/. Retrieved July 8, 2018.

[74] Zhou, R. (2012, May 15). Backdoor.Wiarp. Retrieved February 22, 2018.

[75] Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.

[76] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[77] McNamara, R. (2017, September 5). Linux Based Inter-Process Code Injection Without Ptrace(2). Retrieved December 20, 2017.

[78] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[79] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[80] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[81] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[82] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[83] Linux Kernel Archives. (n.d.). Yama Documentation - ptrace_scope. Retrieved December 20, 2017.

[84] SELinux Project. (2017, November 30). SELinux Project Wiki. Retrieved December 20, 2017.

[85] grsecurity. (2017, December 12). What is grsecurity?. Retrieved December 20, 2017.

[86] AppArmor. (2017, October 19). AppArmor Security Project Wiki. Retrieved December 20, 2017.

[87] Ligh, M.H. et al.. (2014, July). The Art of Memory Forensics: Detecting Malware and Threats in Windows, Linux, and Mac Memory. Retrieved December 20, 2017.

[88] GNU. (2010, February 5). The GNU Accounting Utilities. Retrieved December 20, 2017.

[89] Jahoda, M. et al.. (2017, March 14). redhat Security Guide - Chapter 7 - System Auditing. Retrieved December 20, 2017.

[90] stderr. (2014, February 14). Detecting Userland Preload Rootkits. Retrieved December 20, 2017.

[91] Russinovich, M. & Garnier, T. (2017, May 22). Sysmon v6.20. Retrieved December 13, 2017.

[92] PowerSploit. (n.d.). Retrieved December 4, 2014.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of operating system design features. For example, mitigating specific Windows API calls will likely have unintended side effects, such as prev

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (15)

- [[CLR Assembly Creation and Execution]]
- [[Cobalt Strike Elevate Kit with Beacon Command Elevators]]
- [[Creating and Importing a CLR Assembly for MSSQL Server]]
- [[DirtyPipe Kernel Exploit Privilege Escalation]]
- [[Enumerate MSSQL Server Permissions]]
- [[Kubernetes RBAC Privilege Escalation via Malicious RoleBinding]]
- [[Linux - Docker Privilege Escalation]]
- [[Linux - List Capabilities of Executables]]
- [[Memory Execution of Calculator and WCE with Meterpreter]]
- [[MSSQL Server Extended Stored Procedure DLL Injection]]
- [[Upgrade Windows Meterpreter x32 Shell to x64]]
- [[Windows - Impersonation Privileges Elevation with Meterpreter]]
- [[Windows - Privileged DiagHub Exploit]]
- [[Windows Privilege Escalation - Processes and Tasks Enumeration]]
- [[Windows - Run Programs with Different Permissions using Runas Command]]
