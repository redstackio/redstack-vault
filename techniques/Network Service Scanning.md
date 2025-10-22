---
id: cf59831c-c448-478b-957a-6313c17154c0
name: Network Service Scanning
type: technique
mitre_id: T1046
mitre_url: null
created_at: '2019-08-28T21:17:22.209656+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory Recon using BloodHound and Certipy]]'
- '[[Azure AD Connect Sync Connector Check]]'
- '[[Azure AD Endpoint Enumeration]]'
- '[[Basic Nmap Scan Procedure]]'
- '[[Basic Port Scan and Scripted Service Enumeration]]'
- '[[Basic Port Scan with Aggressive Service Enumeration]]'
- '[[Basic Port Scan with Service Enumeration]]'
- '[[Bettercap Proxy Spoofing Procedure]]'
- '[[Brute Force Virtual Host Domains (Gobuster)]]'
- '[[Brute Force Virtual Host Domains (Wfuzz)]]'
- '[[Docker API Port Scanning and Container Management]]'
- '[[Domain Trust Enumeration]]'
- '[[Dynamic Group Membership and Guest Vendor Email Rule]]'
- '[[Enumerate an SNMP Server (Authenticated)]]'
- '[[Enumerate Windows Samba Services]]'
- '[[Filter Bypass for Server-Side Request Forgery using URL Port Scanner]]'
- '[[Linked Database Crawling for MSSQL Server Enumeration]]'
- '[[MSSQL Database Enumeration]]'
- '[[MSSQL Instance Discovery]]'
- '[[MSSQL Linked Database Crawler]]'
- '[[MSSQL Server Linked Database Enumeration]]'
- '[[Netdiscover Network Discovery]]'
- '[[Network Discovery using Nmap]]'
- '[[Network Discovery with Masscan]]'
- '[[Network Discovery with Nmap]]'
- '[[Network Discovery with Nmap]]'
- '[[Network Discovery with Nmap Full Scan]]'
- '[[Network Discovery with Nmap Scripting Engine]]'
- '[[Network Discovery with Nmap Service Version Detection]]'
- '[[Network Reconnaissance Procedure]]'
- '[[Octal IP Format Server-Side Request Forgery]]'
- '[[Port Scan All TCP Ports with FIN Bit Set]]'
- '[[Port Scan with Vulnerability Enumeration]]'
- '[[Problematic Host Port Scan with Basic Enumeration]]'
- '[[RDS Enumeration: Listing Routing Tables]]'
- '[[RDS Enumeration - Listing VPCs in us-west-1 region]]'
- '[[RDS Lateral Movement via VPC Peering Connections]]'
- '[[RDS Network ACL Enumeration]]'
- '[[RDS Security Group Enumeration]]'
- '[[RDS Subnet Enumeration]]'
- '[[RDS Subnet Group Enumeration]]'
- '[[Scan Ports for Services with No Host Discovery]]'
---

# Network Service Scanning

**MITRE ID**: T1046

## Description

Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information include port scans and vulnerability scans using tools that are brought onto a system.

# Detection

System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as Lateral Movement, based on the information obtained.

Normal, benign system and network events from legitimate remote service scanning may be uncommon, depending on the environment and how they are used. Legitimate open port and vulnerability scanning may be conducted within the environment and will need to be deconflicted with any detection capabilities developed. Network intrusion detection systems can also be used to identify scanning activity. Monitor for process use of the networks and inspect intra-network flows to detect port scans.

# Mitigation

Use network intrusion detection/prevention systems to detect and prevent remote service scans. Ensure that unnecessary ports and services are closed and proper network segmentation is followed to protect critical servers and devices.

Identify unnecessary system utilities or potentially malicious software that may be used to acquire information about services running on remote systems, and audit and/or block them by using whitelisting [24] tools, like AppLocker, [25] [26] or Software Restriction Policies [27] where appropriate. [28]

# Footnotes

[1] Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.

[2] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[3] Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.

[4] FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.

[5] Positive Technologies. (2017, August 16). Cobalt Strikes Back: An Evolving Multinational Threat to Finance. Retrieved September 5, 2018.

[6] Positive Technologies. (2016, December 16). Cobalt Snatch. Retrieved October 9, 2018.

[7] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[8] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[9] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[10] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[11] Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.

[12] Magius, J., et al. (2017, July 19). Koadic. Retrieved June 18, 2018.

[13] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[14] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[15] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[16] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[17] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[18] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.

[19] Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.

[20] DiMaggio, J.. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.

[21] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[22] Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.

[23] Belcher, P.. (2016, July 28). Tunnel of Gov: DNC Hack and the Russian XTunnel. Retrieved August 3, 2016.

[24] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[25] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[26] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[27] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[28] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Use network intrusion detection/prevention systems to detect and prevent remote service scans. Ensure that unnecessary ports and services are closed and proper network segmentation is followed to protect critical servers and devices.

Identify unnecessary

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (42)

- [[Active Directory Recon using BloodHound and Certipy]]
- [[Azure AD Connect Sync Connector Check]]
- [[Azure AD Endpoint Enumeration]]
- [[Basic Nmap Scan Procedure]]
- [[Basic Port Scan and Scripted Service Enumeration]]
- [[Basic Port Scan with Aggressive Service Enumeration]]
- [[Basic Port Scan with Service Enumeration]]
- [[Bettercap Proxy Spoofing Procedure]]
- [[Brute Force Virtual Host Domains (Gobuster)]]
- [[Brute Force Virtual Host Domains (Wfuzz)]]
- [[Docker API Port Scanning and Container Management]]
- [[Domain Trust Enumeration]]
- [[Dynamic Group Membership and Guest Vendor Email Rule]]
- [[Enumerate an SNMP Server (Authenticated)]]
- [[Enumerate Windows Samba Services]]
- [[Filter Bypass for Server-Side Request Forgery using URL Port Scanner]]
- [[Linked Database Crawling for MSSQL Server Enumeration]]
- [[MSSQL Database Enumeration]]
- [[MSSQL Instance Discovery]]
- [[MSSQL Linked Database Crawler]]

*...and 22 more*
