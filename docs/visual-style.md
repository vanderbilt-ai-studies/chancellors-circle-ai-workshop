# Chancellor's Circle document style

Use the instructor-provided **Preparing Students for an AI-Enabled Workforce: Table Discussion Guide** handout as the visual reference. The workshop's printable PDFs share its typography, restrained gold accents, dark question panels, cream deliverable panels, and clear numbered prompts.

## Page and type

- US Letter, with visible content aligned 33 points from the left and right edges.
- A small uppercase gold kicker identifies the event and document type.
- **Caladea Bold**, about 20 points, for the page title; Caladea Bold at about 14 points for section headings.
- **Carlito**, 11.2 points with 14-point leading, for participant instructions. Dense supporting material may use 10.5 points with 13-point leading; table text uses 10 points.
- Gold serif numbers sit separately from the instruction text. Begin each instruction with a short bold action.
- Use small uppercase, letter-spaced gold labels to identify a question, discussion section, or deliverable.

## Palette and emphasis

| Use | Color |
| --- | --- |
| Main text and dark question panels | `#1C1C1C` |
| Gold labels and numbering | `#7A5E1F` |
| Gold heading rule | `#B49248` |
| Label inside a dark panel | `#CFAE70` |
| Cream deliverable panel | `#F6F0E1` |
| Fine borders and footer rule | `#E0D5BB` |
| Supporting notes and footer text | `#5A5A5A` |

A dark panel presents one main question in larger white serif type. A cream panel identifies the concrete output or final action. Keep links readable in the digital PDF. Avoid decorative icons and additional accent colors.

## Choose layout for the task

Use a single reading column for sequential instructions, worksheets, and the 20-minute exercise pages. Use tables for the five approach choices, role comparisons, and simulation inputs/results. Multiple panels or columns are useful only when independent sections can be compared more easily that way. Do not force the reference handout's split lower section onto a sequential exercise.

The table guide and worksheet stay one page each. Keep the student's naming and submission step visible. Supporting materials may use separate pages rather than squeezing text smaller.

## Rebuild and inspect

The [PDF builder](../scripts/build_printables.py) is the shared implementation. Fonts and their accompanying licenses are stored under `assets/fonts/`, so a rebuild does not depend on fonts installed on a student's machine. These are the same typeface families used in the reference handout.

Rebuild all three PDFs with ReportLab, render them to images, and inspect every page. Check that text stays inside the margins, headings and footer lines align, question and deliverable panels are legible, and no page has a clipped or duplicated title. Verify one-page documents and the complete supporting pack before sharing.
