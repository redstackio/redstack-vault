---
id: c02b1e4c-a831-4d14-a258-fe3c72fe7f31
name: 'Ruby Server Side Template Injection: Basic Calculations'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.164027+00:00'
updated_at: '2023-04-10T20:23:42.372198+00:00'
tags:
- '[[Ruby]]'
- '[[Ruby - Basic injections]]'
- '[[Server Side Template Injection]]'
---

# Ruby Server Side Template Injection: Basic Calculations

## Summary

Ruby Server Side Template Injection is a technique that allows an attacker to inject and execute arbitrary code into a web application, resulting in data theft or disruption of application functionality. In this specific case, the attacker can perform basic calculations such as calculating the squa

## Description

# Description

Ruby Server Side Template Injection is a technique that allows an attacker to inject and execute arbitrary code into a web application, resulting in data theft or disruption of application functionality. In this specific case, the attacker can perform basic calculations such as calculating the square of a number or multiplying two numbers. This technique is commonly used in web applications that use Ruby on Rails.

 

## Requirements

1. Access to the web application

1. Knowledge of Ruby syntax

1. Ability to inject code into the web application

 

## Defense

1. Implement input validation to prevent injection attacks

1. Use a web application firewall to detect and block injection attempts

1. Disable or restrict the use of server-side templates if not needed

 

## Objectives

1. Execute arbitrary code on the web application server

1. Steal sensitive data from the server

1. Disrupt the functionality of the web application

 

# Instructions

1. Use the following code to calculate the square of a number:
<%= number * number %>
Replace 'number' with the desired number.

 



**Code**: [[49]]



> This command utilizes Ruby's ERB library to calculate the square of a number. The 'number' variable can be replaced with any desired number. The code uses the multiplication operator to multiply the number by itself, resulting in the square of the number.

2. Use the multiplication operator (*) to calculate the result of 7 multiplied by 7.

 



**Code**: [[49]]



> The multiplication operator (*) is used to perform multiplication in Ruby. In this command, we are multiplying 7 by 7, which results in 49.

## Tags

- [[Ruby]]
- [[Ruby - Basic injections]]
- [[Server Side Template Injection]]


