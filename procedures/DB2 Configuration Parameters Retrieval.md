---
id: b57defa0-8e88-458a-992d-ce6cbb669256
name: DB2 Configuration Parameters Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:33.213247+00:00'
updated_at: '2023-04-10T20:22:01.172393+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
- '[[System Config]]'
commands:
- '[[Retrieve all the database configuration parameters values stored on disk]]'
- '[[Retrieve the automatic maintenance settings in the database configuration stored
  in memory]]'
---

# DB2 Configuration Parameters Retrieval

## Summary

DB2 Configuration Parameters Retrieval is a technique used to extract sensitive information from a DB2 database server. This technique is often used by attackers who have gained access to a web application that uses a DB2 database backend. The attacker can use this technique to extract database con

## Description

# Description

DB2 Configuration Parameters Retrieval is a technique used to extract sensitive information from a DB2 database server. This technique is often used by attackers who have gained access to a web application that uses a DB2 database backend. The attacker can use this technique to extract database configuration parameters such as usernames, passwords, and other sensitive information. This information can be used to further compromise the database server or other systems on the network.

To perform this technique, an attacker must first identify a vulnerable web application that uses a DB2 database backend. Once identified, the attacker can send specially crafted SQL queries to the database server that will return the desired configuration parameters. The attacker can then use this information to escalate privileges or perform other malicious activities.

The business value of this technique is that it allows attackers to gain access to sensitive information that can be used to compromise the security of the organization. By understanding how this technique works, organizations can take steps to secure their web applications and database servers to prevent these types of attacks.

## Requirements

1. Access to a vulnerable web application that uses a DB2 database backend

## Defense

1. Implement proper input validation and sanitization techniques to prevent SQL injection attacks

1. Enforce the principle of least privilege to limit the amount of information that can be accessed by attackers

1. Monitor database logs for suspicious activity

## Objectives

1. Retrieve database configuration parameters

1. Escalate privileges

1. Perform malicious activities

# Instructions

1. To retrieve the database configuration parameters, execute the following commands:
- Execute the first command to retrieve the automatic maintenance settings in the database configuration that are stored in memory for all database partitions.
- Execute the second command to retrieve all the database configuration parameters values stored on disk for all database partitions.

**Code**: [[select dbpartitionnum, name, value from sysibmadm.]]

> The 'select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%'' command retrieves the automatic maintenance settings in the database configuration that are stored in memory for all database partitions. The 'select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg' command retrieves all the database configuration parameters values stored on disk for all database partitions. Both commands require privilege to execute.

**Command** ([[Retrieve the automatic maintenance settings in the database configuration stored in memory]]):

```bash
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%' -- Requires priv.
```

**Command** ([[Retrieve all the database configuration parameters values stored on disk]]):

```bash
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg -- Requires priv.
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve all the database configuration parameters values stored on disk]]
- [[Retrieve the automatic maintenance settings in the database configuration stored in memory]]

## Tags

- [[DB2 Cheatsheet]]
- [[DB2 Injection]]
- [[System Config]]
