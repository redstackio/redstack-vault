---
id: 905f2bc5-61ff-4235-9951-60c199116e86
name: Password in AD User Comment Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.416196+00:00'
updated_at: '2023-04-10T20:26:06.599574+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Password in AD User comment]]'
commands:
- '[[Change user password]]'
- '[[Check if user exists]]'
- '[[Convert password to unicode]]'
- '[[Create Password File]]'
- '[[Get Description Users]]'
- '[[Get User Descriptions]]'
- '[[ldapdomaindump]]'
- '[[Search for a string within a file]]'
---

# Password in AD User Comment Enumeration

## Summary

Password in AD User Comment Enumeration is a technique used to extract passwords that are saved in the description field of an Active Directory user account. This technique can be used to gain access to a domain user's password, which can then be used to escalate privileges and move laterally withi

## Description

# Description

Password in AD User Comment Enumeration is a technique used to extract passwords that are saved in the description field of an Active Directory user account. This technique can be used to gain access to a domain user's password, which can then be used to escalate privileges and move laterally within the network. The technique involves extracting the password from the user comment field using various commands and tools such as LDAP User Description Enumeration and Search for Patterns using Grep Command.

## Requirements

1. Access to Active Directory

1. Authentication credentials

## Defense

1. Ensure that sensitive information is not stored in the user comment field

1. Implement strong password policies to prevent password reuse

1. Monitor for unusual activity in the network, such as unusual logins or privilege escalation

## Objectives

1. Extract passwords from Active Directory user comment field

1. Gain access to domain user's password

1. Escalate privileges and move laterally within the network

# Instructions

1. To enumerate user descriptions in LDAP, use the crackmapexec tool with the 'user-desc' module. Provide the domain or IP address, username, and password as arguments. Alternatively, you can use the 'get-desc-users' module with the '--kdcHost' option to specify the KDC host. The output will show the list of users and their descriptions.

**Code**: [[$ crackmapexec ldap domain.lab -u 'username' -p 'p]]

> The 'user-desc' module of crackmapexec is used to enumerate user descriptions in LDAP. It requires the domain or IP address, username, and password as arguments. The 'get-desc-users' module can also be used with the '--kdcHost' option to specify the KDC host. The output shows the list of users and their descriptions. This information can be useful for reconnaissance and identifying potential targets for further exploitation.

**Command** ([[Get User Descriptions]]):

```bash
$ crackmapexec ldap domain.lab -u 'username' -p 'password' -M user-desc

```

**Command** ([[Get Description Users]]):

```bash
$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 -M get-desc-users

```

2. To retrieve the common fields in an AD schema, use the following commands:
- Get-ADObject -SearchBase 'CN=Schema,CN=Configuration,DC=domain,DC=com' -Filter {name -eq 'objectClass'} -Properties MayContain, SystemMayContain
- Get-ADObject -SearchBase 'CN=Schema,CN=Configuration,DC=domain,DC=com' -Filter {name -eq 'attributeSchema'} -Properties LDAPDisplayName, linkID, syntax, isSingleValued, description
- Get-ADObject -SearchBase 'CN=Schema,CN=Configuration,DC=domain,DC=com' -Filter {name -eq 'classSchema'} -Properties LDAPDisplayName, subClassOf, auxiliaryClass, mustContain, systemMustContain, mayContain, systemMayContain, description

Note: Replace 'domain' with your domain name.

**Code**: [[UserPassword]]

> The first command retrieves the objectClass attribute, which contains the list of classes that can be instantiated in the AD schema. The MayContain and SystemMayContain properties of each class contain the list of attributes that can be used with that class. 

The second command retrieves the attributeSchema, which contains the definition of each attribute in the AD schema. The LDAPDisplayName property contains the name of the attribute, the linkID property contains the unique identifier of the attribute, the syntax property contains the data type of the attribute, the isSingleValued property indicates whether the attribute can have multiple values, and the description property contains a description of the attribute. 

The third command retrieves the classSchema, which contains the definition of each class in the AD schema. The LDAPDisplayName property contains the name of the class, the subClassOf property contains the name of the parent class, the auxiliaryClass property contains the list of auxiliary classes that can be used with the class, the mustContain and systemMustContain properties contain the list of attributes that must be present when an object of the class is created, the mayContain and systemMayContain properties contain the list of attributes that can be used with the class, and the description property contains a description of the class.

**Command** ([[Create Password File]]):

```bash
echo 'UserPassword' > password.txt
```

3. To change the password of a Unix user, use the 'passwd' command followed by the username whose password you want to change.

**Code**: [[UnixUserPassword]]

> The 'passwd' command is used to change the password of a Unix user. When you run the command, you will be prompted to enter the current password for the user, followed by the new password. The password you enter will not be displayed on the screen for security purposes. If you do not have the necessary permissions to change the password of a user, you will receive an error message. The syntax of the command is as follows: 

passwd [username]

Arguments:
- username: The name of the Unix user whose password you want to change.

**Command** ([[Check if user exists]]):

```bash
grep -c '^username:' /etc/passwd
```

**Command** ([[Change user password]]):

```bash
passwd username
```

4. To set a Unicode password, the value must be in the form of a UTF-16 encoded string and enclosed in quotes.

**Code**: [[unicodePwd]]

> The 'unicodePwd' attribute is used to set a user's password in Active Directory using a UTF-16 encoded string. This attribute is write-only and cannot be read. To set the value of this attribute, the password must be enclosed in quotes and encoded in UTF-16. For example, the password 'MyPassword123' would be encoded as '0x4D 0x00 0x79 0x00 0x50 0x00 0x61 0x00 0x73 0x00 0x73 0x00 0x77 0x00 0x6F 0x00 0x72 0x00 0x64 0x00 0x31 0x00 0x32 0x00 0x33 0x00'.

**Command** ([[Convert password to unicode]]):

```bash
unicodePwd
```

5. This command is used to manage the password for the Microsoft Services for UNIX 3.0 (SFU) Active Directory user object. This command can be used to set, change, or delete the password for an SFU Active Directory user object.

**Code**: [[msSFU30Password]]

> The 'msSFU30Password' attribute is used to store the password for an SFU Active Directory user object. The password can be set using the '-s' option followed by the password value. The password can be changed using the '-c' option followed by the current password and the new password. The password can be deleted using the '-d' option. It is important to note that the password is stored in encrypted form and cannot be retrieved or viewed using this command.

6. To retrieve user account information, run the following command:

- For Linux: enum4linux | grep -i desc

- For Windows: Get-WmiObject -Class Win32_UserAccount -Filter "Domain='COMPANYDOMAIN' AND Disabled='False'" | Select Name, Domain, Status, LocalAccount, AccountType, Lockout, PasswordRequired, PasswordChangeable, Description, SID

Replace 'COMPANYDOMAIN' with the name of your domain.

**Code**: [[enum4linux | grep -i desc

Get-WmiObject -Class Wi]]

> This command retrieves information about user accounts on the specified domain. For Linux, the 'enum4linux' command is used to enumerate information about users and groups on the target system, and the 'grep' command is used to filter the output to only show the 'Description' field. For Windows, the 'Get-WmiObject' command is used to query the Windows Management Instrumentation (WMI) for information about user accounts. The 'Select' command is used to choose which fields to display in the output.

7. The grep command is used to search for specific patterns in a file or a set of files. It can search for a single pattern or multiple patterns at once. The basic syntax for using the grep command is as follows:

$ grep [options] pattern [file(s)]

Here, options are the various flags or switches that can be used with the command. The pattern is the string or regular expression that you want to search for. And file(s) are the file or set of files that you want to search in.

For example, to search for the word 'example' in a file named 'test.txt', you can use the following command:

$ grep example test.txt

This will display all the lines in the file that contain the word 'example'.

**Code**: [[grep]]

> The arguments of the grep command are as follows:

1. pattern: This is the string or regular expression that you want to search for.

2. file(s): This is the file or set of files that you want to search in. If you do not specify any files, the command will read from standard input.

3. options: There are various options that can be used with the grep command to modify its behavior. Some of the commonly used options are:

- -i: This option makes the search case-insensitive.
- -r: This option searches for the pattern recursively in all the subdirectories.
- -v: This option displays all the lines that do not match the pattern.
- -c: This option displays only the count of lines that match the pattern.
- -n: This option displays the line numbers along with the matching lines.
- -w: This option matches the pattern only as a whole word.

**Command** ([[Search for a string within a file]]):

```bash
grep 'example' file.txt
```

8. Use the ldapdomaindump command to dump the Active Directory domain information.

The options used in the command are:
-u: Specifies the user account in the format 'DOMAIN\username'.
-p: Specifies the password for the user account.
-o: Specifies the output directory for the dump.

**Code**: [[ldapdomaindump -u 'DOMAIN\john' -p MyP@ssW0rd 10.1]]

> The ldapdomaindump command is used to dump the Active Directory domain information. This command requires authentication, so the user account and password must be specified using the -u and -p options, respectively. The -o option specifies the output directory for the dump.

This command can be useful in situations where you need to gather information about the Active Directory domain, such as during a penetration testing engagement or when troubleshooting issues with domain controllers.

**Command** ([[ldapdomaindump]]):

```bash
ldapdomaindump -u 'DOMAIN\john' -p MyP@ssW0rd 10.10.10.10 -o ~/Documents/AD_DUMP/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Change user password]]
- [[Check if user exists]]
- [[Convert password to unicode]]
- [[Create Password File]]
- [[Get Description Users]]
- [[Get User Descriptions]]
- [[ldapdomaindump]]
- [[Search for a string within a file]]

## Tags

- [[Active Directory Attacks]]
- [[Password in AD User comment]]
