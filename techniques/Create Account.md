---
id: d41b7bc6-6fc8-4ccd-8ec9-047e039f78f8
name: Create Account
type: technique
mitre_id: T1136
mitre_url: null
created_at: '2019-08-28T21:17:19.661714+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Add a Local Administrator to Windows]]'
- '[[ASCII Conversion XSS Filter Bypass]]'
- '[[AWS IAM Access Key Creation]]'
- '[[AWS Shadow Admin Access]]'
- '[[Basic Directory Traversal Exploitation]]'
- '[[Blind XXE Out-of-Band Data Exfiltration]]'
- '[[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]'
- '[[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]'
- '[[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]'
- '[[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]'
- '[[CSP Bypass via Unsafe Inline Script Injection]]'
- '[[Filter Bypass using UTF-7 Encoding for XSS Injection]]'
- '[[Jinja2 Server Side Template Injection with Remote Code Execution]]'
- '[[Linux - Add Root User Persistence]]'
- '[[Linux - Privilege Escalation via Writable /etc/passwd]]'
- '[[Local DTD Injection in Citrix XenMobile Server]]'
- '[[Preventing Cross Site Scripting (XSS) in XML and files]]'
- '[[XSS in Files with XML Payload Injection]]'
- '[[XXE File Retrieval via Base64 Encoding]]'
- '[[XXE File Retrieval via XInclude Attack]]'
---

# Create Account

**MITRE ID**: T1136

## Description

Adversaries with a sufficient level of access may create a local system or domain account. Such accounts may be used for persistence that do not require persistent remote access tools to be deployed on the system.The net user commands can be used to create a local or domain account.

# Detection

Collect data on account creation within a network. Event ID 4720 is generated when a user account is created on a Windows system and domain controller. [13] Perform regular audits of domain and local system accounts to detect suspicious accounts that may have been created by an adversary.

# Mitigation

Use and enforce multifactor authentication. Follow guidelines to prevent or limit adversary access to Valid Accounts that may be used to create privileged accounts within an environment.

Adversaries that create local accounts on systems may have limited access within a network if access levels are properly locked down. These accounts may only be needed for persistence on individual systems and their usefulness depends on the utility of the system they reside on.

Protect domain controllers by ensuring proper security configuration for critical servers. Configure access controls and firewalls to limit access to these systems. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems.

# Footnotes

[1] valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.

[2] Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.

[3] Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.

[4] US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.

[5] US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.

[6] Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.

[7] Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.

[8] Gostev, A. (2012, May 30). Flame: Bunny, Frog, Munch and BeetleJuice…. Retrieved March 1, 2017.

[9] Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.

[10] Gross, J. (2016, February 23). Operation Dust Storm. Retrieved September 19, 2017.

[11] Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.

[12] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

[13] Lich, B., Miroshnikov, A. (2017, April 5). 4720(S): A user account was created. Retrieved June 30, 2017.

## Defense

Use and enforce multifactor authentication. Follow guidelines to prevent or limit adversary access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) that may be used to create privileged accounts within an environment.

Adversaries that creat

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (20)

- [[Add a Local Administrator to Windows]]
- [[ASCII Conversion XSS Filter Bypass]]
- [[AWS IAM Access Key Creation]]
- [[AWS Shadow Admin Access]]
- [[Basic Directory Traversal Exploitation]]
- [[Blind XXE Out-of-Band Data Exfiltration]]
- [[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]
- [[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]
- [[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]
- [[CORS Misconfiguration Exploitation with XSS on Trusted Origin]]
- [[CSP Bypass via Unsafe Inline Script Injection]]
- [[Filter Bypass using UTF-7 Encoding for XSS Injection]]
- [[Jinja2 Server Side Template Injection with Remote Code Execution]]
- [[Linux - Add Root User Persistence]]
- [[Linux - Privilege Escalation via Writable /etc/passwd]]
- [[Local DTD Injection in Citrix XenMobile Server]]
- [[Preventing Cross Site Scripting (XSS) in XML and files]]
- [[XSS in Files with XML Payload Injection]]
- [[XXE File Retrieval via Base64 Encoding]]
- [[XXE File Retrieval via XInclude Attack]]
