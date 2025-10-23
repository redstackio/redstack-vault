---
id: 379c07a3-4155-407e-8170-52322ea7248b
name: Simple .htaccess PHP Handler Configuration Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.874017+00:00'
updated_at: '2023-04-06T23:33:08.414067+00:00'
tags:
- '[[.htaccess simple php]]'
commands:
- '[[AddType application/x-httpd-php .rce]]'
---

# Simple .htaccess PHP Handler Configuration Attack

## Summary

This attack involves modifying the .htaccess file on a web server to configure the PHP handler to allow remote code execution. The attacker can then upload a PHP script containing malicious code that will be executed on the server. This attack can be used to gain access to sensitive data, launch fu

## Description

# Description

This attack involves modifying the .htaccess file on a web server to configure the PHP handler to allow remote code execution. The attacker can then upload a PHP script containing malicious code that will be executed on the server. This attack can be used to gain access to sensitive data, launch further attacks, or use the server as a platform for other malicious activity. From a technical perspective, this attack involves modifying the .htaccess file to include a specific configuration that enables remote code execution. From a business standpoint, this attack can result in significant damage to a company's reputation and financial losses due to stolen data or system downtime.

 

## Requirements

1. Access to the web server's .htaccess file

1. Ability to upload a PHP script containing malicious code

 

## Defense

1. Regularly monitor and review the .htaccess file for unauthorized changes

1. Implement strict file upload restrictions and validation to prevent the upload of malicious code

1. Use a web application firewall to detect and block suspicious activity

 

## Objectives

1. Gain access to sensitive data on the web server

1. Use the server as a platform for further attacks

1. Cause system downtime or other damage to the target organization

 

# Instructions

1. To configure PHP handler on Apache web server, add the above line to your .htaccess file.

 



**Code**: [[AddType application/x-httpd-php .rce]]



> This command adds a new MIME type to the Apache web server configuration, which associates the .rce file extension with the PHP scripting language. This allows the server to correctly interpret and execute PHP code contained within .rce files. To use this command, simply upload an .htaccess file to the root directory of your website, and add the above line to the file.



**Command** ([[AddType application/x-httpd-php .rce]]):

```bash
AddType application/x-httpd-php .rce
```



2. To upload a file for remote code execution, use the following command: 'upload <local_file_path> <remote_file_path>'.

 



**Code**: [[.rce]]



> This command allows you to upload a file from your local machine to the remote server, which can then be executed remotely using another command. The first argument is the path to the file on your local machine, while the second argument is the path where you want to upload the file on the remote server. Make sure to specify the correct paths for both arguments. Once the file is uploaded, you can use another command to execute it remotely.

## Commands Used

- [[AddType application/x-httpd-php .rce]]

## Tags

- [[.htaccess simple php]]


