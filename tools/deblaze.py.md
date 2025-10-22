---
id: 9a267596-2634-4447-afe9-0619dba43566
name: deblaze.py
type: tool
verified: false
created_at: '2019-08-28T21:17:22.477206+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# deblaze.py

## Overview

Through the use of the Flex programming model and the ActionScript language, Flash Remoting was born. Flash applications can make request to a remote server to call server side functions, such as looking up accounts, retrieving additional data and graphics, and performing complex business operation

## Description

Through the use of the Flex programming model and the ActionScript language, Flash Remoting was born. Flash applications can make request to a remote server to call server side functions, such as looking up accounts, retrieving additional data and graphics, and performing complex business operations. However, the ability to call remote methods also increases the attack surface exposed by these applications. This tool will allow you to perform method enumeration and interrogation against flash remoting end points. Deblaze came about as a necessity during a few security assessments of flash based websites that made heavy use of flash remoting. I needed something to give me the ability to dig a little deeper into the technology and identify security holes. On all of the servers I’ve seen so far the names are not case sensitive, making it much easier to bruteforce. Often times HTTP POST requests won’t be logged by the server, so bruteforcing may go unnoticed on poorly monitored systems.Deblaze provides the following functionality: 

Brute Force Service and Method Names

Method Interrogation

Flex Technology Fingerprinting
