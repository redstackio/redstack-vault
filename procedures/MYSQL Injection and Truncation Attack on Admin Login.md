---
id: e93c0f46-f787-492e-ad79-30df40af468d
name: MYSQL Injection and Truncation Attack on Admin Login
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.886383+00:00'
updated_at: '2023-04-10T20:22:50.119050+00:00'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Truncation]]'
commands:
- '[[Check Admin Status]]'
- '[[Check Admin Status]]'
- '[[Set Username]]'
---

# MYSQL Injection and Truncation Attack on Admin Login

## Summary

The MYSQL Injection and Truncation Attack on Admin Login is a common tactic used by attackers to gain access to sensitive information. This attack leverages vulnerabilities in the MYSQL database to inject malicious code and truncate data, which can lead to unauthorized access to the system. In this

## Description

# Description

The MYSQL Injection and Truncation Attack on Admin Login is a common tactic used by attackers to gain access to sensitive information. This attack leverages vulnerabilities in the MYSQL database to inject malicious code and truncate data, which can lead to unauthorized access to the system. In this attack, the attacker attempts to log in to the admin account using a specially crafted username that contains malicious code. If successful, the attacker can gain access to sensitive information, such as customer data, financial records, and other confidential information.

Technical Explanation: The MYSQL Injection and Truncation Attack on Admin Login involves exploiting vulnerabilities in the MYSQL database to inject malicious code and truncate data. The attacker crafts a special username that contains malicious code and submits it to the login form. If the code is successful, the attacker can gain access to the system and steal sensitive information.

Business Value: This attack can have severe consequences for businesses, including financial losses, reputational damage, and legal repercussions. It is essential for organizations to take steps to protect their systems from these types of attacks.

 

## Requirements

1. Access to the login form

1. Knowledge of MYSQL Injection and Truncation techniques

 

## Defense

1. Use parameterized queries to avoid SQL Injection attacks

1. Implement input validation to prevent malicious code injection

1. Limit access to sensitive information to authorized personnel only

 

## Objectives

1. Gain unauthorized access to the admin account

1. Steal sensitive information

 

# Instructions

1. mysql -u [username] -p

 



**Code**: [[admin]]



> This command is used to log in to the MYSQL server as an administrator. Replace [username] with the actual username of the administrator. Once executed, the command will prompt for the administrator's password. After entering the correct password, the administrator will be logged in to the MYSQL server and can perform administrative tasks.



**Command** ([[Check Admin Status]]):

```bash
sudo su
whoami
exit

```



2. To log in as an admin, use the following credentials: username - admin, password - [password]

 



**Code**: [[admin]]



> The 'data' field contains the username attempted to log in. The 'text' field contains the password attempted to log in. The 'instruction' field provides the correct credentials to log in as an admin. The 'explain' field is not applicable for this command.



**Command** ([[Check Admin Status]]):

```bash
admin status
```



3. To create a new table with a username field, use the following SQL command:

 



**Code**: [[`username` varchar(20) not null]]



> This command creates a new table in a SQL database with a field called 'username'. The field is set to a maximum length of 20 characters and is required (not null). This field can be used to store unique usernames for users in a web application or other software system.

4. Use this command to set the username for the application.

 



**Code**: [[username = &quot;admin               a&quot;]]



> The `username` variable is being set to `admin               a`. This command is useful when you want to change the username for the application. The `=` sign is used to assign a value to the `username` variable. The value assigned to the `username` variable should be enclosed in double quotes (`&quot;`) to ensure that the value is properly interpreted by the application. You can replace `admin               a` with any desired username.



**Command** ([[Set Username]]):

```bash
username = &quot;admin               a&quot;
```



## Commands Used

- [[Check Admin Status]]
- [[Check Admin Status]]
- [[Set Username]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Truncation]]


