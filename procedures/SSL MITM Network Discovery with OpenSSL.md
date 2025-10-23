---
id: cb1499bb-7e94-4c27-85b9-112f01665b8b
name: SSL MITM Network Discovery with OpenSSL
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.346466+00:00'
updated_at: '2023-05-26T00:58:56.579155+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[System Network Connections Discovery|T1049 - System Network Connections Discovery]]'
sub_techniques:
- '[[ARP Cache Poisoning|T1557.002 - ARP Cache Poisoning]]'
- '[[Password Filter DLL|T1556.002 - Password Filter DLL]]'
tags:
- '[[Network Discovery]]'
- '[[SSL MITM with OpenSSL]]'
commands:
- '[[Add OpenSSL server address to hosts file]]'
- '[[Generate SSL certificate using OpenSSL]]'
- '[[Replace all occurrences of ''old'' with ''new'']]'
- '[[View Hosts File]]'
---

# SSL MITM Network Discovery with OpenSSL

## Summary

SSL MITM Network Discovery with OpenSSL is a technique used by attackers to intercept SSL traffic and gain access to sensitive information. This technique involves setting up a MITM server with OpenSSL and modifying SSL traffic in transit. Attackers can use this technique to discover network connec

## Description

# Description

SSL MITM Network Discovery with OpenSSL is a technique used by attackers to intercept SSL traffic and gain access to sensitive information. This technique involves setting up a MITM server with OpenSSL and modifying SSL traffic in transit. Attackers can use this technique to discover network connections and steal credentials, such as passwords and usernames. This technique can be used to bypass network security controls, such as firewalls and IDS/IPS systems. The business value of this technique is that it can be used to gain unauthorized access to sensitive information and systems, which can lead to financial gain or reputational damage.

 

## Requirements

1. Access to the network

1. OpenSSL software installed on the MITM server

1. Ability to modify network traffic

 

## Defense

1. Use SSL certificates signed by a trusted CA

1. Implement network segmentation to limit the scope of the attack

1. Monitor network traffic for signs of SSL MITM attacks

 

## Objectives

1. Discover network connections

1. Intercept SSL traffic

1. Steal credentials

 

# Instructions

1. To use this command, follow the steps below:
1. Open a terminal window and navigate to the directory where you have saved the code snippet file.
2. Run the command: openssl s_server -quiet -key key.pem -cert cert.pem -port 443
3. Open another terminal window and run the command: openssl s_client -connect localhost:443
4. Start typing the HTTP request in the client window and press enter.
5. The request will be sent to the server and you will be able to see the response in the server window.
6. If you want to modify the response, you can do so by editing the response in the server window before sending it back to the client.

 



**Code**: [[/etc/hosts]]



> The command uses openssl to create a server that listens on port 443 and a client that connects to the server. You can then use the client to send HTTP requests to the server and see the response in the server window. If there is a MITM vulnerability, you can modify the response in the server window before sending it back to the client. The key.pem and cert.pem files are required for SSL encryption. You can replace them with your own key and certificate files if you want to use SSL encryption.



**Command** ([[View Hosts File]]):

```bash
cat /etc/hosts
```



2. This command adds an OpenSSL server address to the hosts file on a client host. The hosts file is a local file on a computer that maps hostnames to IP addresses. This command is useful when you want to perform a man-in-the-middle attack on a specific domain by redirecting traffic to an OpenSSL server.

 



**Code**: [[sudo echo "[OPENSSL SERVER ADDRESS] [domain.of.ser]]



> The command requires two arguments. The first argument is the OpenSSL server address, which is the IP address of the server you want to redirect traffic to. The second argument is the domain of the server you want to perform the man-in-the-middle attack on. The command appends a line to the hosts file that maps the domain to the OpenSSL server address, effectively redirecting traffic from the domain to the OpenSSL server.



**Command** ([[Add OpenSSL server address to hosts file]]):

```bash
sudo echo "[OPENSSL SERVER ADDRESS] [domain.of.server.to.mitm]" >> /etc/hosts  # On client host
```



3. Use the openssl command to generate a self-signed certificate for the MITM server.

 



**Code**: [[openssl req -subj '/CN=[domain.of.server.to.mitm]']]



> This command generates a self-signed SSL/TLS certificate for the MITM server. The -subj flag is used to specify the Common Name (CN) of the certificate, which should be set to the domain of the server to be intercepted. The -batch flag is used to suppress interactive prompts. The -new flag is used to generate a new certificate request. The -x509 flag is used to generate a self-signed certificate. The -days flag specifies the validity period of the certificate. The -nodes flag is used to generate a certificate and private key without password protection. The -out and -keyout flags specify the output files for the certificate and private key, respectively.



**Command** ([[Generate SSL certificate using OpenSSL]]):

```bash
openssl req -subj '/CN=[domain.of.server.to.mitm]' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```



4. Use this command to setup the infrastructure on the MITM server.

 



**Code**: [[mkfifo response
sudo openssl s_server -cert server]]



> This command sets up the MITM server to listen on a specified interface and port. The server.pem file is used to secure the connection. The response from the target server is piped into a file called response. The tee command is used to duplicate the output and send it to both openssl s_client and cat. The s_client command connects to the target server using the specified domain and IP address. The response from the target server is piped into another file called response. The cat command is used to combine the two response files and save the output to a single file. This command is useful for intercepting traffic between a client and server for analysis.

5. The tee command reads standard input and writes it to both standard output and one or more files.

 



**Code**: [[tee]]



> The tee command is used to split the output of a command so that it is displayed both on the screen and in a file. This can be useful when you want to save the output for later analysis, but still want to see it on the screen as it is generated. The tee command takes one or more file names as arguments, and writes the output to each of those files in addition to printing it to the screen. The tee command can be used in a pipeline to split the output of one command into multiple files or to send it to multiple commands for further processing.

6. sed 's/old_text/new_text/g' filename

 



**Code**: [[sed]]



> The 'sed' command is used to search and replace text in a file. The 's' stands for substitute, and the 'g' stands for global, meaning it will replace all occurrences of the old text with the new text. To use this command, replace 'old_text' with the text you want to replace, 'new_text' with the text you want to replace it with, and 'filename' with the name of the file you want to modify. 



**Command** ([[Replace all occurrences of 'old' with 'new']]):

```bash
s/old/new/g
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Adversary-in-the-Middle|T1557 - Adversary-in-the-Middle]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[System Network Connections Discovery|T1049 - System Network Connections Discovery]]

### Sub-Techniques

- [[ARP Cache Poisoning|T1557.002 - ARP Cache Poisoning]]
- [[Password Filter DLL|T1556.002 - Password Filter DLL]]

## Commands Used

- [[Add OpenSSL server address to hosts file]]
- [[Generate SSL certificate using OpenSSL]]
- [[Replace all occurrences of 'old' with 'new']]
- [[View Hosts File]]

## Tags

- [[Network Discovery]]
- [[SSL MITM with OpenSSL]]


