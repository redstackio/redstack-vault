---
id: 6ea4807a-17f4-439f-baae-c1bf9147f2fc
name: Insecure Deserialisation (Custom Gadget For Java)
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T18:29:54.268028+00:00'
updated_at: '2023-05-26T18:41:43.352795+00:00'
platforms:
- Web
tags:
- '[[Insecure Deserialisation]]'
- '[[java]]'
- '[[Web Applications]]'
---

# Insecure Deserialisation (Custom Gadget For Java)

**Status**: ✓ Verified

## Summary

Description Customs gadget is a piece of code which can be used to create a serialised object . To create gadget one needs to have access to source code to identify the java class that deserialises the object. Instructions 1. Login to the applciation and intercept the request using burp suite. Obse

## Description

Description

Customs gadget is a piece of code which can be used to create a serialised object . To create gadget one needs to have access to source code to identify the java class that deserialises the object. 

Instructions

1. Login to the applciation and intercept the request using burp suite. Observe that the session cookie contains serialised java object.

2. With burp running and proxying the requests through burp , navigate to sitemap in the burp window. Identify the request with ProductTemplate.java file. send the request to the repeater tab.

3. Observe that the ProductTemplate.java response reveals SQL statement .

4. The following Java code will  instantiates the ProductTemplate with id and then serialises the object and then Base64 encodes the object.

*Reference:[ https://github.com/PortSwigger/serialization-examples/blob/master/java/solution/Main.jav](https://github.com/PortSwigger/serialization-examples/blob/master/java/solution/Main.java)a*

**Code**: [[import data.productcatalog.ProductTemplate;
impor]]

5.Compile the java program from above step and create ProductTemplate with id attribute set to single apostrophe('). Copy the Base64 encoded string in the session cookie parameter identified in step1. 

6. The error message in the response confirms the SQL injection vulenrability and the database to be Postgres. 

7. Now modify the *id* attribute in the java code to *union sql statement* to enumerate the numebr of columns in the database.

8.  By enumeration technique we can confirm the number of cloumns to be 8 and columns 4,5 and 6 donot expect a string . 4,5 and 6 columns value can be Null. Now, modify the union statement to extract the password leaving 4,5 and 6 columns to null

*' UNION SELECT NULL, NULL, NULL, cast(password as numeric), NULL, NULL, NULL, NULL FROM users--*

9. Generate a  new java serialised object with the modified id attribute and submit the request to the server to extract the password.

## Platforms

- Web

## Tags

- [[Insecure Deserialisation]]
- [[java]]
- [[Web Applications]]
