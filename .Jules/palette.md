## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - CLI Usage Output Scannability
**Learning:** For argparse CLI tools, omitting `metavar` on subparsers and positional choices creates cluttered, unreadable usage signatures in the help output when there are many choices.
**Action:** Use `metavar` for subparsers and positional arguments with many choices, and append `%(choices)s` to the `help` string so options remain visible in the detailed help text while keeping the usage string clean.
