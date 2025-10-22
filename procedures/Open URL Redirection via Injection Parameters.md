---
id: c3f9f29a-3820-47b8-9a31-c99592751951
name: Open URL Redirection via Injection Parameters
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.853488+00:00'
updated_at: '2023-04-10T20:23:05.573402+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Data from Information Repositories|T1213 - Data from Information Repositories]]'
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
tags:
- '[[Common injection parameters]]'
- '[[Open URL Redirection]]'
---

# Open URL Redirection via Injection Parameters

## Summary

Open URL redirection via injection parameters is a common web application vulnerability that allows attackers to redirect users to malicious websites. Attackers can inject malicious code into input fields that redirect the user to a different URL than intended. This technique is often used in phish

## Description

# Description

Open URL redirection via injection parameters is a common web application vulnerability that allows attackers to redirect users to malicious websites. Attackers can inject malicious code into input fields that redirect the user to a different URL than intended. This technique is often used in phishing attacks and can be difficult to detect. In order to exploit this vulnerability, attackers must first identify a web application that is vulnerable to open URL redirection.

From a technical standpoint, this vulnerability occurs when a web application fails to properly validate user input. Attackers can exploit this vulnerability by injecting code into input fields that redirect the user to a malicious website. This can be accomplished by modifying the URL parameters or by using a specially crafted URL.

The business value of this technique is that it allows attackers to bypass security controls and redirect users to malicious websites. This can result in the theft of sensitive information, such as login credentials or financial data. Additionally, this technique can be used to spread malware or conduct phishing attacks.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of injection parameters

1. Ability to craft a malicious URL

## Defense

1. Validate user input to ensure that it is properly formatted and does not contain any malicious code

1. Use parameterized queries to prevent SQL injection attacks

1. Implement proper access controls to prevent unauthorized access to sensitive data

## Objectives

1. To redirect users to a malicious website

1. To steal sensitive information

1. To spread malware or conduct phishing attacks

# Instructions

1. Use these payloads to test the URL redirection vulnerability of a web application. Inject the payload in the vulnerable parameter and observe the redirection URL. The payload can be used to redirect the user to a malicious website or phishing page.

**Code**: [[/{payload}
?next={payload}
?url={payload}
?target=]]

> The payload contains various parameters such as next, url, target, rurl, dest, destination, redir, redirect_uri, redirect_url, redirect, redirect/{payload}, cgi-bin/redirect.cgi?{payload}, out/{payload}, out?{payload}, view={payload}, login?to={payload}, image_url={payload}, go={payload}, return={payload}, returnTo={payload}, return_to={payload}, checkout_url={payload}, continue={payload}, return_path={payload}. These parameters are used by web applications to redirect the user to a specific page or URL. An attacker can manipulate these parameters to redirect the user to a malicious website or phishing page.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Data from Information Repositories|T1213 - Data from Information Repositories]]
- [[Drive-by Compromise|T1189 - Drive-by Compromise]]

## Tags

- [[Common injection parameters]]
- [[Open URL Redirection]]
