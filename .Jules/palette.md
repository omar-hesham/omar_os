## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2026-09-30 - Clean Up Help Output with Metavars
**Learning:** In a CLI tool using argparse, long lists of choices or subcommands can clutter the usage syntax and make the help menu difficult to read.
**Action:** Use `metavar` on subparsers and positional arguments to hide the exhaustive list in the usage syntax, and append `%(choices)s` to the `help` string so users can still see the valid options in the detailed help text.
