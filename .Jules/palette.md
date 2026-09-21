## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - CLI Empty State Guidance
**Learning:** For a CLI, an empty state without arguments typically results in a brief, unhelpful argparse missing argument error. Printing the full help text (usage and options) serves as a helpful empty state that guides users.
**Action:** When no arguments are passed to the CLI entry point, output the parser's help message instead of letting argparse show a generic failure.
