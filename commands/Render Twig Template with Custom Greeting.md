---
id: 1679df36-e3a3-407b-ad1d-406486a1d71b
name: Render Twig Template with Custom Greeting
type: command
executor: bash
data: "$output = $twig->render(\n  'Dear' . $_GET['custom_greeting'],\n  array(\"\
  first_name\" => $user.first_name)\n);\n"
output: null
created_at: '2023-04-06T03:56:40.304497+00:00'
updated_at: '2023-04-10T20:23:51.948542+00:00'
---

# Render Twig Template with Custom Greeting

```bash
$output = $twig->render(
  'Dear' . $_GET['custom_greeting'],
  array("first_name" => $user.first_name)
);

```


