---
id: tool-infogram-java-001
url: 'https://developers.infogr.am/rest/'
tags:
  - api-client
  - infogram
type: tool
verified: false
platforms:
  - Java
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.594Z'
validated: true
submitted: true
---
# Infogram-Java-API-Library

**Status**: Unverified

## Overview

The official Java client library for Infogram's REST API, used to create, manage, and publish infographics programmatically. In security testing, it's leveraged to inject payloads into content parameters for vulnerabilities like stored XSS.

## Description

This library wraps HTTP requests to Infogram endpoints, handling authentication via API key/secret. Key features include sendRequest method for POST/GET, supporting JSON payloads for infographic creation. Commonly used in offensive ops to automate exploit submission without browser interaction. Configuration: Initialize with credentials, pass HashMap parameters.

## Features

- Feature 1: Authenticated REST API calls with key/secret
- Feature 2: Support for infographic creation via POST /infographics with custom content JSON
- Feature 3: Response handling for status and body parsing

## Installation

### Requirements

- JDK 8+
- Build tool like Maven (add as dependency if available) or direct JAR

### Install Commands

```bash
# Download JAR from https://developers.infogr.am/rest/
wget https://path-to-jar/infogram-java-api.jar
# Add to classpath: javac -cp .:infogram-java-api.jar Main.java
```

## Basic Usage

```java
import com.infogram.api.InfogramAPI;
import com.infogram.api.Response;

InfogramAPI api = new InfogramAPI("key", "secret");
Response res = api.sendRequest("POST", "infographics", params);
```

### Common Options

| Option | Description |
|--------|-------------|
| sendRequest(method, endpoint, params) | Core method for API calls |
| isSuccessful() | Checks response status |
| getResponseBody() | Retrieves InputStream of body |

## Examples

### Example 1: Basic Usage

```java
// Create infographic
Map<String, String> params = new HashMap<>();
params.put("title", "Test");
Response r = api.sendRequest("POST", "infographics", params);
if (r.isSuccessful()) System.out.println("Created!");
```

### Example 2: Advanced Usage

```java
// With malicious content
params.put("content", "[{\"type\":\"h1\",\"text\":\"Payload\"}]");
Response r = api.sendRequest("POST", "infographics", params);
// Handle as in commands
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (when injecting payloads)

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to api.infogr.am with POST /infographics
- Java process with infogram-api.jar in stack traces
- Anomalous infographic creations in logs

## Related Procedures

- [[procedures/Create-Infographic-via-API-to-Inject-Stored-XSS]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]

## Related Tools

- [[tools/Postman]] (alternative for API testing)
- [[tools/curl]] (for non-Java requests)

## References

- Official documentation: https://developers.infogr.am/rest/
- HackerOne report: https://hackerone.com/reports/287562
