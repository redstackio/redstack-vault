---
id: eb691bf4-46b3-4bf3-a22a-cb50e90a8be0
name: Active Directory ASREPRoast to Kerberoast (have username)
type: attack_chain
description: With valid usernames attempt asreproast / kerberoast
verified: false
submitted: false
step_count: 4
created_at: '2023-01-11T20:54:04.613349+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
procedures:
- '[[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]'
- '[[ASREPRoast SPN without pre-auth (have username)]]'
- '[[Crack asrep hash]]'
- '[[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]'
tags:
- With valid usernames attempt asreproast / kerberoast
---

# Active Directory ASREPRoast to Kerberoast (have username)

**Description**: With valid usernames attempt asreproast / kerberoast

## Overview

This attack chain consists of 4 steps.

## Attack Steps

### Step 1: Brute Force Users with "Do Not Require Kerberos Preauth." Set

**Procedure**: [[Brute Force Users with "Do Not Require Kerberos Preauth." Set]]

> Users with "Do not require Kerberos preauthentication" will disclose their TGT without authenticating with a valid password, as long as the username is correct. This allows attackers to build a wordlist and brute force valid users with GetNPUsers.py, also retreiving their TGT. 

---

### Step 2: ASREPRoast SPN without pre-auth (have username)

**Procedure**: [[ASREPRoast SPN without pre-auth (have username)]]

> Active Directory try to get hash from username. Looking user without pre-auth attribute on Kerberos. Send AS_REQ to DC to receive encrypted user key to crack. Can achieve without domain account, just a username. 

---

### Step 3: Crack asrep hash

**Procedure**: [[Crack asrep hash]]

> Using hashcat to crack asrep hash obtained from impacket or rubeus tools on DC. 

---

### Step 4: Query Domain for SPN and Attempt to Kerberoast (Authenticated)

**Procedure**: [[Query Domain for SPN and Attempt to Kerberoast (Authenticated)]]

> Sevrice principal names (SPN) are unique identifiers used by Kerberos authentication. Due to how Kerberos handles service tickets, attackers may be able to query a domain controller with valid credentials, make a request to the ticket granting service (TGT), and receive the hash of other accounts. 

---

## Chain Summary

- **Total Steps**: 4
- **Key Procedures**: 4 procedures
