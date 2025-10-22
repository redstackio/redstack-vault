---
id: ea729a92-2dce-4865-848d-30bc9daa929a
name: DB2 Injection - System Environment Information Query
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.156000+00:00'
updated_at: '2023-04-10T20:22:02.267615+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Hostname/IP and OS INFO]]'
commands:
- '[[Query System Information]]'
---

# DB2 Injection - System Environment Information Query

## Summary

DB2 Injection is a technique used to exploit vulnerabilities in a DB2 database to gain unauthorized access to sensitive information. The 'System Environment Information Query' command can be used to obtain detailed information about the host system, including the hostname, IP address, and operating

## Description

# Description

DB2 Injection is a technique used to exploit vulnerabilities in a DB2 database to gain unauthorized access to sensitive information. The 'System Environment Information Query' command can be used to obtain detailed information about the host system, including the hostname, IP address, and operating system version. This information can be used to plan further attacks against the system.

To execute this attack, an attacker would need to identify a vulnerability in the DB2 database and use SQL injection techniques to inject malicious code into the database query. Once the code is executed, the attacker can extract the system information.

This attack can result in a data breach and compromise the confidentiality of sensitive information stored in the DB2 database. It can also lead to system downtime and damage to the organization's reputation.

## Requirements

1. Access to a vulnerable DB2 database

1. Knowledge of SQL injection techniques

## Defense

1. Regularly patch and update the DB2 database to prevent known vulnerabilities from being exploited.

1. Implement secure coding practices to prevent SQL injection attacks.

1. Monitor database activity for suspicious behavior and limit access to sensitive information.

## Objectives

1. Obtain detailed information about the host system, including the hostname, IP address, and operating system version.

# Instructions

1. This command retrieves information about the system environment, including the operating system name, version, release, and host name. It requires privileges to execute, and can only be run from procedures or UDFs.

**Code**: [[select os_name,os_version,os_release,host_name fro]]

> The 'select' statement is used to retrieve data from the 'sysibmadm.env_sys_info' table, which contains information about the system environment. The 'os_name' column returns the name of the operating system, while 'os_version' returns the version and 'os_release' returns the release. The 'host_name' column returns the name of the host machine. Note that this command can only be executed from procedures or UDFs, and requires privileges to run.

**Command** ([[Query System Information]]):

```bash
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Query System Information]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Hostname/IP and OS INFO]]
