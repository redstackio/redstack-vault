---
id: 19cf629a-9b36-4863-b29f-f89fe75ca4aa
name: Add user to group using ADModule (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T17:29:54.291622+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
platforms:
- Windows
tags:
- '[[persistence]]'
commands:
- '[[Add member to group with ADModule]]'
---

# Add user to group using ADModule (credentials)

## Summary

If permissions are obtained to add a user to a group, the following ADModule can be used. 

## Description

# Description

If permissions are obtained to add a user to a group, the following ADModule can be used.



## Objective

There are instances administrative rights can be accessed and deemed necessary to add a user to a group.

Or a users group has GenericAll permissions on another group, whereas can add user to the group and access privileges.



1. Add user to a group using ADModule



# Instructions

1. Add a user to a group





**Command** ([[Add member to group with ADModule]]):

```bash
Add-ADGroupMember -Identity $GROUP_NAME -Members $USER
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Add member to group with ADModule]]

## Tags

- [[persistence]]


