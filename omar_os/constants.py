"""Constants for OMAR OS Project Core (v0.2).

Single source of truth for paths, classifications, and lifecycle stages.
Stdlib only.
"""

from pathlib import Path

# --- Repo paths (resolved relative to the repository root) -------------------
# The repo root is the parent directory of this package's parent (omar_os/..).
REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = REPO_ROOT / "projects"
TEMPLATE_DIR = PROJECTS_DIR / "_template"
MANIFEST_FILE = "project.json"
STATE_FILE = "state.json"

# The 6 required markdown scaffold files (single-source rule, ADR-0002).
SCAFFOLD_MD_FILES = (
    "PROJECT.md",
    "REQUIREMENTS.md",
    "FLOW.md",
    "DECISIONS.md",
    "TASKS.md",
    "REVIEW.md",
)
# A real project must contain the 6 markdown files PLUS the two JSON manifests.
REQUIRED_PROJECT_FILES = SCAFFOLD_MD_FILES + (MANIFEST_FILE, STATE_FILE)

# --- Classifications (ADR-0002) ----------------------------------------------
# Only `public` is permitted inside the public repo.
CLASSIFICATIONS = ("public", "internal", "confidential", "restricted")
PUBLIC_CLASSIFICATION = "public"

# --- Effort levels ------------------------------------------------------------
EFFORT_LEVELS = ("low", "medium", "high")
DEFAULT_EFFORT = "low"

# --- Lifecycle stages (from workflows/project_lifecycle.md) -------------------
LIFECYCLE_STAGES = (
    "idea",
    "intake",
    "problem_definition",
    "decomposition",
    "research",
    "flow",
    "logic_review",
    "alternatives",
    "decision",
    "plan",
    "execution",
    "testing",
    "review",
    "fix",
    "document",
    "lessons",
    "knowledge",
    "complete",
)
REVIEW_STAGE = "review"
COMPLETE_STAGE = "complete"

# --- Status values ------------------------------------------------------------
STATUSES = ("todo", "in_progress", "blocked", "done")
STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in_progress"
STATUS_DONE = "done"

# --- Schema / manifest versions ----------------------------------------------
SCHEMA_VERSION = "1.0"

# kebab-case: lowercase letters/digits, single hyphens, no leading/trailing hyphen.
KEBAB_CASE_RE = r"^[a-z0-9]+(-[a-z0-9]+)*$"
