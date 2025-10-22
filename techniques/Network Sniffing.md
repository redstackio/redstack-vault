---
id: 1fbd2060-4396-423c-8896-a1939d7be07b
name: Network Sniffing
type: technique
mitre_id: T1040
mitre_url: null
created_at: '2019-08-28T21:17:22.511551+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[Domain Trust Enumeration]]'
- '[[MSSQL Linked Database Crawler]]'
- '[[Network Packet Recording with Meterpreter]]'
- '[[Network Trace Capture]]'
- '[[Passive Network Traffic Fingerprinting]]'
- '[[Sniff Unencrypted LDAP Queries via the Loopback]]'
---

# Network Sniffing

**MITRE ID**: T1040

## Description

Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as LLMNR/NBT-NS Poisoning and Relay, can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.Network sniffing may also reveal configuration details, such as running services, version numbers, and other network characteristics (ex: IP addressing, hostnames, VLAN IDs) necessary for follow-on Lateral Movement and/or Defense Evasion activities.

# Detection

Detecting the events leading up to sniffing network traffic may be the best method of detection. From the host level, an adversary would likely need to perform a man-in-the-middle attack against other devices on a wired network in order to capture traffic that was not to or from the current compromised system. This change in the flow of information is detectable at the enclave network level. Monitor for ARP spoofing and gratuitous ARP broadcasts. Detecting compromised network devices is a bit more challenging. Auditing administrator logins, configuration changes, and device images is required to detect malicious changes.

# Mitigation

Ensure that all wireless traffic is encrypted appropriately. Use Kerberos, SSL, and multifactor authentication wherever possible. Monitor switches and network for span port usage, ARP/DNS poisoning, and router reconfiguration.

Identify and block potentially malicious software that may be used to sniff or analyze network traffic by using whitelisting [11] tools, like AppLocker, [12] [13] or Software Restriction Policies [14] where appropriate. [15]

# Footnotes

[1] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[2] Smith, L. and Read, B.. (2017, August 11). APT28 Targets Hospitality Sector, Presents Threat to Travelers. Retrieved August 17, 2017.

[3] Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.

[4] Salvio, J.. (2014, June 27). New Banking Malware Uses Network Sniffing for Data Theft. Retrieved March 25, 2019.

[5] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[6] SecureAuth. (n.d.).  Retrieved January 15, 2019.

[7] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[8] Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.

[9] Gaffie, L. (2016, August 25). Responder. Retrieved November 17, 2017.

[10] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[11] Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.

[12] Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.

[13] NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.

[14] Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved November 18, 2014.

[15] Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.

## Defense

Ensure that all wireless traffic is encrypted appropriately. Use Kerberos, SSL, and multifactor authentication wherever possible. Monitor switches and network for span port usage, ARP/DNS poisoning, and router reconfiguration.

Identify and block potentia

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

## Related Procedures (7)

- [[Disable LLMNR and NetBIOS over TCP/IP]]
- [[Domain Trust Enumeration]]
- [[MSSQL Linked Database Crawler]]
- [[Network Packet Recording with Meterpreter]]
- [[Network Trace Capture]]
- [[Passive Network Traffic Fingerprinting]]
- [[Sniff Unencrypted LDAP Queries via the Loopback]]
