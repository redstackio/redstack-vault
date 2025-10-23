---
id: a02acd1f-2583-487d-849c-bb94e1a422c1
name: AdminCount Abuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.381712+00:00'
updated_at: '2023-04-10T20:26:29.938154+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Groups]]'
- '[[Dangerous Built-in Groups Usage]]'
commands:
- '[[adsisearcher]]'
- '[[crackmapexec ldap]]'
- '[[Get-ADGroup]]'
- '[[Get-ADUser]]'
- '[[jq]]'
- '[[python ldapdomaindump]]'
- '[[Query AdminSDHolder]]'
- '[[Set Admin Count]]'
---

# AdminCount Abuse

## Summary

AdminCount Abuse is a technique used by attackers to escalate privileges in Active Directory environments. This technique involves modifying the AdminCount attribute of a user or group to gain administrative privileges. The AdminCount attribute is used by Active Directory to determine if a user or 

## Description

# Description

AdminCount Abuse is a technique used by attackers to escalate privileges in Active Directory environments. This technique involves modifying the AdminCount attribute of a user or group to gain administrative privileges. The AdminCount attribute is used by Active Directory to determine if a user or group should be protected by the AdminSDHolder object, which in turn applies a set of security permissions to the object. By setting the AdminCount attribute to 1, an attacker can gain administrative privileges over the object. This technique can be used to gain access to sensitive resources, such as domain controllers or critical infrastructure.

 

## Requirements

1. Authenticated access to Active Directory environment

1. Permission to modify AdminCount attribute

 

## Defense

1. Regularly review and remove unnecessary administrative privileges

1. Monitor for changes to AdminCount attribute

1. Implement strict access controls for critical resources

 

## Objectives

1. Escalate privileges in Active Directory environment

1. Gain access to sensitive resources

 

# Instructions

1. To disable ACL overwrite on the AdminSDHolder object, follow these steps:
1. Open ADSI Edit on the domain controller
2. Connect to the Default Naming Context
3. Navigate to CN=System
4. Locate the CN=AdminSDHolder object
5. Right-click the object and select Properties
6. Locate the adminCount attribute and set it to 0
7. Click OK to save changes

 



**Code**: [[CN=AdminSDHolder,CN=System]]



> The AdminSDHolder object is a security feature in Active Directory that ensures that specific security settings are applied to protected accounts and groups. By default, these settings are reapplied every hour, which can overwrite any changes made to the ACLs of these objects. To prevent this from happening, the adminCount attribute on the AdminSDHolder object can be set to 0, which disables the ACL overwrite feature. This command provides instructions on how to disable ACL overwrite on the AdminSDHolder object using ADSI Edit.



**Command** ([[Query AdminSDHolder]]):

```bash
CN=AdminSDHolder,CN=System
```



2. Use this command to set or view the minimum count of a certain item or element.

 



**Code**: [[&quot;dminCount]]



> The argument for this command should be the name or ID of the item or element you want to set or view the minimum count for. This command is useful for inventory management or tracking the availability of certain resources. The minimum count can be set to any number and will trigger a notification when the count falls below that number.

3. The attribute value assignment command assigns a value to an HTML element attribute.

 



**Code**: [[0]]



> The command takes two arguments: the attribute name and the attribute value. The attribute name specifies which attribute of the HTML element to assign the value to. The attribute value is the value to be assigned to the attribute. For example, the command 'attribute to src 'https://example.com/image.jpg'' assigns the value 'https://example.com/image.jpg' to the 'src' attribute of an HTML element.

4. To search for users based on their admin count, use the following command:

 



**Code**: [[AdminCount=1]]



> The 'AdminCount' argument is used to specify the number of administrators associated with the user account. In this case, we are searching for users with only one administrator associated with their account. This command can be useful when auditing user accounts to ensure that only authorized personnel have administrative access.



**Command** ([[Set Admin Count]]):

```bash
AdminCount=1
```



5. To find users and groups with AdminCount set to 1, you can use any of the following commands:

 



**Code**: [[crackmapexec ldap 10.10.10.10 -u username -p passw]]



> The AdminCount attribute is used to keep track of the number of times an object has been added to a group with administrative privileges. By default, this attribute is set to 0. However, when an object is added to a group with administrative privileges, the AdminCount attribute is incremented by 1.

The provided commands will search for users and groups with AdminCount set to 1:
- crackmapexec ldap
- python ldapdomaindump.py
- jq
- Get-ADUser
- Get-ADGroup
- adsisearcher

Please note that these commands require different arguments and may have different output formats. Refer to the documentation of each command for more information.



**Command** ([[crackmapexec ldap]]):

```bash
10.10.10.10 -u username -p password --admin-count
```





**Command** ([[python ldapdomaindump]]):

```bash
-u example.com\john -p pass123 -d ';' 10.10.10.10
```





**Command** ([[jq]]):

```bash
'.[].attributes | select(.adminCount == [1]) | .sAMAccountName[]' domain_users.json
```





**Command** ([[Get-ADUser]]):

```bash
-LDAPFilter "(objectcategory=person)(samaccountname=*)(admincount=1)"
```





**Command** ([[Get-ADGroup]]):

```bash
-LDAPFilter "(objectcategory=group) (admincount=1)"
```





**Command** ([[adsisearcher]]):

```bash
"(AdminCount=1)"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]

## Commands Used

- [[adsisearcher]]
- [[crackmapexec ldap]]
- [[Get-ADGroup]]
- [[Get-ADUser]]
- [[jq]]
- [[python ldapdomaindump]]
- [[Query AdminSDHolder]]
- [[Set Admin Count]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Groups]]
- [[Dangerous Built-in Groups Usage]]


