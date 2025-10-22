---
id: 3811d169-b88a-44b7-b053-ae371bf20ee9
name: Group Policy Modification
type: technique
mitre_id: T1484
mitre_url: null
created_at: '2019-08-28T21:17:42.189555+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Abuse GPO with PowerView to Push Empire Stager]]'
- '[[Abusing Group Policy Objects with StandIn to Manage Local Administrators and
  User Rights]]'
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[AdminCount Abuse]]'
- '[[Cloudflare XSS Bypass via SVG Onload Alert]]'
- '[[Domain Takeover via Certifried CVE-2022-26923]]'
- '[[Exploit Group Policy Objects with Write Access]]'
- '[[Golden Certificate Domain Persistence]]'
- '[[GPO Abuse with PowerGPOAbuse]]'
- '[[Windows Defender Application Control Device Guard Configuration]]'
---

# Group Policy Modification

**MITRE ID**: T1484

## Description

Adversaries may modify Group Policy Objects (GPOs) to subvert the intended discretionary access controls for a domain, usually with the intention of escalating privileges on the domain. Group policy allows for centralized management of user and computer settings in Active Directory (AD). GPOs are containers for group policy settings made up of files stored within a predicable network path \<DOMAIN>\SYSVOL\<DOMAIN>\Policies\.[1][2] Like other objects in AD, GPOs have access controls associated with them. By default all user accounts in the domain have permission to read GPOs. It is possible to delegate GPO access control permissions, e.g. write access, to specific users or groups in the domain.Malicious GPO modifications can be used to implement Scheduled Task, Disabling Security Tools, Remote File Copy, Create Account, Service Execution and more.[2][3][4][5][6] Since GPOs can control so many user and machine settings in the AD environment, there are a great number of potential attacks that can stem from this GPO abuse.[3] Publicly available scripts such as New-GPOImmediateTask can be leveraged to automate the creation of a malicious Scheduled Task by modifying GPO settings, in this case modifying <GPO_PATH>\Machine\Preferences\ScheduledTasks\ScheduledTasks.xml.[3][4] In some cases an adversary might modify specific user rights like SeEnableDelegationPrivilege, set in <GPO_PATH>\MACHINE\Microsoft\Windows NT\SecEdit\GptTmpl.inf, to achieve a subtle AD backdoor with complete control of the domain because the user account under the adversary's control would then be able to modify GPOs.[7]

# Detection

It is possible to detect GPO modifications by monitoring directory service changes using Windows event logs. Several events may be logged for such GPO modifications, including: Event ID 5136 - A directory service object was modified Event ID 5137 - A directory service object was created Event ID 5138 - A directory service object was undeleted Event ID 5139 - A directory service object was moved* Event ID 5141 - A directory service object was deleted

GPO abuse will often be accompanied by some other behavior such as Scheduled Task, which will have events associated with it to detect. Subsequent permission value modifications, like those to SeEnableDelegationPrivilege, can also be searched for in events associated with privileges assigned to new logons (Event ID 4672) and assignment of user rights (Event ID 4704). 

# Mitigation

Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as Bloodhound (version 1.5.1 and later)[9].

Consider implementing WMI and security filtering to further tailor which users and computers a GPO will apply to.[3][10][11]

# Footnotes

[1] srachui. (2012, February 13). Group Policy Basics – Part 1: Understanding the Structure of a Group Policy Object. Retrieved March 5, 2019.

[2] Metcalf, S. (2016, March 14). Sneaky Active Directory Persistence #17: Group Policy. Retrieved March 5, 2019.

[3] Robbins, A. (2018, April 2). A Red Teamer’s Guide to GPOs and OUs. Retrieved March 5, 2019.

[4] Schroeder, W. (2016, March 17). Abusing GPO Permissions. Retrieved March 5, 2019.

[5] Mandiant. (2016, February 25). Mandiant M-Trends 2016. Retrieved March 5, 2019.

[6] Microsoft Secure Team. (2016, June 1). Hacking Team Breach: A Cyber Jurassic Park. Retrieved March 5, 2019.

[7] Schroeder, W. (2017, January 10). The Most Dangerous User Right You (Probably) Have Never Heard Of. Retrieved March 5, 2019.

[8] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[9] Robbins, A., Vazarkar, R., and Schroeder, W. (2016, April 17). Bloodhound: Six Degrees of Domain Admin. Retrieved March 5, 2019.

[10] Microsoft. (2008, September 11). Fun with WMI Filters in Group Policy. Retrieved March 13, 2019.

[11] Microsoft. (2018, May 30). Filtering the Scope of a GPO. Retrieved March 13, 2019.

## Defense

Identify and correct GPO permissions abuse opportunities (ex: GPO modification privileges) using auditing tools such as Bloodhound (version 1.5.1 and later)(Citation: GitHub Bloodhound).

Consider implementing WMI and security filtering to further tailor 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (10)

- [[Abuse GPO with PowerView to Push Empire Stager]]
- [[Abusing Group Policy Objects with StandIn to Manage Local Administrators and User Rights]]
- [[Active Directory ACLs/ACEs Password Reset]]
- [[AdminCount Abuse]]
- [[Cloudflare XSS Bypass via SVG Onload Alert]]
- [[Domain Takeover via Certifried CVE-2022-26923]]
- [[Exploit Group Policy Objects with Write Access]]
- [[Golden Certificate Domain Persistence]]
- [[GPO Abuse with PowerGPOAbuse]]
- [[Windows Defender Application Control Device Guard Configuration]]
