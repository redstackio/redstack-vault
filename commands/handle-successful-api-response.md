---
id: cmd-handle-response-001
data: >-
  if (response.isSuccessful()) { InputStream is = response.getResponseBody();
  System.out.print(getStringFromInputStream(is).replace(",", ",\n")); }
tags:
  - response-handling
type: command
output: Printed response body with newlines
executor: java
platforms:
  - Java
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.613Z'
verified: false
validated: true
submitted: true
---
# handle-successful-api-response

## Command

```java
if (response.isSuccessful()) { InputStream is = response.getResponseBody(); System.out.print(getStringFromInputStream(is).replace(",", ",\n")); }
```

## Description

Checks if the API response is successful and prints the body content with commas replaced by newlines for readability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| response | Response object from sendRequest | Yes |

## Examples

### Basic Usage

```java
if (response.isSuccessful()) { 
  InputStream is = response.getResponseBody(); 
  System.out.print(getStringFromInputStream(is).replace(",", ",\n")); 
}
```

### Advanced Usage

Full context:

```java
Response response = infogram.sendRequest("POST", "infographics", parameters);
if (response.isSuccessful()) { 
  // ... print as above
} else {
  System.out.println("Error: " + response.getStatusCode());
}
```

Note: Requires getStringFromInputStream helper method.

## Expected Output

Formatted JSON body printed to console, e.g., infographic ID and details on new lines.

## Related

- [[commands/send-post-request-to-infographics]]
- [[procedures/Create-Infographic-via-API-to-Inject-Stored-XSS]]
