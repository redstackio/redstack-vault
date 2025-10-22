---
id: 5cb64eaf-88a4-49b5-a7ab-38c1ad3f2716
name: Trusted Relationship
type: technique
mitre_id: T1199
mitre_url: null
created_at: '2019-08-28T21:17:25.603818+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
procedures:
- '[[Cassandra Login Bypass via SQL Injection]]'
- '[[DB2 Privilege Escalation]]'
- '[[MSSQL Credential Theft]]'
- '[[MSSQL Trusted Links Exploitation]]'
- '[[Redis SSRF Exploitation with Webshell and Reverse Shell]]'
- '[[SCF and URL File Attack Against Writeable Share]]'
---

# Trusted Relationship

**MITRE ID**: T1199

## Description

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship exploits an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, Valid Accounts used by the other party for access to internal network systems may be compromised and used.

# Detection

Establish monitoring for activity conducted by second and third party providers and other trusted entities that may be leveraged as a means to gain access to the network. Depending on the type of relationship, an adversary may have access to significant amounts of information about the target before conducting an operation, especially if the trusted relationship is based on IT services. Adversaries may be able to act quickly towards an objective, so proper monitoring for behavior related to Credential Access, Lateral Movement, and Collection will be important to detect the intrusion.

# Mitigation

Network segmentation can be used to isolate infrastructure components that do not require broad network access. Properly manage accounts and permissions used by parties in trusted relationships to minimize potential abuse by the party and if the party is compromised by an adversary. Vet the security policies and procedures of organizations that are contracted for work that require privileged access to network resources.

# Footnotes

[1] Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved September 13, 2018.

[2] PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.

[3] FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.

## Defense

Network segmentation can be used to isolate infrastructure components that do not require broad network access. Properly manage accounts and permissions used by parties in trusted relationships to minimize potential abuse by the party and if the party is 

## Tactics

- [[Initial Access|TA0001 - Initial Access]]

## Related Procedures (6)

- [[Cassandra Login Bypass via SQL Injection]]
- [[DB2 Privilege Escalation]]
- [[MSSQL Credential Theft]]
- [[MSSQL Trusted Links Exploitation]]
- [[Redis SSRF Exploitation with Webshell and Reverse Shell]]
- [[SCF and URL File Attack Against Writeable Share]]
