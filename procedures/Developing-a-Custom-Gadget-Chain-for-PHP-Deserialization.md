---
type: procedure
description: >-
  Crafts a custom gadget chain to exploit PHP deserialization vulnerabilities in
  web applications, enabling arbitrary command execution such as file deletion.
verified: true
submitted: true
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - deserialization
  - web-applications
  - rce
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Developing-a-Custom-Gadget-Chain-for-PHP-Deserialization

## Summary

This procedure demonstrates how to analyze a vulnerable PHP application's source code to identify and craft a custom gadget chain for deserialization attacks. By manipulating serialized session data, an attacker can trigger arbitrary code execution, such as deleting files on the server, leading to remote code execution (RCE) in web environments.

## Description

PHP deserialization vulnerabilities occur when untrusted data is deserialized without proper validation, allowing attackers to inject malicious objects that invoke dangerous methods. In this scenario, the application uses serialized objects in session cookies, and by inspecting the source code of classes like CustomTemplate and DefaultMap, a gadget chain can be constructed to call the exec() function with attacker-controlled commands. This technique requires access to the application's login and source code exposure points, typically in lab environments like PortSwigger's Web Security Academy. The attack assumes the target uses PHP's unserialize() function on user-supplied data and exposes class implementations that can be chained for gadget exploitation.

## Requirements

1. Valid login credentials to the target web application.
2. Access to a proxy tool like [[tools/Burp-Suite]] for intercepting and modifying HTTP requests and decoding data.
3. Knowledge of the target's source code, often exposed via directory traversal or sitemap enumeration.
4. A vulnerable PHP application with deserialization in session handling, such as one using CustomTemplate and DefaultMap classes.
5. Network access to the target web server.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user-supplied data before deserialization; prefer JSON over PHP serialization.
- Use allowlists for expected classes in unserialize() calls.
- Implement web application firewalls (WAFs) to detect anomalous serialized payloads in cookies or POST data.
- Enable PHP logging for deserialization errors and monitor for unexpected method invocations like exec().
- Regularly audit source code for exposed gadgets and apply property-based deserialization restrictions.

## Objectives

1. Identify exploitable gadget chains in the application's PHP classes.
2. Craft and encode a malicious serialized object to trigger command execution.
3. Achieve RCE, such as file deletion, by injecting the payload into session data.
4. Verify successful exploitation through application responses or file system changes.

## Instructions

### Step 1: Authenticate and Inspect Session Data

**Context**: Log in to the application to obtain a serialized PHP object in the session cookie, confirming the deserialization entry point.

Navigate to the login page and authenticate using provided credentials. Use [[tools/Burp-Suite]] to intercept the response and examine the session cookie for serialized PHP objects starting with 'O:' or 's:' indicators.

> This step establishes the baseline serialized format and ensures the session is active for manipulation.

### Step 2: Enumerate and Retrieve Source Code

**Context**: Locate and fetch the source code of relevant PHP files to identify potential gadget classes and methods.

From the application's sitemap or directory listing, identify files like `/cgi-bin/libs/CustomTemplate.php`. Intercept a GET request to this file using [[tools/Burp-Suite]] and retrieve the source code. Analyze for magic methods like `__wakeup()` and classes with callable properties, such as CustomTemplate referencing default_desc_type and desc, and DefaultMap with a callback property that invokes methods like exec().

> Understanding the class structure reveals how to chain objects: CustomTemplate's __wakeup() creates a Product using desc, which calls DefaultMap's get() method, allowing callback execution.

### Step 3: Decode the Original Session Cookie

**Context**: Decode the legitimate session cookie to understand its structure and prepare for payload injection.

Copy the session cookie value from the intercepted login response. Paste it into the Burp Decoder (under the Inspector or Decoder tab in [[tools/Burp-Suite]]) and select Base64 decode to reveal the serialized PHP object.

> Decoding confirms the format (e.g., O:ClassName:properties) and identifies modifiable fields like object properties.

### Step 4: Craft the Custom Gadget Chain

**Context**: Construct a malicious serialized object using identified gadgets to execute a command, such as file deletion.

Reference the [[codes/Custom-PHP-Deserialization-Gadget-for-File-Deletion]] payload. Set CustomTemplate->default_desc_type to the desired command (e.g., "rm /home/carlos/morale.txt"), CustomTemplate->desc to a DefaultMap object, and DefaultMap->callback to "exec". Serialize the object manually or via a PHP script, then encode it in Base64 using Burp Decoder.

> The gadget chain exploits the __wakeup() method to trigger the callback during deserialization, executing the command.

### Step 5: Encode and Inject the Payload

**Context**: Apply URL encoding to the Base64 payload and inject it into the session cookie to trigger deserialization on the next request.

In Burp Decoder, take the Base64-encoded serialized object and apply URL encoding. Replace the original session cookie value in a subsequent request (e.g., to the homepage) with the encoded payload. Forward the request to the server.

> URL encoding ensures the payload survives HTTP transmission without breaking the cookie format.

### Step 6: Verify Exploitation

**Context**: Confirm the command executed successfully by checking application responses or target file system.

Observe the server's response to the injected request; a 200 OK without errors indicates successful deserialization and execution. If applicable, verify the file deletion (e.g., attempt to access /home/carlos/morale.txt and confirm 404).

> Success is indicated by no deserialization errors and achievement of the command's effect, such as file removal.
