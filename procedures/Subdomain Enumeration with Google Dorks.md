---
id: 65d8e640-5bc6-405b-9780-fdce7cc05e44
name: Subdomain Enumeration with Google Dorks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.435775+00:00'
updated_at: '2023-04-10T20:25:37.737810+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
sub_techniques:
- '[[Digital Certificates|T1596.003 - Digital Certificates]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using Google Dorks and Google Transparency Report]]'
commands:
- '[[Search for files with specific extensions]]'
- '[[Search for login, register, upload, logout, redirect, redir, goto, admin URLs]]'
- '[[Search for PDF files]]'
- '[[Search for subdomains]]'
- '[[Search for subdomains with any level]]'
- '[[Search for URLs with ampersand]]'
---

# Subdomain Enumeration with Google Dorks

## Summary

Subdomain enumeration is a critical phase in reconnaissance, as it helps attackers to identify potential targets and vulnerabilities. Google Dorks and Google Transparency Report can be used to identify subdomains of a domain. Google Dorks are search queries that use advanced operators to filter res

## Description

# Description

Subdomain enumeration is a critical phase in reconnaissance, as it helps attackers to identify potential targets and vulnerabilities. Google Dorks and Google Transparency Report can be used to identify subdomains of a domain. Google Dorks are search queries that use advanced operators to filter results, while Google Transparency Report is a tool that helps to identify subdomains that have been recently added to a domain's certificate. By combining these two techniques, an attacker can identify a large number of subdomains that can be used as potential targets for further attacks.

Technical Explanation: To perform subdomain enumeration with Google Dorks, an attacker can use search queries like 'site:*.domain.ext' or 'inurl:*.domain.ext'. These queries will return a list of subdomains that are indexed by Google. Google Transparency Report can be used to identify subdomains that are not indexed by Google but are still part of the domain's certificate. An attacker can use this information to identify subdomains that are not easily discoverable.

Business Value: Subdomain enumeration can help attackers to identify potential targets and vulnerabilities that can be exploited to gain access to sensitive information or systems.

## Requirements

1. Access to Google search engine

1. Knowledge of Google Dorks

1. Access to Google Transparency Report

## Defense

1. Implement proper access control mechanisms to prevent unauthorized access to sensitive information or systems

1. Regularly monitor and review domain certificates to identify any unauthorized subdomains

1. Implement network segmentation to limit the impact of a potential subdomain takeover

## Objectives

1. Identify all subdomains of a domain

1. Identify potential targets and vulnerabilities for further attacks

# Instructions

1. These commands can be used for domain reconnaissance, to gather information about a domain and its subdomains. The 'site' command filters results to a specific domain or subdomain. The 'filetype' command filters results to a specific file type. The 'inurl' command filters results to pages that contain a specific string in their URL. The 'ext' command filters results to pages with a specific file extension.

**Code**: [[site:*.domain.com -www
site:domain.com filetype:pd]]

> The first command 'site:*.domain.com -www' searches for all subdomains of the specified domain, excluding any subdomains that contain 'www'.
The second command 'site:domain.com filetype:pdf' searches for all PDF files on the specified domain.
The third command 'site:domain.com inurl:'&'' searches for all pages on the specified domain that contain an ampersand in their URL.
The fourth command 'site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin' searches for pages on the specified domain that contain any of the specified keywords in their URL.
The fifth command 'site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf' searches for pages on the specified domain with any of the specified file extensions.
The sixth command 'site:*.*.domain.com' searches for all subdomains of the specified domain, regardless of their subdomain name.

**Command** ([[Search for subdomains]]):

```bash
site:*.domain.com -www
```

**Command** ([[Search for PDF files]]):

```bash
site:domain.com filetype:pdf
```

**Command** ([[Search for URLs with ampersand]]):

```bash
site:domain.com inurl:'&'
```

**Command** ([[Search for login, register, upload, logout, redirect, redir, goto, admin URLs]]):

```bash
site:domain.com inurl:login,register,upload,logout,redirect,redir,goto,admin
```

**Command** ([[Search for files with specific extensions]]):

```bash
site:domain.com ext:php,asp,aspx,jsp,jspa,txt,swf
```

**Command** ([[Search for subdomains with any level]]):

```bash
site:*.*.domain.com
```

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

### Sub-Techniques

- [[Digital Certificates|T1596.003 - Digital Certificates]]

## Commands Used

- [[Search for files with specific extensions]]
- [[Search for login, register, upload, logout, redirect, redir, goto, admin URLs]]
- [[Search for PDF files]]
- [[Search for subdomains]]
- [[Search for subdomains with any level]]
- [[Search for URLs with ampersand]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using Google Dorks and Google Transparency Report]]
