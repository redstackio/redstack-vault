---
id: 127ca79c-659c-4b26-a80c-488213f23fb2
name: Third-party Software
type: technique
mitre_id: T1072
mitre_url: null
created_at: '2019-08-28T21:17:43.776970+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[LFI to RCE via SSH Log File Inclusion]]'
---

# Third-party Software

**MITRE ID**: T1072

## Description

Third-party applications and software deployment systems may be in use in the network environment for administration purposes (e.g., SCCM, VNC, HBSS, Altiris, etc.). If an adversary gains access to these systems, then they may be able to execute code.Adversaries may gain access to and use third-party application deployment systems installed within an enterprise network. Access to a network-wide or enterprise-wide software deployment system enables an adversary to have remote code execution on all systems that are connected to such a system. The access may be used to laterally move to systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the deployment server, or specific domain credentials may be required. However, the system may require an administrative account to log in or to perform software deployment.

# Detection

Detection methods will vary depending on the type of third-party software or system and how it is typically used. 

The same investigation process can be applied here as with other potentially malicious activities where the distribution vector is initially unknown but the resulting activity follows a discernible pattern. Analyze the process execution trees, historical activities from the third-party application (such as what types of files are usually pushed), and the resulting activities or events from the file/binary/script pushed to systems. 

Often these third-party applications will have logs of their own that can be collected and correlated with other data from the environment. Audit software deployment logs and look for suspicious or unauthorized activity. A system not typically used to push software to clients that suddenly is used for such a task outside of a known admin function may be suspicious.

Perform application deployment at regular times so that irregular deployment activity stands out. Monitor process activity that does not correlate to known good software. Monitor account login activity on the deployment system.

# Mitigation

Evaluate the security of third-party software that could be used to deploy or execute programs. Ensure that access to management systems for deployment systems is limited, monitored, and secure. Have a strict approval policy for use of deployment systems.

Grant access to application deployment systems only to a limited number of authorized administrators. Ensure proper system and access isolation for critical network systems through use of firewalls, account privilege separation, group policy, and multifactor authentication. Verify that account credentials that may be used to access deployment systems are unique and not used throughout the enterprise network. Patch deployment systems regularly to prevent potential remote access through Exploitation for Privilege Escalation. 

If the application deployment system can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the application deployment system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled.

# Footnotes

[1] Dell SecureWorks Counter Threat Unit Special Operations Team. (2015, May 28). Living off the Land. Retrieved January 26, 2016.

[2] Dell SecureWorks. (2013, March 21). Wiper Malware Analysis Attacking Korean Financial Sector. Retrieved May 13, 2015.

## Defense

Evaluate the security of third-party software that could be used in the enterprise environment. Ensure that access to management systems for third-party systems is limited, monitored, and secure. Have a strict approval policy for use of third-party system

## Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (1)

- [[LFI to RCE via SSH Log File Inclusion]]
