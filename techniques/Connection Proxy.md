---
id: 0de9a563-3f4f-4c23-bcc3-70974e21e953
name: Connection Proxy
type: technique
mitre_id: T1090
mitre_url: null
created_at: '2019-08-28T21:17:35.688299+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Azure AD Connect PTA Backdoor Installation and Log Retrieval]]'
- '[[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]'
- '[[Cobalt Strike Malleable C2 Profile Checking]]'
- '[[Dynamic Port Forwarding with an SSH SOCKS Proxy]]'
- '[[Filter Bypass using Alternate Redirects]]'
- '[[LFI to RCE via Apache and Nginx Log Files]]'
- '[[Metasploit Network Pivoting with Meterpreter Port Forwarding and Routing]]'
- '[[Meterpreter SOCKS Proxy]]'
- '[[Network Pivoting with Proxychains]]'
- '[[Network Pivoting with sshuttle]]'
- '[[ngrok Port Forwarding]]'
- '[[RDS Routing Tables Destination and Target Rules]]'
- '[[Remote Port Forwarding Over HTTP Proxy]]'
- '[[Remote Port Forwarding with Reverse SSH Tunneling]]'
- '[[Reverse Socks Proxy Pivoting]]'
- '[[Rpivot - Network Pivoting Techniques]]'
- '[[Server-Side Request Forgery via Bypassing Filters with HTTPS]]'
- '[[SQL Injection WAF Bypass using MySQL Specific Commands]]'
- '[[SSH Local Port Forwarding]]'
- '[[SSH Port Forwarding with an Isolated Host]]'
- '[[SSH Tunneling and SOCKS Proxy]]'
- '[[Web SOCKS Pivoting with Pivotnacci]]'
---

# Connection Proxy

**MITRE ID**: T1090

## Description

A connection proxy is used to direct network traffic between systems or act as an intermediary for network communications. Many tools exist that enable traffic redirection through proxies or port redirection, including HTRAN, ZXProxy, and ZXPortMap. [1]The definition of a proxy can also be expanded out to encompass trust relationships between networks in peer-to-peer, mesh, or trusted connections between networks consisting of hosts or systems that regularly communicate with each other.The network may be within a single organization or across organizations with trust relationships. Adversaries could use these types of relationships to manage command and control communications, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between victims to avoid suspicion.

# Detection

Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Network activities disassociated from user-driven actions from processes that normally require user direction are suspicious.

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server or between clients that should not or often do not communicate with one another). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect communications that do not follow the expected protocol behavior for the port that is being used. [38]

# Mitigation

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific C2 protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [38]

# Footnotes

[1] Wilhoit, K. (2013, March 4). In-Depth Look: APT Attack Tools of the Trade. Retrieved December 2, 2015.

[2] FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.

[3] Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.

[4] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[5] Moran, N., et al. (2014, November 21). Operation Double Tap. Retrieved January 14, 2016.

[6] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[7] Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.

[8] FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved May 1, 2015.

[9] US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.

[10] Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.

[11] ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.

[12] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[13] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[14] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[15] ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.

[16] US-CERT. (2018, February 05). Malware Analysis Report (MAR) - 10135536-F. Retrieved June 11, 2018.

[17] Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.

[18] US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.

[19] Haq, T., Moran, N., Vashisht, S., Scott, M. (2014, September). OPERATION QUANTUM ENTANGLEMENT. Retrieved November 4, 2015.

[20] The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.

[21] Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.

[22] Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.

[23] US-CERT. (2017, November 22). Alert (TA17-318A): HIDDEN COBRA – North Korean Remote Administration Tool: FALLCHILL. Retrieved December 7, 2017.

[24] FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.

[25] Symantec DeepSight Adversary Intelligence Team. (2018, December 10). Seedworm: Group Compromises Government Agencies, Oil & Gas, NGOs, Telecoms, and IT Firms. Retrieved December 14, 2018.

[26] Kaspersky Lab's Global Research and Analysis Team. (2017, February 8). Fileless attacks against enterprise networks. Retrieved February 8, 2017.

[27] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[28] Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.

[29] MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.

[30] Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.

[31] Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.

[32] Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.

[33] Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.

[34] Kaspersky Lab's Global Research & Analysis Team. (2016, August 8). ProjectSauron: top level cyber-espionage platform covertly extracts encrypted government comms. Retrieved August 17, 2016.

[35] US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.

[36] Zhou, R. (2012, May 15). Backdoor.Vasport. Retrieved February 22, 2018.

[37] Alperovitch, D.. (2016, June 15). Bears in the Midst: Intrusion into the Democratic National Committee. Retrieved August 3, 2016.

[38] Gardiner, J.,  Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.

## Defense

Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (22)

- [[Azure AD Connect PTA Backdoor Installation and Log Retrieval]]
- [[Chisel Port Forwarding and SOCKS Proxy Network Pivoting]]
- [[Cobalt Strike Malleable C2 Profile Checking]]
- [[Dynamic Port Forwarding with an SSH SOCKS Proxy]]
- [[Filter Bypass using Alternate Redirects]]
- [[LFI to RCE via Apache and Nginx Log Files]]
- [[Metasploit Network Pivoting with Meterpreter Port Forwarding and Routing]]
- [[Meterpreter SOCKS Proxy]]
- [[Network Pivoting with Proxychains]]
- [[Network Pivoting with sshuttle]]
- [[ngrok Port Forwarding]]
- [[RDS Routing Tables Destination and Target Rules]]
- [[Remote Port Forwarding Over HTTP Proxy]]
- [[Remote Port Forwarding with Reverse SSH Tunneling]]
- [[Reverse Socks Proxy Pivoting]]
- [[Rpivot - Network Pivoting Techniques]]
- [[Server-Side Request Forgery via Bypassing Filters with HTTPS]]
- [[SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[SSH Local Port Forwarding]]
- [[SSH Port Forwarding with an Isolated Host]]

*...and 2 more*
