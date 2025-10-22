---
id: 19531c20-bb2c-436f-81db-6b15cf22cc03
name: Virtualization/Sandbox Evasion
type: technique
mitre_id: T1497
mitre_url: null
created_at: '2019-08-28T21:17:35.613594+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Filter Bypass using Null Byte Injection]]'
- '[[Freemarker Sandbox Bypass Remote Code Execution]]'
- '[[Linux APT Backdoor Persistence]]'
- '[[Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning]]'
---

# Virtualization/Sandbox Evasion

**MITRE ID**: T1497

## Description

Adversaries may check for the presence of a virtual machine environment (VME) or sandbox to avoid potential detection of tools and activities. If the adversary detects a VME, they may alter their malware to conceal the core functions of the implant or disengage from the victim. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use several methods including Security Software Discovery to accomplish Virtualization/Sandbox Evasion by searching for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) to help determine if it is an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandboxes. [1]Virtual Machine Environment Artifacts DiscoveryAdversaries may use utilities such as Windows Management Instrumentation, PowerShell, Systeminfo, and the Query Registry to obtain system information and search for VME artifacts. Adversaries may search for VME artifacts in memory, processes, file system, and/or the Registry. Adversaries may use Scripting to combine these checks into one script and then have the program exit if it determines the system to be a virtual environment. Also, in applications like VMWare, adversaries can use a special I/O port to send commands and receive output. Adversaries may also check the drive size. For example, this can be done using the Win32 DeviceIOControl function. Example VME Artifacts in the Registry[2]HKLM\SOFTWARE\Oracle\VirtualBox Guest AdditionsHKLM\HARDWARE\Description\System\"SystemBiosVersion";"VMWARE"HKLM\HARDWARE\ACPI\DSDT\BOX_Example VME files and DLLs on the system[2]WINDOWS\system32\drivers\vmmouse.sys WINDOWS\system32\vboxhook.dllWindows\system32\vboxdisp.dllCommon checks may enumerate services running that are unique to these applications, installed programs on the system, manufacturer/product fields for strings relating to virtual machine applications, and VME-specific hardware/processor instructions.[2]User Activity DiscoveryAdversaries may search for user activity on the host (e.g., browser history, cache, bookmarks, number of files in the home directories, etc.) for reassurance of an authentic environment. They might detect this type of information via user interaction and digital signatures. They may have malware check the speed and frequency of mouse clicks to determine if it’s a sandboxed environment.[3] Other methods may rely on specific user interaction with the system before the malicious code is activated. Examples include waiting for a document to close before activating a macro [4] and waiting for a user to double click on an embedded image to activate [5].Virtual Hardware Fingerprinting DiscoveryAdversaries may check the fan and temperature of the system to gather evidence that can be indicative a virtual environment. An adversary may perform a CPU check using a WMI query $q = "Select * from Win32_Fan" Get-WmiObject -Query $q. If the results of the WMI query return more than zero elements, this might tell them that the machine is a physical one. [6]

# Detection

Virtualization, sandbox, and related discovery techniques will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection.

# Mitigation

Mitigation of this technique with preventative controls may impact the adversary's decision process depending on what they're looking for, how they use the information, and what their objectives are. Since it may be difficult to mitigate all aspects of information that could be gathered, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised.

# Footnotes

[1] Falcone, R., Wartell, R.. (2015, July 27). UPS: Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved April 23, 2019.

[2] Roccia, T. (2017, January 19). Stopping Malware With a Fake Virtual Machine. Retrieved April 17, 2019.

[3] Keragala, D. (2016, January 16). Detecting Malware and Sandbox Evasion Techniques. Retrieved April 17, 2019.

[4] Falcone, R., Lee, B.. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved April 23, 2019.

[5] Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.

[6] Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.

[7] Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.

[8] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[9] F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.

[10] Symantec Security Response. (2015, June 23). Dyre: Emerging threat on financial fraud landscape. Retrieved August 23, 2018.

[11] FinFisher. (n.d.). Retrieved December 20, 2017.

[12] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[13] Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.

[14] Lancaster, T., Idrizovic, E. (2017, June 27). Paranoid PlugX. Retrieved April 19, 2019.

[15] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[16] Brumaghin, E., Unterbrink, H. (2018, August 22). Picking Apart Remcos Botnet-In-A-Box. Retrieved November 6, 2018.

[17] Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.

[18] Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.

[19] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[20] Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.

[21] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[22] Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.

[23] Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.

[24] Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.

## Defense

Mitigation of this technique with preventative controls may impact the adversary's decision process depending on what they're looking for, how they use the information, and what their objectives are. Since it may be difficult to mitigate all aspects of in

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

## Related Procedures (4)

- [[Filter Bypass using Null Byte Injection]]
- [[Freemarker Sandbox Bypass Remote Code Execution]]
- [[Linux APT Backdoor Persistence]]
- [[Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning]]
