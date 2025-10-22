---
id: 4f07c787-5715-4a14-8b01-f504793e7b60
name: /etc/passwd and /etc/shadow
type: sub-technique
mitre_id: T1003.008
mitre_url: null
created_at: '2023-04-06T00:31:26.972212+00:00'
updated_at: '2023-04-06T00:31:26.972212+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# /etc/passwd and /etc/shadow

**MITRE ID**: T1003.008

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enable offline password cracking. Most modern Linux operating systems use a combination of <code>/etc/passwd</code> and <code>/etc/shadow</code> to store user account information including passwo

## Description

Adversaries may attempt to dump the contents of <code>/etc/passwd</code> and <code>/etc/shadow</code> to enable offline password cracking. Most modern Linux operating systems use a combination of <code>/etc/passwd</code> and <code>/etc/shadow</code> to store user account information including password hashes in <code>/etc/shadow</code>. By default, <code>/etc/shadow</code> is only readable by the root user.(Citation: Linux Password and Shadow File Formats)

The Linux utility, unshadow, can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper:(Citation: nixCraft - John the Ripper) <code># /usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db</code>

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
