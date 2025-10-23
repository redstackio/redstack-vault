---
id: fd32ba48-d464-433d-b691-d2825cec433d
name: PHP Juggling Type and Magic Hashes - True Statement Comparison
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.627050+00:00'
updated_at: '2023-04-06T03:56:40.659142+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PHP Juggling type and magic hashes]]'
- '[[True statements]]'
- '[[Type Juggling]]'
commands:
- '[[Comparison of 0 and false]]'
- '[[Comparison of empty string, 0, false and null]]'
- '[[Comparison of empty string and 0]]'
- '[[Comparison of false and null]]'
- '[[Comparison of null and empty string]]'
- '[[Comparison of strings and hexadecimals]]'
- '[[Comparison of strings and numbers]]'
- '[[Comparison of strings and numbers]]'
- '[[Comparison of strings and numbers]]'
---

# PHP Juggling Type and Magic Hashes - True Statement Comparison

## Summary

In PHP, type juggling can lead to vulnerabilities when comparing variables. This is due to PHP's loose typing system that allows variables to be automatically converted from one type to another. Attackers can exploit this behavior by using magic hashes to bypass string comparison checks. By craftin

## Description

# Description

In PHP, type juggling can lead to vulnerabilities when comparing variables. This is due to PHP's loose typing system that allows variables to be automatically converted from one type to another. Attackers can exploit this behavior by using magic hashes to bypass string comparison checks. By crafting a specially-crafted input, an attacker can bypass authentication mechanisms and gain unauthorized access to sensitive data. This technique can be used as a stepping stone to further attacks, such as privilege escalation or lateral movement.

Technical Explanation: Type juggling is the process of converting a variable from one data type to another. In PHP, this can lead to vulnerabilities when comparing variables. When comparing two variables with the '==' operator, PHP will try to convert the variables to the same type before making the comparison. This can lead to unexpected behavior if the variables are not of the same type. Magic hashes are specially crafted strings that have the same hash value as another string. This can be used to bypass string comparison checks, leading to authentication bypass.

Business Value: This technique can be used by attackers to gain unauthorized access to sensitive data, leading to data breaches and financial losses for organizations.

 

## Requirements

1. Access to the target system

1. Knowledge of PHP type juggling and magic hashes

1. Ability to craft a specially-crafted input

 

## Defense

1. Use strict comparison operators (===, !==) instead of loose comparison operators (==, !=)

1. Use input validation to prevent specially-crafted inputs

1. Implement multi-factor authentication to mitigate the risk of authentication bypass

 

## Objectives

1. Bypass authentication mechanisms

1. Gain unauthorized access to sensitive data

 

# Instructions

1. To compare two variables in PHP, you can use either the '==' operator or the '===' operator.

The '==' operator compares the values of the variables, but it does not compare the data types. For example, '0010e2' is equal to '1e3' because they have the same value, even though they are represented differently.

The '===' operator, on the other hand, compares both the values and the data types of the variables. For example, '0x01' is not equal to 1 when using the '===' operator because they have different data types.

 



**Code**: [[var_dump('0010e2' == '1e3');           # true
var_]]



> In the provided code snippet, we are comparing different variables using both the '==' and '===' operators in PHP. The comments in the code indicate whether the comparison returns true or false.

The first comparison returns true because '0010e2' and '1e3' have the same value.

The second comparison returns true in PHP 5.0 because it only compares the values and ignores the extra whitespace in the second variable. However, it returns false in PHP 7.0 because it also compares the whitespace.

The third comparison returns true in PHP 5.0 because it only compares the values and ignores the leading whitespace in the second variable. However, it returns false in PHP 7.0 because it also compares the whitespace.

The fourth comparison returns true in PHP 5.0 because it only compares the values and ignores the data types. However, it returns false in PHP 7.0 because it also compares the data types.

The fifth comparison returns false because '0x1234Ab' and '1193131' have different values and data types.



**Command** ([[Comparison of strings and hexadecimals]]):

```bash
var_dump('0010e2' == '1e3');           # true
var_dump('0xABCdef' == ' 0xABCdef');     # true PHP 5.0 / false PHP 7.0
var_dump('0xABCdef' == '     0xABCdef'); # true PHP 5.0 / false PHP 7.0
var_dump('0x01' == 1)                # true PHP 5.0 / false PHP 7.0
var_dump('0x1234Ab' == '1193131');
```



2. The string equality operator (==) compares two values for equality, and returns true if they are equal. In PHP, the == operator performs type coercion, which means that if the two values being compared are of different types, PHP will attempt to convert one or both of the values to a compatible type. In the example above, the first comparison returns true because the string '123' is converted to the integer 123 before the comparison is made. The second comparison returns true because the string '123a' is converted to the integer 123 before the comparison is made. The third comparison returns false because the string 'abc' cannot be converted to a numeric value, so it is treated as 0.

 



**Code**: [['123'  == 123
'123a' == 123
'abc'  == 0]]



> The == operator is useful for checking if two values are equal, regardless of their type. However, it can lead to unexpected results if you are not careful. It is generally recommended to use the === operator for strict equality checking, which compares both the value and the type of the operands.



**Command** ([[Comparison of strings and numbers]]):

```bash
'123'  == 123
```





**Command** ([[Comparison of strings and numbers]]):

```bash
'123a' == 123
```





**Command** ([[Comparison of strings and numbers]]):

```bash
'abc'  == 0
```



3. To compare empty string, 0, false and NULL in PHP, you can use the double equals (==) operator.

 



**Code**: [['' == 0 == false == NULL
'' == 0       # true
0  =]]



> The double equals (==) operator in PHP compares the values of two operands, and returns true if they are equal, regardless of their data types. In the given example, the comparison between empty string, 0, false and NULL is evaluated as follows:

- '' == 0 == false == NULL: This expression compares empty string with 0, then compares the result with false, and finally compares the result with NULL. As all values are equal, the expression returns true.
- '' == 0: This expression compares empty string with 0, and returns true because both values are considered falsy in PHP.
- 0 == false: This expression compares 0 with false, and returns true because both values are considered falsy in PHP.
- false == NULL: This expression compares false with NULL, and returns true because both values are considered falsy in PHP.
- NULL == '': This expression compares NULL with empty string, and returns true because both values are considered falsy in PHP.



**Command** ([[Comparison of empty string, 0, false and null]]):

```bash
'' == 0 == false == NULL
```





**Command** ([[Comparison of empty string and 0]]):

```bash
'' == 0
```





**Command** ([[Comparison of 0 and false]]):

```bash
0  == false
```





**Command** ([[Comparison of false and null]]):

```bash
false == NULL
```





**Command** ([[Comparison of null and empty string]]):

```bash
NULL == ''
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Comparison of 0 and false]]
- [[Comparison of empty string, 0, false and null]]
- [[Comparison of empty string and 0]]
- [[Comparison of false and null]]
- [[Comparison of null and empty string]]
- [[Comparison of strings and hexadecimals]]
- [[Comparison of strings and numbers]]
- [[Comparison of strings and numbers]]
- [[Comparison of strings and numbers]]

## Tags

- [[PHP Juggling type and magic hashes]]
- [[True statements]]
- [[Type Juggling]]


