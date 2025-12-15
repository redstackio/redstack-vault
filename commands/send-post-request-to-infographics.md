---
id: cmd-send-post-infographics-001
data: 'Response response = infogram.sendRequest("POST", "infographics", parameters);'
tags:
  - api-request
type: command
output: Response object with 201 status if successful
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.624Z'
verified: false
validated: true
submitted: true
---
# send-post-request-to-infographics

## Command

```java
Response response = infogram.sendRequest("POST", "infographics", parameters);
```

## Description

Sends a POST request to the /infographics endpoint using the authenticated API client and parameters map to create a new infographic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| infogram | Initialized InfogramAPI instance | Yes |
| method | "POST" string | Yes |
| endpoint | "infographics" string | Yes |
| parameters | HashMap with payload | Yes |

## Examples

### Basic Usage

```java
Response response = infogram.sendRequest("POST", "infographics", parameters);
```

### Advanced Usage

With error check:

```java
try {
  Response response = infogram.sendRequest("POST", "infographics", parameters);
  if (!response.isSuccessful()) {
    System.err.println("Failed: " + response.getStatusCode());
  }
} catch (Exception e) {
  e.printStackTrace();
}
```

## Expected Output

Response object; check isSuccessful() for true on 201, body contains infographic JSON.

## Related

- [[commands/handle-successful-api-response]]
- [[procedures/Create-Infographic-via-API-to-Inject-Stored-XSS]]
