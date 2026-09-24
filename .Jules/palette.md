## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - CLI Usage Empathy
**Learning:** For Python CLI tools, users often run the base command without arguments first to see what it does. Defaulting to an `argparse` missing argument error provides a poor first impression compared to displaying the help text.
**Action:** Always intercept zero-argument invocations in `main()` to `print_help()` and exit cleanly.
