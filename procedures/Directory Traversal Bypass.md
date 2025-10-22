---
id: 7f5f9349-9024-493f-9b53-3c1c5afed5d8
name: Directory Traversal Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.856182+00:00'
updated_at: '2023-04-10T20:22:08.582264+00:00'
tags:
- '[[Basic exploitation]]'
- '[[Bypass "../" replaced by ""]]'
- '[[Directory Traversal]]'
---

# Directory Traversal Bypass

## Summary

Directory Traversal Bypass is a technique used to bypass Web Application Firewalls (WAF) that remove the "../" characters from the strings. This technique simply duplicates the "../" characters to bypass the filter. This technique can be used to access restricted files or directories on the server.

## Description

# Description

Directory Traversal Bypass is a technique used to bypass Web Application Firewalls (WAF) that remove the "../" characters from the strings. This technique simply duplicates the "../" characters to bypass the filter. This technique can be used to access restricted files or directories on the server.

Technical Explanation: The "../" characters are used to navigate up one directory in a file path. When a WAF removes these characters, it can prevent directory traversal attacks. By duplicating the "../" characters, the WAF can be bypassed, and the attacker can access restricted files or directories.

Business Value: This technique can be used to gain unauthorized access to sensitive data or files stored on servers. By bypassing WAFs, attackers can gain access to data that they are not authorized to view.

## Requirements

## Defense

1. Implement input validation to ensure that directory traversal attacks cannot be performed.

1. Configure WAFs to block directory traversal attacks.

1. Monitor network traffic for suspicious activity.

## Objectives

1. Bypass Web Application Firewalls (WAFs)

1. Gain unauthorized access to restricted files or directories

# Instructions

1. Use the following commands to duplicate the "../" characters:

**Code**: [[..././
...\.\]]

> The "..././" command duplicates the "../" characters by using the "./" sequence. The "...\.\" command duplicates the "../" characters by using the "\.\" sequence.

## Tags

- [[Basic exploitation]]
- [[Bypass "../" replaced by ""]]
- [[Directory Traversal]]
