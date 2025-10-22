---
id: 8838e226-1119-4892-8eef-b3a2a3c48eb5
name: MYSQL File Content Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:34.775623+00:00'
updated_at: '2023-04-10T20:22:51.242098+00:00'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Read content of a file]]'
commands:
- '[[Check file privileges]]'
- '[[Grant file privileges to root user for all databases]]'
- '[[Load file into memory]]'
---

# MYSQL File Content Extraction

## Summary

This procedure focuses on extracting the contents of a file through MYSQL Injection. This can be achieved by exploiting the MYSQL server to execute unauthorized commands, which can result in the extraction of sensitive data. The attacker can use this procedure to gain access to confidential informa

## Description

# Description

This procedure focuses on extracting the contents of a file through MYSQL Injection. This can be achieved by exploiting the MYSQL server to execute unauthorized commands, which can result in the extraction of sensitive data. The attacker can use this procedure to gain access to confidential information such as passwords, configuration files, and other sensitive data. The technical explanation of this procedure involves exploiting the MYSQL server to execute unauthorized commands to read the contents of files. The business value of this procedure is that it can be used to gain access to sensitive data and use it for malicious purposes.

## Requirements

1. Access to MYSQL server

1. Knowledge of MYSQL Injection techniques

## Defense

1. Ensure that MYSQL server is up-to-date with the latest security patches

1. Limit access to MYSQL server to authorized personnel only

1. Implement strict file permissions to prevent unauthorized access to sensitive files

## Objectives

1. Extract the contents of a file through MYSQL Injection

1. Gain access to sensitive data such as passwords and configuration files

# Instructions

1. chmod

**Code**: [[filepriv]]

> The 'chmod' command is used to change the permission of a file or directory. The arguments for this command are the permission setting (e.g. 755), followed by the file or directory that the permission should be applied to. The permission setting is a three-digit number, where the first digit represents the permission for the owner of the file, the second digit represents the permission for the group owner of the file, and the third digit represents the permission for all other users. Each digit is a sum of the following values: 4 for read permission, 2 for write permission, and 1 for execute permission. For example, a permission setting of 755 gives the owner of the file read, write, and execute permissions, and all other users read and execute permissions.

**Command** ([[Check file privileges]]):

```bash
filepriv
```

2. To resolve this issue, you can either disable the secure-file-priv option or move the file to the directory specified by the option.

**Code**: [[ERROR 1290 (HY000): The MySQL server is running wi]]

> The secure-file-priv option restricts the location from which files can be loaded using LOAD DATA INFILE or SELECT ... INTO OUTFILE statements. This error occurs when a file is attempted to be loaded from a directory that is not allowed by the secure-file-priv option.

3. This command is used to retrieve the password file from the server. It uses the LOAD_FILE function in MySQL to read the contents of the file and return it as a result set.

**Code**: [[' UNION ALL SELECT LOAD_FILE('/etc/passwd') --]]

> The argument '/etc/passwd' specifies the location of the password file on the server. It is a common file used by Unix-based operating systems to store user account information. This command can be used by attackers to gain access to sensitive information such as usernames and hashed passwords.

4. This command can be used to extract PHP code from a web server that uses MySQL as its database management system. The 'LOAD_FILE' function is used to read the contents of the specified file and the 'TO_base64' function is used to encode the contents in base64 format. The 'UNION ALL SELECT' statement is used to combine the encoded contents with the results of a valid SQL query.

**Code**: [[UNION ALL SELECT TO_base64(LOAD_FILE('/var/www/htm]]

> The 'LOAD_FILE' function takes a file path as its argument and returns the contents of the file. The 'TO_base64' function is used to encode the contents of the file in base64 format, which can be decoded later. The 'UNION ALL SELECT' statement is used to combine the encoded contents with the results of a valid SQL query. This can be used to extract sensitive information from the database, such as user credentials or other confidential data.

5. running a Linux or Unix system, the root user is the most powerful user on the system with full administrative privileges. The root user can perform any operation on the system, including modifying system files and installing or removing software packages. It is important to use the root user account with caution and only when necessary.

**Code**: [[root]]

> The 'root' in this command refers to the root user account on a Linux or Unix system. This command is often used to check information about the root user, such as the user ID (UID) or group ID (GID).

6. This command is used to load a file into the database.

**Code**: [[LOAD_FILE]]

> The LOAD_FILE command allows you to load a file into the database. This can be useful for importing data or restoring a backup. The command takes the path to the file as an argument. Once the file is loaded, you can re-enable any disabled indexes or constraints.

**Command** ([[Load file into memory]]):

```bash
LOAD_FILE file.txt
```

7. This command grants file permissions to the specified user on all databases and tables. The 'root'@'localhost' specifies the user and host that the permissions are being granted to. The FLUSH PRIVILEGES command is used to reload the grant tables in case any changes were made.

**Code**: [[GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRI]]

> The GRANT FILE command is used to grant file access to a user account. The *.* specifies that the permissions are being granted to all databases and tables. The TO 'root'@'localhost' specifies the user and host that the permissions are being granted to. The FLUSH PRIVILEGES command is used to reload the grant tables in case any changes were made.

**Command** ([[Grant file privileges to root user for all databases]]):

```bash
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
```

## Commands Used

- [[Check file privileges]]
- [[Grant file privileges to root user for all databases]]
- [[Load file into memory]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Read content of a file]]
