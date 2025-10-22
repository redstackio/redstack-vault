---
id: ce35d704-d12c-49c7-a33d-931841e2da63
name: Remote Services
type: technique
mitre_id: T1021
mitre_url: null
created_at: '2019-08-28T21:17:19.270839+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[AWS SSM Command Execution - EC2 Shell Script]]'
- '[[Azure Generate Shared Access Signature (SAS) URLs for Blob Storage]]'
- '[[Azure Pass the Certificate: AD Cert Request and RCE]]'
- '[[Azure Web Apps: Remote SSH Connection]]'
- '[[Bash TCP Reverse Shell Connection]]'
- '[[Cloudflare Tunnel Exposer Pivoting]]'
- '[[Copying EC2 Instances using AMI Image in AWS]]'
- '[[DCOM Lateral Movement]]'
- '[[DCOM Office Remote Code Execution]]'
- '[[DCOM ShellBrowserWindow Calculator Execution]]'
- '[[DCOM ShellExecute Calculator Execution]]'
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[GitHack - Exploiting Insecure Source Code Management]]'
- '[[Go Application Proxification with Graftcp]]'
- '[[Inter-User Messaging]]'
- '[[Java RMI Server RCE using Metasploit]]'
- '[[Linked Database Column Extraction]]'
- '[[Linked Database Top 5 Columns Extraction]]'
- '[[Linux Meterpreter Reverse TCP Shell]]'
- '[[Linux Reverse Shell Persistence with Ncat]]'
- '[[Linux Staged Reverse TCP Meterpreter Shell]]'
- '[[Metasploit Network Pivoting with Meterpreter Port Forwarding and Routing]]'
- '[[Meterpreter Payload Generation]]'
- '[[Ncat Reverse Shell]]'
- '[[Network Pivoting with Gost]]'
- '[[Network Pivoting with plink Port Forwarding]]'
- '[[Network Pivoting with sshuttle]]'
- '[[NGINX/ALB Bypass Directory Traversal]]'
- '[[PrintNightmare Remote Code Execution]]'
- '[[RDS Lateral Movement - Listing Subnets]]'
- '[[RDS Lateral Movement: List Instances on Specified Subnet]]'
- '[[RDS Lateral Movement through EC2 Instances in VPC]]'
- '[[RDS Lateral Movement via EC2 Route Tables]]'
- '[[RDS Lateral Movement via VPC Peering Connections]]'
- '[[RDS Routing Tables Destination and Target Rules]]'
- '[[Remote DPAPI Credential Dumping with DonPAPI]]'
- '[[Remote File Inclusion via SMB]]'
- '[[Remote Port Forwarding with Reverse SSH Tunneling]]'
- '[[Ruby Bind Shell]]'
- '[[samAccountName Spoofing Attack]]'
- '[[SSH Beacon Payload with Cobalt Strike]]'
- '[[Subversion Source Code Disclosure]]'
- '[[WebDAV Relay Attack]]'
- '[[Windows - Impacket Psexec Remote Command Execution]]'
- '[[Windows - PowerShell Remoting Protocol with PSSESSION]]'
- '[[Windows Remote Share Connection]]'
- '[[Windows - SMBExec with Impacket for Command Execution]]'
- '[[Windows - Using Impacket and PSExec with Credentials]]'
- '[[Windows WinRM Credential Access]]'
- '[[Workstation Takeover with RBCD]]'
---

# Remote Services

**MITRE ID**: T1021

## Description

An adversary may use Valid Accounts to log into a service specifically designed to accept remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

# Detection

Correlate use of login activity related to remote services with unusual behavior or other malicious or suspicious activity. Adversaries will likely need to learn about an environment and the relationships between systems through Discovery techniques prior to attempting Lateral Movement.

# Mitigation

Limit the number of accounts that may use remote services. Use multifactor authentication where possible. Limit the permissions for accounts that are at higher risk of compromise; for example, configure SSH so users can only run specific programs. Prevent Credential Access techniques that may allow an adversary to acquire Valid Accounts that can be used by existing services.

# Footnotes

[1] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[2] Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved December 20, 2017.

[3] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[4] Kaspersky Lab's Global Research & Analysis Team. (2016, February 8). APT-style bank robberies increase with Metel, GCMAN and Carbanak 2.0 attacks. Retrieved April 20, 2016.

[5] Plan, F., et all. (2019, March 4). APT40: Examining a China-Nexus Espionage Actor. Retrieved March 18, 2019.

[6] Anomali Labs. (2018, December 6). Pulling Linux Rabbit/Rabbot Malware Out of a Hat. Retrieved March 4, 2019.

[7] PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.

[8] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[9] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

[10] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

## Defense

Limit the number of accounts that may use remote services. Use multifactor authentication where possible. Limit the permissions for accounts that are at higher risk of compromise; for example, configure SSH so users can only run specific programs. Prevent

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (50)

- [[AWS SSM Command Execution - EC2 Shell Script]]
- [[Azure Generate Shared Access Signature (SAS) URLs for Blob Storage]]
- [[Azure Pass the Certificate: AD Cert Request and RCE]]
- [[Azure Web Apps: Remote SSH Connection]]
- [[Bash TCP Reverse Shell Connection]]
- [[Cloudflare Tunnel Exposer Pivoting]]
- [[Copying EC2 Instances using AMI Image in AWS]]
- [[DCOM Lateral Movement]]
- [[DCOM Office Remote Code Execution]]
- [[DCOM ShellBrowserWindow Calculator Execution]]
- [[DCOM ShellExecute Calculator Execution]]
- [[Disable LLMNR and NetBIOS over TCP/IP]]
- [[GitHack - Exploiting Insecure Source Code Management]]
- [[Go Application Proxification with Graftcp]]
- [[Inter-User Messaging]]
- [[Java RMI Server RCE using Metasploit]]
- [[Linked Database Column Extraction]]
- [[Linked Database Top 5 Columns Extraction]]
- [[Linux Meterpreter Reverse TCP Shell]]
- [[Linux Reverse Shell Persistence with Ncat]]

*...and 30 more*
