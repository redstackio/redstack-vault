---
id: 9b3b2e21-2205-4160-b04c-5f270c5e8837
name: Access Token Manipulation
type: technique
mitre_id: T1134
mitre_url: null
created_at: '2019-08-28T21:17:20.745458+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abusing Backup Operators Group for Sensitive File Access]]'
- '[[Active Directory Object Owner Hijacking]]'
- '[[AWS EC2 Metadata SSRF]]'
- '[[AWS IAM User Policy Attachment]]'
- '[[AWS Lambda Function Privilege Escalation via IAM Policy Attachment]]'
- '[[AWS Role Assumption for Persistence]]'
- '[[AWS Shadow Admin Access]]'
- '[[AWS SSH Persistence with Authorized Keys]]'
- '[[Backdooring Git User Configurations]]'
- '[[Docker API Port Scanning and Container Management]]'
- '[[Elevating Privileges via RottenPotato and Token Impersonation]]'
- '[[Escalate Windows Privileges with Juicy Potato]]'
- '[[Execute PowerShell Commands as Another User (PSSession)]]'
- '[[Forge an Internal Forest Trust Ticket and Escalate to DA in Parent (SIDHistory)]]'
- '[[HiveNightmare Password Looting]]'
- '[[Kubernetes Service Account Token Access]]'
- '[[LAPS Password Retrieval]]'
- '[[Linux - Privilege Escalation via Capabilities]]'
- '[[Local Administrator to NT SYSTEM Privilege Escalation]]'
- '[[Meterpreter Get System]]'
- '[[Misconfigured Certificate Templates]]'
- '[[Misconfigured Certificate Templates]]'
- '[[MSSQL Server Impersonation Exploitation]]'
- '[[SAML Injection with XML Signature Wrapping Attack]]'
- '[[Windows - Default Writeable Folders Privilege Escalation]]'
- '[[Windows - EoP Looting for Passwords]]'
- '[[Windows - Impersonation Privileges Elevation with Meterpreter]]'
- '[[Windows - JuicyPotatoNG Privilege Escalation]]'
- '[[Windows - Password Looting via Alternate Data Stream]]'
- '[[Windows Privilege Escalation via IIS Web Config Looting]]'
- '[[Windows - SAM and SYSTEM Hash Extraction]]'
- '[[XLM Excel 4.0 GruntHttp Payload Generation]]'
---

# Access Token Manipulation

**MITRE ID**: T1134

## Description

Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token. For example, Microsoft promotes the use of access tokens as a security best practice. Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command runas. [1]Adversaries may use access tokens to operate under a different user or system security context to perform actions and evade detection. An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system. [2]Access tokens can be leveraged by adversaries through three methods: [3]Token Impersonation/Theft - An adversary creates a new access token that duplicates an existing token using DuplicateToken(Ex). The token can then be used with ImpersonateLoggedOnUser to allow the calling thread to impersonate a logged on user's security context, or with SetThreadToken to assign the impersonated token to a thread. This is useful for when the target user has a non-network logon session on the system.Create Process with a Token - An adversary creates a new access token with DuplicateToken(Ex) and uses it with CreateProcessWithTokenW to create a new process running under the security context of the impersonated user. This is useful for creating a new process under the security context of a different user.Make and Impersonate Token - An adversary has a username and password but the user is not logged onto the system. The adversary can then create a logon session for the user using the LogonUser function. The function will return a copy of the new session's access token and the adversary can use SetThreadToken to assign the token to a thread.Any standard user can use the runas command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account.Metasploit’s Meterpreter payload allows arbitrary token manipulation and uses token impersonation to escalate privileges. [4]  The Cobalt Strike beacon payload allows arbitrary token impersonation and can also create tokens. [5]

# Detection

If an adversary is using a standard command-line shell, analysts can detect token manipulation by auditing command-line activity. Specifically, analysts should look for use of the runas command. Detailed command-line logging is not enabled by default in Windows. [24]

If an adversary is using a payload that calls the Windows token APIs directly, analysts can detect token manipulation only through careful analysis of user network activity, examination of running processes, and correlation with other endpoint and network behavior. 

There are many Windows API calls a payload can take advantage of to manipulate access tokens (e.g., LogonUser [25], DuplicateTokenEx [26], and ImpersonateLoggedOnUser [27]). Please see the referenced Windows API pages for more information.

Query systems for process and thread token information and look for inconsistencies such as user owns processes impersonating the local SYSTEM account. [3]

# Mitigation

Access tokens are an integral part of the security system within Windows and cannot be turned off. However, an attacker must already have administrator level access on the local system to make full use of this technique; be sure to restrict users and accounts to the least privileges they require to do their job.

Any user can also spoof access tokens if they have legitimate credentials. Follow mitigation guidelines for preventing adversary use of Valid Accounts. Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [22] Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token. [23]

Also limit opportunities for adversaries to increase privileges by limiting Privilege Escalation opportunities.

# Footnotes

[1] Microsoft TechNet. (n.d.). Runas. Retrieved April 21, 2017.

[2] netbiosX. (2017, April 3). Token Manipulation. Retrieved April 21, 2017.

[3] Atkinson, J., Winchester, R. (2017, December 7). A Process is No One: Hunting for Token Manipulation. Retrieved December 21, 2017.

[4] Offensive Security. (n.d.). What is Incognito. Retrieved April 21, 2017.

[5] Mudge, R. (n.d.). Windows Access Tokens and Alternate Credentials. Retrieved April 21, 2017.

[6] FireEye Labs. (2015, April 18). Operation RussianDoll: Adobe & Windows Zero-Day Exploits Likely Leveraged by Russia’s APT28 in Highly-Targeted Attack. Retrieved April 24, 2017.

[7] Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.

[8] Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.

[9] Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.

[10] Kaspersky Lab. (2015, June 11). The Duqu 2.0. Retrieved April 21, 2017.

[11] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[12] FinFisher. (n.d.). Retrieved December 20, 2017.

[13] Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.

[14] Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.

[15] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[16] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Tools Report. Retrieved March 10, 2016.

[17] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[18] PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.

[19] PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.

[20] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[21] Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.

[22] Brower, N., Lich, B. (2017, April 19). Create a token object. Retrieved December 19, 2017.

[23] Brower, N., Lich, B. (2017, April 19). Replace a process level token. Retrieved December 19, 2017.

[24] Mathers, B. (2017, March 7). Command line process auditing. Retrieved April 21, 2017.

[25] Microsoft TechNet. (n.d.). Retrieved April 25, 2017.

[26] Microsoft TechNet. (n.d.). Retrieved April 25, 2017.

[27] Microsoft TechNet. (n.d.). Retrieved April 25, 2017.

## Defense

Access tokens are an integral part of the security system within Windows and cannot be turned off. However, an attacker must already have administrator level access on the local system to make full use of this technique; be sure to restrict users and acco

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (32)

- [[Abusing Backup Operators Group for Sensitive File Access]]
- [[Active Directory Object Owner Hijacking]]
- [[AWS EC2 Metadata SSRF]]
- [[AWS IAM User Policy Attachment]]
- [[AWS Lambda Function Privilege Escalation via IAM Policy Attachment]]
- [[AWS Role Assumption for Persistence]]
- [[AWS Shadow Admin Access]]
- [[AWS SSH Persistence with Authorized Keys]]
- [[Backdooring Git User Configurations]]
- [[Docker API Port Scanning and Container Management]]
- [[Elevating Privileges via RottenPotato and Token Impersonation]]
- [[Escalate Windows Privileges with Juicy Potato]]
- [[Execute PowerShell Commands as Another User (PSSession)]]
- [[Forge an Internal Forest Trust Ticket and Escalate to DA in Parent (SIDHistory)]]
- [[HiveNightmare Password Looting]]
- [[Kubernetes Service Account Token Access]]
- [[LAPS Password Retrieval]]
- [[Linux - Privilege Escalation via Capabilities]]
- [[Local Administrator to NT SYSTEM Privilege Escalation]]
- [[Meterpreter Get System]]

*...and 12 more*
