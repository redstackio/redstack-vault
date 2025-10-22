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

2.*<%= test %> *will be used to test the applciation's response* *to the *payload. Error message *reveals that underlying template used is of *ruby. *

3. Test the application with another *Payload  *which * *gets parsed by the application and the response can be seen in the page. 

*payload <% = 3*3%>*

4. In* ruby , system() *method is used to execute the arbitary commands. craft the payload to execute OS commands using system() function.

*Payload *

*<%= system("rm /home/carlos/morale.txt") %>*

The payload executes the *system()* command on server an removesd the *morale.txt* file from the server.
