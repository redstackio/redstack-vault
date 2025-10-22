---
id: ea801e48-173e-4e2a-b3f7-13fbef40eb46
name: Update /etc/hosts with IP and Hostname
type: procedure
verified: true
submitted: true
created_at: '2019-09-12T20:40:41.066848+00:00'
updated_at: '2023-05-26T00:39:38.069025+00:00'
tactics:
- '[[Stage Capabilities|TA0026 - Stage Capabilities]]'
techniques:
- '[[Upload, install, and configure software/tools|T1362 - Upload, install, and configure
  software/tools]]'
platforms:
- Linux
tags:
- '[[Network]]'
---

# Update /etc/hosts with IP and Hostname

**Status**: ✓ Verified

## Summary

In some situations (for example web servers using vhost to direct traffic), it may be necessary to update the attacker's /etc/hosts file, allowing them  to associate hostnames and their IP without sending requests to external DNS servers. 

## Description

# Description

In some situations (for example web servers using vhost to direct traffic), it may be necessary to update the attacker's `/etc/hosts file`, allowing them  to associate hostnames and their IP without sending requests to external DNS servers.

# Instructions

1. Using an editor, open the hosts file (/etc/hosts)
2. Add additional domain names using the format:

**Code**: [[<IP> <SUBDOMAIN.DOMAINNAME1>  <SUBDOMAIN.DOMAINNAM]]

Example hosts file with `testsite1.domain.com` and `testsite2.domain.com` added:

**Code**: [[127.0.0.1       localhost
127.0.1.1       kali

10]]

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Stage Capabilities|TA0026 - Stage Capabilities]]

### Techniques

- [[Upload, install, and configure software/tools|T1362 - Upload, install, and configure software/tools]]

## Tags

- [[Network]]
