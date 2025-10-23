---
id: 5cb45f41-6083-415a-95ed-25dc70f57e71
name: Active Directory Recon using BloodHound Custom Queries
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.200748+00:00'
updated_at: '2023-04-10T20:25:51.102732+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Remote System Discovery|T1018 - Remote System Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Recon]]'
- '[[Using BloodHound]]'
commands:
- '[[Check BloodHound Custom Queries Path]]'
- '[[Viewing customqueries.json file]]'
---

# Active Directory Recon using BloodHound Custom Queries

## Summary

Active Directory Recon using BloodHound Custom Queries is a technique used by attackers to gain insight into an Active Directory environment. BloodHound is a tool that allows attackers to visualize the relationships between users, computers, and groups in an AD environment. This technique involves 

## Description

# Description

Active Directory Recon using BloodHound Custom Queries is a technique used by attackers to gain insight into an Active Directory environment. BloodHound is a tool that allows attackers to visualize the relationships between users, computers, and groups in an AD environment. This technique involves creating custom queries in BloodHound to identify high-value targets, such as privileged users or computers. The attacker can then use this information to plan their attack and move laterally within the network.

From a technical perspective, this technique involves creating custom queries in BloodHound using the 'Custom Query' and 'OR Operator' commands. These queries can be used to identify specific users, computers, or groups that the attacker is interested in. Once the queries are created, BloodHound will visualize the relationships between these entities, allowing the attacker to identify potential attack paths.

The business value of this technique lies in its ability to help attackers identify high-value targets within an AD environment. By identifying these targets, attackers can focus their efforts on compromising these entities and gaining access to sensitive data or systems.

 

## Requirements

1. Access to an Active Directory environment

1. BloodHound tool installed on the attacker's machine

 

## Defense

1. Limit access to sensitive systems and data to only authorized personnel

1. Implement strong password policies and multi-factor authentication

1. Regularly monitor the network for suspicious activity

 

## Objectives

1. Identify high-value targets within an Active Directory environment

1. Plan lateral movement within the network

 

# Instructions

1. To replace the customqueries.json file, follow these steps:
1. Open the terminal.
2. Navigate to the directory where the new customqueries.json file is located.
3. Copy the new customqueries.json file.
4. Navigate to the directory where the old customqueries.json file is located.
5. Paste the new customqueries.json file and replace the old one.

 



**Code**: [[/home/username/.config/bloodhound/customqueries.js]]



> This command is used to replace the customqueries.json file that is used by Bloodhound. The customqueries.json file contains custom queries that can be used to search for specific information within Bloodhound. By replacing this file, you can update the custom queries that are available to you. The 'data' field in the JSON object specifies the location of the customqueries.json file that will be replaced.



**Command** ([[Viewing customqueries.json file]]):

```bash
cat /home/username/.config/bloodhound/customqueries.json
```



2. To create a custom query with OR operator, follow the below steps:
1. Open BloodHound and go to the 'Queries' tab.
2. Click on the 'Custom' button and select 'Custom Query'.
3. In the 'Custom Query' window, click on the 'Edit' button next to the 'Query' field.
4. Enter the query using the OR operator in the desired format.
5. Click on 'Save' to save the query.
6. The saved query will be stored in the 'customqueries.json' file at the location 'C:\Users\USERNAME\AppData\Roaming\BloodHound\'.

 



**Code**: [[C:\Users\USERNAME\AppData\Roaming\BloodHound\custo]]



> The 'or' operator is used to combine two or more conditions in a query. It returns all the objects that satisfy any of the given conditions. For example, if we want to find all the users who have either 'Domain Admins' or 'Enterprise Admins' group membership, we can use the OR operator in our custom query as follows:

(user)-[MemberOf]->(group {name:'Domain Admins'}) or (user)-[MemberOf]->(group {name:'Enterprise Admins'})

This will return all the users who are either a member of the 'Domain Admins' or 'Enterprise Admins' group.



**Command** ([[Check BloodHound Custom Queries Path]]):

```bash
C:\Users\USERNAME\AppData\Roaming\BloodHound\customqueries.json
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Remote System Discovery|T1018 - Remote System Discovery]]

## Commands Used

- [[Check BloodHound Custom Queries Path]]
- [[Viewing customqueries.json file]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Recon]]
- [[Using BloodHound]]


