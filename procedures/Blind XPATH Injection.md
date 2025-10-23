---
id: fd0961f9-fbbe-4a3e-9ab0-f1341fd01f19
name: Blind XPATH Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.409657+00:00'
updated_at: '2023-04-10T20:24:47.566388+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
- '[[Web Session Cookie|T1506 - Web Session Cookie]]'
sub_techniques:
- '[[DLL Side-Loading|T1574.002 - DLL Side-Loading]]'
tags:
- '[[Blind Exploitation]]'
- '[[XPATH Injection]]'
---

# Blind XPATH Injection

## Summary

Blind XPATH Injection is a type of injection attack that targets web applications which use XML-based data sources. This attack is carried out by injecting malicious code into the XML data source, which is then processed by the application. The injected code can be used to extract sensitive data, m

## Description

# Description

Blind XPATH Injection is a type of injection attack that targets web applications which use XML-based data sources. This attack is carried out by injecting malicious code into the XML data source, which is then processed by the application. The injected code can be used to extract sensitive data, modify data, or perform other malicious actions. This type of attack is called 'blind' because the attacker does not receive a response from the application, making it difficult to determine the success or failure of the attack. 

In technical terms, XPATH Injection is a type of injection attack that targets the XPATH language used to access and manipulate XML data. The attacker can modify the XPATH query to extract data that is not intended to be accessed, modify data, or perform other malicious actions. 

The business value of this attack is that it can be used to extract sensitive data such as user credentials, financial data, or other confidential information. This can lead to reputational damage, financial loss, and legal liabilities for the affected organization.

 

## Requirements

1. Access to the target web application

1. Knowledge of the XML data source structure

1. Access to the internet

 

## Defense

1. Ensure that the web application is updated with the latest security patches

1. Implement input validation to prevent injection attacks

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Extract sensitive data from the XML data source

1. Modify data in the XML data source

1. Perform other malicious actions on the application

 

# Instructions

1. This command is used to retrieve the size of a string in a SQL query. The 'account' field should be replaced with the name of the string column you want to retrieve the size of. The 'SIZE_INT' field should be replaced with the expected size of the string in integer format.

 



**Code**: [[and string-length(account)=SIZE_INT]]



> The 'string-length' function is used to retrieve the length of the string in the specified column. The 'SIZE_INT' argument is used to compare the length of the string to the expected size. This command can be useful for data validation or data cleansing purposes.

2. This command extracts a character from the username of a user with userid 5. The character to extract can be specified using either a single character or its integer Unicode codepoint value.

 



**Code**: [[substring(//user[userid=5]/username,2,1)=CHAR_HERE]]



> The 'substring' function is used to extract a specific character from the username. The first argument specifies the string to extract from, the second argument specifies the starting position (in this case, the second character), and the third argument specifies how many characters to extract (in this case, just 1). The extracted character can be compared to either a single character using the '=' operator, or an integer Unicode codepoint value using the 'codepoints-to-string' function. For example, to extract the second character 'b' from the username and compare it to the character 'c', the command would be: 'substring(//user[userid=5]/username,2,1)='c''. To extract the second character 'b' and compare it to the Unicode codepoint value for 'b' (98), the command would be: 'substring(//user[userid=5]/username,2,1)=codepoints-to-string(98)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Hijack Execution Flow|T1574 - Hijack Execution Flow]]
- [[Web Session Cookie|T1506 - Web Session Cookie]]

### Sub-Techniques

- [[DLL Side-Loading|T1574.002 - DLL Side-Loading]]

## Tags

- [[Blind Exploitation]]
- [[XPATH Injection]]


