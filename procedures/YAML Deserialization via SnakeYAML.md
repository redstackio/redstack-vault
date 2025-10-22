---
id: dfa18819-270e-4856-a89b-2b9125ec4291
name: YAML Deserialization via SnakeYAML
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.544381+00:00'
updated_at: '2023-04-06T03:55:59.555831+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Scheduled Transfer|T1029 - Scheduled Transfer]]'
tags:
- '[[SnakeYAML]]'
- '[[YAML Deserialization]]'
---

# YAML Deserialization via SnakeYAML

## Summary

YAML is a data serialization format that is commonly used for configuration files. SnakeYAML is a popular Java library for parsing YAML files. However, it is vulnerable to deserialization attacks when parsing untrusted data. An attacker can craft a malicious YAML payload that, when deserialized by 

## Description

# Description

YAML is a data serialization format that is commonly used for configuration files. SnakeYAML is a popular Java library for parsing YAML files. However, it is vulnerable to deserialization attacks when parsing untrusted data. An attacker can craft a malicious YAML payload that, when deserialized by SnakeYAML, can execute arbitrary code on the target system. This can lead to full compromise of the system and allow the attacker to achieve their objectives. This attack can be used as a vector for initial access, allowing the attacker to gain a foothold in the target environment.

## Requirements

1. Access to the target system's network.

1. Ability to send a malicious YAML payload to the target system.

## Defense

1. Do not deserialize untrusted data. Always validate and sanitize any input data before deserializing it.

1. Use a secure deserialization library that has been designed to prevent deserialization attacks, such as Jackson or Gson.

1. Implement strict network controls to prevent attackers from accessing the target system's network and sending malicious payloads.

## Objectives

1. To gain initial access to the target system through exploiting the vulnerability in SnakeYAML's deserialization process.

1. To execute arbitrary code on the target system through the crafted malicious YAML payload.

# Instructions

1. Execute the following command to deserialize the malicious YAML payload using SnakeYAML:

**Code**: [[!!javax.script.ScriptEngineManager [
  !!java.net.]]

> The `ScriptEngineManager` class is used to create a `ScriptEngine` instance, which can be used to execute arbitrary code. The `URLClassLoader` is used to load classes from a remote location, in this case, the attacker's server. The `URL` object specifies the location of the remote class to be loaded. When the YAML payload is deserialized, the `ScriptEngine` instance is created and the remote class is loaded, allowing the attacker to execute arbitrary code on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Scheduled Transfer|T1029 - Scheduled Transfer]]

## Tags

- [[SnakeYAML]]
- [[YAML Deserialization]]
