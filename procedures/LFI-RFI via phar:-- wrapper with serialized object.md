---
id: 81c17528-45ce-4573-8fa4-c6e427fdbfe1
name: LFI/RFI via phar:// wrapper with serialized object
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.437781+00:00'
updated_at: '2023-04-10T20:22:20.107482+00:00'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper phar://]]'
---

# LFI/RFI via phar:// wrapper with serialized object

## Summary

LFI/RFI via phar:// wrapper with serialized object is a technique used by attackers to execute arbitrary code on a target system. Using this technique, an attacker can create a phar file with a serialized object in its meta-data. When a file operation is performed on the phar file via the phar:// w

## Description

# Description

LFI/RFI via phar:// wrapper with serialized object is a technique used by attackers to execute arbitrary code on a target system. Using this technique, an attacker can create a phar file with a serialized object in its meta-data. When a file operation is performed on the phar file via the phar:// wrapper, the serialized meta data is unserialized. If the application has a class named AnyClass and it has the magic method __destruct() or __wakeup() defined, those methods are automatically invoked. This can allow the attacker to execute arbitrary code on the target system. This technique can be used to gain access to sensitive data or to execute malicious code on the target system.

 

## Requirements

1. Access to the target system

 

## Defense

1. Do not allow user input to be used in file operations

1. Ensure that classes with __destruct() or __wakeup() methods are not used in the application

1. Use a PHP version that has the phar:// wrapper disabled by default

 

## Objectives

1. Execute arbitrary code on the target system

1. Gain access to sensitive data

 

# Instructions

1. 

 



**Code**: [[// create new Phar
$phar = new Phar('test.phar');
]]



> This command creates a new Phar file with the name 'test.phar' and adds a file named 'test.txt' with the contents 'text'. It then sets the stub of the Phar file and adds an object of the 'AnyClass' class as meta data. The object has a 'data' property set to 'rips'.

2. 

 



**Code**: [[class AnyClass {
    function __destruct() {
     ]]



> This command includes the phar file 'test.phar' via the phar:// wrapper. If the application has a class named 'AnyClass' and it has the magic method __destruct() or __wakeup() defined, those methods are automatically invoked. In this case, the __destruct() method echoes the 'data' property of the 'AnyClass' object which is 'rips'.

3. 

 



**Code**: [[file_exists('phar://test.phar');]]



> This command triggers the unserialize for the phar:// wrapper in any file operation. In this case, the 'file_exists' function is used to check if the phar file 'test.phar' exists. This triggers the unserialize of the serialized meta data in the phar file.

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper phar://]]


