## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-05-24 - CLI Help Scannability
**Learning:** For CLI tools using `argparse`, a long list of choices or subcommands can clutter the default `usage:` output, making it unreadable.
**Action:** Use `metavar` to simplify the top-level usage string, and append `(%(choices)s)` to the argument's help text so users still see valid options when reading detailed descriptions.
