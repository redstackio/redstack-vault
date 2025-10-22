---
id: f2e4e229-bc14-491d-9569-815fb2b26418
name: Application Deployment Software
type: technique
mitre_id: T1017
mitre_url: null
created_at: '2019-08-28T21:17:26.616396+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[AWS API Enumeration]]'
- '[[AWS API Gateway Method Enumeration]]'
---

# Application Deployment Software

**MITRE ID**: T1017

## Description

Adversaries may deploy malicious software to systems within a network using application deployment systems employed by enterprise administrators. The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the deployment server, or specific domain credentials may be required. However, the system may require an administrative account to log in or to perform software deployment.Access to a network-wide or enterprise-wide software deployment system enables an adversary to have remote code execution on all systems that are connected to such a system. The access may be used to laterally move to systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

# Detection

Monitor application deployments from a secondary system. Perform application deployment at regular times so that irregular deployment activity stands out. Monitor process activity that does not correlate to known good software. Monitor account login activity on the deployment system.

# Mitigation

Grant access to application deployment systems only to a limited number of authorized administrators. Ensure proper system and access isolation for critical network systems through use of firewalls, account privilege separation, group policy, and multifactor authentication. Verify that account credentials that may be used to access deployment systems are unique and not used throughout the enterprise network. Patch deployment systems regularly to prevent potential remote access through Exploitation for Privilege Escalation. 

If the application deployment system can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the application deployment system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled.

# Footnotes

[1] Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.

## Defense

Grant access to application deployment systems only to a limited number of authorized administrators. Ensure proper system and access isolation for critical network systems through use of firewalls, account privilege separation, group policy, and multifac

## Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (2)

- [[AWS API Enumeration]]
- [[AWS API Gateway Method Enumeration]]
