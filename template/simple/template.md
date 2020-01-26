[% title = "Remark" %]
[% BLOCK content %]

class: center, middle

# My big title

---

# First slide
Blabla

---

# \\(\KaTeX{}\\) in remark

# Display and Inline

1. This is an inline integral: \\(\int_a^bf(x)dx\\)
2. More $x={a \over b}$ formulae.

Display formula:

$$e^{i\pi} + 1 = 0$$

---

# Graphs via mermaid

<div class="mermaid">
graph LR
        A-->B
        B-->C
        C-->A
        D-->C
</div>

---

# Simple layout

.left-column[
- bullet 1
- bullet 2
]

.right-column[
- bullet 1
- bullet 2
- bullet 3
]

[% END %]
[% INCLUDE "template.html" %]