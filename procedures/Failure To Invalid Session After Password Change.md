---
id: 32e5da02-e91b-4852-84ce-1bfa30f6542c
name: Failure To Invalid Session After Password Change
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T15:43:14.482448+00:00'
updated_at: '2023-05-26T18:23:50.080804+00:00'
platforms:
- Web
tags:
- '[[Session Management]]'
- '[[Web Applications]]'
---

# Failure To Invalid Session After Password Change

**Status**: ✓ Verified

## Summary

A valid session has to be destroyed once the session is closed. Otherwise an attacker will try to exploit the session to impersonate the victim. 

## Description

# Description

 A valid session has to be destroyed once the session is closed. Otherwise an attacker will try to exploit the session to impersonate the victim.

# Instructions

1. Login into two different browsers using same credentials.

2.Change password in one browser and observe  that another browser still validate the session even after password change (even after refresh the page).

## Platforms

- Web

## Tags

- [[Session Management]]
- [[Web Applications]]
