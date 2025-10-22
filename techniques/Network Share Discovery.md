---
id: 15e07a5d-5170-4107-9656-834da32d0591
name: Network Share Discovery
type: technique
mitre_id: T1135
mitre_url: null
created_at: '2019-08-28T21:17:43.581909+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory SCCM Loot Inventory and Download]]'
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[AWS SSRF Credential Access via Lambda Function]]'
- '[[Cloud Instance SSRF]]'
- '[[List NFS Shares]]'
- '[[List SMB Shares]]'
- '[[Mount a Windows CIFS Share]]'
- '[[Open Shares Enumeration]]'
- '[[SSRF Filter Bypass using IP Address Retrieval]]'
- '[[SSRF for Cloud Instances with Packet Metadata Userdata]]'
- '[[SSRF through File Integration as an Image or Text]]'
- '[[SSRF via XXE Injection]]'
- '[[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]'
- '[[Windows - Network Enumeration for Privilege Escalation]]'
- '[[XXE Injection via SVG Image]]'
---

# Network Share Discovery

**MITRE ID**: T1135

## Description

Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. WindowsFile sharing over a Windows network occurs over the SMB protocol. [1] [2]Net can be used to query a remote system for available shared drives using the net view \remotesystem command. It can also be used to query shared drives on the local system using net share.Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement.MacOn Mac, locally mounted shares can be viewed with the df -aH command.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events related to legitimate remote system discovery may be uncommon, depending on the environment and how they are used. Monitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.

# Mitigation

Identify unnecessary system utilities or potentially malicious software that may be used to acquire network share information, and audit and/or block them by using whitelisting [19] tools, like AppLocker, [20] [21] or Software Restriction Policies [22] where appropriate. [23]

# Footnotes

[1] Wikipedia. (2017, April 15). Shared resource. Retrieved June 30, 2017.

[2] Microsoft. (n.d.). Share a Folder or Drive. Retrieved June 30, 2017.

[3] Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.

[4] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[5] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[6] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[7] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[8] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[9] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[10] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[11] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[12] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[13] Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.

[14] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[15] Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.

[16] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[17] Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.

[18] Kaspersky Lab's Global Research & Analysis Team. (2018, February 20). A Slice of 2017 Sofacy Activity. Retrieved November 27, 2018.

[19] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[20] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[21] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[22] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[23] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Identify unnecessary system utilities or potentially malicious software that may be used to acquire network share information, and audit and/or block them by using whitelisting (Citation: Beechey 2010) tools, like AppLocker, (Citation: Windows Commands JP

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (15)

- [[Active Directory SCCM Loot Inventory and Download]]
- [[Automated Password Extraction from SYSVOL and Group Policy Preferences]]
- [[AWS SSRF Credential Access via Lambda Function]]
- [[Cloud Instance SSRF]]
- [[List NFS Shares]]
- [[List SMB Shares]]
- [[Mount a Windows CIFS Share]]
- [[Open Shares Enumeration]]
- [[SSRF Filter Bypass using IP Address Retrieval]]
- [[SSRF for Cloud Instances with Packet Metadata Userdata]]
- [[SSRF through File Integration as an Image or Text]]
- [[SSRF via XXE Injection]]
- [[Windows Local DTD and Side Channel Leak to Disclose HTTP Response/File Contents]]
- [[Windows - Network Enumeration for Privilege Escalation]]
- [[XXE Injection via SVG Image]]
