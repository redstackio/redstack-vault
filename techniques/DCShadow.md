---
id: c499166a-1754-4c41-b0be-0272690c72c8
name: DCShadow
type: technique
mitre_id: T1207
mitre_url: null
created_at: '2019-08-28T21:17:19.995053+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[Brute Force Login with MongoDB Query Injection]]'
- '[[Checksum Validation Exploitation for Active Directory]]'
- '[[NoSQL Injection: Extract User Data]]'
- '[[PrintNightmare - Exploiting CVE to gain SYSTEM shell on DC via Anonymous SMB
  Server]]'
- '[[Server Side Template Injection with Twig Template Rendering]]'
- '[[Twig Template Remote Code Execution]]'
---

# DCShadow

**MITRE ID**: T1207

## Description

DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a Domain Controller (DC). [1] [2] Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema, which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. [3]This technique may bypass system logging and security monitors such as security information and event management (SIEM) products (since actions taken on a rogue DC may not be reported to these sensors). [1] The technique may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries may also utilize this technique to perform SID-History Injection and/or manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence. [1] [2]

# Detection

Monitor and analyze network traffic associated with data replication (such as calls to DrsAddEntry, DrsReplicaAdd, and especially GetNCChanges) between DCs as well as to/from non DC hosts. [5] [1] [2] DC replication will naturally take place every 15 minutes but can be triggered by an attacker or by legitimate urgent changes (ex: passwords). [2] Also consider monitoring and alerting on the replication of AD objects (Audit Detailed Directory Service Replication Events 4928 and 4929). [1]

Leverage AD directory synchronization (DirSync) to monitor changes to directory state using AD replication cookies. [6] [7]

Baseline and periodically analyze the Configuration partition of the AD schema and alert on creation of nTDSDSA objects. [2]

Investigate usage of Kerberos Service Principal Names (SPNs), especially those associated with services (beginning with "GC/") by computers not present in the DC organizational unit (OU). The SPN associated with the Directory Replication Service (DRS) Remote Protocol interface (GUID E3514235–4B06–11D1-AB04–00C04FC2DCD2) can be set without logging. [7] A rogue DC must authenticate as a service using these two SPNs for the replication process to successfully complete.

# Mitigation

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of AD design features. For example, mitigating specific AD API calls will likely have unintended side effects, such as preventing DC replication from operating properly. Efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identification of subsequent malicious behavior.

# Footnotes

[1] Delpy, B. & LE TOUX, V. (n.d.). DCShadow. Retrieved March 20, 2018.

[2] Delpy, B. & LE TOUX, V. (2018, January 24). Active Directory: What can make your million dollar SIEM go blind?. Retrieved March 20, 2018.

[3] Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.

[4] Deply, B. (n.d.). Mimikatz. Retrieved September 29, 2015.

[5] Spencer S. (2018, February 22). DCSYNCMonitor. Retrieved March 30, 2018.

[6] Microsoft. (n.d.). Polling for Changes Using the DirSync Control. Retrieved March 30, 2018.

[7] Lucand,G. (2018, February 18). Detect DCShadow, impossible?. Retrieved March 30, 2018.

## Defense

This type of attack technique cannot be easily mitigated with preventive controls since it is based on the abuse of AD design features. For example, mitigating specific AD API calls will likely have unintended side effects, such as preventing DC replicati

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures (6)

- [[Brute Force Login with MongoDB Query Injection]]
- [[Checksum Validation Exploitation for Active Directory]]
- [[NoSQL Injection: Extract User Data]]
- [[PrintNightmare - Exploiting CVE to gain SYSTEM shell on DC via Anonymous SMB Server]]
- [[Server Side Template Injection with Twig Template Rendering]]
- [[Twig Template Remote Code Execution]]
