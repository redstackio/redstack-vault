---
id: 74000980-d4b4-45da-879d-ed603794af64
name: Filter Bypass for Server-Side Request Forgery using URL Port Scanner
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.609336+00:00'
updated_at: '2023-04-10T20:24:02.030258+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Bypass filter_var() php function]]'
- '[[Bypassing filters]]'
- '[[Server-Side Request Forgery]]'
---

# Filter Bypass for Server-Side Request Forgery using URL Port Scanner

## Summary

This procedure describes how to bypass filters in order to perform Server-Side Request Forgery (SSRF) attacks. Specifically, it focuses on bypassing the filter_var() PHP function using a URL Port Scanner. 

An attacker can use SSRF attacks to target internal systems that are not directly accessible

## Description

# Description

This procedure describes how to bypass filters in order to perform Server-Side Request Forgery (SSRF) attacks. Specifically, it focuses on bypassing the filter_var() PHP function using a URL Port Scanner. 

An attacker can use SSRF attacks to target internal systems that are not directly accessible from the internet. By exploiting a vulnerable web application, the attacker can send requests to internal systems using the web application as a proxy. 

The URL Port Scanner tool allows the attacker to scan for open ports on internal systems, which can then be used to launch further attacks.

## Requirements

1. Access to a vulnerable web application

1. URL Port Scanner tool

## Defense

1. Implement input validation and sanitization to prevent the use of vulnerable web applications

1. Implement network segmentation to prevent attackers from accessing internal systems

1. Monitor network traffic for suspicious activity, such as requests to internal systems

## Objectives

1. Identify vulnerable web applications that can be used to perform SSRF attacks

1. Bypass filters in order to successfully perform SSRF attacks

1. Scan for open ports on internal systems using the URL Port Scanner tool

# Instructions

1. Use this command to scan multiple URLs for open ports.

**Code**: [[0://evil.com:80;http://google.com:80/ ]]

> This command takes in a list of URLs separated by semicolons (;) and scans each of them for open ports. The URLs should be in the format protocol://domain:port. For example, http://example.com:80. The command will return a list of open ports for each URL. This can be useful for identifying potential vulnerabilities in a website's security.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Tags

- [[Bypass filter_var() php function]]
- [[Bypassing filters]]
- [[Server-Side Request Forgery]]
