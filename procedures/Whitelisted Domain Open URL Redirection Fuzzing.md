---
id: ae1b3048-5e3b-49c1-acaf-27965af8d364
name: Whitelisted Domain Open URL Redirection Fuzzing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.776465+00:00'
updated_at: '2023-04-10T20:23:06.271279+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Spearphishing Attachment|T1193 - Spearphishing Attachment]]'
tags:
- '[[Fuzzing]]'
- '[[Open URL Redirection]]'
---

# Whitelisted Domain Open URL Redirection Fuzzing

## Summary

Whitelisted Domain Open URL Redirection Fuzzing is a technique used to test for open URL redirection vulnerabilities in web applications. This technique involves sending a variety of payloads to the target application in order to identify whether it is possible to redirect a user to a malicious web

## Description

# Description

Whitelisted Domain Open URL Redirection Fuzzing is a technique used to test for open URL redirection vulnerabilities in web applications. This technique involves sending a variety of payloads to the target application in order to identify whether it is possible to redirect a user to a malicious website. The payloads used in this technique are limited to a pre-defined list of whitelisted domains, which helps to reduce the risk of a successful attack.

From a technical perspective, this technique involves sending requests to the target application with various payloads in the query string or request body. The payloads are designed to test whether the application will allow a user to be redirected to a malicious website. If the application is vulnerable, it will redirect the user to the specified URL, which could be used to launch further attacks.

The business value of this technique is that it can help to identify vulnerabilities in web applications before they can be exploited by attackers. By identifying and fixing these vulnerabilities, organizations can improve the security of their web applications and reduce the risk of data breaches or other security incidents.

## Requirements

1. Access to the target web application

1. A list of whitelisted domains to use as payloads

## Defense

1. Implement input validation and sanitization to prevent malicious payloads from being processed

1. Implement proper access controls to prevent unauthorized users from accessing the application

1. Regularly monitor and review logs to detect and respond to any suspicious activity

## Objectives

1. Identify whether the target application is vulnerable to open URL redirection attacks

1. Test the effectiveness of whitelisted domain filtering in preventing open URL redirection attacks

1. Provide information to developers and security teams on how to fix any vulnerabilities identified

# Instructions

1. To use this command, replace the value of WHITELISTEDDOMAIN with the specific white listed domain that you want to use in your test case. Then, run the command in your terminal. The command will replace all instances of www.whitelisteddomain.tld in the Open-Redirect-payloads.txt file with the specified white listed domain. It will also append the specified white listed domain to the end of the Open-Redirect-payloads-burp file.

**Code**: [[WHITELISTEDDOMAIN="www.test.com" && sed 's/www.whi]]

> This command is useful for testing open redirect vulnerabilities in web applications. By replacing the default domain with a specific white listed domain, you can test if the application is vulnerable to open redirects to untrusted domains. The command uses sed to replace the default domain in the Open-Redirect-payloads.txt file with the specified white listed domain. It also uses awk to append the specified white listed domain to the end of the Open-Redirect-payloads-burp file. This allows you to easily test for open redirect vulnerabilities using Burp Suite.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Spearphishing Attachment|T1193 - Spearphishing Attachment]]

## Tags

- [[Fuzzing]]
- [[Open URL Redirection]]
