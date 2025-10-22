---
id: 034c6eb4-0088-4e30-ae63-0147d0261710
name: Credential Dumping
type: technique
mitre_id: T1003
mitre_url: null
created_at: '2019-08-28T21:17:19.989914+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Active Directory Certificate Services ESC9 Attack]]'
- '[[Active Directory Credential Dumping via Vssadmin]]'
- '[[Active Directory Recon using BloodHound and Certipy]]'
- '[[Add DCSync Rights with WriteDACL Active Directory Permissions]]'
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[AWS EC2 IAM Instance Profile Enumeration]]'
- '[[AWS ECR Repository Enumeration]]'
- '[[AWS ECS Task Enumeration]]'
- '[[AWS Lambda Event Source Mapping Enumeration]]'
- '[[AWS Lambda Layer Enumeration]]'
- '[[Azure AD Connect - Password Extraction via AD Sync Account DCSync]]'
- '[[Azure Key Vault Access and Query with PowerShell]]'
- '[[Azure Pass The PRT with Mimikatz]]'
- '[[Azure Retrieving Passwords using Microburst]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
- '[[CCACHE Ticket Reuse from SSSD KCM and Android Devices]]'
- '[[Checksum Validation Exploitation for Active Directory]]'
- '[[CLR Assembly Creation and Execution]]'
- '[[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]'
- '[[Credential Harvesting from Task Scheduler using Mimikatz]]'
- '[[Credential Theft with Mimikatz and DPAPI]]'
- '[[DC PrintSpooler Service Check and ntlmrelayx with printerbug.py]]'
- '[[Decrypt a Cisco Type 7 Password]]'
- '[[Decrypt a Group Policy Preferences (GPP) Password]]'
- '[[DPAPI Credential Theft with Hekatomb]]'
- '[[Drop the MIC - Resource Based Constrained Delegation Attack]]'
- '[[Dump a Process''s Memory (cmd.exe)]]'
- '[[Dumping Active Directory Credentials via NTDS.dit File]]'
- '[[Dumping AD Domain Credentials using Mimikatz sekurlsa]]'
- '[[Dumping AD Domain Credentials using ndtsutil]]'
- '[[Dumping AD Domain Credentials using Vshadow]]'
- '[[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy,
  and CrackMapExec]]'
- '[[Dumping AD Domain Credentials via NTDS Reversible Encryption]]'
- '[[Dumping AD Domain Credentials with DiskShadow]]'
- '[[Dump Kerberos Tickets]]'
- '[[Dump Local Administrator Hash and Activate Password with DSRM Credentials]]'
- '[[Dump Secrets from a Remote System]]'
- '[[Encrypt a Cisco Type 7 Password]]'
- '[[Enumerate MSSQL Server Permissions]]'
- '[[Extract Chrome Cookies and Credentials from a User''s Profile with Domain Admin]]'
- '[[Extracting GMSA Passwords from Active Directory]]'
- '[[Extract LM/NTLM Hashes from SAM/SYSTEM Hives]]'
- '[[Forest to Forest Trust Ticket Hash Dump]]'
- '[[GraphQL Batching Attacks using finishChannelVerificationMutation]]'
- '[[HiveNightmare Password Looting]]'
- '[[Identify Encrypted Databases via MSSQL Server]]'
- '[[Impersonation Credential Check]]'
- '[[Kerberos Constrained Delegation - Identify Trusted Computers and Delegation Permissions]]'
- '[[Kerberos Unconstrained Delegation via SpoolService Abuse]]'
- '[[Kubernetes RBAC Listing Secrets]]'
- '[[LAPS Password Reader]]'
- '[[LAPS Password Retrieval]]'
- '[[Linux - In Memory Password Extraction]]'
- '[[List Credentials in Windows Credential Manager Vault]]'
- '[[List Windows Autologon Logon Credentials]]'
- '[[Mimikatz DCSync Password Retrieval]]'
- '[[Mimikatz LSA Protection Bypass]]'
- '[[Mimikatz Mini Dump Password Extraction]]'
- '[[Mimikatz RDP Password Extraction]]'
- '[[MS-EFSRPC Abuse with Unconstrained Delegation and PetitPotam Attack]]'
- '[[MSSQL List Columns Injection]]'
- '[[MYSQL Time Based Injection using SLEEP in a subselect]]'
- '[[Net-NTLMv1/NTLMv1 Hash Capture and Crack]]'
- '[[Net-NTLMv2/NTLMv2 Hash Capture and Cracking]]'
- '[[NTDS Database Dumping]]'
- '[[NTDS Hash Extraction]]'
- '[[NTDS Reversible Encryption Dumping]]'
- '[[Pass the Hash with Meterpreter]]'
- '[[Password in AD User Comment Enumeration]]'
- '[[Password of Pre-Created Computer Account Attack]]'
- '[[PXE Boot Image Attack - Local Admin Account Hijack]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[RDP Session Takeover with Mimikatz]]'
- '[[Remote DPAPI Credential Dumping with DonPAPI]]'
- '[[samAccountName Spoofing Attack]]'
- '[[samAccountName Spoofing Attack]]'
- '[[SAMAccountName Spoofing via SMB Credential Enumeration]]'
- '[[SCCM Network Access Account Credential Theft]]'
- '[[Shadow Credential Harvesting]]'
- '[[Skeleton Key Password Injection]]'
- '[[SMB Credential Testing with Crackmapexec]]'
- '[[SQL Server Database Name Retrieval]]'
- '[[Steal an NTLMv2 Hash with an SCF File and SMB]]'
- '[[Stealing Chrome Cookies and Credentials with Mimikatz]]'
- '[[Windows - Creating a PSCredential Object with a Secure Password]]'
- '[[Windows - Credential Enumeration]]'
- '[[Windows Credentials Impacket Commands]]'
- '[[Windows DPAPI Credential Files Enumeration]]'
- '[[Windows DPAPI Credential Theft]]'
- '[[Windows - Mimikatz Mini Dump]]'
- '[[Windows - Mimikatz Password Extraction]]'
- '[[Windows - Mimikatz Password Extraction]]'
- '[[Windows - Mimikatz RDP Password Extraction]]'
- '[[Windows Password and Credential Query via Registry]]'
- '[[Windows - Privilege Escalation: EoP Looting for Passwords (SessionGopher)]]'
- '[[Windows - SAM and SYSTEM Hash Extraction]]'
- '[[Windows Sandbox Credential Access]]'
- '[[Windows SSH with Kerberos Authentication]]'
- '[[Windows Unattend Password Extraction]]'
- '[[Windows - Using Impacket and PSExec with Credentials]]'
---

# Credential Dumping

**MITRE ID**: T1003

## Description

Credential dumping is the process of obtaining account login and password information, normally in the form of a hash or a clear text password, from the operating system and software. Credentials can then be used to perform Lateral Movement and access restricted information.Several of the tools mentioned in this technique may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.WindowsSAM (Security Accounts Manager)The SAM is a database file that contains local accounts for the host, typically those found with the ‘net user’ command. To enumerate the SAM database, system level access is required. A number of tools can be used to retrieve the SAM file through in-memory techniques:pwdumpx.exe gsecdumpMimikatzsecretsdump.pyAlternatively, the SAM can be extracted from the Registry with Reg:reg save HKLM\sam samreg save HKLM\system systemCreddump7 can then be used to process the SAM database locally to retrieve hashes. [1]Notes:Rid 500 account is the local, in-built administrator.Rid 501 is the guest account.User accounts start with a RID of 1,000+.Cached CredentialsThe DCC2 (Domain Cached Credentials version 2) hash, used by Windows Vista and newer caches credentials when the domain controller is unavailable. The number of default cached credentials varies, and this number can be altered per system. This hash does not allow pass-the-hash style attacks. A number of tools can be used to retrieve the SAM file through in-memory techniques.pwdumpx.exe gsecdumpMimikatzAlternatively, reg.exe can be used to extract from the Registry and Creddump7 used to gather the credentials.Notes:Cached credentials for Windows Vista are derived using PBKDF2.Local Security Authority (LSA) SecretsWith SYSTEM access to a host, the LSA secrets often allows trivial access from a local account to domain-based account credentials. The Registry is used to store the LSA secrets. When services are run under the context of local or domain users, their passwords are stored in the Registry. If auto-logon is enabled, this information will be stored in the Registry as well. A number of tools can be used to retrieve the SAM file through in-memory techniques.pwdumpx.exe gsecdumpMimikatzsecretsdump.pyAlternatively, reg.exe can be used to extract from the Registry and Creddump7 used to gather the credentials.Notes:The passwords extracted by his mechanism are UTF-16 encoded, which means that they are returned in plaintext.Windows 10 adds protections for LSA Secrets described in Mitigation.NTDS from Domain ControllerActive Directory stores information about members of the domain including devices and users to verify credentials and define access rights. The Active Directory domain database is stored in the NTDS.dit file. By default the NTDS file will be located in %SystemRoot%\NTDS\Ntds.dit of a domain controller. [2]The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes.Volume Shadow Copysecretsdump.pyUsing the in-built Windows tool, ntdsutil.exeInvoke-NinjaCopyGroup Policy Preference (GPP) FilesGroup Policy Preferences (GPP) are tools that allowed administrators to create domain policies with embedded credentials. These policies, amongst other things, allow administrators to set local accounts.These group policies are stored in SYSVOL on a domain controller, this means that any domain user can view the SYSVOL share and decrypt the password (the AES private key was leaked on-line. [3] [4]The following tools and scripts can be used to gather and decrypt the password file from Group Policy Preference XML files:Metasploit’s post exploitation module: "post/windows/gather/credentials/gpp"Get-GPPPassword [5]gpprefdecrypt.pyNotes:On the SYSVOL share, the following can be used to enumerate potential XML files.dir /s * .xmlService Principal Names (SPNs)See Kerberoasting.Plaintext CredentialsAfter a user logs on to a system, a variety of credentials are generated and stored in the Local Security Authority Subsystem Service (LSASS) process in memory. These credentials can be harvested by a administrative user or SYSTEM.SSPI (Security Support Provider Interface) functions as a common interface to several Security Support Providers (SSPs): A Security Support Provider is a dynamic-link library (DLL) that makes one or more security packages available to applications.The following SSPs can be used to access credentials:Msv: Interactive logons, batch logons, and service logons are done through the MSV authentication package.Wdigest: The Digest Authentication protocol is designed for use with Hypertext Transfer Protocol (HTTP) and Simple Authentication Security Layer (SASL) exchanges. [6]Kerberos: Preferred for mutual client-server domain authentication in Windows 2000 and later.CredSSP:  Provides SSO and Network Level Authentication for Remote Desktop Services. [7] The following tools can be used to enumerate credentials:Windows Credential EditorMimikatzAs well as in-memory techniques, the LSASS process memory can be dumped from the target host and analyzed on a local system.For example, on the target host use procdump:procdump -ma lsass.exe lsass_dumpLocally, mimikatz can be run:sekurlsa::Minidump lsassdump.dmpsekurlsa::logonPasswordsDCSyncDCSync is a variation on credential dumping which can be used to acquire sensitive information from a domain controller. Rather than executing recognizable malicious code, the action works by abusing the domain controller's  application programming interface (API) [8] [9] [10] [11] to simulate the replication process from a remote domain controller. Any members of the Administrators, Domain Admins, Enterprise Admin groups or computer accounts on the domain controller are able to run DCSync to pull password data [12] from Active Directory, which may include current and historical hashes of potentially useful accounts such as KRBTGT and Administrators. The hashes can then in turn be used to create a Golden Ticket for use in Pass the Ticket [13] or change an account's password as noted in Account Manipulation. [14] DCSync functionality has been included in the "lsadump" module in Mimikatz. [15] Lsadump also includes NetSync, which performs DCSync over a legacy replication protocol. [16]LinuxProc filesystemThe /proc filesystem on Linux contains a great deal of information regarding the state of the running operating system. Processes running with root privileges can use this facility to scrape live memory of other running programs. If any of these programs store passwords in clear text or password hashes in memory, these values can then be harvested for either usage or brute force attacks, respectively. This functionality has been implemented in the MimiPenguin, an open source tool inspired by Mimikatz. The tool dumps process memory, then harvests passwords and hashes by looking for text strings and regex patterns for how given applications such as Gnome Keyring, sshd, and Apache use memory to store such authentication artifacts.

# Detection

Windows

Common credential dumpers such as Mimikatz access the LSA Subsystem Service (LSASS) process by opening the process, locating the LSA secrets key, and decrypting the sections in memory where credential details are stored. Credential dumpers may also use methods for reflective Process Injection to reduce potential indicators of malicious activity.

Hash dumpers open the Security Accounts Manager (SAM) on the local file system (%SystemRoot%/system32/config/SAM) or create a dump of the Registry SAM key to access stored account password hashes. Some hash dumpers will open the local file system as a device and parse to the SAM table to avoid file access defenses. Others will make an in-memory copy of the SAM table before reading hashes. Detection of compromised Valid Accounts in-use by adversaries may help as well. 

On Windows 8.1 and Windows Server 2012 R2, monitor Windows Logs for LSASS.exe creation to verify that LSASS started as a protected process.

Monitor processes and command-line arguments for program execution that may be indicative of credential dumping. Remote access tools may contain built-in features or incorporate existing tools like Mimikatz. PowerShell scripts also exist that contain credential dumping functionality, such as PowerSploit's Invoke-Mimikatz module, [118] which may require additional logging features to be configured in the operating system to collect necessary information for analysis.

Monitor domain controller logs for replication requests and other unscheduled activity possibly associated with DCSync. [8] [9] [10] Note: Domain controllers may not log replication requests originating from the default domain controller account. [119]. Also monitor for network protocols  [8] [16] and other replication requests [120] from IPs not associated with known domain controllers. [115]

Linux

To obtain the passwords and hashes stored in memory, processes must open a maps file in the /proc filesystem for the process being analyzed. This file is stored under the path /proc//maps, where the  directory is the unique pid of the program being interrogated for such authentication data. The AuditD monitoring tool, which ships stock in many Linux distributions, can be used to watch for hostile processes opening this file in the proc file system, alerting on the pid, process name, and arguments of such programs.

# Mitigation

Windows

Monitor/harden access to LSASS and SAM table with tools that allow process whitelisting. Limit credential overlap across systems to prevent lateral movement opportunities using Valid Accounts if passwords and hashes are obtained. Ensure that local administrator accounts have complex, unique passwords across all systems on the network. Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled, as this is often equivalent to having a local administrator account with the same password on all systems. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [106]

On Windows 8.1 and Windows Server 2012 R2, enable Protected Process Light for LSA. [107]

Identify and block potentially malicious software that may be used to dump credentials by using whitelisting [108] tools, like AppLocker, [109] [110] or Software Restriction Policies [111] where appropriate. [112]

With Windows 10, Microsoft implemented new protections called Credential Guard to protect the LSA secrets that can be used to obtain credentials through forms of credential dumping. It is not configured by default and has hardware and firmware system requirements. [113] It also does not protect against all forms of credential dumping. [114]

Manage the access control list for "Replicating Directory Changes" and other permissions associated with domain controller replication. [115] [116]

Consider disabling or restricting NTLM traffic. [117]

Linux

Scraping the passwords from memory requires root privileges. Follow best practices in restricting access to escalated privileges to avoid hostile programs from accessing such sensitive regions of memory.

# Footnotes

[1] Flathers, R. (2018, February 19). creddump7. Retrieved April 11, 2018.

[2] Wikipedia. (2018, March 10). Active Directory. Retrieved April 11, 2018.

[3] Microsoft. (n.d.). 2.2.1.1.4 Password Encryption. Retrieved April 11, 2018.

[4] Security Research and Defense. (2014, May 13). MS14-025: An Update for Group Policy Preferences. Retrieved January 28, 2015.

[5] Campbell, C. (2012, May 24). GPP Password Retrieval with PowerShell. Retrieved April 11, 2018.

[6] Wilson, B. (2016, April 18). The Importance of KB2871997 and KB2928120 for Credential Protection. Retrieved April 11, 2018.

[7] Microsoft. (2008, July 25). Credential Security Service Provider and SSO for Terminal Services Logon. Retrieved April 11, 2018.

[8] Microsoft. (2017, December 1). MS-DRSR Directory Replication Service (DRS) Remote Protocol. Retrieved December 4, 2017.

[9] Microsoft. (n.d.). IDL_DRSGetNCChanges (Opnum 3). Retrieved December 4, 2017.

[10] SambaWiki. (n.d.). DRSUAPI. Retrieved December 4, 2017.

[11] Wine API. (n.d.). samlib.dll. Retrieved December 4, 2017.

[12] Metcalf, S. (2015, September 25). Mimikatz DCSync Usage, Exploitation, and Detection. Retrieved August 7, 2017.

[13] Schroeder, W. (2015, September 22). Mimikatz and DCSync and ExtraSids, Oh My. Retrieved August 7, 2017.

[14] Warren, J. (2017, July 11). Manipulating User Passwords with Mimikatz. Retrieved December 4, 2017.

[15] Deply, B., Le Toux, V. (2016, June 5). module ~ lsadump. Retrieved August 7, 2017.

[16] Microsoft. (2017, December 1). MS-NRPC - Netlogon Remote Protocol. Retrieved December 6, 2017.

[17] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[18] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[19] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[20] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[21] Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.

[22] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[23] Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.

[24] Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.

[25] FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved March 1, 2018.

[26] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[27] Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.

[28] Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.

[29] Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.

[30] Symantec Security Response. (2014, July 7). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.

[31] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[32] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[33] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[34] Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.

[35] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[36] F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.

[37] F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.

[38] Huss, D.. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.

[39] DiMaggio, J. (2016, April 28). Tick cyberespionage group zeros in on Japan. Retrieved July 16, 2018.

[40] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[41] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[42] Core Security. (n.d.). Impacket. Retrieved November 2, 2017.

[43] Trend Micro. (2019, January 16). Exploring Emotet's Activities . Retrieved March 25, 2019.

[44] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[45] Higgins, K. (2015, October 13). Prolific Cybercrime Gang Favors Legit Login Credentials. Retrieved October 4, 2017.

[46] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[47] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[48] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[49] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[50] Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.

[51] TrueSec. (n.d.). gsecdump v2.0b5. Retrieved September 29, 2015.

[52] Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved September 26, 2016.

[53] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[54] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[55] SecureAuth. (n.d.).  Retrieved January 15, 2019.

[56] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[57] Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.

[58] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[59] Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.

[60] Zanni, A. (n.d.). The LaZagne Project !!!. Retrieved December 14, 2018.

[61] Kálnai, P., Cherepanov A. (2018, April 03). Lazarus KillDisks Central American casino. Retrieved May 17, 2018.

[62] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[63] Plan, F., et all. (2019, March 4). APT40: Examining a China-Nexus Espionage Actor. Retrieved March 18, 2019.

[64] Mandiant. (2018). Mandiant M-Trends 2018. Retrieved July 9, 2018.

[65] ClearSky Cyber Security and Trend Micro. (2017, July). Operation Wilted Tulip: Exposing a cyber espionage apparatus. Retrieved August 21, 2017.

[66] Minerva Labs LTD and ClearSky Cyber Security. (2015, November 23). CopyKittens Attack Group. Retrieved September 11, 2017.

[67] Twi1ight. (2015, July 11). AD-Pentest-Script - wmiexec.vbs. Retrieved June 29, 2017.

[68] Deply, B. (n.d.). Mimikatz. Retrieved September 29, 2015.

[69] Grafnetter, M. (2015, October 26). Retrieving DPAPI Backup Keys from Active Directory. Retrieved December 19, 2017.

[70] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[71] Gregal, H. (2017, May 12). MimiPenguin. Retrieved December 5, 2017.

[72] Stama, D.. (2015, February 6). Backdoor.Mivast. Retrieved February 15, 2016.

[73] ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.

[74] Lancaster, T.. (2017, November 14). Muddying the Water: Targeted Attacks in the Middle East. Retrieved March 15, 2018.

[75] Symantec DeepSight Adversary Intelligence Team. (2018, December 10). Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms. Retrieved December 14, 2018.

[76] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[77] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[78] US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.

[79] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[80] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[81] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[82] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[83] Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved August 3, 2016.

[84] Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.

[85] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[86] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[87] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[88] Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.

[89] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[90] Wikipedia. (1985, June 22). pwdump. Retrieved June 22, 2016.

[91] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[92] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[93] Accenture Security. (2018, April 23). Hogfish Redleaves Campaign. Retrieved July 2, 2018.

[94] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[95] Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.

[96] Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.

[97] Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.

[98] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[99] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 17, 2016.

[100] DiMaggio, J.. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.

[101] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[102] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[103] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[104] Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.

[105] Amplia Security. (n.d.). Windows Credentials Editor (WCE) F.A.Q.. Retrieved December 17, 2015.

[106] Plett, C., Poggemeyer, L. (12, October 26). Securing Privileged Access Reference Material. Retrieved April 25, 2017.

[107] Microsoft. (2013, July 31). Configuring Additional LSA Protection. Retrieved February 13, 2015.

[108] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[109] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[110] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[111] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[112] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

[113] Lich, B. (2016, May 31). Protect derived domain credentials with Credential Guard. Retrieved June 1, 2016.

[114] NSA IAD. (2017, April 20). Secure Host Baseline - Credential Guard. Retrieved April 25, 2017.

[115] Metcalf, S. (2015, September 25). Mimikatz DCSync Usage, Exploitation, and Detection. Retrieved December 4, 2017.

[116] Microsoft. (n.d.). How to grant the "Replicating Directory Changes" permission for the Microsoft Metadirectory Services ADMA service account. Retrieved December 4, 2017.

[117] Microsoft. (2012, November 29). Using security policies to restrict NTLM traffic. Retrieved December 4, 2017.

[118] PowerSploit. (n.d.). Retrieved December 4, 2014.

[119] Schroeder, W. (2015, September 22). Mimikatz and DCSync and ExtraSids, Oh My. Retrieved December 4, 2017.

[120] Microsoft. (n.d.). MS-SAMR Security Account Manager (SAM) Remote Protocol (Client-to-Server) - Transport. Retrieved December 4, 2017.

## Defense

### Windows
Monitor/harden access to LSASS and SAM table with tools that allow process whitelisting. Limit credential overlap across systems to prevent lateral movement opportunities using [Valid Accounts](https://attack.mitre.org/techniques/T1078) if pas

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (100)

- [[Active Directory Certificate Services ESC9 Attack]]
- [[Active Directory Credential Dumping via Vssadmin]]
- [[Active Directory Recon using BloodHound and Certipy]]
- [[Add DCSync Rights with WriteDACL Active Directory Permissions]]
- [[Automated Password Extraction from SYSVOL and Group Policy Preferences]]
- [[AWS EC2 IAM Instance Profile Enumeration]]
- [[AWS ECR Repository Enumeration]]
- [[AWS ECS Task Enumeration]]
- [[AWS Lambda Event Source Mapping Enumeration]]
- [[AWS Lambda Layer Enumeration]]
- [[Azure AD Connect - Password Extraction via AD Sync Account DCSync]]
- [[Azure Key Vault Access and Query with PowerShell]]
- [[Azure Pass The PRT with Mimikatz]]
- [[Azure Retrieving Passwords using Microburst]]
- [[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]
- [[CCACHE Ticket Reuse from SSSD KCM and Android Devices]]
- [[Checksum Validation Exploitation for Active Directory]]
- [[CLR Assembly Creation and Execution]]
- [[Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz]]
- [[Credential Harvesting from Task Scheduler using Mimikatz]]

*...and 80 more*
