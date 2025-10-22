---
id: 71864523-a602-4683-9b26-aaa5c3d3a00d
name: Render Twig Template with First Name
type: command
executor: bash
data: "$output = $twig->render(\n  \"Dear {first_name}\",\n  array(\"first_name\"\
  \ => $user.first_name)\n);"
output: null
created_at: '2023-04-06T03:56:40.304622+00:00'
updated_at: '2023-04-10T20:23:51.948542+00:00'
---

# Render Twig Template with First Name

```bash
$output = $twig->render(
  "Dear {first_name}",
  array("first_name" => $user.first_name)
);
```
