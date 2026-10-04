## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - Python argparse UX improvements
**Learning:** For Python CLI tools using `argparse`, long lists of choices (like `LIFECYCLE_STAGES`) clutter the `usage:` block, making it hard to scan. By using `metavar`, we can hide the massive list from the usage string. Using `%(choices)s` in the `help=` text ensures options remain visible in the detailed help text instead, providing a much cleaner user experience.
**Action:** Always use `metavar` for positional arguments or subparsers with many choices to keep usage blocks concise. Use `%(choices)s` in the `help` string to present the available choices neatly.
