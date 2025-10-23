---
id: ef9e39b6-66b1-48d8-a453-15e1e297b960
name: Hashcat Installation Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.543894+00:00'
updated_at: '2023-04-06T03:56:17.557959+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Hashcat]]'
- '[[Hashcat Install]]'
- '[[Hash Cracking]]'
commands:
- '[[Clone and Build Hashcat]]'
- '[[Install CMake, Build-Essential, and Git]]'
---

# Hashcat Installation Procedure

## Summary

The Hashcat installation procedure is a process to install and configure Hashcat on a system for password cracking. This procedure is commonly used by penetration testers and security researchers to test the strength of passwords in their environment. Hashcat is a powerful password cracking tool th

## Description

# Description

The Hashcat installation procedure is a process to install and configure Hashcat on a system for password cracking. This procedure is commonly used by penetration testers and security researchers to test the strength of passwords in their environment. Hashcat is a powerful password cracking tool that supports a wide range of hashing algorithms and attack modes. It utilizes the power of GPUs to perform password cracking at a faster rate. The business value of this procedure is to identify weak passwords in an organization and improve the overall security posture.

 

## Requirements

1. Access to a system where Hashcat needs to be installed

1. Sufficient privileges to install software on the system

1. GPU with CUDA support for faster password cracking

 

## Defense

1. Ensure that the system where Hashcat is installed is adequately secured to prevent unauthorized access

1. Implement strong password policies, including the use of complex and unique passwords

1. Monitor the network for any suspicious activity related to password cracking

 

## Objectives

1. To install and configure Hashcat on a system

1. To perform password cracking using Hashcat

1. To identify weak passwords in an organization

 

# Instructions

1. To install Hashcat, run the following command:

apt install cmake build-essential -y
apt install checkinstall git -y
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install

 



**Code**: [[apt install cmake build-essential -y
apt install c]]



> This command installs Hashcat, a password recovery tool. The first line installs the necessary dependencies for building Hashcat, including cmake and build-essential. The second line installs checkinstall and git. The third line clones the Hashcat repository from GitHub and navigates to the directory. The fourth line builds Hashcat with 8 threads and installs it on the system. Note that this command requires administrative privileges to run.



**Command** ([[Install CMake, Build-Essential, and Git]]):

```bash
apt install cmake build-essential -y
apt install checkinstall git -y
```





**Command** ([[Clone and Build Hashcat]]):

```bash
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Clone and Build Hashcat]]
- [[Install CMake, Build-Essential, and Git]]

## Tags

- [[Hashcat]]
- [[Hashcat Install]]
- [[Hash Cracking]]


