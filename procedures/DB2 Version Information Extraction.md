---
id: 05ecd9dd-531d-4177-9465-76cbc9a9aa9a
name: DB2 Version Information Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.544071+00:00'
updated_at: '2023-04-10T20:21:57.257452+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[Version]]'
commands:
- '[[Retrieve database and instance service and build level]]'
- '[[Retrieve database product version]]'
- '[[Retrieve database service level]]'
- '[[Retrieve database version and timestamp]]'
- '[[Retrieve installed product information]]'
---

# DB2 Version Information Extraction

## Summary

DB2 Version Information Extraction is a technique used to identify the version of the DB2 database. This information can be useful for attackers to identify vulnerabilities or misconfigurations that can be exploited. Attackers can use this technique to identify the version of the DB2 database by ex

## Description

# Description

DB2 Version Information Extraction is a technique used to identify the version of the DB2 database. This information can be useful for attackers to identify vulnerabilities or misconfigurations that can be exploited. Attackers can use this technique to identify the version of the DB2 database by executing a specially crafted query against the database. This query can be executed through various means such as a web application or directly through the command line.

Technical Explanation:
When an attacker sends a specially crafted query to the DB2 database, the database responds with the version information. This query can be executed through various means such as a web application or directly through the command line. This technique can be used to identify the version of the DB2 database and determine if it is vulnerable to known exploits.

Business Value:
By identifying the version of the DB2 database, organizations can better understand their security posture and identify potential vulnerabilities that need to be addressed. This technique can also be used by organizations to test the effectiveness of their security controls and identify areas for improvement.

 

## Requirements

1. Access to the DB2 database

1. Knowledge of SQL queries

 

## Defense

1. Ensure that the DB2 database is properly configured and up-to-date with the latest security patches

1. Implement proper access controls to limit who can access the database

1. Regularly monitor the database for unauthorized access or suspicious activity

 

## Objectives

1. Identify the version of the DB2 database

1. Determine if the database is vulnerable to known exploits

1. Assess the effectiveness of security controls

 

# Instructions

1. This command provides database version information.

 



**Code**: [[select versionnumber, version_timestamp from sysib]]



> The 'sysibm.sysversions' table contains information about the database version number and the timestamp of the version. The 'sysproc.env_get_inst_info()' function returns information about the instance, including the service level. The 'getvariable('sysibm.version')' function returns the version of the database. The 'sysproc.env_get_prod_info()' function returns information about the installed products, including the product release and the installed product fullname. The 'sysibmadm.env_inst_info' table contains information about the instance, including the service level and the build level.



**Command** ([[Retrieve database version and timestamp]]):

```bash
select versionnumber, version_timestamp from sysibm.sysversions;
```





**Command** ([[Retrieve database service level]]):

```bash
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo
```





**Command** ([[Retrieve database product version]]):

```bash
select getvariable('sysibm.version') from sysibm.sysdummy1 -- (v8+)
```





**Command** ([[Retrieve installed product information]]):

```bash
select prod_release,installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo
```





**Command** ([[Retrieve database and instance service and build level]]):

```bash
select service_level,bld_level from sysibmadm.env_inst_info
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve database and instance service and build level]]
- [[Retrieve database product version]]
- [[Retrieve database service level]]
- [[Retrieve database version and timestamp]]
- [[Retrieve installed product information]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[Version]]


