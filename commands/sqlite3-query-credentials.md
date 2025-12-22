---
data: sqlite3 webview.db "SELECT * FROM webviewCookies;"
tags:
  - sqlite
  - query
  - extraction
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.782Z'
id: 16d17017-2008-4f97-a72a-902267ace367
verified: false
validated: true
submitted: true
---
# sqlite3-query-credentials

## Command

```bash
sqlite3 webview.db "SELECT * FROM webviewCookies;"
```

## Description

This sqlite3 command opens the extracted WebView database and queries the webviewCookies table (or similar) to dump plain text credential entries like usernames and passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `webview.db` | Path to the SQLite database file | Yes |
| `SELECT * FROM webviewCookies;` | SQL query to retrieve all rows from the credentials table | Yes |

## Examples

### Basic Usage

```bash
sqlite3 webview.db "SELECT * FROM webviewCookies;"
```

### Advanced Usage

```bash
sqlite3 webview.db "SELECT name, value FROM webviewCookies WHERE name LIKE '%user%';"
```

## Expected Output

Tabular output of database rows, e.g., columns showing unencrypted data: "username	password123". No errors if table exists.

## Related

- [[Related Procedure|procedures/Extract-Credentials-from-Vine-WebView-Database]]
