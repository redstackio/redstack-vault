---
id: 42c7baf8-e66a-4af5-bce3-c5dad16c8dc0
name: Non-Standard Port
type: technique
mitre_id: T1571
mitre_url: null
created_at: '2023-04-06T00:31:26.739949+00:00'
updated_at: '2023-04-06T03:56:35.284989+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Awk Interactive Reverse Shell]]'
- '[[Bash UDP Reverse Shell]]'
- '[[DB2 Injection - Time Delay]]'
- '[[MSSQL Time Based SQL Injection]]'
- '[[OpenSSL Reverse Shell]]'
- '[[Oracle SQL Injection Time-Based Attack]]'
- '[[Python Bind Shell]]'
---

# Non-Standard Port

**MITRE ID**: T1571

## Description

Adversaries may communicate using a protocol and port paring that are typically not associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (7)

- [[Awk Interactive Reverse Shell]]
- [[Bash UDP Reverse Shell]]
- [[DB2 Injection - Time Delay]]
- [[MSSQL Time Based SQL Injection]]
- [[OpenSSL Reverse Shell]]
- [[Oracle SQL Injection Time-Based Attack]]
- [[Python Bind Shell]]
