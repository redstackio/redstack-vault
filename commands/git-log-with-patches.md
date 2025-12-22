---
id: e8bad82f-9c87-414b-b192-8d7148f4ec39
name: git-log-with-patches
type: command
executor: bash
data: git log -p
output: >-
  commit 584d5f1a2f95e117244d9128bff7a579ca1d4968 (HEAD -> master,
  origin/master)

  Author: bob <bob@corp.net>

  Date:   Sat Oct 29 12:01:40 2018 +0530

      changed auth

  diff --git a/src/main/java/com/test.java b/src/main/java/com/test.java

  new file mode 100644

  index 0000000..2789c42

  --- /dev/null

  +++ b/src/main/java/com/test.java

  @@ -0,0 +1,16 @@

  +@Service

  +public class Test {

  +    // potential secret here

  +}
created_at: '2019-10-16T22:13:26.080727+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - git
  - secrets
verified: true
validated: true
---

# git-log-with-patches

## Command

```bash
git log -p
```

## Description

This command displays the commit history of the Git repository with full patch diffs (-p flag), allowing inspection of file changes for sensitive information like credentials in added or modified lines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Show patch/diff for each commit | Yes |
| `--all` | (Optional) Include all branches; use if not default | No |

## Examples

### Basic Usage

```bash
git log -p
```

### Advanced Usage

```bash
git log -p --author="bob" | grep -i password
```

Filter for specific authors or keywords to narrow down secrets.

## Expected Output

Description of what output to expect when the command runs successfully.

```
commit 584d5f1a2f95e117244d9128bff7a579ca1d4968 (Secrets (HEAD -> master, origin/master)
Author: bob <bob@corp.net>
Date:   Sat Oct 29 12:01:40 2018 +0530

    changed auth

diff --git a/src/main/java/com/test.java b/src/main/java/com/test.java
new file mode 100644
index 0000000..2789c42
--- /dev/null
+++ b/src/main/java/com/test.java
@@ -0,0 +1,16 @@
+@Service
+public class Test {
+    // Look for secrets in diffs
+}
```

## Related

- [[procedures/Enumerate-Git-Repository-for-Secrets]]
- [[commands/git-reflog-with-patches]]
