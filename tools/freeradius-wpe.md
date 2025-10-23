---
id: 58ddf169-873c-4fda-8b32-4b6a5e93d243
name: freeradius-wpe
type: tool
verified: false
created_at: '2019-08-28T21:17:30.208054+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# freeradius-wpe

## Overview

A patch for the popular open-source FreeRADIUS implementation to demonstrate RADIUS impersonation vulnerabilities by Joshua Wright and Brad Antoniewicz. This patch adds the following functionality: Simplifies the setup of FreeRADIUS by adding all RFC1918 addresses as acceptable NAS devices; Simplif

## Description

A patch for the popular open-source FreeRADIUS implementation to demonstrate RADIUS impersonation vulnerabilities by Joshua Wright and Brad Antoniewicz. This patch adds the following functionality:



Simplifies the setup of FreeRADIUS by adding all RFC1918 addresses as acceptable NAS devices;



Simplifies the setup of EAP authentication by including support for all FreeRADIUS supported EAP types;



Adds WPE logging in $prefix/var/log/radius/freeradius-server-wpe.log, can be controlled in radius.conf by changing the “wpelogfile” directive;



Simplified the setup of user authentication with a default “users” file that accepts authentication for any username;



Adds credential logging for multiple EAP types including PEAP, TTLS, LEAP, EAP-MD5, EAP-MSCHAPv2, PAP, CHAP and others










