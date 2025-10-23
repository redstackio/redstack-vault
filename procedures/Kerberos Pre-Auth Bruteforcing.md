---
id: 05f0a796-d7bc-4882-9425-bcaad62e5426
name: Kerberos Pre-Auth Bruteforcing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.263036+00:00'
updated_at: '2023-04-10T20:36:09.914409+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
sub_techniques:
- '[[Password Guessing|T1110.001 - Password Guessing]]'
- '[[Password Spraying|T1110.003 - Password Spraying]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos pre-auth bruteforcing]]'
- '[[Password spraying]]'
commands:
- '[[Brute Force Usernames]]'
- '[[Kerbrute Password Spray with domain_users.txt and 123456]]'
- '[[Kerbrute Password Spray with domain_users.txt and Password123]]'
- '[[Kerbrute Password Spray with domain_users.txt and rockyou.txt]]'
---

# Kerberos Pre-Auth Bruteforcing

## Summary

Kerberos pre-auth bruteforcing is a technique used to discover weak passwords for user accounts in an Active Directory environment. This technique involves sending a large number of authentication attempts to the Kerberos service using a list of possible passwords. The goal is to identify accounts 

## Description

# Description

Kerberos pre-auth bruteforcing is a technique used to discover weak passwords for user accounts in an Active Directory environment. This technique involves sending a large number of authentication attempts to the Kerberos service using a list of possible passwords. The goal is to identify accounts that have weak passwords that can be easily guessed or brute-forced. Once weak passwords are identified, attackers can use them to gain access to sensitive information and systems within the network.

Technical Explanation: Kerberos is the authentication protocol used in Active Directory environments. When a user attempts to log in, their password is encrypted and sent to the Kerberos service for authentication. Kerberos pre-auth bruteforcing involves sending a large number of authentication requests to the Kerberos service using a list of possible passwords. If a password matches, the Kerberos service will issue a ticket that can be used to access network resources.

Business Value: Attackers can use Kerberos pre-auth bruteforcing to gain access to sensitive information and systems within an organization. This can result in data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to the Active Directory environment

1. Valid credentials or anonymous access

1. Kerbrute tool

 

## Defense

1. Enforce strong password policies to prevent weak passwords

1. Monitor for failed authentication attempts and lockout suspicious accounts

1. Implement multi-factor authentication to prevent password-based attacks

 

## Objectives

1. Identify user accounts with weak passwords

1. Gain access to sensitive information and systems within the network

 

# Instructions

1. This command is used to perform user enumeration on a target domain. It uses a wordlist of usernames to brute force the domain and find valid usernames. The command requires the following arguments:
1. -d: The target domain to enumerate users on.
2. --dc: The IP address of the domain controller to use for the enumeration.
3. usernames.txt: The wordlist of usernames to use for the brute force.

 



**Code**: [[root@kali:~$ ./kerbrute_linux_amd64 userenum -d do]]



> This command is useful for penetration testing and can help identify valid usernames on a target domain. It can also be used for security assessments to identify weak usernames that can be easily guessed by an attacker. It is important to note that this command should only be used with permission from the target organization and should not be used for malicious purposes.

2. To use Kerbrute for user password bruteforcing, follow these steps:
1. Download and install Kerbrute on your system.
2. Open a terminal or command prompt and navigate to the directory where Kerbrute is installed.
3. Run the following command: ./kerbrute_linux_amd64 bruteuser -d [domain] --dc [domain controller IP] [wordlist file path] [username]
4. Replace [domain] with the target domain name, [domain controller IP] with the IP address of the domain controller, [wordlist file path] with the path to your password wordlist file, and [username] with the target username.
5. Wait for Kerbrute to finish the password bruteforcing process and check the output for any successful attempts.

 



**Code**: [[root@kali:~$ ./kerbrute_linux_amd64 bruteuser -d d]]



> The 'bruteuser' command in Kerbrute is used for user password bruteforcing. The '-d' option is used to specify the target domain name, while the '--dc' option is used to specify the IP address of the domain controller. The 'rockyou.txt' file is a password wordlist file that contains a list of commonly used passwords. The 'username' argument is the target username that you want to bruteforce the password for. Kerbrute will iterate through the wordlist file and try each password combination until it finds the correct one. It is important to note that password bruteforcing is a time-consuming process and may take a long time to complete depending on the complexity of the password and the size of the wordlist file.



**Command** ([[Brute Force Usernames]]):

```bash
rockyou.txt
```



3. The Kerbrute Password Spray command is used to perform a brute force attack on Active Directory user accounts to guess their passwords. The command takes the following arguments:

-d: Specifies the domain name.
--dc: Specifies the IP address of the domain controller.
-v: Enables verbose output.
--delay: Specifies the delay between each request in milliseconds.
-o: Specifies the output file name.

The command also requires a file containing a list of user accounts to target and a file containing a list of passwords to try.

 



**Code**: [[root@kali:~$ ./kerbrute_linux_amd64 passwordspray ]]



> The Kerbrute Password Spray command is a commonly used technique by attackers to gain access to an Active Directory environment. It involves guessing a large number of passwords against a list of user accounts until a valid combination is found. The command can be customized to use different password lists, delay times, and output file names. It is important to note that this command should only be used for legitimate security testing purposes and with appropriate authorization.



**Command** ([[Kerbrute Password Spray with domain_users.txt and Password123]]):

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt Password123
```





**Command** ([[Kerbrute Password Spray with domain_users.txt and rockyou.txt]]):

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt rockyou.txt
```





**Command** ([[Kerbrute Password Spray with domain_users.txt and 123456]]):

```bash
./kerbrute_linux_amd64 passwordspray -d domain.local --dc 10.10.10.10 domain_users.txt '123456' -v --delay 100 -o kerbrute-passwordspray-123456.log
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

### Sub-Techniques

- [[Password Guessing|T1110.001 - Password Guessing]]
- [[Password Spraying|T1110.003 - Password Spraying]]

## Commands Used

- [[Brute Force Usernames]]
- [[Kerbrute Password Spray with domain_users.txt and 123456]]
- [[Kerbrute Password Spray with domain_users.txt and Password123]]
- [[Kerbrute Password Spray with domain_users.txt and rockyou.txt]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos pre-auth bruteforcing]]
- [[Password spraying]]


