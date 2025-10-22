---
id: fe01c8c2-aed6-4171-973f-f641730516ff
name: Password Policy Discovery
type: technique
mitre_id: T1201
mitre_url: null
created_at: '2019-08-28T21:17:30.500273+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
procedures:
- '[[Active Directory ACLs/ACEs Password Reset]]'
- '[[Active Recon - DNS Zone Transfer Enumeration]]'
- '[[Cloudflare XSS Prompt Bypass]]'
- '[[GraphQL Injection Exploit: Identifying Injection Points]]'
- '[[GraphQL SQL Injection Exploitation]]'
- '[[HQL Injection via Unsupported Comment Error]]'
- '[[LDAP Injection Password Brute Force]]'
- '[[LDAP Injection with Default Attributes]]'
- '[[Lessjs Server Side Template Injection via Inline Import]]'
- '[[LFI to RCE via Mail Log File Inclusion]]'
- '[[MYSQL Error Based - UpdateXML function Data Extraction]]'
- '[[Subdomain Enumeration with Knockpy and EyeWitness]]'
---

# Password Policy Discovery

**MITRE ID**: T1201

## Description

Password policies for networks are a way to enforce complex passwords that are difficult to guess or crack through Brute Force. An adversary may attempt to access detailed information about the password policy used within an enterprise network. This would help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).Password policies can be set and discovered on Windows, Linux, and macOS systems. [1] [2]Windowsnet accountsnet accounts /domainLinuxchage -l cat /etc/pam.d/common-passwordmacOSpwpolicy getaccountpolicies

# Detection

Monitor processes for tools and command line arguments that may indicate they're being used for password policy discovery. Correlate that activity with other suspicious activity from the originating system to reduce potential false positives from valid user or administrator activity. Adversaries will likely attempt to find the password policy early in an operation and the activity is likely to happen with other Discovery activity.

# Mitigation

Mitigating discovery of password policies is not advised since the information is required to be known by systems and users of a network. Ensure password policies are such that they mitigate brute force attacks yet will not give an adversary an information advantage because the policies are too light. Active Directory is a common way to set and enforce password policies throughout an enterprise network. [7]

# Footnotes

[1] Matutiae, M. (2014, August 6). How to display password policy information for a user (Ubuntu)?. Retrieved April 5, 2018.

[2] Holland, J. (2016, January 25). User password policies on non AD machines. Retrieved April 5, 2018.

[3] Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.

[4] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[5] Singh, S., Yin, H. (2016, May 22). https://www.fireeye.com/blog/threat-research/2016/05/targeted_attacksaga.html. Retrieved April 5, 2018.

[6] Nettitude. (2016, June 8). PoshC2: Powershell C2 Server and Implants. Retrieved April 23, 2019.

[7] Hall, J., Lich, B. (2017, September 9). Password must meet complexity requirements. Retrieved April 5, 2018.

## Defense

Mitigating discovery of password policies is not advised since the information is required to be known by systems and users of a network. Ensure password policies are such that they mitigate brute force attacks yet will not give an adversary an informatio

## Tactics

- [[Discovery|TA0007 - Discovery]]

## Related Procedures (12)

- [[Active Directory ACLs/ACEs Password Reset]]
- [[Active Recon - DNS Zone Transfer Enumeration]]
- [[Cloudflare XSS Prompt Bypass]]
- [[GraphQL Injection Exploit: Identifying Injection Points]]
- [[GraphQL SQL Injection Exploitation]]
- [[HQL Injection via Unsupported Comment Error]]
- [[LDAP Injection Password Brute Force]]
- [[LDAP Injection with Default Attributes]]
- [[Lessjs Server Side Template Injection via Inline Import]]
- [[LFI to RCE via Mail Log File Inclusion]]
- [[MYSQL Error Based - UpdateXML function Data Extraction]]
- [[Subdomain Enumeration with Knockpy and EyeWitness]]
