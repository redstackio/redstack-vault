---
id: 4d390b1c-23b7-4844-8350-8fd5658434e0
name: MSSQL Injection - List Permissions
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.167537+00:00'
updated_at: '2023-04-10T20:22:47.315515+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[List permissions]]'
- '[[MSSQL Injection]]'
commands:
- '[[Check database permissions]]'
- '[[Check If User is a sysadmin]]'
- '[[Check Server Permissions]]'
- '[[View Permissions for Sales.vIndividualCustomer]]'
---

# MSSQL Injection - List Permissions

## Summary

MSSQL Injection is a technique used to exploit SQL Injection vulnerabilities in Microsoft SQL Server. This specific procedure focuses on listing permissions in the server and databases. By exploiting these vulnerabilities, an attacker can gain access to sensitive information, modify or delete data,

## Description

# Description

MSSQL Injection is a technique used to exploit SQL Injection vulnerabilities in Microsoft SQL Server. This specific procedure focuses on listing permissions in the server and databases. By exploiting these vulnerabilities, an attacker can gain access to sensitive information, modify or delete data, and even take control of the server. To list permissions, the attacker can use commands such as Server Permissions Listing, Database Permissions Listing, View Permissions, and Check Server Role Membership. This procedure can be used by attackers to gain a better understanding of the target environment and identify potential targets for further exploitation.

From a technical perspective, MSSQL Injection works by injecting malicious SQL code into user inputs, such as login forms or search fields. This code is then executed by the server, allowing the attacker to manipulate the database and execute arbitrary commands. From a business perspective, this attack can result in data theft, data manipulation, and server compromise, leading to reputational damage, financial losses, and legal consequences.

 

## Requirements

1. Access to a vulnerable Microsoft SQL Server

1. Knowledge of SQL Injection techniques

1. Access to a tool capable of executing SQL Injection attacks

 

## Defense

1. Implement input validation and sanitization techniques to prevent SQL Injection vulnerabilities

1. Enforce the principle of least privilege by limiting user permissions to only what is necessary

1. Monitor SQL Server logs for suspicious activity and unauthorized access attempts

 

## Objectives

1. List server and database permissions

1. Identify potential targets for further exploitation

 

# Instructions

1. This command lists all of the effective permissions that the current user has on the server. The output will include details such as the type of permission, the object that the permission applies to, and the grantor of the permission. This command can be useful for troubleshooting permission issues or auditing user access to the server.

 



**Code**: [[SELECT * FROM fn_my_permissions(NULL, 'SERVER');]]



> The 'fn_my_permissions' function takes two arguments: the object for which to retrieve permissions (in this case, 'NULL' indicates the entire server), and the type of object ('SERVER' in this case). The output of the function will return a table with columns for the permission name, the permission state, the permission type, the permission object name, the principal name, and the grantor name.



**Command** ([[Check Server Permissions]]):

```bash
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```



2. This command retrieves a list of all the permissions that the current user has on the database.

 



**Code**: [[SELECT * FROM fn_my_permissions (NULL, 'DATABASE')]]



> The 'fn_my_permissions' function is used to retrieve the permissions of the current user on the database. The first argument specifies the object for which the permissions are being retrieved, and in this case, it is set to NULL to retrieve permissions for the current database. The second argument specifies the type of object for which permissions are being retrieved, and in this case, it is set to 'DATABASE' to retrieve database-level permissions. The command returns a table with columns for the permission name, the permission type, and whether the permission is granted or denied.



**Command** ([[Check database permissions]]):

```bash
SELECT * FROM fn_my_permissions (NULL, 'DATABASE');
```



3. To list the effective permissions of the current user on a view, execute the following SQL query:

 

This command will return a list of permissions that the current user has on the specified view. The results will be ordered by subentity_name and permission_name. The subentity_name column will contain the name of the view, and the permission_name column will contain the name of the permission (e.g. SELECT, INSERT, UPDATE, DELETE).



**Command** ([[View Permissions for Sales.vIndividualCustomer]]):

```bash
SELECT * FROM fn_my_permissions('Sales.vIndividualCustomer', 'OBJECT') ORDER BY subentity_name, permission_name;
```



4. Specify the server role you want to check membership for in the argument of the is_srvrolemember function.

 



**Code**: [[-- possible roles: sysadmin, serveradmin, dbcreato]]



> This command is used to determine if the current user is a member of a specified server role. The function is_srvrolemember takes a single argument, the name of the server role you want to check membership for. The possible server roles are: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin. The function will return a 1 if the user is a member of the specified server role, and a 0 if they are not.



**Command** ([[Check If User is a sysadmin]]):

```bash
-- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin
SELECT is_srvrolemember('sysadmin');
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Check database permissions]]
- [[Check If User is a sysadmin]]
- [[Check Server Permissions]]
- [[View Permissions for Sales.vIndividualCustomer]]

## Tags

- [[List permissions]]
- [[MSSQL Injection]]


