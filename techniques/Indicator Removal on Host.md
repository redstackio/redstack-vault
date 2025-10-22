---
id: c8bbdc3f-f213-4963-b622-137bc71f8ea1
name: Indicator Removal on Host
type: technique
mitre_id: T1070
mitre_url: null
created_at: '2019-08-28T21:17:41.394740+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Application Escape and Breakout via Context Menus and File Search Command]]'
- '[[Bypassing filters using Curl with Verbose Output]]'
- '[[Clear Linux Logs to Hide an Attack]]'
- '[[Clear Windows Event Logs with a Meterpreter Session]]'
- '[[Disable Script Logging and Clear Signatures]]'
- '[[Jinja2 Server Side Template Injection with os.popen().read()]]'
- '[[Linux APT Backdoor Persistence]]'
- '[[Linux Command History Evasion]]'
- '[[Obfuscating AWS CloudTrail and GuardDuty Logs]]'
- '[[Race Condition Turbo Intruder 2 Requests]]'
- '[[SQLite Injection - Remote Command Execution using Load_extension]]'
- '[[Windows - Clear Event Logs for Anti-Virus Evasion]]'
---

# Indicator Removal on Host

**MITRE ID**: T1070

## Description

Adversaries may delete or alter generated artifacts on a host system, including logs and potentially captured files such as quarantined malware. Locations and format of logs will vary, but typical organic system logs are captured as Windows events or Linux/macOS files such as Bash History and /var/log/* .Actions that interfere with eventing and other notifications that can be used to detect intrusion activity may compromise the integrity of security solutions, causing events to go unreported. They may also make forensic analysis and incident response more difficult due to lack of sufficient data to determine what occurred.Clear Windows Event LogsWindows event logs are a record of a computer's alerts and notifications. Microsoft defines an event as "any significant occurrence in the system or in a program that requires users to be notified or an entry added to a log." There are three system-defined sources of Events: System, Application, and Security.Adversaries performing actions related to account management, account logon and directory service access, etc. may choose to clear the events in order to hide their activities.The event logs can be cleared with the following utility commands:wevtutil cl systemwevtutil cl applicationwevtutil cl securityLogs may also be cleared through other mechanisms, such as PowerShell.

# Detection

File system monitoring may be used to detect improper deletion or modification of indicator files. For example, deleting Windows event logs (via native binaries [28], API functions [29], or PowerShell [30]) may generate an alterable event (Event ID 1102: "The audit log was cleared"). Events not stored on the file system may require different detection mechanisms.

# Mitigation

Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system. Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary.

# Footnotes

[1] Alperovitch, D.. (2016, June 15). Bears in the Midst: Intrusion into the Democratic National Committee. Retrieved August 3, 2016.

[2] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[3] Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved October 4, 2016.

[4] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[5] FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 6, 2018.

[6] US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.

[7] Cherepanov, A.. (2016, January 3). BlackEnergy by the SSHBearDoor: attacks against Ukrainian news media and electric industry. Retrieved May 18, 2016.

[8] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[9] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[10] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[11] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[12] FinFisher. (n.d.). Retrieved December 20, 2017.

[13] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[14] FireEye Threat Intelligence. (2015, July 13). Demonstrating Hustle, Chinese APT Groups Quickly Use Zero-Day Vulnerability (CVE-2015-5119) Following Hacking Team Leak. Retrieved January 25, 2016.

[15] Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.

[16] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[17] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[18] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[19] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[20] Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.

[21] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[22] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[23] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[24] Faou, M. and Boutin, J.. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.

[25] Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.

[26] Ivanov, A. et al.. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.

[27] Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.

[28] Plett, C. et al.. (2017, October 16). wevtutil. Retrieved July 2, 2018.

[29] Microsoft. (n.d.). EventLog.Clear Method (). Retrieved July 2, 2018.

[30] Microsoft. (n.d.). Clear-EventLog. Retrieved July 2, 2018.

## Defense

Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (12)

- [[Application Escape and Breakout via Context Menus and File Search Command]]
- [[Bypassing filters using Curl with Verbose Output]]
- [[Clear Linux Logs to Hide an Attack]]
- [[Clear Windows Event Logs with a Meterpreter Session]]
- [[Disable Script Logging and Clear Signatures]]
- [[Jinja2 Server Side Template Injection with os.popen().read()]]
- [[Linux APT Backdoor Persistence]]
- [[Linux Command History Evasion]]
- [[Obfuscating AWS CloudTrail and GuardDuty Logs]]
- [[Race Condition Turbo Intruder 2 Requests]]
- [[SQLite Injection - Remote Command Execution using Load_extension]]
- [[Windows - Clear Event Logs for Anti-Virus Evasion]]
