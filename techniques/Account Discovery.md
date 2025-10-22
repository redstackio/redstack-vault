---
id: 6a5bd6c0-de19-4ab4-af27-0bff15d78f72
name: Account Discovery
type: technique
mitre_id: T1087
mitre_url: null
created_at: '2019-08-28T21:17:29.022476+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[AWS EKS Cluster Enumeration]]'
- '[[AWS Extract Backup to EC2 Instance]]'
- '[[AWS Extract Backup to EC2 Instance]]'
- '[[AWS IAM Group Enumeration]]'
- '[[AWS IAM List Access Keys]]'
- '[[AWS IAM User Group Enumeration]]'
- '[[AWS KMS Key Policy Listing]]'
- '[[AWS Managed Policy Version Enumeration]]'
- '[[AWS Privilege Escalation via Default Policy Information]]'
- '[[AWS Secrets Manager Enumeration]]'
- '[[Azure AD Connect Monitoring Disable and Password Reset]]'
- '[[Azure AD Enumeration with AzureAD Powershell (Creds)]]'
- '[[Azure Storage Blob Enumeration]]'
- '[[Azure Tenant Enumeration with Az PowerShell (Creds)]]'
- '[[Azure Tenant ID Enumeration]]'
- '[[Brute Force SMB Users Using RID (Authenticated)]]'
- '[[DPAPI Credential Theft with Hekatomb]]'
- '[[Enumerate Linux Privilege Escalation Paths (LinEnum)]]'
- '[[Enumerate Linux Privilege Escalation Paths (linPEAS)]]'
- '[[Enumerate Windows for Privilege Escalation (JAWS)]]'
- '[[Enumerate Windows for Privilege Escalation (PowerUp)]]'
- '[[Enumerate Windows for Privilege Escalation (SharpUp)]]'
- '[[Enumerate Windows for Privilege Escalation (winPEAS)]]'
- '[[GitLab Repository Enumeration and Search]]'
- '[[Kubernetes RBAC Listing Secrets]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[List All Active Directory Users]]'
- '[[Password Spraying with BadPwdCount Attribute Enumeration]]'
- '[[Query LDAP and Enumerate the Base DN (ldapsearch)]]'
- '[[Query MSSQL Server for Sysadmins]]'
- '[[RDS VPC Enumeration]]'
- '[[SID Enumeration and WMI Query for MS14-068 Checksum Validation]]'
- '[[SQL Server User Information Retrieval]]'
- '[[Windows - Credential Enumeration]]'
- '[[Windows User Enumeration and Privilege Escalation]]'
---

# Account Discovery

**MITRE ID**: T1087

## Description

Adversaries may attempt to get a listing of local system or domain accounts. WindowsExample commands that can acquire this information are net user, net group , and net localgroup  using the Net utility or through use of dsquery. If adversaries attempt to identify the primary user, currently logged in user, or set of users that commonly uses a system, System Owner/User Discovery may apply.MacOn Mac, groups can be enumerated through the groups and id commands. In mac specifically, dscl . list /Groups and dscacheutil -q group can also be used to enumerate groups and users.LinuxOn Linux, local users can be enumerated through the use of the /etc/passwd file which is world readable. In mac, this same file is only used in single-user mode in addition to the /etc/master.passwd file.Also, groups can be enumerated through the groups and id commands.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\EnumerateAdministrators. It can be disabled through GPO: Computer Configuration > [Policies] > Administrative Templates > Windows Components > Credential User Interface: E numerate administrator accounts on elevation. [41]

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about system and domain accounts, and audit and/or block them by using whitelisting [42] tools, like AppLocker, [43] [44] or Software Restriction Policies [45] where appropriate. [46]

# Footnotes

[1] FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.

[2] The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.

[3] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[4] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[5] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[6] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[7] Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.

[8] GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.

[9] Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.

[10] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[11] Microsoft. (n.d.). Dsquery. Retrieved April 18, 2016.

[12] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[13] Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.

[14] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[15] Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.

[16] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[17] F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.

[18] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[19] Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.

[20] Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.

[21] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[22] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[23] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[24] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[25] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[26] Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.

[27] Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.

[28] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[29] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[30] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[31] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[32] Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.

[33] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[34] Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.

[35] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[36] Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.

[37] Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.

[38] Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.

[39] Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.

[40] Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.

[41] UCF. (n.d.). The system must require username and password to elevate a running application.. Retrieved December 18, 2017.

[42] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[43] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[44] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[45] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[46] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located <code>HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\Enume

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (35)

- [[AWS EKS Cluster Enumeration]]
- [[AWS Extract Backup to EC2 Instance]]
- [[AWS Extract Backup to EC2 Instance]]
- [[AWS IAM Group Enumeration]]
- [[AWS IAM List Access Keys]]
- [[AWS IAM User Group Enumeration]]
- [[AWS KMS Key Policy Listing]]
- [[AWS Managed Policy Version Enumeration]]
- [[AWS Privilege Escalation via Default Policy Information]]
- [[AWS Secrets Manager Enumeration]]
- [[Azure AD Connect Monitoring Disable and Password Reset]]
- [[Azure AD Enumeration with AzureAD Powershell (Creds)]]
- [[Azure Storage Blob Enumeration]]
- [[Azure Tenant Enumeration with Az PowerShell (Creds)]]
- [[Azure Tenant ID Enumeration]]
- [[Brute Force SMB Users Using RID (Authenticated)]]
- [[DPAPI Credential Theft with Hekatomb]]
- [[Enumerate Linux Privilege Escalation Paths (LinEnum)]]
- [[Enumerate Linux Privilege Escalation Paths (linPEAS)]]
- [[Enumerate Windows for Privilege Escalation (JAWS)]]

*...and 15 more*
