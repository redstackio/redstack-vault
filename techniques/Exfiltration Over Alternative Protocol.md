---
id: ed641c19-3e6d-4c54-a249-a05a44968c1e
name: Exfiltration Over Alternative Protocol
type: technique
mitre_id: T1048
mitre_url: null
created_at: '2019-08-28T21:17:35.228019+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[AWS KMS Decrypt Exfiltration]]'
- '[[AWS S3 Download by Authenticated User]]'
- '[[AWS S3 Secret Text Retrieval - Public Access Data Exfiltration]]'
- '[[AWS S3 Time-Based URL Exfiltration]]'
- '[[AWS Secrets Manager Credential Exfiltration]]'
- '[[Azure Storage Blob Download]]'
- '[[Blind XSS Data Exfiltration]]'
- '[[Blind XXE Data Exfiltration via OOB Attack]]'
- '[[Blind XXE Out-of-Band Data Exfiltration]]'
- '[[Cobalt Strike VPN & Pivots]]'
- '[[Create a Windows SMB Share with PowerShell]]'
- '[[DNS Data Exfiltration with Command Injection]]'
- '[[Download all files from Amazon S3 Bucket]]'
- '[[Download all files from Amazon S3 Bucket]]'
- '[[Download Files and Folders Recursively from FTP]]'
- '[[Exfiltrate Data Using Ping]]'
- '[[File Retrieval via XXE Injection]]'
- '[[IAM-Based Authentication Data Exfiltration via RDS]]'
- '[[IAM-Based Authentication for RDS MySQL Database]]'
- '[[Mercurial Source Code Extraction with rip-hg.pl]]'
- '[[Mount a Windows SMB Share with PowerShell (Authenticated)]]'
- '[[MSSQL Out of Band DNS Exfiltration]]'
- '[[MSSQL UNC Path Out-of-Band Data Retrieval]]'
- '[[MYSQL Injection Out-of-Band Data Exfiltration]]'
- '[[MYSQL Injection with Out of Band DNS Exfiltration]]'
- '[[Portforwarding with Meterpreter]]'
- '[[RDS Password-based Authentication Data Exfiltration]]'
- '[[Remote File Read via Jinja2 Server-Side Template Injection]]'
- '[[XXE Injection in SOAP Messages]]'
---

# Exfiltration Over Alternative Protocol

**MITRE ID**: T1048

## Description

Data exfiltration is performed with a different protocol from the main command and control protocol or channel. The data is likely to be sent to an alternate network location from the main command and control server. Alternate protocols include FTP, SMTP, HTTP/S, DNS, or some other network protocol. Different channels could include Internet Web services such as cloud storage.

# Detection

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [18]

# Mitigation

Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network. For example, if services like FTP are not required for sending information outside of a network, then block FTP-related ports at the network perimeter. Enforce proxies and use dedicated servers for services such as DNS and only allow those systems to communicate over respective ports/protocols, instead of all systems within a network. [17] These actions will help reduce command and control and exfiltration path opportunities.

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [18]

# Footnotes

[1] Brumaghin, E., et al. (2018, October 15). Old dog, new tricks - Analysing new RTF-based campaign distributing Agent Tesla, Loki with PyREbox. Retrieved November 5, 2018.

[2] Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.

[3] Microsoft. (n.d.). BITSAdmin Tool. Retrieved January 12, 2018.

[4] ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.

[5] Merritt, E.. (2015, November 16). Shining the Spotlight on Cherry Picker PoS Malware. Retrieved April 20, 2016.

[6] F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.

[7] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[8] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[9] Wikipedia. (2016, June 15). File Transfer Protocol. Retrieved July 20, 2016.

[10] FireEye Labs. (2015, July). HAMMERTOSS: Stealthy Tactics Define a Russian Cyber Threat Group. Retrieved September 17, 2015.

[11] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[12] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[13] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.

[14] Grunzweig, J. and Falcone, R.. (2016, October 4). OilRig Malware Campaign Updates Toolset and Expands Targets. Retrieved May 3, 2017.

[15] Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 17, 2016.

[16] Security Response Attack Investigation Team. (2018, June 19). Thrip: Espionage Group Hits Satellite, Telecoms, and Defense Companies. Retrieved July 10, 2018.

[17] Microsoft. (2004, February 6). Perimeter Firewall Design. Retrieved April 25, 2016.

[18] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network. For example, if services like FTP are not required for sending information outside of a network, then block FTP-related port

## Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures (29)

- [[AWS KMS Decrypt Exfiltration]]
- [[AWS S3 Download by Authenticated User]]
- [[AWS S3 Secret Text Retrieval - Public Access Data Exfiltration]]
- [[AWS S3 Time-Based URL Exfiltration]]
- [[AWS Secrets Manager Credential Exfiltration]]
- [[Azure Storage Blob Download]]
- [[Blind XSS Data Exfiltration]]
- [[Blind XXE Data Exfiltration via OOB Attack]]
- [[Blind XXE Out-of-Band Data Exfiltration]]
- [[Cobalt Strike VPN & Pivots]]
- [[Create a Windows SMB Share with PowerShell]]
- [[DNS Data Exfiltration with Command Injection]]
- [[Download all files from Amazon S3 Bucket]]
- [[Download all files from Amazon S3 Bucket]]
- [[Download Files and Folders Recursively from FTP]]
- [[Exfiltrate Data Using Ping]]
- [[File Retrieval via XXE Injection]]
- [[IAM-Based Authentication Data Exfiltration via RDS]]
- [[IAM-Based Authentication for RDS MySQL Database]]
- [[Mercurial Source Code Extraction with rip-hg.pl]]

*...and 9 more*
