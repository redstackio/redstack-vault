---
id: d0a84ede-1eae-4751-9618-c0dc5e70866f
name: Credentials in Files
type: technique
mitre_id: T1081
mitre_url: null
created_at: '2019-08-28T21:17:48.060954+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory Credential Dumping via Vssadmin]]'
- '[[AWS Metadata Credential Theft]]'
- '[[Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell]]'
- '[[Dumping Active Directory Credentials via NTDS.dit File]]'
- '[[Dumping AD Domain Credentials using Esentutl.exe]]'
- '[[Enumerate a Git Repository for Secrets]]'
- '[[Github API Key Leakage]]'
- '[[Github API Key Leakage]]'
- '[[Github API Key Leakage]]'
- '[[Linux - Password Looting from Files]]'
- '[[Linux - Privilege Escalation: Looting for Old Passwords]]'
- '[[RODC Key List Extraction and Golden Ticket Creation]]'
- '[[Server Side Template Injection - Django Templates - Admin Credentials Leak]]'
- '[[Twitter Bearer Token Leak Exploitation]]'
- '[[Twitter Bearer Token Leak Exploitation]]'
- '[[Twitter Bearer Token Leak Exploitation]]'
- '[[Windows - Creating a PSCredential Object with a Secure Password]]'
- '[[Windows Credentials Decryption using Powershell Secure String]]'
- '[[Windows Elevation of Privilege - Looting WiFi Passwords]]'
- '[[Windows - EoP Looting for Passwords]]'
- '[[Windows - Guest Credential Default Password]]'
- '[[Windows Privilege Escalation - Looting LAPS Settings]]'
- '[[Windows - Sticky Notes Password Extraction]]'
- '[[Windows Unattend Password Extraction]]'
---

# Credentials in Files

**MITRE ID**: T1081

## Description

Adversaries may search local file systems and remote file shares for files containing passwords. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.It is possible to extract passwords from backups or saved virtual machines through Credential Dumping. [1] Passwords may also be obtained from Group Policy Preferences stored on the Windows Domain Controller. [2]

# Detection

While detecting adversaries accessing these files may be difficult without knowing they exist in the first place, it may be possible to detect adversary use of credentials they have obtained. Monitor the command-line arguments of executing processes for suspicious words or regular expressions that may indicate searching for a password (for example: password, pwd, login, secure, or credentials). See Valid Accounts for more information.

# Mitigation

Establish an organizational policy that prohibits password storage in files. Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint systems or servers. Preemptively search for files containing passwords and remove when found. Restrict file shares to specific directories with access only to necessary users. Remove vulnerable Group Policy Preferences. [29]

# Footnotes

[1] CG. (2014, May 20). Mimikatz Against Virtual Machine Memory Part 1. Retrieved November 12, 2014.

[2] Security Research and Defense. (2014, May 13). MS14-025: An Update for Group Policy Preferences. Retrieved January 28, 2015.

[3] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[4] Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.

[5] F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.

[6] Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.

[7] US-CERT. (2018, July 20). Alert (TA18-201A) Emotet Malware. Retrieved March 25, 2019.

[8] CIS. (2018, December 12). MS-ISAC Security Primer- Emotet. Retrieved March 25, 2019.

[9] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[10] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[11] Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.

[12] Zanni, A. (n.d.). The LaZagne Project !!!. Retrieved December 14, 2018.

[13] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[14] Grafnetter, M. (2015, October 26). Retrieving DPAPI Backup Keys from Active Directory. Retrieved December 19, 2017.

[15] Symantec DeepSight Adversary Intelligence Team. (2018, December 10). Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms. Retrieved December 14, 2018.

[16] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[17] Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.

[18] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[19] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[20] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[21] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[22] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[23] Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.

[24] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[25] Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.

[26] Llimos, N., Pascual, C.. (2019, February 12). Trickbot Adds Remote Application Credential-Grabbing Capabilities to Its Repertoire. Retrieved March 12, 2019.

[27] Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.

[28] Belcher, P.. (2016, July 28). Tunnel of Gov: DNC Hack and the Russian XTunnel. Retrieved August 3, 2016.

[29] Microsoft. (2014, May 13). MS14-025: Vulnerability in Group Policy Preferences could allow elevation of privilege. Retrieved January 28, 2015.

## Defense

Establish an organizational policy that prohibits password storage in files. Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint sys

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (24)

- [[Active Directory Credential Dumping via Vssadmin]]
- [[AWS Metadata Credential Theft]]
- [[Azure Access Tokens and Service Principal Secrets in Azure CLI and PowerShell]]
- [[Dumping Active Directory Credentials via NTDS.dit File]]
- [[Dumping AD Domain Credentials using Esentutl.exe]]
- [[Enumerate a Git Repository for Secrets]]
- [[Github API Key Leakage]]
- [[Github API Key Leakage]]
- [[Github API Key Leakage]]
- [[Linux - Password Looting from Files]]
- [[Linux - Privilege Escalation: Looting for Old Passwords]]
- [[RODC Key List Extraction and Golden Ticket Creation]]
- [[Server Side Template Injection - Django Templates - Admin Credentials Leak]]
- [[Twitter Bearer Token Leak Exploitation]]
- [[Twitter Bearer Token Leak Exploitation]]
- [[Twitter Bearer Token Leak Exploitation]]
- [[Windows - Creating a PSCredential Object with a Secure Password]]
- [[Windows Credentials Decryption using Powershell Secure String]]
- [[Windows Elevation of Privilege - Looting WiFi Passwords]]
- [[Windows - EoP Looting for Passwords]]

*...and 4 more*
