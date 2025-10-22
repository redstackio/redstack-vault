---
id: fd4cca67-4cb0-41cc-ac4d-c69153abd96a
name: Admin Site URL Leak via Server Side Template Injection in Django Templates
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.524308+00:00'
updated_at: '2023-04-10T20:23:31.031181+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Admin Site URL leak]]'
- '[[Django Templates]]'
- '[[Server Side Template Injection]]'
---

# Admin Site URL Leak via Server Side Template Injection in Django Templates

## Summary

A Server Side Template Injection (SSTI) vulnerability in Django Templates can be exploited to obtain the Admin Site URL. This vulnerability can be used by an attacker to gain unauthorized access to the admin site and perform actions such as adding, modifying or deleting data. The vulnerability occu

## Description

# Description

A Server Side Template Injection (SSTI) vulnerability in Django Templates can be exploited to obtain the Admin Site URL. This vulnerability can be used by an attacker to gain unauthorized access to the admin site and perform actions such as adding, modifying or deleting data. The vulnerability occurs when user input is not properly sanitized and is passed directly to the template engine. An attacker can use this vulnerability to inject malicious code into the template, which is then executed on the server. This can lead to complete compromise of the server.

Technical Explanation: Django Templates are used to render HTML pages dynamically. The template engine replaces variables in a template with their values and generates a final HTML page. If user input is not properly sanitized, it can be used to inject malicious code into the template. This can lead to SSTI vulnerabilities. The Admin Site URL leak vulnerability occurs when the admin site URL is included in an error message that is displayed when a template fails to render.

Business Value: An attacker can use this vulnerability to gain unauthorized access to the admin site and perform actions such as adding, modifying or deleting data. This can lead to loss of sensitive data, financial loss, and damage to the organization's reputation.

## Requirements

1. Access to a vulnerable application

1. Knowledge of Django Templates and SSTI vulnerabilities

## Defense

1. Sanitize all user input before passing it to the template engine

1. Disable debug mode in production environments to prevent error messages from being displayed

1. Regularly review and update the application and its dependencies to ensure that known vulnerabilities are patched

## Objectives

1. Obtain the Admin Site URL

1. Gain unauthorized access to the admin site

1. Perform actions such as adding, modifying or deleting data

# Instructions

1. Multiple Commands

This command includes the 'admin/base.html' template in the current page. The 'admin/base.html' template provides a base structure for the admin pages and includes common elements such as the header, footer, and navigation menu. This command can be used to reduce code duplication and maintain consistency across multiple admin pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Admin Site URL leak]]
- [[Django Templates]]
- [[Server Side Template Injection]]
