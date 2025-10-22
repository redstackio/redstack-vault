---
id: a324ce85-6f41-441b-b5d0-41519e29f42a
name: Account Manipulation
type: technique
mitre_id: T1098
mitre_url: null
created_at: '2019-08-28T21:17:27.203260+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]'
- '[[Add User to Active Directory Domain Group]]'
- '[[AWS IAM Policy Version Retrieval]]'
- '[[Azure AD Connect Monitoring Disable and Password Reset]]'
- '[[Azure Resource Management and Privilege Checking with PowerShell]]'
- '[[Change an AD Domain User''s Password]]'
- '[[Extracting GMSA Passwords from Active Directory]]'
- '[[ForceChangePassword Active Directory Attack]]'
- '[[GMSA Password Forging]]'
- '[[Kubernetes API Request Simulation]]'
- '[[Kubernetes Privileged Service Account Token Retrieval]]'
- '[[Kubernetes RBAC Privilege Escalation via Malicious RoleBinding]]'
- '[[Kubernetes Service Account Token Theft]]'
- '[[Linux - Add Root User Persistence]]'
- '[[PXE Boot Image Attack - Local Admin Account Hijack]]'
- '[[Skeleton Key Persistence]]'
---

# Account Manipulation

**MITRE ID**: T1098

## Description

Account manipulation may aid adversaries in maintaining access to credentials and certain permission levels within an environment. Manipulation could consist of modifying permissions, modifying credentials, adding or changing permission groups, modifying account settings, or modifying how authentication is performed. These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to subvert password duration policies and preserve the life of compromised credentials. In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain.

# Detection

Collect events that correlate with changes to account objects on systems and the domain, such as event ID 4738. [10] Monitor for modification of accounts in correlation with other suspicious activity. Changes may occur at unusual times or from unusual systems. Especially flag events where the subject and target accounts differ [11] or that include additional flags such as changing a password without knowledge of the old password. [12]

Use of credentials may also occur at unusual times or to unusual systems or services and may correlate with other suspicious activity.

# Mitigation

Use multifactor authentication. Follow guidelines to prevent or limit adversary access to Valid Accounts.

Protect domain controllers by ensuring proper security configuration for critical servers. Configure access controls and firewalls to limit access to these systems. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems.

# Footnotes

[1] valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.

[2] Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.

[3] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[4] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[5] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.

[6] Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved March 2, 2016.

[7] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[8] Metcalf, S. (2015, January 19). Attackers Can Now Use Mimikatz to Implant Skeleton Key on Domain Controllers & BackDoor Your Active Directory Forest. Retrieved February 3, 2015.

[9] Dell SecureWorks. (2015, January 12). Skeleton Key Malware Analysis. Retrieved April 8, 2019.

[10] Lich, B., Miroshnikov, A. (2017, April 5). 4738(S): A user account was changed. Retrieved June 30, 2017.

[11] Warren, J. (2017, July 11). Manipulating User Passwords with Mimikatz. Retrieved December 4, 2017.

[12] Warren, J. (2017, June 22). lsadump::changentlm and lsadump::setntlm work, but generate Windows events #92. Retrieved December 4, 2017.

## Defense

Use multifactor authentication. Follow guidelines to prevent or limit adversary access to [Valid Accounts](https://attack.mitre.org/techniques/T1078).

Protect domain controllers by ensuring proper security configuration for critical servers. Configure ac

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (16)

- [[Abusing WriteDACL to Grant Permissions to Interesting Group for User1]]
- [[Add User to Active Directory Domain Group]]
- [[AWS IAM Policy Version Retrieval]]
- [[Azure AD Connect Monitoring Disable and Password Reset]]
- [[Azure Resource Management and Privilege Checking with PowerShell]]
- [[Change an AD Domain User's Password]]
- [[Extracting GMSA Passwords from Active Directory]]
- [[ForceChangePassword Active Directory Attack]]
- [[GMSA Password Forging]]
- [[Kubernetes API Request Simulation]]
- [[Kubernetes Privileged Service Account Token Retrieval]]
- [[Kubernetes RBAC Privilege Escalation via Malicious RoleBinding]]
- [[Kubernetes Service Account Token Theft]]
- [[Linux - Add Root User Persistence]]
- [[PXE Boot Image Attack - Local Admin Account Hijack]]
- [[Skeleton Key Persistence]]
