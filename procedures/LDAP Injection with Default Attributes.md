---
id: 969d7224-b118-4de7-8081-81b716c1372a
name: LDAP Injection with Default Attributes
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.659206+00:00'
updated_at: '2023-04-10T20:36:27.662307+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[Defaults attributes]]'
- '[[LDAP Injection]]'
commands:
- '[[Fields for User Creation]]'
---

# LDAP Injection with Default Attributes

## Summary

LDAP injection is a type of injection attack that targets LDAP-enabled applications. Attackers can use this technique to manipulate LDAP queries to retrieve unauthorized information or modify data. In this specific procedure, attackers use default attributes to perform the injection attack. By inje

## Description

# Description

LDAP injection is a type of injection attack that targets LDAP-enabled applications. Attackers can use this technique to manipulate LDAP queries to retrieve unauthorized information or modify data. In this specific procedure, attackers use default attributes to perform the injection attack. By injecting a payload like `*)(ATTRIBUTE_HERE=*`, attackers can retrieve all entries in the LDAP directory that contain the default attribute specified. This can be used to extract sensitive information such as usernames and passwords.

From a technical standpoint, LDAP injection occurs when user input is not properly sanitized and is included in an LDAP query without proper encoding or filtering. This allows attackers to modify the query to their liking and execute arbitrary code. The business value of this attack lies in its ability to extract sensitive information and potentially gain access to critical systems.

 

## Requirements

1. Access to an LDAP-enabled application

1. Knowledge of default attributes used in the application

1. Ability to execute LDAP queries

 

## Defense

1. Properly sanitize user input to prevent injection attacks

1. Implement access controls to limit the information that can be retrieved from the LDAP directory

1. Monitor LDAP queries for suspicious activity

 

## Objectives

1. Retrieve sensitive information from an LDAP-enabled application

1. Modify data in an LDAP directory

 

# Instructions

1. 

 



**Code**: [[*)(ATTRIBUTE_HERE=*]]



> This payload can be used to retrieve all entries in the LDAP directory that contain the default attribute specified.

2. 

 



**Code**: [[userPassword
surname
name
cn
sn
objectClass
mail
g]]



> These are some of the default attributes that can be used in an LDAP injection attack. By injecting the payload with one of these attributes, attackers can retrieve all entries in the LDAP directory that contain that attribute.



**Command** ([[Fields for User Creation]]):

```bash
userPassword
surname
name
cn
sn
objectClass
mail
givenName
commonName
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Commands Used

- [[Fields for User Creation]]

## Tags

- [[Defaults attributes]]
- [[LDAP Injection]]


