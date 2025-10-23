---
id: 12668a66-533e-42d3-8f0a-6d59938c404d
name: Linux Privilege Escalation Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.422827+00:00'
updated_at: '2023-04-10T20:34:36.492276+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]'
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
- '[[Sudo|T1169 - Sudo]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[Tools]]'
commands:
- '[[Download lse.sh script]]'
- '[[Download lse.sh script using curl]]'
- '[[LinEnum with keyword search and reporting]]'
- '[[Run lse.sh script with level 1 verbosity]]'
- '[[Run lse.sh script with level 2 verbosity]]'
---

# Linux Privilege Escalation Enumeration

## Summary

Linux Privilege Escalation Enumeration is a procedure used to identify potential privilege escalation paths on a Linux system. This procedure involves the use of enumeration tools such as LinPEAS, Linux Smart Enumeration, and LinEnum.sh. The objective of this procedure is to identify misconfigurati

## Description

# Description

Linux Privilege Escalation Enumeration is a procedure used to identify potential privilege escalation paths on a Linux system. This procedure involves the use of enumeration tools such as LinPEAS, Linux Smart Enumeration, and LinEnum.sh. The objective of this procedure is to identify misconfigurations or vulnerabilities that can be exploited to escalate privileges from a low-privileged user to a higher privileged user or root. This procedure is commonly used by penetration testers and red teamers to assess the security posture of Linux systems.

 

## Requirements

1. Access to a Linux system

1. Enumeration tools such as LinPEAS, Linux Smart Enumeration, and LinEnum.sh

 

## Defense

1. Ensure that all Linux systems are properly configured and hardened

1. Implement the principle of least privilege to limit the access of low-privileged users

1. Regularly monitor and review system logs for any suspicious activity

 

## Objectives

1. Identify potential privilege escalation paths on a Linux system

1. Assess the security posture of a Linux system

1. Provide recommendations for securing the Linux system

 

# Instructions

1. To use this script, download it using either wget or curl command. After downloading, run the script using the following commands:

./linpeas.sh -a # Run all checks, this will perform deeper system enumeration but it takes longer to complete.
./linpeas.sh -s # Run in superfast and stealth mode, this will bypass some time-consuming checks. In stealth mode, nothing will be written to the disk.
./linpeas.sh -P # Pass a password that will be used with sudo -l and bruteforcing other users.

 



**Code**: [[wget "https://github.com/carlospolop/PEASS-ng/rele]]



> The LinPEAS script is a tool used for privilege escalation in Linux. It performs a thorough system enumeration to identify potential vulnerabilities that can be exploited to escalate privileges. The script can be run in different modes depending on the level of system enumeration required. The -a option runs all checks, which performs deeper system enumeration but takes longer to complete. The -s option runs in superfast and stealth mode, which bypasses some time-consuming checks. In stealth mode, nothing will be written to the disk. The -P option allows you to pass a password that will be used with sudo -l and bruteforcing other users.

2. To use this tool, run the following commands:
1. `wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh` or `curl "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -o lse.sh` to download the script.
2. Run `./lse.sh -l1` to show interesting information that should help you to privesc.
3. Run `./lse.sh -l2` to dump all the information it gathers about the system.

 



**Code**: [[wget "https://raw.githubusercontent.com/diego-trei]]



> Linux Smart Enumeration is a set of enumeration tools for pentesting and CTFs. This tool can be used to gather useful information about a Linux system that can help with privilege escalation. To use this tool, you need to download the script using either `wget` or `curl` and then run it with the appropriate options. The `-l1` option will show interesting information that should help you to privesc, while the `-l2` option will dump all the information it gathers about the system.



**Command** ([[Download lse.sh script]]):

```bash
wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh
```





**Command** ([[Download lse.sh script using curl]]):

```bash
curl "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -o lse.sh
```





**Command** ([[Run lse.sh script with level 1 verbosity]]):

```bash
./lse.sh -l1
```





**Command** ([[Run lse.sh script with level 2 verbosity]]):

```bash
./lse.sh -l2
```



3. The LinEnum script is used for scripted local Linux enumeration and privilege escalation checks. The script can be run with various options and arguments to perform specific checks and generate reports. The available options are:
-s: Run in stealth mode
-k <keyword>: Search for specific keywords in the output
-r <report>: Generate a report of the findings
-e <directory>: Specify a directory to output the report
-t: Include thorough (slow) tests

 



**Code**: [[./LinEnum.sh -s -k keyword -r report -e /tmp/ -t]]



> The LinEnum.sh script is a useful tool for performing Linux enumeration and checking for privilege escalation opportunities. The -s option runs the script in stealth mode, which can help avoid detection. The -k option allows you to search for specific keywords in the output, which can be useful for finding specific information. The -r option generates a report of the findings, which can be saved to a file using the <report> argument. The -e option allows you to specify a directory to output the report. The -t option includes thorough (slow) tests, which can take longer to run but may provide more comprehensive results.



**Command** ([[LinEnum with keyword search and reporting]]):

```bash
./LinEnum.sh -s -k keyword -r report -e /tmp/ -t
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]
- [[Setuid and Setgid|T1166 - Setuid and Setgid]]
- [[Sudo|T1169 - Sudo]]

## Commands Used

- [[Download lse.sh script]]
- [[Download lse.sh script using curl]]
- [[LinEnum with keyword search and reporting]]
- [[Run lse.sh script with level 1 verbosity]]
- [[Run lse.sh script with level 2 verbosity]]

## Tags

- [[Linux - Privilege Escalation]]
- [[Tools]]


