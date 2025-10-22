---
id: 9ed42429-b473-4418-bee1-eaac66fc41ea
name: Command Injection via Curl Arguments
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:54.022953+00:00'
updated_at: '2023-04-06T03:55:54.041570+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Argument Injection]]'
commands:
- '[[Download Python file from Google France homepage]]'
- '[[Execute Curl Command]]'
- '[[Get Post]]'
- '[[Retrieve post data from jsonplaceholder]]'
---

# Command Injection via Curl Arguments

## Summary

Command injection is a technique used by attackers to execute arbitrary commands on a system. In this case, the attacker is able to inject additional arguments to the curl command to execute commands on the system. This can be used to download and execute malicious files, exfiltrate data, or perfor

## Description

# Description

Command injection is a technique used by attackers to execute arbitrary commands on a system. In this case, the attacker is able to inject additional arguments to the curl command to execute commands on the system. This can be used to download and execute malicious files, exfiltrate data, or perform other malicious activities. By injecting additional arguments, the attacker can bypass input validation and execute any command they want. This technique is often used in combination with other attack techniques to achieve persistence or escalate privileges.

## Requirements

1. Access to a vulnerable system with curl installed

## Defense

1. Implement input validation to prevent injection of additional arguments

1. Use parameterized queries to prevent injection of malicious commands

1. Limit access to system resources to prevent unauthorized access

## Objectives

1. Execute arbitrary commands on the system

1. Download and execute malicious files

1. Exfiltrate data from the system

# Instructions

1. python python_rce.py "https://www.google.fr -o test.py"

**Code**: [[curl]]

> This command will generate a curl command that downloads the Google France homepage and saves it to a file named test.py.

**Command** ([[Get Post]]):

```bash
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

2. 

**Code**: [[from shlex import quote,split
import sys
import su]]

> This Python script takes the generated curl command and executes it on the system. The additional arguments are split and added to the curl command, allowing the attacker to execute arbitrary commands.

**Command** ([[Execute Curl Command]]):

```bash
from shlex import quote,split
import sys
import subprocess

if __name__=="__main__":
    command = ['curl']
    command = command + split(sys.argv[1])
    print(command)
    r = subprocess.Popen(command)
```

3. 

**Code**: [[curl]]

> By injecting additional arguments to the curl command, the attacker can execute arbitrary commands on the system. This can be used to download and execute malicious files, exfiltrate data, or perform other malicious activities.

**Command** ([[Retrieve post data from jsonplaceholder]]):

```bash
curl -X GET https://jsonplaceholder.typicode.com/posts/1
```

4. 

**Code**: [[['curl', 'https://www.google.fr', '-o', 'test.py']]]

> This command prints the generated curl command to the console, showing how the additional arguments are split and added to the command.

**Command** ([[Download Python file from Google France homepage]]):

```bash
['curl', 'https://www.google.fr', '-o', 'test.py']
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Download Python file from Google France homepage]]
- [[Execute Curl Command]]
- [[Get Post]]
- [[Retrieve post data from jsonplaceholder]]

## Tags

- [[Argument Injection]]
