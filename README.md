# MD Notes

Notes in MarkDown

This repo uses [VSCode-renderable Markdown](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview) for all its files (except `README.md` which uses [GFM](https://github.github.com/gfm/)).

[Pandoc](https://pandoc.org/) is used to convert [Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) into HTML and PDF versions.

### Creation of PDF

By default, Pandoc uses [LaTeX](https://www.latex-project.org/) for generating PDFs.

The `pdf-meta.yaml` file is used as options for LaTeX code generation from the Markdown. The options specify the page margins, font-size and extra package `mhchem` (used to render chemical equations.)

### Creation of HTML

By default, [Pandoc uses Unicode Characters](https://pandoc.org/MANUAL.html#math-rendering-in-html) to render Math characters. However, this gives acceptable results for basic math only.

The other options provided by Pandoc to render math in HTML are: [MathJax](https://www.mathjax.org/), [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML), WebTeX (renders equations as images), [KaTeX](https://katex.org/) and [GladTeX](https://humenda.github.io/GladTeX/)

This repo uses [KaTeX](https://katex.org/) for Math rendering in HTML.

The `html-meta.yaml` file defines a couple of scripts to be included in the HTML, which define a macro for naming of chemical equations, and add the KaTeX version of `mhchem`.

### Automation

The two conversions of `MarkDown -> (LaTeX) -> PDF` and `MarkDown -> (KaTeX) -> HTML` take place through Pandoc. The Pandoc commands are run from the `index.js` file.

There is a `npm` `convert` script setup which runs the `index.js` file with the passed filename. For example, `npm run convert Chemistry\AcidsBasesSalts.md` will generate `Chemistry\AcidsBasesSalts.pdf` and `Chemistry\AcidsBasesSalts.html.`
