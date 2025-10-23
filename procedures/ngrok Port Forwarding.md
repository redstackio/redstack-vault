---
id: cc463d6b-b9c7-4615-919b-1cd020bf8407
name: ngrok Port Forwarding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.045438+00:00'
updated_at: '2023-05-26T00:58:48.970228+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[ngrok]]'
commands:
- '[[Authenticate ngrok]]'
- '[[Deploy port forwarding for 4433]]'
- '[[Download and unzip ngrok binary]]'
---

# ngrok Port Forwarding

## Summary

The ngrok port forwarding technique is used to create a secure tunnel from a public endpoint to a locally running service. It is often used by red teams and attackers to bypass firewall restrictions and exfiltrate data from a target network. The technique works by deploying a client and server comp

## Description

# Description

The ngrok port forwarding technique is used to create a secure tunnel from a public endpoint to a locally running service. It is often used by red teams and attackers to bypass firewall restrictions and exfiltrate data from a target network. The technique works by deploying a client and server component of ngrok, which establishes a secure connection between them, allowing the attacker to access the target network from a remote location. The business value of this technique is that it allows for remote access to internal resources, which can be beneficial for remote workers or for troubleshooting purposes.

 

## Requirements

1. Access to a public endpoint.

1. Deploying ngrok client and server components.

 

## Defense

1. Implement network segmentation to prevent unauthorized access to critical assets.

1. Monitor network traffic for suspicious activity, including traffic to known ngrok endpoints.

1. Implement strong authentication mechanisms to prevent unauthorized access to sensitive data.

 

## Objectives

1. Establish a secure connection between a public endpoint and a locally running service.

1. Bypass firewall restrictions to gain access to a target network.

1. Exfiltrate data from a target network.

 

# Instructions

1. To deploy a port forwarding using ngrok, follow these steps:

 



**Code**: [[# get the binary
wget https://bin.equinox.io/c/4Vm]]



> 1. Download the ngrok binary from https://ngrok.com/download and extract the contents of the zip file.
2. Log in to your ngrok account by running the command `./ngrok authtoken [YOUR_AUTH_TOKEN]`.
3. Deploy a port forwarding for port 4433 by running the command `./ngrok http 4433` or `./ngrok tcp 4433` depending on your use case.

Note: Make sure to replace [YOUR_AUTH_TOKEN] with your actual ngrok auth token.



**Command** ([[Download and unzip ngrok binary]]):

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
```





**Command** ([[Authenticate ngrok]]):

```bash
./ngrok authtoken 3U[REDACTED_TOKEN]Hm
```





**Command** ([[Deploy port forwarding for 4433]]):

```bash
./ngrok http 4433
./ngrok tcp 4433
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Authenticate ngrok]]
- [[Deploy port forwarding for 4433]]
- [[Download and unzip ngrok binary]]

## Tags

- [[Network Pivoting Techniques]]
- [[ngrok]]


