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
- '[[aws-ssm-command-execution-ec2-shell-script]]'
- '[[Generate-Azure-Blob-Storage-SAS-URLs]]'
- '[[azure-pass-the-certificate-ad-cert-request-and-rce]]'
- '[[azure-web-apps-remote-ssh-connection]]'
- '[[Establish-Bash-TCP-Reverse-Shell]]'
- '[[Cloudflare-Tunnel-Pivoting-for-Lateral-Movement]]'
- '[[Copy-EC2-Instance-via-AMI-Creation-in-AWS]]'
- '[[dcom-lateral-movement]]'
- '[[DCOM-Office-Remote-Code-Execution]]'
- '[[dcom-shellbrowserwindow-calculator-execution]]'
- '[[dcom-shellexecute-calculator-execution]]'
- '[[Disable LLMNR and NetBIOS over TCP/IP]]'
- '[[GitHack-Exploiting-Insecure-Source-Code-Management]]'
- '[[Proxify-Go-Application-with-Graftcp]]'
- '[[Inter-User-Messaging]]'
- '[[Java-RMI-Server-RCE-using-Metasploit]]'
- '[[Extract-Data-from-Linked-SQL-Server-Database]]'
- '[[Extract-Top-5-Columns-from-Linked-Database]]'
- '[[Establish-Linux-Meterpreter-Reverse-TCP-Shell]]'
- '[[linux-reverse-shell-persistence-via-ncat-systemd]]'
- '[[Linux-Staged-Reverse-TCP-Meterpreter-Shell]]'
- '[[Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]'
- '[[Meterpreter-Payload-Generation]]'
- '[[Establish-Reverse-Shell-with-Ncat]]'
- '[[Network-Pivoting-with-Gost]]'
- '[[Network-Pivoting-with-Plink-Port-Forwarding]]'
- '[[network-pivoting-with-sshuttle]]'
- '[[NGINX/ALB Bypass Directory Traversal]]'
- '[[PrintNightmare-Remote-Code-Execution]]'
- '[[List-Subnets-in-VPC-for-Lateral-Movement]]'
- '[[List-EC2-Instances-in-Specific-Subnet-for-Lateral-Movement]]'
- '[[rds-lateral-movement-via-ec2-instances-in-vpc]]'
- '[[RDS-Lateral-Movement-via-EC2-Route-Tables]]'
- '[[rds-lateral-movement-via-vpc-peering-connections]]'
- '[[Modify-AWS-VPC-Route-Tables-for-RDS-Traffic-Redirection]]'
- '[[Remote-DPAPI-Credential-Dumping-with-DonPAPI]]'
- '[[Remote-File-Inclusion-via-SMB]]'
- '[[Establish-Reverse-SSH-Tunnel-for-Remote-Port-Forwarding]]'
- '[[Ruby-Bind-Shell]]'
- '[[Sam-Account-Name-Spoofing-for-User-Impersonation]]'
- '[[Deploy-SSH-Beacon-via-Cobalt-Strike]]'
- '[[Subversion-Source-Code-Disclosure]]'
- '[[WebDAV-Relay-Attack]]'
- '[[Windows-Impacket-Psexec-Remote-Command-Execution]]'
- '[[windows-powershell-remoting-with-pssession]]'
- '[[Connect-to-Windows-Remote-Share]]'
- '[[windows-smbexec-impacket-remote-command-execution]]'
- '[[windows-impacket-psexec-remote-execution-with-credentials]]'
- '[[windows-winrm-credential-access]]'
- '[[Workstation-Takeover-with-RBCD]]'
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

- [[aws-ssm-command-execution-ec2-shell-script]]
- [[Generate-Azure-Blob-Storage-SAS-URLs]]
- [[azure-pass-the-certificate-ad-cert-request-and-rce]]
- [[azure-web-apps-remote-ssh-connection]]
- [[Establish-Bash-TCP-Reverse-Shell]]
- [[Cloudflare-Tunnel-Pivoting-for-Lateral-Movement]]
- [[Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[dcom-lateral-movement]]
- [[DCOM-Office-Remote-Code-Execution]]
- [[dcom-shellbrowserwindow-calculator-execution]]
- [[dcom-shellexecute-calculator-execution]]
- [[Disable LLMNR and NetBIOS over TCP/IP]]
- [[GitHack-Exploiting-Insecure-Source-Code-Management]]
- [[Proxify-Go-Application-with-Graftcp]]
- [[Inter-User-Messaging]]
- [[Java-RMI-Server-RCE-using-Metasploit]]
- [[Extract-Data-from-Linked-SQL-Server-Database]]
- [[Extract-Top-5-Columns-from-Linked-Database]]
- [[Establish-Linux-Meterpreter-Reverse-TCP-Shell]]
- [[linux-reverse-shell-persistence-via-ncat-systemd]]

*...and 30 more*


