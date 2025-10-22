---
id: b53d7546-58f6-4425-ab4f-3804c2a9ccae
name: Remote Access Tools
type: technique
mitre_id: T1219
mitre_url: null
created_at: '2019-08-28T21:17:44.654848+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Awk Interactive Reverse Shell]]'
- '[[Cobalt Strike VPN & Pivots]]'
- '[[Cross-Site WebSocket Hijacking (CSWSH) Attack]]'
- '[[DNS Rebinding Exploitation]]'
- '[[Golang Reverse Shell Cheat Sheet]]'
- '[[Insecure Source Code Management with Bazaar using rip-bzr.pl]]'
- '[[Java Reverse Shell Cheat Sheet]]'
- '[[Java Reverse Shell Payload - War]]'
- '[[Lan Turtle AutoSSH]]'
- '[[Linux Privilege Escalation via SSH Key]]'
- '[[Lua Reverse Shell Cheat Sheet]]'
- '[[Metasploit Reverse Shell Handler]]'
- '[[PHP Deserialization POP Chain Attack]]'
- '[[PHP Reverse Shell]]'
- '[[Powershell Reverse Shell Cheat Sheet]]'
- '[[Session Management with Metasploit]]'
- '[[SMB Beacon Payload with Command Line Interactions]]'
- '[[Socat Reverse Shell Cheat Sheet]]'
- '[[Springboot-Actuator Remote Code Execution via /env]]'
- '[[SSH Beacon Payload with Cobalt Strike]]'
- '[[Telnet Reverse Shell]]'
- '[[Windows Reverse Shell]]'
- '[[XSS in Angular and AngularJS - Stored/Reflected XSS with Simple Alert]]'
---

# Remote Access Tools

**MITRE ID**: T1219

## Description

An adversary may use legitimate desktop support and remote access software, such as Team Viewer, Go2Assist, LogMein, AmmyyAdmin, etc, to establish an interactive command and control channel to target systems within networks. These services are commonly used as legitimate technical support software, and may be whitelisted within a target environment. Remote access tools like VNC, Ammy, and Teamviewer are used frequently when compared with other legitimate software commonly used by adversaries. [1]Remote access tools may be established and used post-compromise as alternate communications channel for Redundant Access or as a way to establish an interactive remote desktop session with the target system. They may also be used as a component of malware to establish a reverse connection or back-connect to a service or adversary controlled system.Admin tools such as TeamViewer have been used by several groups targeting institutions in countries of interest to the Russian state and criminal campaigns. [2] [3]

# Detection

Monitor for applications and processes related to remote admin tools. Correlate activity with other suspicious behavior that may reduce false positives if these tools are used by legitimate users and administrators.

Analyze network data for uncommon data flows (e.g., a client sending significantly more data than it receives from a server). Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Analyze packet contents to detect application layer protocols that do not follow the expected protocol for the port that is being used.

Domain Fronting may be used in conjunction to avoid defenses. Adversaries will likely need to deploy and/or install these remote tools to compromised systems. It may be possible to detect or prevent the installation of these tools with host-based solutions.

# Mitigation

Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access tools.

Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to these services as well.

Use application whitelisting to mitigate use of and installation of unapproved software.

# Footnotes

[1] Wueest, C., Anand, H. (2017, July). Living off the land and fileless attack techniques. Retrieved April 10, 2018.

[2] CrowdStrike Intelligence. (2016). 2015 Global Threat Report. Retrieved April 11, 2018.

[3] CrySyS Lab. (2013, March 20). TeamSpy – Obshie manevri. Ispolzovat’ tolko s razreshenija S-a. Retrieved April 11, 2018.

[4] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[5] Group-IB and Fox-IT. (2014, December). Anunak: APT against financial institutions. Retrieved April 20, 2016.

[6] Positive Technologies. (2017, August 16). Cobalt Strikes Back: An Evolving Multinational Threat to Finance. Retrieved September 5, 2018.

[7] Positive Technologies. (2016, December 16). Cobalt Snatch. Retrieved October 9, 2018.

[8] Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.

[9] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[10] Security Response Attack Investigation Team. (2018, June 19). Thrip: Espionage Group Hits Satellite, Telecoms, and Defense Companies. Retrieved July 10, 2018.

## Defense

Properly configure firewalls, application firewalls, and proxies to limit outgoing traffic to sites and services used by remote access tools.

Network intrusion detection and prevention systems that use network signatures may be able to prevent traffic to

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (23)

- [[Awk Interactive Reverse Shell]]
- [[Cobalt Strike VPN & Pivots]]
- [[Cross-Site WebSocket Hijacking (CSWSH) Attack]]
- [[DNS Rebinding Exploitation]]
- [[Golang Reverse Shell Cheat Sheet]]
- [[Insecure Source Code Management with Bazaar using rip-bzr.pl]]
- [[Java Reverse Shell Cheat Sheet]]
- [[Java Reverse Shell Payload - War]]
- [[Lan Turtle AutoSSH]]
- [[Linux Privilege Escalation via SSH Key]]
- [[Lua Reverse Shell Cheat Sheet]]
- [[Metasploit Reverse Shell Handler]]
- [[PHP Deserialization POP Chain Attack]]
- [[PHP Reverse Shell]]
- [[Powershell Reverse Shell Cheat Sheet]]
- [[Session Management with Metasploit]]
- [[SMB Beacon Payload with Command Line Interactions]]
- [[Socat Reverse Shell Cheat Sheet]]
- [[Springboot-Actuator Remote Code Execution via /env]]
- [[SSH Beacon Payload with Cobalt Strike]]

*...and 3 more*
