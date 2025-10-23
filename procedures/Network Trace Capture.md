---
id: 81d38402-834c-46d0-b696-7336b510bcc6
name: Network Trace Capture
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.114120+00:00'
updated_at: '2023-04-10T20:25:12.020303+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Sniffing|T1040 - Network Sniffing]]'
tags:
- '[[Capture a network trace with builtin tools]]'
- '[[Network Pivoting Techniques]]'
commands:
- '[[Capture every TCP packet]]'
- '[[Capture everything on port 22]]'
- '[[Capture packets and print ASCII]]'
- '[[Capture packets and write to file]]'
- '[[Convert ETL to PCAPNG]]'
- '[[Install tcpdump]]'
- '[[Start Netsh Capture]]'
- '[[Start Netsh Capture with Filters]]'
- '[[Start Netsh Capture with Persistence]]'
- '[[Stop Netsh Trace]]'
---

# Network Trace Capture

## Summary

Network Trace Capture is a technique used to capture network traffic in order to analyze it for potential vulnerabilities or security threats. This technique involves capturing network traffic using built-in tools such as Wireshark or tcpdump on Windows or Linux operating systems. Network Trace Cap

## Description

# Description

Network Trace Capture is a technique used to capture network traffic in order to analyze it for potential vulnerabilities or security threats. This technique involves capturing network traffic using built-in tools such as Wireshark or tcpdump on Windows or Linux operating systems. Network Trace Capture can be used by attackers to gather sensitive information such as passwords, credit card numbers, or other confidential data transmitted over the network.

From a technical perspective, Network Trace Capture involves capturing packets of data that are transmitted over a network. These packets can then be analyzed to identify patterns or anomalies that may indicate a security threat. Network Trace Capture can be used to identify vulnerabilities in network protocols or applications, and can also be used to identify potential insider threats or malicious activity.

The business value of Network Trace Capture is that it allows organizations to proactively identify and mitigate security threats before they can cause damage to the organization.

 

## Requirements

1. Access to a Windows or Linux operating system

1. Built-in tools such as Wireshark or tcpdump

 

## Defense

1. Use encryption to protect sensitive data transmitted over the network

1. Implement network segmentation to limit the scope of potential attacks

1. Regularly monitor network traffic for anomalies or suspicious activity

 

## Objectives

1. Capture network traffic to analyze for potential vulnerabilities or security threats

1. Identify potential insider threats or malicious activity

1. Proactively identify and mitigate security threats before they can cause damage to the organization

 

# Instructions

1. To start capturing network traffic on Windows, run the following command:

netsh trace start capture=yes report=disabled tracefile=c:\trace.etl maxsize=16384

To stop the trace, run the following command:

netsh trace stop

To persist the trace across reboots, run the following command:

netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384

To open the captured traffic in Wireshark, you need to convert the etl file to the cap file format. Microsoft provides a converter for this task. Download the latest version of etl2pcapng.exe and run the following command:

etl2pcapng.exe c:\trace.etl c:\trace.pcapng

To filter the captured traffic, use the following command:

netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384

Replace the filter arguments with the desired values.

 



**Code**: [[# start a capture use the netsh command.
netsh tra]]



> This command helps in capturing network traffic on Windows. The command uses the netsh command to start and stop the capture. The captured traffic is saved in the ETL format, which can be converted to the more widely used PCAPNG format using the etl2pcapng.exe converter. The captured traffic can also be filtered using the Ethernet.Type and IPv4.Address arguments. The command can be used by network administrators and security professionals to monitor network traffic and detect any suspicious activity.



**Command** ([[Start Netsh Capture]]):

```bash
netsh trace start capture=yes report=disabled tracefile=c:\trace.etl maxsize=16384
```





**Command** ([[Stop Netsh Trace]]):

```bash
netsh trace stop
```





**Command** ([[Start Netsh Capture with Persistence]]):

```bash
netsh trace start capture=yes report=disabled persistent=yes tracefile=c:\trace.etl maxsize=16384
```





**Command** ([[Convert ETL to PCAPNG]]):

```bash
etl2pcapng.exe c:\trace.etl c:\trace.pcapng
```





**Command** ([[Start Netsh Capture with Filters]]):

```bash
netsh trace start capture=yes report=disabled Ethernet.Type=IPv4 IPv4.Address=10.200.200.3 tracefile=c:\trace.etl maxsize=16384
```



2. To capture network traffic on a Linux machine using tcpdump, follow these steps:
1. Install tcpdump using the command 'sudo apt-get install tcpdump'.
2. To capture all network traffic and save it to a file named '0001.pcap' on interface 'eth0', run the command 'tcpdump -w 0001.pcap -i eth0'.
3. To capture and display all network traffic on interface 'eth0', run the command 'tcpdump -A -i eth0'.
4. To capture only TCP packets on interface 'eth0', run the command 'tcpdump -i eth0 tcp'.
5. To capture all traffic on port 22 (SSH), run the command 'tcpdump -i eth0 port 22'.

 



**Code**: [[sudo apt-get install tcpdump
tcpdump -w 0001.pcap ]]



> The 'tcpdump' command is used to capture network traffic on a Linux machine. The '-w' option is used to write the captured packets to a file. The '-A' option is used to print out the captured packets in ASCII. The '-i' option is used to specify the interface to capture on. The 'tcp' option is used to capture only TCP packets, and the 'port' option is used to capture traffic on a specific port.



**Command** ([[Install tcpdump]]):

```bash
sudo apt-get install tcpdump
```





**Command** ([[Capture packets and write to file]]):

```bash
tcpdump -w 0001.pcap -i eth0
```





**Command** ([[Capture packets and print ASCII]]):

```bash
tcpdump -A -i eth0
```





**Command** ([[Capture every TCP packet]]):

```bash
tcpdump -i eth0 tcp
```





**Command** ([[Capture everything on port 22]]):

```bash
tcpdump -i eth0 port 22
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Sniffing|T1040 - Network Sniffing]]

## Commands Used

- [[Capture every TCP packet]]
- [[Capture everything on port 22]]
- [[Capture packets and print ASCII]]
- [[Capture packets and write to file]]
- [[Convert ETL to PCAPNG]]
- [[Install tcpdump]]
- [[Start Netsh Capture]]
- [[Start Netsh Capture with Filters]]
- [[Start Netsh Capture with Persistence]]
- [[Stop Netsh Trace]]

## Tags

- [[Capture a network trace with builtin tools]]
- [[Network Pivoting Techniques]]


