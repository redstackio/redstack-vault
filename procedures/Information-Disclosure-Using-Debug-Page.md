---
type: procedure
description: >-
  Extract sensitive information such as SECRET_KEY from debug pages in web
  applications using Burp Suite.
verified: true
submitted: true
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - information-disclosure
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
---

# Information-Disclosure-Using-Debug-Page

## Summary

This procedure demonstrates how to identify and exploit debug pages in web applications to disclose sensitive information, such as SECRET_KEY values, which are typically intended for development environments only. By leveraging tools like Burp Suite, attackers can uncover configuration details, credentials, or server information that aid in further exploitation.

## Description

Debug pages, such as phpinfo.php, are often left accessible in production environments due to misconfigurations. These pages can reveal critical details like encryption keys, database configurations, or server paths. This technique targets information disclosure vulnerabilities (OWASP A6: Sensitive Data Exposure) and is commonly used during reconnaissance or initial access phases in web penetration testing. The procedure assumes the target is a PHP-based web application but can be adapted for other frameworks with similar debug endpoints. Success depends on the application's configuration and the presence of unremoved development artifacts.

## Requirements

1. Burp Suite Professional or Community Edition installed and running as a proxy.
2. Browser configured to route traffic through Burp Proxy (e.g., FoxyProxy extension or manual settings).
3. Network access to the target web application.
4. Basic knowledge of HTTP requests and web application structure.

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to debug endpoints (e.g., phpinfo.php) in production environments using .htaccess rules or server configurations.
- Implement web application firewalls (WAFs) to block requests to known debug paths.
- Enable logging for unusual requests to administrative or debug URLs and monitor for tools like Burp Suite via user-agent strings or proxy patterns.
- Conduct regular code reviews and use automated scanners to identify exposed sensitive information.

## Objectives

1. Identify hidden debug pages through source code inspection and site mapping.
2. Access and analyze responses from debug endpoints to extract sensitive data like SECRET_KEY.
3. Validate the impact of the disclosure for potential follow-on attacks, such as session hijacking or encryption bypass.

## Instructions

### Step 1: Configure Burp Proxy and Access the Target Application

**Context**: Set up traffic interception to monitor and manipulate requests to the web application, ensuring all interactions are proxied through Burp Suite for analysis.

Configure your browser to use Burp as the proxy (typically localhost:8080). Launch the target web application in the browser and navigate to the main page. In Burp Suite, ensure the Proxy tab is active and intercept is enabled if needed for initial requests.

> This step establishes the foundation for inspecting traffic. Successful proxy configuration is indicated by requests appearing in Burp's Proxy > HTTP history tab.

### Step 2: Inspect Page Source for Debug References

**Context**: Debug pages are often referenced in HTML comments or source code, providing clues to hidden endpoints that can be directly accessed.

In the browser, right-click on the loaded page and select 'View Page Source' (or Ctrl+U). Search for comments or scripts mentioning debug, phpinfo, or similar terms (e.g., <!-- debug: /phpinfo.php -->). Note any URLs or paths discovered.

> Expected output includes visible references in comments, such as paths to debug files. If no comments are found, proceed to manual enumeration of common debug paths like /debug.php or /info.php.

### Step 3: Map and Navigate to the Debug Page in Burp Target

**Context**: Use Burp's site map to discover and target potential debug endpoints, allowing for organized exploration of the application's structure.

Switch to Burp Suite's Target > Site map tab. If not already captured, browse the application to populate the site map. Locate or manually add the suspected debug path (e.g., /phpinfo.php). Right-click the entry and select 'Send to Repeater' to prepare for request manipulation.

> This isolates the request for detailed inspection. Success is confirmed when the debug path appears in the site map without errors.

### Step 4: Send Request to Repeater and Analyze Response for Sensitive Data

**Context**: Replay and examine the HTTP response from the debug page to extract disclosed information, such as configuration variables or keys.

In the Repeater tab, click 'Send' to execute the request to the debug endpoint. Review the response body for sensitive details, such as PHP configuration info, environment variables, or SECRET_KEY values. Use the 'Inspect' feature to highlight or search for keywords like 'secret', 'key', or 'config'.

> Expected output is a detailed server information page (e.g., phpinfo output) containing the SECRET_KEY or similar data. Copy any sensitive values for further use, and note potential impacts like key compromise.
