---
id: 0337d235-d9ae-47d5-93a2-c9961b077724
name: Subversion Source Code Disclosure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.244519+00:00'
updated_at: '2023-04-10T20:33:55.574650+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Example (Wordpress)]]'
- '[[Insecure Source Code Management]]'
- '[[Subversion]]'
---

# Subversion Source Code Disclosure

## Summary

An attacker can use this technique to obtain sensitive information from a target by exploiting an insecure Subversion (SVN) repository. In this example, the attacker can obtain the WordPress configuration file (wp-config.php) by accessing the .svn directory on the web server. The wp-config.php file

## Description

# Description

An attacker can use this technique to obtain sensitive information from a target by exploiting an insecure Subversion (SVN) repository. In this example, the attacker can obtain the WordPress configuration file (wp-config.php) by accessing the .svn directory on the web server. The wp-config.php file contains database credentials and other sensitive information that can be used to further compromise the WordPress installation.

To exploit this vulnerability, an attacker only needs to send a GET request to the .svn directory on the web server. The attacker can then use the information obtained from the configuration file to escalate privileges or perform other malicious actions on the target system. This technique can be used by attackers to gain access to sensitive information and escalate privileges in both corporate and personal environments.

## Requirements

1. Access to the target system

1. Knowledge of the location of the .svn directory on the web server

## Defense

1. Ensure that SVN repositories are not accessible from the internet

1. Regularly scan web servers for exposed .svn directories

1. Remove all .svn directories from web servers

## Objectives

1. Obtain sensitive information from a target system

1. Escalate privileges or perform other malicious actions on the target system

# Instructions

1. curl http://blog.domain.com/.svn/text-base/wp-config.php.svn-base

**Code**: [[curl http://blog.domain.com/.svn/text-base/wp-conf]]

> This command sends a GET request to the .svn directory on the web server to obtain the WordPress configuration file (wp-config.php).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Tags

- [[Example (Wordpress)]]
- [[Insecure Source Code Management]]
- [[Subversion]]
