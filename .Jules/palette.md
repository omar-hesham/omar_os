## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-05-18 - CLI Argument Discoverability
**Learning:** For CLI tools, naked invocations (no arguments) resulting in raw errors are a poor user experience. Presenting the `--help` menu instead guides users intuitively. Providing `help=` text and using `choices=` constraints for `argparse` improves discoverability.
**Action:** Always intercept empty argument lists to display the help menu, add descriptive help text, and strictly constrain choices for argument parsers.
