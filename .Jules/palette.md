## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.
## 2024-03-24 - Argparse CLI Scannability
**Learning:** For Python CLI tools using `argparse`, the default `usage:` string can become very long and unreadable when there are many subparsers or long lists of choices.
**Action:** Use `metavar` on subparsers (e.g., `metavar="COMMAND"`) and arguments to shorten the positional arguments and options lists in the usage output. Concurrently, append `(choices: %(choices)s)` to the argument's `help` string so that the valid options remain visible in the detailed parameter descriptions.
