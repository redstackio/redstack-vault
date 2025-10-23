---
id: 2269e6cf-ec4c-443b-8ab6-c3e81c0d0d60
name: Union SQL Injection to Retrieve Data From Other Tables
type: procedure
verified: true
submitted: true
created_at: '2020-08-28T06:13:51.602441+00:00'
updated_at: '2023-05-26T01:33:56.323376+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
---

# Union SQL Injection to Retrieve Data From Other Tables

**Status**: ✓ Verified

## Summary

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns. 

## Description

# Description

Union SQL injection will retrieve data from the database tables. First number of columns in the table has to be identified. Then the payload is customised based on the columns.



# Procedure



1. Access the application and apply filter to observe category parameter in the URL. Inject SQL injection payload through the parameter.



*'+UNION+SELECT+'abc','def'--*



![dc2f0f5a-5db4-47be-99a9-6b6e7bcf940b.png]()



2. This payload confirms that there are two columns in the table that contain text as the application loaded without any error.







![41c8e48b-1653-49e7-86dc-8930d3adb15f.png]()





3. Based on the number of columns and containing text, construct the payload by trying to retrieve content from other tables.



*'+UNION+SELECT+username,+password+FROM+users--*





![d6fecd9a-1064-47f0-88b0-e186e56c08a0.png]()



4. Observe that the payload fetches the usernames and passwords from the users table.



## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]


