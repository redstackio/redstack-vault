---
id: 0d83954a-2be5-44fc-b557-dbeceabd4e42
name: Server Side Template Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-03T17:58:46.299866+00:00'
updated_at: '2023-05-26T01:32:21.298703+00:00'
---

# Server Side Template Injection

**Status**: ✓ Verified

## Summary

Template injection occurs when an unvalidated user input is embedded in a template .For example PHP uses smarty.twig etc.. templates . 

## Description

# Description

Template injection occurs when an unvalidated user input is embedded in a template .For example PHP uses smarty.twig etc.. templates .

# 

# Instructions

# 

1. Observe the url message where it says "Unfortunately the product is out of stock"





![4ed14b1e-0223-42a1-b49e-b809baeadfe8.png](_assets/images/Mash/4ed14b1e-0223-42a1-b49e-b809baeadfe8.png)







2.*<%= test %> *will be used to test the applciation's response* *to the *payload. Error message *reveals that underlying template used is of *ruby. *







![d751e7f2-0456-43c1-a2f3-42876e1ec0f7.PNG]()







3. Test the application with another *Payload  *which * *gets parsed by the application and the response can be seen in the page. 



*payload <% = 3*3%>*



![79296578-adca-425b-b8bd-b920681eb713.png](_assets/images/Mash/79296578-adca-425b-b8bd-b920681eb713.png)







4. In* ruby , system() *method is used to execute the arbitary commands. craft the payload to execute OS commands using system() function.



*Payload *

*<%= system("rm /home/carlos/morale.txt") %>*







![64ed2116-96e1-4203-b934-0533704627a9.png](_assets/images/Mash/64ed2116-96e1-4203-b934-0533704627a9.png)







The payload executes the *system()* command on server an removesd the *morale.txt* file from the server.


