#!/usr/bin/env python3
"""Convert the assembled markdown manuscript to LaTeX."""

import re
import sys

INPUT = "/Users/alex/Codes/playground/path-to-satoshis-vision/manuscript/正本清源比特币.md"
OUTPUT = "/Users/alex/Codes/playground/path-to-satoshis-vision/latex/main.tex"

# ── Structure mapping ──────────────────────────────────────────────
# Line numbers (1-indexed) for parts and chapters
PARTS = {
    342: ("歧路", ""),
    1562: ("正本", ""),
    3910: ("清源", ""),
}

# Sub-part section headers (unnumbered sections within 正本)
SUBPART_HEADERS = {
    1564: "一、内核：比特币是什么",
    1889: "二、骨架：比特币如何运作",
    2658: "三、外延：比特币的设计哲学",
    3369: "四、能力：比特币能做什么",
}

CHAPTERS = {
    344: "第一章：区块链行业的现状",
    556: "第二章：比特币之前——数字货币的探索",
    812: "第三章：一个误解引发的连锁反应",
    1062: "第四章：扩容的死胡同",
    1306: "第五章：分布式数据库不是区块链",
    1566: "第六章：电子现金——一个被遗忘的定义",
    1891: "第七章：交易——产权转移的数字表达",
    2161: "第八章：工作量证明——用能量锚定秩序",
    2392: "第九章：激励与网络——自运行的经济机器",
    2660: "第十章：隐私——可审计的假名系统",
    2862: "第十一章：比特币与法律——在法律框架内运作的系统",
    3120: "第十二章：治理——写入石头的规则",
    3371: "第十三章：扩容——一条链承载全球",
    3662: "第十四章：脚本与智能合约——图灵完备的比特币",
    3912: "第十五章：比特币与 BTC——协议分裂的真相",
    4208: "第十六章：BSV——回归原始协议",
    4408: "第十七章：全球账本——数字经济的基础设施",
}

# Preface (序章) — treated as unnumbered chapter
PREFACE_LINE = 8  # "# 序章：一切从双花开始"

# Lines to skip entirely
SKIP_LINES = {1, 2, 3, 4, 5, 6, 7}  # Title block and --- separator
# Also skip the --- separators
SEPARATOR_LINES = {6, 340, 554, 810, 1060, 1304, 1549, 1560, 1866, 1887, 2159, 2390, 2656, 2860, 3118, 3367, 3660, 3908, 4206, 4406}


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in text, but preserve markdown formatting."""
    # Don't escape backslashes that are part of LaTeX commands (we'll add those later)
    # Escape in specific order to avoid double-escaping
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('{', r'\{')
    text = text.replace('}', r'\}')
    text = text.replace('~', r'\textasciitilde{}')
    text = text.replace('^', r'\textasciicircum{}')
    return text


def process_inline(text: str) -> str:
    """Process inline markdown formatting after LaTeX escaping."""
    # Bold: **text** → \textbf{text}
    # We need to handle escaped chars: \*\* becomes the marker after escaping
    # Actually, * is not escaped in LaTeX, so **text** stays as-is
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic: *text* → \textit{text}  (single *)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\\textit{\1}', text)
    # Inline code: `text` → \texttt{text}
    text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', text)
    # Em dash: — stays as-is in XeLaTeX with UTF-8
    return text


def convert():
    with open(INPUT, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    body_lines = []
    i = 0
    in_quote = False
    quote_buffer = []

    def flush_quote():
        nonlocal in_quote, quote_buffer
        if not in_quote:
            return
        in_quote = False
        # Check if this is a whitepaper quote (contains both EN and CN text)
        full_text = '\n'.join(quote_buffer)
        is_whitepaper = any(c in full_text for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') and \
                        any('\u4e00' <= c <= '\u9fff' for c in full_text)

        if is_whitepaper:
            body_lines.append('')
            body_lines.append(r'\begin{quoting}')
            body_lines.append(r'\small')
            for ql in quote_buffer:
                processed = escape_latex(ql)
                processed = process_inline(processed)
                body_lines.append(processed)
                body_lines.append('')
            # Remove trailing empty line
            if body_lines and body_lines[-1] == '':
                body_lines.pop()
            body_lines.append(r'\end{quoting}')
            body_lines.append('')
        else:
            body_lines.append('')
            body_lines.append(r'\begin{quote}')
            for ql in quote_buffer:
                processed = escape_latex(ql)
                processed = process_inline(processed)
                body_lines.append(processed)
            body_lines.append(r'\end{quote}')
            body_lines.append('')
        quote_buffer = []

    while i < len(lines):
        lineno = i + 1  # 1-indexed
        line = lines[i].rstrip('\n')

        # Skip title block lines
        if lineno in SKIP_LINES or lineno in SEPARATOR_LINES:
            i += 1
            continue

        # Handle quote blocks
        if line.startswith('> ') or line == '>':
            if not in_quote:
                in_quote = True
                quote_buffer = []
            content = line[2:] if line.startswith('> ') else ''
            if content:  # skip empty > lines between EN and CN
                quote_buffer.append(content)
            i += 1
            continue
        else:
            if in_quote:
                flush_quote()

        # Handle preface
        if lineno == PREFACE_LINE:
            body_lines.append(r'\chapter*{序章：一切从双花开始}')
            body_lines.append(r'\addcontentsline{toc}{chapter}{序章：一切从双花开始}')
            body_lines.append(r'\markboth{序章：一切从双花开始}{序章：一切从双花开始}')
            i += 1
            continue

        # Handle parts
        if lineno in PARTS:
            part_name, _ = PARTS[lineno]
            body_lines.append('')
            body_lines.append(r'\part{' + escape_latex(part_name) + '}')
            body_lines.append('')
            i += 1
            continue

        # Handle sub-part headers (## lines that serve as sub-part divisions)
        if lineno in SUBPART_HEADERS:
            header_text = SUBPART_HEADERS[lineno]
            # Use a styled section-like header without numbering
            body_lines.append('')
            body_lines.append(r'\vspace{2em}')
            body_lines.append(r'\begin{center}')
            body_lines.append(r'{\Large\bfseries ' + escape_latex(header_text) + '}')
            body_lines.append(r'\end{center}')
            body_lines.append(r'\vspace{1em}')
            body_lines.append(r'\addcontentsline{toc}{section}{' + escape_latex(header_text) + '}')
            body_lines.append('')
            i += 1
            continue

        # Handle chapters
        if lineno in CHAPTERS:
            ch_title = CHAPTERS[lineno]
            # Strip "第X章：" prefix since ctexbook adds its own chapter numbering
            import re as re_mod
            stripped = re_mod.sub(r'^第.+?章[：:]\s*', '', ch_title)
            body_lines.append('')
            body_lines.append(r'\chapter{' + escape_latex(stripped) + '}')
            body_lines.append('')
            i += 1
            continue

        # Handle ## Section headers
        if line.startswith('## '):
            title = line[3:]
            body_lines.append('')
            body_lines.append(r'\section*{' + escape_latex(title) + '}')
            body_lines.append(r'\addcontentsline{toc}{section}{' + escape_latex(title) + '}')
            body_lines.append('')
            i += 1
            continue

        # Handle ### Subsection headers
        if line.startswith('### '):
            title = line[4:]
            body_lines.append('')
            body_lines.append(r'\subsection*{' + escape_latex(title) + '}')
            body_lines.append(r'\addcontentsline{toc}{subsection}{' + escape_latex(title) + '}')
            body_lines.append('')
            i += 1
            continue

        # Handle # headers that aren't parts/chapters/preface (shouldn't happen but safety)
        if line.startswith('# '):
            title = line[2:]
            body_lines.append('')
            body_lines.append(r'\chapter{' + escape_latex(title) + '}')
            body_lines.append('')
            i += 1
            continue

        # Regular text
        if line.strip() == '':
            body_lines.append('')
        else:
            processed = escape_latex(line)
            processed = process_inline(processed)
            body_lines.append(processed)

        i += 1

    # Flush any remaining quote
    if in_quote:
        flush_quote()

    # Post-process: fix special Unicode characters in section headings
    processed_lines = []
    for bl in body_lines:
        # Fix ≠ in section/subsection headings and TOC entries
        if '≠' in bl and ('\\section' in bl or '\\addcontentsline' in bl):
            if '\\addcontentsline' in bl:
                bl = bl.replace('≠', r'$\neq$')
                # Wrap for PDF bookmarks
                bl = bl.replace(r'\addcontentsline{toc}{section}{',
                               r'\addcontentsline{toc}{section}{\texorpdfstring{')
                bl = bl.rstrip('}') + r'}{Ticker ≠ 协议}}'
            else:
                bl = bl.replace('≠', r'$\neq$')
        processed_lines.append(bl)
    body_lines = processed_lines

    # Build the full LaTeX document
    preamble = r"""\documentclass[a4paper,12pt,openany]{ctexbook}

% ── Geometry ──────────────────────────────────────────────────────
\usepackage[
  a4paper,
  top=2.5cm,
  bottom=2.5cm,
  inner=3cm,
  outer=2.5cm
]{geometry}

% ── Fonts ─────────────────────────────────────────────────────────
\setCJKmainfont{STSong}
\setCJKsansfont{STHeiti}
\setCJKmonofont{STKaiti}

% ── Spacing ───────────────────────────────────────────────────────
\usepackage{setspace}
\setstretch{1.35}

% ── Quoting environment (for whitepaper quotes) ──────────────────
\newenvironment{quoting}{%
  \par\vspace{0.5em}%
  \begin{list}{}{%
    \setlength{\leftmargin}{2em}%
    \setlength{\rightmargin}{2em}%
    \setlength{\parsep}{0.3em}%
    \setlength{\itemsep}{0pt}%
    \setlength{\topsep}{0pt}%
  }%
  \item\relax
}{%
  \end{list}%
  \par\vspace{0.5em}%
}

% ── Hyperlinks & bookmarks ────────────────────────────────────────
\usepackage[
  bookmarks=true,
  bookmarksnumbered=true,
  bookmarksopen=true,
  unicode=true,
  pdfencoding=auto,
  colorlinks=true,
  linkcolor=black,
  citecolor=black,
  urlcolor=blue,
  pdfauthor={佟晓峰},
  pdftitle={正本清源比特币},
]{hyperref}

% ── Chapter/section formatting ────────────────────────────────────
\ctexset{
  part/format = \Huge\bfseries\centering,
  chapter/format = \huge\bfseries,
  section/format = \Large\bfseries,
  subsection/format = \large\bfseries,
}

% ── Misc ──────────────────────────────────────────────────────────
\usepackage{indentfirst}
\setlength{\parindent}{2em}

% Prevent overfull hboxes in CJK text
\tolerance=1000
\emergencystretch=1em

\begin{document}

% ── Title page ────────────────────────────────────────────────────
\begin{titlepage}
\centering
\vspace*{5cm}
{\Huge\bfseries 正本清源比特币\par}
\vspace{1.5cm}
{\Large\itshape Bitcoin: The Path to Satoshi's Vision\par}
\vspace{3cm}
{\Large 佟晓峰\par}
\vfill
\end{titlepage}

% ── Table of contents ─────────────────────────────────────────────
\frontmatter
\tableofcontents
\mainmatter

"""

    epilogue = r"""
\end{document}
"""

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(preamble)
        f.write('\n'.join(body_lines))
        f.write(epilogue)

    print(f"Written {OUTPUT}")
    print(f"Total body lines: {len(body_lines)}")


if __name__ == '__main__':
    convert()
