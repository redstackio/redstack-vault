---
id: 4517d0ec-f638-4fa0-af82-1de3ffcd1bc8
name: Basic Linux Users and Permissions
type: cheatsheet
verified: true
created_at: '2020-03-10T08:17:54.447090+00:00'
updated_at: '2023-05-30T20:06:41.053468+00:00'
---

# Basic Linux Users and Permissions

**Status**: ✓ Verified

# Description

Very basic overview of Linux filesystem permissions

## File Permissions

**Code**: [[-rwxr-xr-x 1 root root 1.2M Nov 10 05:45 /bin/bash]]

- three sets of three permissions (rwx) (listed from left to right): user, group, other

- each set of privileges are: (r)ead, (w)rite, e(x)ecute (rwx)

- these dictate who can access files and what they can do

## Folder Permissions

**Code**: [[drwxr-xr-x   3 root root   4.0K Mar 10 03:57 home]]

- first field is a "d" indicating directory

- user, group, other permissions stay the same

- read and write bit stay the same, but x controls whether a user can "cd" into the directory

System users are found in /etc/passwd

System groups are found in /etc/group

**Command** ([[Add a User on a Linux System]]):

```bash
adduser $_NAME
```

**Command** ([[Change Ownership of a Folder Recursively]]):

```bash
chown  -R $_USER:$_GROUP $_PATH
```

**Command** ([[Change File Permissions to rwxrw-rw-]]):

```bash
chmod 755 $_FILENAME
```

## Numerical File Permissions

Permissions are determined by:

- 1 = execute

- 2 = write

- 4 = read

Add together for the effective permissions.

eg: read + write = 6

Command like chmod accept numerical permissions

eg. Set full control for user/group, and read only for others:

**Code**: [[chmod 774 /path/to/somefile]]

## Special Bit Permissoins

**SUID**

-rwsr-xr-x 1 root root 119K Mar 10 08:31 priv

- users who execute the file execute it as the owner

- many programs have legitimate uses of SUID, though vulnerabilities can be catastrophic

**GUID**

drwxr-srwx 2 root root    6 Mar 10 08:36 test

- users who create files in the directory create them with the group rights of the creator

- useful for sharing files across users and groups

## passwd File Structure

user:password:userid:groupid:usercomment:homedir:shell

bob:x:1000:1000:Mark,,,:/home/alice:/bin/bash

## shadow File Structure

user:password:lastpasschanged:minpasschange:maxpasschange:warnpass:expireafterinactive:dayssinceexpired

bob:$1$NtYp9mSe$Lc6zOjqaSLxBaJ7QXlGuj1:18331:0:99999:7:::

## Common Shadow Password Formats

- $1$ - MD5

- $2a$ - Blowfish

- $2y$ - Blowfish

- $5$ - SHA-256

- $6$ - SHA-512

**Command** ([[mkpasswd Generate a MD5 Hash]]):

```bash
mkpasswd -5 -S $_SALT $_PASSWORD
```
