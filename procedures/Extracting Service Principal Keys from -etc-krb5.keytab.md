---
id: dc8e93e2-96d6-449d-8eee-643a486b7df1
name: Extracting Service Principal Keys from /etc/krb5.keytab
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.683044+00:00'
updated_at: '2023-04-10T20:26:03.570155+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
- '[[Web Session Cookie|T1550.004 - Web Session Cookie]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Extract accounts from /etc/krb5.keytab]]'
commands:
- '[[Basic Usage]]'
- '[[Crackmapexec - Authenticate with Hash]]'
- '[[Dump Keytab using Bifrost]]'
- '[[Installation]]'
- '[[Keytab file import]]'
- '[[List Kerberos keytab entries]]'
---

# Extracting Service Principal Keys from /etc/krb5.keytab

## Summary

Extracting Service Principal Keys from /etc/krb5.keytab can be used by attackers to gain access to a Kerberos service account. Kerberos is a widely used authentication protocol in Active Directory environments, and service accounts are often heavily privileged. By extracting these keys, attackers c

## Description

# Description

Extracting Service Principal Keys from /etc/krb5.keytab can be used by attackers to gain access to a Kerberos service account. Kerberos is a widely used authentication protocol in Active Directory environments, and service accounts are often heavily privileged. By extracting these keys, attackers can use them to authenticate to various services and escalate privileges within the network. This technique can be used in combination with other attacks, such as Pass the Ticket, to move laterally within the network.

Technical Explanation: The /etc/krb5.keytab file contains the encrypted keys of all the service accounts that are used by the Kerberos service. Attackers can use various tools such as KeyTabExtract or Dump Keytab to extract these keys. Once the keys have been extracted, they can be used to authenticate to various services, such as SMB or LDAP, and escalate privileges within the network.

Business Value: By gaining access to service accounts, attackers can gain access to sensitive data, intellectual property, and other critical assets. This can lead to reputational damage, loss of revenue, and legal liabilities for the organization.

 

## Requirements

1. Valid credentials with permission to access the /etc/krb5.keytab file

1. Tools such as KeyTabExtract or Dump Keytab

 

## Defense

1. Ensure that the /etc/krb5.keytab file is protected and only accessible to authorized personnel

1. Monitor for any suspicious activity related to the extraction of Service Principal Keys

1. Implement multi-factor authentication and least privilege access control to limit the impact of a compromised account

 

## Objectives

1. Extract Service Principal Keys from /etc/krb5.keytab

1. Gain access to privileged accounts

1. Escalate privileges within the network

 

# Instructions

1. To list the Kerberos service principal keys, run the following command:

klist.exe -t -K -e -k FILE:<path_to_keytab_file>

Replace <path_to_keytab_file> with the actual path to the keytab file. The command will display the list of service principal keys stored in the keytab file.

 



**Code**: [[$ klist.exe -t -K -e -k FILE:C:\Users\User\downloa]]



> The 'klist' command is used to list the Kerberos tickets that a user has obtained. When used with the '-t' option, it displays the ticket's flags. The '-K' option is used to display the service principal keys stored in the keytab file. The '-e' option is used to display the encryption type of the keys. The '-k' option is used to specify the keytab file to use. In this example, the keytab file is located at 'C:\Users\User\downloads\krb5.keytab'. The output of the command lists the service principal keys stored in the keytab file, along with their key version number, key type, key value, and time stamp.



**Command** ([[List Kerberos keytab entries]]):

```bash
$ klist.exe -t -K -e -k FILE:C:\Users\User\downloads\krb5.keytab
```



2. To extract the keytab and NTLM hash using KeyTabExtract, run the following command:

```python3 keytabextract.py krb5.keytab```

This will import the keytab file and extract the NTLM hash. If no RC4-HMAC is located, the tool will be unable to extract the NTLM hash.

 



**Code**: [[$ python3 keytabextract.py krb5.keytab 
[!] No RC4]]



> KeyTabExtract is a tool used for extracting keytabs and NTLM hashes. The keytab file contains the secret keys of the service principals stored on the KDC. The NTLM hash is a one-way function of the user's password, which can be used to authenticate as that user. The RC4-HMAC is a hash algorithm used to encrypt and decrypt data in Kerberos authentication. If the RC4-HMAC is not located, the tool will be unable to extract the NTLM hash. 



**Command** ([[Keytab file import]]):

```bash
$ python3 keytabextract.py krb5.keytab
```



3. the 'bifrost' command

 



**Code**: [[bifrost]]



> to securely transfer files between devices using end-to-end encryption. The 'bifrost' command can be used with various arguments to specify the source and destination devices, as well as the files to be transferred. For example, you can use the '-s' argument to specify the source device and the '-d' argument to specify the destination device. You can also use the '-f' argument to specify the file(s) to be transferred. The 'bifrost' command also supports various other options and flags, such as '-v' for verbose output and '-h' for help.



**Command** ([[Installation]]):

```bash
git clone https://github.com/techbliss/bifrost.git
 cd bifrost
 pip3 install -r requirements.txt
```





**Command** ([[Basic Usage]]):

```bash
python3 bifrost.py -f malware.exe
```



4. Use this command to dump the contents of a keytab file.

 



**Code**: [[./bifrost -action dump -source keytab -path test]]



> This command takes in three arguments:
1. -action: Specifies the action to perform. In this case, it is 'dump'.
2. -source: Specifies the source of the keytab file. In this case, it is 'keytab'.
3. -path: Specifies the path to the keytab file to be dumped.



**Command** ([[Dump Keytab using Bifrost]]):

```bash
./bifrost -action dump -source keytab -path test
```



5. To connect to a machine using the account and the hash with CME, run the following command:

$ crackmapexec [IP_ADDRESS] -u '[ACCOUNT_NAME]$' -H "[NTLM_HASH]" -d "[DOMAIN_NAME]"

 



**Code**: [[$ crackmapexec 10.XXX.XXX.XXX -u 'COMPUTER$' -H "3]]



> This command uses CrackMapExec (CME) to connect to a machine using the provided account name and NTLM hash. The -u flag specifies the account name to use, followed by a '$' to indicate that it is a machine account. The -H flag specifies the NTLM hash to use for authentication. The -d flag specifies the domain name. The command will connect to the specified machine and return information about the connection, including the hostname and the domain name.



**Command** ([[Crackmapexec - Authenticate with Hash]]):

```bash
$ crackmapexec 10.XXX.XXX.XXX -u 'COMPUTER$' -H "31d6cfe0d16ae931b73c59d7e0c089c0" -d "DOMAIN"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]
- [[Web Session Cookie|T1550.004 - Web Session Cookie]]

## Commands Used

- [[Basic Usage]]
- [[Crackmapexec - Authenticate with Hash]]
- [[Dump Keytab using Bifrost]]
- [[Installation]]
- [[Keytab file import]]
- [[List Kerberos keytab entries]]

## Tags

- [[Active Directory Attacks]]
- [[Extract accounts from /etc/krb5.keytab]]


