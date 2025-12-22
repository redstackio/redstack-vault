---
id: tool-uuid-001
name: Infogram-Java-Library
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.602Z'
platforms:
  - Java
tags:
  - api-client
  - infogram
url: 'https://developers.infogr.am/rest/'
validated: true
submitted: true
---

# Infogram-Java-Library

**Status**: Unverified

## Overview

The Infogram Java Library is an official client for interacting with Infogram's REST API, used for creating, managing, and publishing infographics programmatically. In security testing, it's leveraged to inject payloads into API endpoints.

## Description

This library handles authentication via API Key/Secret and provides methods like sendRequest for HTTP operations. It's useful for automating infographic creation in exploit scenarios targeting content sanitization flaws.

## Features

- Feature 1: OAuth-based authentication with Key/Secret
- Feature 2: POST/GET requests to endpoints like /infographics
- Feature 3: JSON parameter handling for content payloads

## Installation

### Requirements

- JDK 8 or higher
- Maven or Gradle for dependency management

### Install Commands

```bash
# Add to pom.xml for Maven
<dependency>
    <groupId>com.infogram</groupId>
    <artifactId>infogram-api</artifactId>
    <version>latest</version>
</dependency>
# Then mvn install
```

## Basic Usage

```java
InfogramAPI api = new InfogramAPI("key", "secret");
api.sendRequest("POST", "endpoint", params);
```

### Common Options

| Option | Description |
|--------|-------------|
| sendRequest(method, path, params) | Execute HTTP request with parameters |
| isSuccessful() | Check response status |

## Examples

### Example 1: Basic Usage

```java
HashMap<String, String> params = new HashMap<>();
params.put("title", "Test");
Response resp = api.sendRequest("POST", "infographics", params);
```

### Example 2: Advanced Usage

```java
// With malicious content as in exploit
params.put("content", "malicious payload");
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Java processes importing com.infogram.api
- API logs showing requests from Java User-Agent
- Unusual infographic creation patterns

## Related Procedures


## Related Tools


## References

- Official documentation: https://developers.infogr.am/rest/
- Related resources: Infogram API docs
