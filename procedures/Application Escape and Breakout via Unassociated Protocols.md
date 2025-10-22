---
id: 0a02e3e7-e6b3-45cd-9788-6718ef775959
name: Application Escape and Breakout via Unassociated Protocols
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.464837+00:00'
updated_at: '2023-04-06T03:56:17.493019+00:00'
tags:
- '[[Application Escape and Breakout]]'
- '[[Internet Explorer]]'
- '[[Unassociated Protocols]]'
commands:
- '[[Connect to IRC server]]'
- '[[Connect to localhost via telnet]]'
- '[[Download file.txt from ftp.example.com]]'
- '[[Enable HTTPS]]'
- '[[Join channel]]'
- '[[Send email]]'
- '[[Sending HTTP request]]'
---

# Application Escape and Breakout via Unassociated Protocols

## Summary

Application Escape and Breakout via Unassociated Protocols is a technique used to escape from a restricted browser environment, such as a kiosk, by using alternate protocols to access the internet. This technique involves using protocols that are not typically associated with web browsing, such as 

## Description

# Description

Application Escape and Breakout via Unassociated Protocols is a technique used to escape from a restricted browser environment, such as a kiosk, by using alternate protocols to access the internet. This technique involves using protocols that are not typically associated with web browsing, such as FTP, Telnet, or email, to bypass browser restrictions and access the internet. An attacker can use this technique to download and execute malicious code, steal sensitive data, or pivot to other systems.

To execute this technique, the attacker would need to identify the protocols that are allowed by the browser environment and use them to access the internet. This can be achieved by manually entering the protocol into the browser address bar or by crafting a link or file that invokes the protocol. This technique can be used in combination with other techniques, such as social engineering or spear-phishing, to increase the likelihood of success.

The business value of this technique lies in the ability to access the internet from a restricted environment, which can be useful for conducting research or accessing resources that are otherwise blocked. However, this technique can also be used for malicious purposes and can result in data theft, system compromise, or other security breaches.

## Requirements

1. Access to a restricted browser environment

1. Knowledge of alternate protocols allowed by the environment

1. Ability to craft links or files that invoke alternate protocols

## Defense

1. Restrict access to alternate protocols that are not required for business purposes

1. Monitor network traffic for suspicious activity related to alternate protocols

1. Implement browser restrictions and security policies to prevent application escape and breakout

## Objectives

1. Escape from a restricted browser environment

1. Access the internet using alternate protocols

1. Download and execute malicious code

1. Steal sensitive data

1. Pivot to other systems

# Instructions

1. To escape a browser based kiosk using an alternate protocol, follow these steps:
1. Open the browser's developer tools
2. Navigate to the 'Console' tab
3. Type in the following command: 'window.location="[alternate protocol]://[desired URL]"'
4. Press 'Enter'
5. You should now be redirected to the desired URL using the alternate protocol

**Code**: [[http]]

> This command allows users to escape a browser based kiosk by using an alternate protocol other than the default 'http'. By following the above instructions, users can redirect the browser to the desired URL using the alternate protocol of their choice.

**Command** ([[Sending HTTP request]]):

```bash
http.post('example.com/api', {data: 'example'}).json()
```

2. To access a website, you need to use either HTTP or HTTPS protocol.

**Code**: [[https]]

> HTTP stands for Hypertext Transfer Protocol and HTTPS stands for Hypertext Transfer Protocol Secure. Both protocols are used to transfer data between a web server and a web browser. HTTP is not secure and data is transferred in plain text. HTTPS, on the other hand, encrypts the data being transferred, making it more secure. When accessing sensitive information, such as passwords or credit card details, it is recommended to use HTTPS to prevent unauthorized access.

**Command** ([[Enable HTTPS]]):

```bash
Add SSL certificate to server
```

3. To use a known protocol, simply enter the protocol followed by a colon, then the address you wish to connect to. For example, to connect to an IRC server, you can enter 'irc://irc.server.com'.

**Code**: [[irc]]

> The 'known protocols' refer to the various communication protocols that are supported by the browser. These include http, https, ftp, irc, and many others. By specifying the protocol in the address bar, you can connect to a server or resource that uses that protocol. For example, entering 'ftp://ftp.server.com' would connect you to an FTP server, while entering 'http://www.google.com' would load the Google homepage using the HTTP protocol.

**Command** ([[Connect to IRC server]]):

```bash
irc.connect('irc.server.com')
```

**Command** ([[Join channel]]):

```bash
irc.join('#channel')
```

4. Use the FTP command to establish a connection to a remote server and transfer files.

**Code**: [[ftp]]

> The FTP command is used to connect to a remote server and transfer files. It can be used to download files from the remote server to your local machine or upload files from your local machine to the remote server. The command requires the following arguments:

1. Hostname: The hostname or IP address of the remote server.
2. Username: The username to use for authentication on the remote server.
3. Password: The password to use for authentication on the remote server.

Once connected, you can use a variety of commands to navigate the remote server and transfer files. Some common commands include:

- ls: List the files and directories in the current remote directory.
- cd: Change the remote directory.
- get: Download a file from the remote server to your local machine.
- put: Upload a file from your local machine to the remote server.
- bye: Close the FTP connection.

For more information on the FTP command and its available options, please refer to the command's manual page.

**Command** ([[Download file.txt from ftp.example.com]]):

```bash
open ftp.example.com
user
password
get file.txt
```

5. telnet [host] [port]

**Code**: [[telnet]]

> The telnet command is used to establish a connection to a remote host using the Telnet protocol. The [host] argument specifies the IP address or hostname of the remote host, and the [port] argument specifies the port number to connect to. Once the connection is established, you can interact with the remote host using the command line interface.

**Command** ([[Connect to localhost via telnet]]):

```bash
telnet localhost
```

6. Multiple Commands: 
1. To open default email client and create a new email, use the following command: 
   `open 'mailto:recipient@example.com?subject=Subject&body=Body'`
2. To include multiple recipients, separate their email addresses with commas: 
   `mailto:recipient1@example.com, recipient2@example.com`
3. To include a subject and body in the email, use the following format: 
   `mailto:recipient@example.com?subject=Subject&body=Body`

**Code**: [[mailto]]

> The `mailto` command is used to open the default email client and create a new email. It can be used with multiple commands and instructions to include multiple recipients, subject, and body of the email. This command is useful for sending emails directly from the terminal without having to open the email client separately.

**Command** ([[Send email]]):

```bash
mailto:example@example.com?subject=Hello%20World
```

## Commands Used

- [[Connect to IRC server]]
- [[Connect to localhost via telnet]]
- [[Download file.txt from ftp.example.com]]
- [[Enable HTTPS]]
- [[Join channel]]
- [[Send email]]
- [[Sending HTTP request]]

## Tags

- [[Application Escape and Breakout]]
- [[Internet Explorer]]
- [[Unassociated Protocols]]
