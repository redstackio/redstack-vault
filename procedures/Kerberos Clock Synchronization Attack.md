---
id: b11067ab-467c-4d10-bfa7-e16d37e41198
name: Kerberos Clock Synchronization Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:02.086832+00:00'
updated_at: '2023-04-10T20:36:13.210245+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
- '[[Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Clock Synchronization]]'
commands:
- '[[Fake time with faketime]]'
- '[[Nmap scan with service detection]]'
- '[[Set system time on Linux]]'
- '[[Set system time on Windows]]'
---

# Kerberos Clock Synchronization Attack

## Summary

The Kerberos Clock Synchronization Attack is a technique used to bypass Kerberos authentication by exploiting clock skew. Kerberos is a network authentication protocol that uses tickets to allow access to network resources. The Kerberos protocol relies on the clocks of the client and server being s

## Description

# Description

The Kerberos Clock Synchronization Attack is a technique used to bypass Kerberos authentication by exploiting clock skew. Kerberos is a network authentication protocol that uses tickets to allow access to network resources. The Kerberos protocol relies on the clocks of the client and server being synchronized to within a certain tolerance. If the clocks are not synchronized, the authentication process can fail. Attackers can exploit this by manipulating the system clock of the target computer to create a time difference that allows them to bypass authentication. This attack can be used to gain access to sensitive information and resources within an Active Directory environment.

 

## Requirements

1. Access to the target network.

1. Knowledge of the target Active Directory environment.

1. Tools to manipulate the system clock of the target computer.

 

## Defense

1. Ensure that all systems in the Active Directory environment have synchronized clocks.

1. Implement time-based access controls to limit the impact of clock skew.

1. Monitor network traffic for signs of Kerberos ticket manipulation.

 

## Objectives

1. Gain unauthorized access to sensitive information and resources within an Active Directory environment.

1. Bypass authentication mechanisms using Kerberos tickets.

1. Exploit clock skew to manipulate authentication processes.

 

# Instructions

1. To detect clock skew automatically with nmap, use the following command:

`nmap -sV -sC <target>`

This will perform a version and script scan on the target IP address and report the clock skew.

 



**Code**: [[$ nmap -sV -sC 10.10.10.10
clock-skew: mean: -1998]]



> The `nmap` command is a powerful tool for network exploration and security auditing. The `-sV` flag enables version detection, while the `-sC` flag enables running default scripts. By running these scans on a target IP address, `nmap` can detect the clock skew of the target system. Clock skew is the difference between the time reported by the system clock and the actual time. This can be caused by a variety of factors, including hardware issues, software bugs, and misconfigured time settings. Detecting clock skew can be useful for troubleshooting and security analysis, as it can help identify potential issues with system time synchronization and detect attempts to manipulate system time for malicious purposes.



**Command** ([[Nmap scan with service detection]]):

```bash
$ nmap -sV -sC 10.10.10.10
```



2. This command uses the nmap tool to scan for SMB2 Time on the target IP address 10.10.10.10 and port 445. The smb2-time script is used to retrieve the time difference between the target and the scanning machine. The -vv flag is used to increase the verbosity of the output.

 



**Code**: [[nmap -sT 10.10.10.10 -p445 --script smb2-time -vv]]



> -sT: Use TCP SYN scan.
-p: Specifies the port number to scan.
--script: Runs the specified Nmap script.
-vv: Increases the verbosity level of the output.

3. This command is used to fix the system clock on both Linux and Windows operating systems. The command uses the 'date' command on Linux and the 'net time' command on Windows to set the system clock to a specific date and time.

 



**Code**: [[sudo date -s "14 APR 2015 18:25:16" # Linux
net ti]]



> The 'sudo date -s' command on Linux sets the system date and time to the specified value. The 'net time /domain /set' command on Windows sets the system time to the time of the primary domain controller. This command is useful when the system clock is off by a significant amount and needs to be corrected.



**Command** ([[Set system time on Linux]]):

```bash
sudo date -s "14 APR 2015 18:25:16"
```





**Command** ([[Set system time on Windows]]):

```bash
net time /domain /set
```



4. Use the faketime command to manipulate the system time.

 



**Code**: [[faketime -f '+8h' date]]



> The faketime command allows you to manipulate the system time for a specific command or program. The -f option specifies the time offset from the current time, in this case adding 8 hours. The 'date' argument specifies the command to run with the manipulated time. This can be useful for testing or debugging time-sensitive applications.



**Command** ([[Fake time with faketime]]):

```bash
faketime -f '+8h' date
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]
- [[Pass the Ticket|T1550.003 - Pass the Ticket]]

## Commands Used

- [[Fake time with faketime]]
- [[Nmap scan with service detection]]
- [[Set system time on Linux]]
- [[Set system time on Windows]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Clock Synchronization]]


