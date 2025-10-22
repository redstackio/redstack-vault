---
id: 5993834a-3471-48a5-a065-b8310b2567b5
name: Valid Accounts
type: technique
mitre_id: T1078
mitre_url: null
created_at: '2019-08-28T21:17:19.095178+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Active Directory Object Owner Hijacking]]'
- '[[AWS Console Access via API Keys]]'
- '[[AWS EC2 Instance Connect with SSH Key Push]]'
- '[[AWS IAM Access Key Creation]]'
- '[[AWS Managed Policies Enumeration]]'
- '[[AWS Role Assumption for Persistence]]'
- '[[AWS SSH Key Persistence]]'
- '[[AWS SSH Persistence with Authorized Keys]]'
- '[[Azure AD App Secrets for Service Principal Authentication]]'
- '[[Azure Pass the Certificate: AD Cert Request and RCE]]'
- '[[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]'
- '[[Connect to an SSH Server with a Private Key]]'
- '[[Create Windows Credentials Object]]'
- '[[Dynamic Group Membership - Set Secondary Email for Azure AD User]]'
- '[[Exotic Payloads for Bypassing Space Filter]]'
- '[[GitHack - Exploiting Insecure Source Code Management]]'
- '[[IAM-Based Authentication for RDS MySQL Database]]'
- '[[JWT Token Creation]]'
- '[[Linux Privilege Escalation via SSH Key]]'
- '[[MSSQL Server Impersonation Exploitation]]'
- '[[Network Pivoting with Gost]]'
- '[[RDS Lateral Movement via EC2 Route Tables]]'
- '[[Run a Command as Another User using Saved Credentials]]'
- '[[Windows - Elevated RDP Backdoor with Sticky Keys]]'
- '[[Windows - Impersonation Privileges Elevation with Meterpreter]]'
- '[[Windows - PowerShell Remoting Protocol with PSSESSION]]'
- '[[Windows - PsExec with Different User Credentials]]'
- '[[Windows - WMIExec with Impacket]]'
---

# Valid Accounts

**MITRE ID**: T1078

## Description

Adversaries may steal the credentials of a specific user or service account using Credential Access techniques or capture credentials earlier in their reconnaissance process through social engineering for means of gaining Initial Access. Accounts that an adversary may use can fall into three categories: default, local, and domain accounts. Default accounts are those that are built-into an OS such as Guest or Administrator account on Windows systems or default factory/provider set accounts on other types of systems, software, or devices. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. [1] Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover users, administrators, and services.Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop. Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.Default accounts are also not limited to Guest and Administrator on client machines, they also include accounts that are preset for equipment such as network devices and computer applications whether they are internal, open source, or COTS. Appliances that come preset with a username and password combination pose a serious threat to organizations that do not change it post installation, as they are easy targets for an adversary. Similarly, adversaries may also utilize publicly disclosed private keys, or stolen private keys, to legitimately connect to remote environments via Remote Services [2]The overlap of account access, credentials, and permissions across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise. [3]

# Detection

Configure robust, consistent account activity audit policies across the enterprise and with externally accessible services. [45] Look for suspicious account behavior across systems that share accounts, either user, admin, or service accounts. Examples: one account logged into multiple systems simultaneously; multiple accounts logged into the same machine simultaneously; accounts logged in at odd times or outside of business hours. Activity may be from interactive login sessions or process ownership from accounts being used to execute binaries on a remote system as a particular account. Correlate other security systems with login information (e.g., a user has an active login session but has not entered the building or does not have VPN access).

Perform regular audits of domain and local system accounts to detect accounts that may have been created by an adversary for persistence. Checks on these accounts could also include whether default accounts such as Guest have been activated. These audits should also include checks on any appliances and applications for default credentials or SSH keys, and if any are discovered, they should be updated immediately. 

# Mitigation

Take measures to detect or prevent techniques such as Credential Dumping or installation of keyloggers to acquire credentials through Input Capture. Limit credential overlap across systems to prevent access if account credentials are obtained. Ensure that local administrator accounts have complex, unique passwords across all systems on the network. Do not put user or admin domain accounts in the local administrator groups across systems unless they are tightly controlled and use of accounts is segmented, as this is often equivalent to having a local administrator account with the same password on all systems. 

Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [42] 

Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [3] [43] These audits should also include if default accounts have been enabled, or if new local accounts are created that have not be authorized. 

Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment. [44] When possible, applications that use SSH keys should be updated periodically and properly secured. 

# Footnotes

[1] Microsoft. (2018, December 9). Local Accounts. Retrieved February 11, 2019.

[2] undefined. (n.d.). Retrieved April 12, 2019.

[3] Microsoft. (2016, April 15). Attractive Accounts for Credential Theft. Retrieved June 3, 2016.

[4] Adair, S. (2017, February 17). Detecting and Responding to Advanced Threats within Exchange Environments. Retrieved March 20, 2017.

[5] Hacquebord, F.. (2017, April 25). Two Years of Pawn Storm: Examining an Increasingly Relevant Threat. Retrieved May 3, 2017.

[6] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[7] Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.

[8] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

[9] Davis, S. and Carr, N. (2017, September 21). APT33: New Insights into Iranian Cyber Espionage Group. Retrieved February 15, 2018.

[10] Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.

[11] Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.

[12] Kaspersky Lab's Global Research and Analysis Team. (2015, February). CARBANAK APT THE GREAT BANK ROBBERY. Retrieved August 23, 2018.

[13] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[14] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[15] Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.

[16] Smith, A.. (2017, December 22). Protect your network from Emotet Trojan with Malwarebytes Endpoint Security. Retrieved January 17, 2019.

[17] FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved June 25, 2017.

[18] Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.

[19] Vengerik, B. & Dennesen, K.. (2014, December 5). Hacking the Street?  FIN4 Likely Playing the Market. Retrieved January 15, 2019.

[20] Scavella, T. and Rifki, A. (2017, July 20). Are you Ready to Respond? (Webinar). Retrieved October 4, 2017.

[21] Higgins, K. (2015, October 13). Prolific Cybercrime Gang Favors Legit Login Credentials. Retrieved October 4, 2017.

[22] Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.

[23] FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved June 1, 2016.

[24] McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.

[25] Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy:  New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.

[26] Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.

[27] PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.

[28] McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.

[29] Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.

[30] US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.

[31] Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.

[32] Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.

[33] Bizeul, D., Fontarensky, I., Mouchoux, R., Perigaud, F., Pernet, C. (2014, July 11). Eye of the Tiger. Retrieved September 29, 2015.

[34] Symantec Security Response. (2015, July 13). “Forkmeiamfamous”: Seaduke, latest weapon in the Duke armory. Retrieved July 22, 2015.

[35] FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved January 11, 2017.

[36] ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.

[37] DiMaggio, J.. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.

[38] Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.

[39] Dell SecureWorks Counter Threat Unit Special Operations Team. (2015, May 28). Living off the Land. Retrieved January 26, 2016.

[40] Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.

[41] Fernando Mercês. (2016, September 5). Pokémon-themed Umbreon Linux Rootkit Hits x86, ARM Systems. Retrieved March 5, 2018.

[42] Plett, C., Poggemeyer, L. (12, October 26). Securing Privileged Access Reference Material. Retrieved April 25, 2017.

[43] Microsoft. (2016, April 16). Implementing Least-Privilege Administrative Models. Retrieved June 3, 2016.

[44] undefined. (n.d.). Risks of Default Passwords on the Internet. Retrieved April 12, 2019.

[45] Microsoft. (2016, April 15). Audit Policy Recommendations. Retrieved June 3, 2016.

## Defense

Take measures to detect or prevent techniques such as [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) or installation of keyloggers to acquire credentials through [Input Capture](https://attack.mitre.org/techniques/T1056). Limit credent

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (28)

- [[Active Directory Object Owner Hijacking]]
- [[AWS Console Access via API Keys]]
- [[AWS EC2 Instance Connect with SSH Key Push]]
- [[AWS IAM Access Key Creation]]
- [[AWS Managed Policies Enumeration]]
- [[AWS Role Assumption for Persistence]]
- [[AWS SSH Key Persistence]]
- [[AWS SSH Persistence with Authorized Keys]]
- [[Azure AD App Secrets for Service Principal Authentication]]
- [[Azure Pass the Certificate: AD Cert Request and RCE]]
- [[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]
- [[Connect to an SSH Server with a Private Key]]
- [[Create Windows Credentials Object]]
- [[Dynamic Group Membership - Set Secondary Email for Azure AD User]]
- [[Exotic Payloads for Bypassing Space Filter]]
- [[GitHack - Exploiting Insecure Source Code Management]]
- [[IAM-Based Authentication for RDS MySQL Database]]
- [[JWT Token Creation]]
- [[Linux Privilege Escalation via SSH Key]]
- [[MSSQL Server Impersonation Exploitation]]

*...and 8 more*
