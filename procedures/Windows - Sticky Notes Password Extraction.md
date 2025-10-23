---
id: 290eaa08-23d9-496d-ae5e-742a886f3952
name: Windows - Sticky Notes Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.208534+00:00'
updated_at: '2023-04-10T20:37:32.224175+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Sticky Notes passwords]]'
- '[[Windows - Privilege Escalation]]'
---

# Windows - Sticky Notes Password Extraction

## Summary

The Sticky Notes application in Windows allows users to create and save notes on their desktop. These notes may contain sensitive information such as passwords or login credentials. This procedure focuses on extracting passwords from the Sticky Notes application using the SQLite database location. 

## Description

# Description

The Sticky Notes application in Windows allows users to create and save notes on their desktop. These notes may contain sensitive information such as passwords or login credentials. This procedure focuses on extracting passwords from the Sticky Notes application using the SQLite database location. Attackers can use this information to escalate privileges and gain access to sensitive data.

Technical Explanation: Sticky Notes stores its data in an SQLite database file located at %AppData%\Microsoft\Sticky Notes\StickyNotes.snt. The database contains a table named Note, which stores the text of each note along with its creation and modification dates. When a user saves a note containing a password, it is stored in plaintext in this database.

Business Value: This procedure can be used by attackers to gain access to sensitive information such as login credentials, which can be used to further compromise the organization's network.

 

## Requirements

1. Access to target Windows system

1. Knowledge of Sticky Notes SQLite database location

 

## Defense

1. Encrypt sensitive information such as passwords

1. Restrict access to the Sticky Notes application and its database

1. Monitor for suspicious activity related to Sticky Notes usage

 

## Objectives

1. Extract passwords from Sticky Notes application

1. Escalate privileges using extracted passwords

 

# Instructions

1. To access the SQLite database of Sticky Notes, you can use any SQLite client application such as DB Browser for SQLite. Open the application and navigate to the location of the database file mentioned in the 'data' field. Once you have opened the database file, you can view and modify the data stored in the Sticky Notes app.

 



**Code**: [[C:\Users\&lt;user&gt;\AppData\Local\Packages\Micro]]



> The 'data' field provides the file path to the SQLite database file used by Sticky Notes app. This database file contains all the notes and their associated metadata. By accessing this database file, you can view and modify the notes stored in the Sticky Notes app. However, it is recommended to make a backup of the database file before making any changes to it.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]

## Tags

- [[EoP - Looting for passwords]]
- [[Sticky Notes passwords]]
- [[Windows - Privilege Escalation]]


