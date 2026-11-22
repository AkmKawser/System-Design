#!/usr/bin/env python3
"""
remake_canonical_diagrams.py

Systematically remakes low-quality / blurry source diagrams across all 40 chapters
of umlBook into Canonical Claude Standalone Vector SVGs:
- Strict compliance with architecture/diagram_style_guide.md
- Dark-mode adaptability (@media (prefers-color-scheme: dark))
- Accessible vector elements (<title>, <desc>, role="img")
- Animated Canonical Claude sequence diagrams with moving amber dot & dynamic captions
- XML validation on every generated SVG
- Safe chapter markdown link replacement (only links genuine Canonical Claude SVGs)
"""

import os
import re
import sys
import xml.etree.ElementTree as ET

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UML_DIR = os.path.join(
    BASE_DIR,
    "topics",
    "0.FUNDAMENTALS",
    "System Requirements",
    "UML-DIAGRAMMING",
    "Data_Ingestion",
    "Books",
    "umlBook",
)
CHAP_DIR = os.path.join(UML_DIR, "chapters")
IMAGES_DIR = os.path.join(UML_DIR, "images")
VECTOR_DIR = os.path.join(UML_DIR, "vector_images")

# ==============================================================================
# BASE CANONICAL CLAUDE STYLES
# ==============================================================================

BASE_CSS = """
text { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; fill: #2C2C2A; }
.th { font-size: 14px; font-weight: 600; text-anchor: middle; dominant-baseline: central; }
.ts { font-size: 12px; fill: #5F5E5A; text-anchor: middle; dominant-baseline: central; }
.t-left { text-anchor: start; dominant-baseline: central; }
.lbl { font-size: 11px; fill: #5F5E5A; }
.badge { font-size: 10px; font-weight: 700; fill: #FFFFFF; text-anchor: middle; dominant-baseline: central; }
.box { rx: 8px; stroke-width: 1px; }

.gray rect { fill: #F4F3EF; stroke: #888780; }
.gray .th { fill: #2C2C2A; } .gray .ts { fill: #5F5E5A; }

.purple rect { fill: #EEEDFE; stroke: #534AB7; }
.purple .th { fill: #3C3489; } .purple .ts { fill: #534AB7; }

.teal rect { fill: #E1F5EE; stroke: #0F6E56; }
.teal .th { fill: #085041; } .teal .ts { fill: #0F6E56; }

.coral rect { fill: #FAECE7; stroke: #D85A38; }
.coral .th { fill: #993C1D; } .coral .ts { fill: #D85A38; }

.blue rect { fill: #EBF3FE; stroke: #378ADD; }
.blue .th { fill: #185ABC; } .blue .ts { fill: #378ADD; }

.amber rect { fill: #FEF7E0; stroke: #B06000; }
.amber .th { fill: #7A4100; } .amber .ts { fill: #B06000; }

.flow-line { stroke: #444441; stroke-width: 1.5; fill: none; }
.flow-dashed { stroke: #5F5E5A; stroke-width: 1.5; stroke-dasharray: 4 3; fill: none; }
.lifeline { stroke: #888780; stroke-width: 1; stroke-dasharray: 4 4; fill: none; }
.frame-box { stroke: #378ADD; stroke-width: 1; stroke-dasharray: 4 4; fill: rgba(235,243,254,0.12); rx: 6px; }
.actor-line { stroke: #378ADD; stroke-width: 1.5; fill: none; stroke-linecap: round; }

@media (prefers-color-scheme: dark) {
  text { fill: #E3E1D8; }
  .ts { fill: #B4B2A9; }
  .lbl { fill: #B4B2A9; }
  .gray rect { fill: #2B2A27; stroke: #6B6963; }
  .gray .th { fill: #E3E1D8; } .gray .ts { fill: #B4B2A9; }
  
  .purple rect { fill: #26214A; stroke: #7F77DD; }
  .purple .th { fill: #CECBF6; } .purple .ts { fill: #AFA9EC; }
  
  .teal rect { fill: #053329; stroke: #3B9E7F; }
  .teal .th { fill: #9FE1CB; } .teal .ts { fill: #5DCAA5; }
  
  .coral rect { fill: #421A10; stroke: #E27B58; }
  .coral .th { fill: #F6B39E; } .coral .ts { fill: #F0997D; }
  
  .blue rect { fill: #0F2B4A; stroke: #669DF6; }
  .blue .th { fill: #AECBFA; } .blue .ts { fill: #8AB4F8; }
  
  .amber rect { fill: #3D2B03; stroke: #E3A024; }
  .amber .th { fill: #FDE293; } .amber .ts { fill: #FDD663; }
  
  .flow-line { stroke: #D3D1C7; }
  .flow-dashed { stroke: #B4B2A9; }
  .lifeline { stroke: #55544E; }
  .frame-box { stroke: #669DF6; fill: rgba(18,52,90,0.25); }
  .actor-line { stroke: #669DF6; }
}
"""

MARKERS_DEFS = """
<defs>
<marker id="arr-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M2 1L8 5L2 9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</marker>
<marker id="arr-l" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<path d="M8 1L2 5L8 9" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</marker>
<marker id="arr-solid" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
<polygon points="2,1 8,5 2,9" fill="#444441"/>
</marker>
<marker id="arr-inherit" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto">
<polygon points="2,2 10,6 2,10" fill="#FFFFFF" stroke="#444441" stroke-width="1.5"/>
</marker>
</defs>
"""

def xml_escape(s):
    if not isinstance(s, str):
        return str(s)
    # Clear existing entities to prevent double-escaping
    s = s.replace("&amp;", "&").replace("&AMP;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def make_header(w, h, title, desc, extra_css=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" role="img" aria-labelledby="title desc">
<title id="title">{xml_escape(title)}</title>
<desc id="desc">{xml_escape(desc)}</desc>
<style>
{BASE_CSS}
{extra_css}
</style>
{MARKERS_DEFS}
"""

# ==============================================================================
# 1. UP PHASE & TAXONOMY PYRAMID BUILDERS (Chapter 1)
# ==============================================================================

def generate_up_phase_svg(phase_name, input_name, activities, output_name):
    w, h = 760, 260
    title = f"Unified Process {phase_name} Phase Workflow"
    desc = f"Architectural workflow illustrating inputs, core activities, and output artifacts of the {phase_name} phase."
    out = [make_header(w, h, title, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="220"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(phase_name.upper())} PHASE ARCHITECTURE</text>')

    out.append('<g class="blue">')
    out.append('<rect class="box" x="40" y="75" width="160" height="130"/>')
    out.append('<text class="ts" x="120" y="100">INPUT ARTIFACT</text>')
    out.append(f'<text class="th" x="120" y="135">{xml_escape(input_name)}</text>')
    out.append('</g>')

    out.append('<line class="flow-line" x1="200" y1="140" x2="250" y2="140" marker-end="url(#arr-r)"/>')

    out.append('<g class="purple">')
    out.append('<rect class="box" x="260" y="60" width="240" height="160"/>')
    out.append(f'<text class="th" x="380" y="85">{xml_escape(phase_name)} Phase</text>')
    out.append('<text class="ts" x="380" y="105">Core Engineering Activities</text>')
    y_act = 130
    for idx, act in enumerate(activities, 1):
        out.append(f'<circle cx="285" cy="{y_act}" r="8" fill="#534AB7"/>')
        out.append(f'<text class="badge" x="285" y="{y_act}">{idx}</text>')
        out.append(f'<text class="lbl t-left" x="305" y="{y_act}">{xml_escape(act)}</text>')
        y_act += 25
    out.append('</g>')

    out.append('<line class="flow-line" x1="500" y1="140" x2="550" y2="140" marker-end="url(#arr-r)"/>')

    out.append('<g class="teal">')
    out.append('<rect class="box" x="560" y="75" width="160" height="130"/>')
    out.append('<text class="ts" x="640" y="100">OUTPUT ARTIFACT</text>')
    out.append(f'<text class="th" x="640" y="135">{xml_escape(output_name)}</text>')
    out.append('</g>')

    out.append('</svg>')
    return "".join(out)

def generate_pyramid_svg():
    w, h = 760, 420
    title = "Pyramid of Unified Modeling Language (UML) Diagrams"
    desc = "Tiered architectural classification of behavioral, structural, and physical implementation UML diagrams."
    out = [make_header(w, h, title, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="380"/>')
    out.append('<text class="th t-left" x="35" y="45">PYRAMID OF UML DIAGRAMS &amp; MODELING PERSPECTIVES</text>')

    out.append('<g class="amber">')
    out.append('<rect class="box" x="230" y="70" width="300" height="75"/>')
    out.append('<text class="th" x="380" y="95">Implementation &amp; Deployment Tier</text>')
    out.append('<text class="ts" x="380" y="120">Component Diagram • Deployment Diagram</text>')
    out.append('</g>')
    out.append('<line class="flow-line" x1="380" y1="145" x2="380" y2="175" marker-end="url(#arr-r)"/>')

    out.append('<g class="purple">')
    out.append('<rect class="box" x="150" y="175" width="460" height="85"/>')
    out.append('<text class="th" x="380" y="202">Structural Domain Modeling Tier</text>')
    out.append('<text class="ts" x="380" y="225">Class Diagram • Object Diagram • Package Diagram</text>')
    out.append('<text class="lbl" x="380" y="244" text-anchor="middle">Static classifiers, attributes, operations, and associations</text>')
    out.append('</g>')
    out.append('<line class="flow-line" x1="380" y1="260" x2="380" y2="290" marker-end="url(#arr-r)"/>')

    out.append('<g class="teal">')
    out.append('<rect class="box" x="60" y="290" width="640" height="95"/>')
    out.append('<text class="th" x="380" y="318">Dynamic Behavioral &amp; Interaction Tier</text>')
    out.append('<text class="ts" x="380" y="342">Use Case Diagram • Activity Diagram • State Machine Diagram</text>')
    out.append('<text class="lbl" x="380" y="362" text-anchor="middle">Sequence Diagram • Communication Diagram • Timing Diagram</text>')
    out.append('</g>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 2. DFD LEVEL 0 & 1 BUILDERS (Chapter 2)
# ==============================================================================

def generate_dfd0_svg(system_name, actors, data_in, data_out):
    w, h = 760, 340
    title = f"DFD Level 0 Context Diagram: {system_name}"
    desc = f"Level 0 context data flow diagram showing external entities and central {system_name} process."
    out = [make_header(w, h, title, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="300"/>')
    out.append(f'<text class="th t-left" x="35" y="45">LEVEL 0 DFD: CONTEXT DIAGRAM</text>')

    actor_left = xml_escape(actors[0] if actors else "Primary User")
    out.append('<g class="blue">')
    out.append('<rect class="box" x="40" y="110" width="150" height="100"/>')
    out.append('<text class="ts" x="115" y="140">EXTERNAL ENTITY</text>')
    out.append(f'<text class="th" x="115" y="170">{actor_left[:18]}</text>')
    out.append('</g>')

    out.append('<g class="purple">')
    out.append('<circle cx="380" cy="160" r="75" stroke="#534AB7" stroke-width="1.5" fill="#EEEDFE"/>')
    out.append('<text class="ts" x="380" y="130">0.0</text>')
    out.append(f'<text class="th" x="380" y="155">{xml_escape(system_name[:18])}</text>')
    out.append(f'<text class="th" x="380" y="175">{xml_escape(system_name[18:36])}</text>')
    out.append('<text class="ts" x="380" y="200">Central System</text>')
    out.append('</g>')

    actor_right = xml_escape(actors[1] if len(actors) > 1 else "Service Provider")
    out.append('<g class="teal">')
    out.append('<rect class="box" x="570" y="110" width="150" height="100"/>')
    out.append('<text class="ts" x="645" y="140">EXTERNAL ENTITY</text>')
    out.append(f'<text class="th" x="645" y="170">{actor_right[:18]}</text>')
    out.append('</g>')

    out.append('<path class="flow-line" d="M 190 140 L 305 140" marker-end="url(#arr-r)"/>')
    out.append(f'<text class="lbl" x="247" y="130" text-anchor="middle">{xml_escape(data_in[0] if data_in else "Request Data")}</text>')

    out.append('<path class="flow-dashed" d="M 305 180 L 190 180" marker-end="url(#arr-l)"/>')
    out.append(f'<text class="lbl" x="247" y="195" text-anchor="middle">{xml_escape(data_out[0] if data_out else "Response / Confirmation")}</text>')

    out.append('<path class="flow-line" d="M 570 140 L 455 140" marker-end="url(#arr-l)"/>')
    out.append(f'<text class="lbl" x="512" y="130" text-anchor="middle">{xml_escape(data_in[1] if len(data_in) > 1 else "Service Records")}</text>')

    out.append('<path class="flow-dashed" d="M 455 180 L 570 180" marker-end="url(#arr-r)"/>')
    out.append(f'<text class="lbl" x="512" y="195" text-anchor="middle">{xml_escape(data_out[1] if len(data_out) > 1 else "Fulfillment / Reports")}</text>')

    out.append('</svg>')
    return "".join(out)

def generate_dfd1_svg(system_name, processes, stores):
    w, h = 760, 480
    title = f"DFD Level 1 Decomposition: {system_name}"
    desc = f"Level 1 data flow diagram decomposing {system_name} into sub-processes and persistent datastores."
    out = [make_header(w, h, title, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="440"/>')
    out.append(f'<text class="th t-left" x="35" y="45">LEVEL 1 DFD: SUB-PROCESS ARCHITECTURE ({xml_escape(system_name.upper())})</text>')

    col_x = [70, 410]
    row_y = [80, 180, 280]
    for idx, (p_num, p_name) in enumerate(processes[:6]):
        cx = col_x[idx % 2]
        cy = row_y[idx // 2]
        out.append('<g class="purple">')
        out.append(f'<rect class="box" x="{cx}" y="{cy}" width="280" height="70"/>')
        out.append(f'<circle cx="{cx + 25}" cy="{cy + 35}" r="14" fill="#534AB7"/>')
        out.append(f'<text class="badge" x="{cx + 25}" y="{cy + 35}">{p_num}</text>')
        out.append(f'<text class="th t-left" x="{cx + 50}" y="{cy + 28}">{xml_escape(p_name[:24])}</text>')
        out.append(f'<text class="ts t-left" x="{cx + 50}" y="{cy + 48}">Process {p_num}</text>')
        out.append('</g>')

    ds_x = [70, 235, 400, 565]
    for idx, (ds_id, ds_name) in enumerate(stores[:4]):
        dx = ds_x[idx]
        out.append('<g class="gray">')
        out.append(f'<rect class="box" x="{dx}" y="380" width="125" height="55"/>')
        out.append(f'<text class="th" x="{dx + 62}" y="400">{xml_escape(ds_id)}</text>')
        out.append(f'<text class="lbl" x="{dx + 62}" y="420" text-anchor="middle">{xml_escape(ds_name[:14])}</text>')
        out.append('</g>')

    out.append('<line class="flow-dashed" x1="130" y1="350" x2="130" y2="380" marker-end="url(#arr-r)"/>')
    out.append('<line class="flow-dashed" x1="300" y1="350" x2="300" y2="380" marker-end="url(#arr-r)"/>')
    out.append('<line class="flow-dashed" x1="460" y1="350" x2="460" y2="380" marker-end="url(#arr-r)"/>')
    out.append('<line class="flow-dashed" x1="620" y1="350" x2="620" y2="380" marker-end="url(#arr-r)"/>')
    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 3. ANIMATED CANONICAL CLAUDE SEQUENCE DIAGRAM BUILDER
# ==============================================================================

def generate_animated_sequence_svg(system_name, title_text, participants, messages, captions, duration=15):
    n_part = len(participants)
    w = max(680, 160 + 140 * (n_part - 1) + 160)
    msg_start_y = 120
    msg_step_y = 45
    h = msg_start_y + len(messages) * msg_step_y + 90

    m_count = len(messages)
    step_pct = 85.0 / max(1, m_count)
    
    extra_css = ["""
.msg, .dot-amber, .cap { opacity: 0; }
.cap.static { opacity: 1; }
.dot-amber { fill: #EF9F27; stroke: #854F0B; stroke-width: 1.5; }
.step-badge { fill: #378ADD; stroke: #185ABC; stroke-width: 1; }
.badge-txt { font-size: 11px; font-weight: 600; fill: #FFFFFF; text-anchor: middle; dominant-baseline: central; }

@media (prefers-color-scheme: dark) {
  .dot-amber { stroke: #FAC775; }
  .step-badge { fill: #1A73E8; stroke: #8AB4F8; }
}

@media (prefers-reduced-motion: no-preference) {
  .cap.static { display: none; }
  .dot-amber { animation: dotSequence """ + f"{duration}s" + """ linear infinite; }
"""]

    for i in range(1, m_count + 1):
        extra_css.append(f"  .m{i} {{ animation: msgFade{i} {duration}s linear infinite; }}")
        extra_css.append(f"  .c{i} {{ animation: capFade{i} {duration}s linear infinite; }}")

    extra_css.append("\n  @keyframes dotSequence {")
    extra_css.append("    0% { opacity: 0; transform: translate(160px, 120px); }")
    extra_css.append("    2% { opacity: 1; transform: translate(160px, 120px); }")
    for idx, (src_idx, tgt_idx, _, _) in enumerate(messages):
        p_start = 2 + idx * step_pct
        p_end = 2 + (idx + 1) * step_pct - 2
        p_next = 2 + (idx + 1) * step_pct
        x_src = 160 + 140 * src_idx
        x_tgt = 160 + 140 * tgt_idx
        y_cur = msg_start_y + idx * msg_step_y
        y_next = msg_start_y + (idx + 1) * msg_step_y if idx + 1 < m_count else y_cur
        extra_css.append(f"    {p_start:.1f}% {{ transform: translate({x_src}px, {y_cur}px); opacity: 1; }}")
        extra_css.append(f"    {p_end:.1f}% {{ transform: translate({x_tgt}px, {y_cur}px); opacity: 1; }}")
        extra_css.append(f"    {p_next:.1f}% {{ transform: translate({x_tgt}px, {y_next}px); opacity: 1; }}")
    extra_css.append("    88% { opacity: 0; }")
    extra_css.append("    100% { opacity: 0; }")
    extra_css.append("  }")

    for idx in range(m_count):
        m_num = idx + 1
        p_arr = 2 + (idx + 0.3) * step_pct
        extra_css.append(f"\n  @keyframes msgFade{m_num} {{")
        extra_css.append(f"    0%, {p_arr - 1:.1f}% {{ opacity: 0.15; }}")
        extra_css.append(f"    {p_arr:.1f}%, 88% {{ opacity: 1; }}")
        extra_css.append(f"    92%, 100% {{ opacity: 0.15; }}")
        extra_css.append("  }")

    for idx in range(m_count):
        c_num = idx + 1
        p_show = 2 + idx * step_pct
        p_hide = 2 + (idx + 1) * step_pct
        extra_css.append(f"\n  @keyframes capFade{c_num} {{")
        extra_css.append(f"    0%, {p_show - 1:.1f}% {{ opacity: 0; }}")
        extra_css.append(f"    {p_show:.1f}%, {p_hide - 1:.1f}% {{ opacity: 1; }}")
        extra_css.append(f"    {p_hide:.1f}%, 100% {{ opacity: 0; }}")
        extra_css.append("  }")

    extra_css.append("}")

    desc = f"Canonical Claude animated sequence diagram for {system_name} showing dynamic message passing."
    out = [make_header(w, h, title_text, desc, "\n".join(extra_css))]
    out.append(f'<rect class="frame-box" x="20" y="20" width="{w - 40}" height="{h - 40}"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    colors = ["blue", "purple", "teal", "coral", "amber", "gray"]
    for i, p in enumerate(participants):
        cx = 160 + 140 * i
        bx = cx - 60
        palette = colors[i % len(colors)]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{bx}" y="65" width="120" height="36"/>')
        out.append(f'<text class="th" x="{cx}" y="83">{xml_escape(p)}</text>')
        out.append('</g>')
        out.append(f'<line class="lifeline" x1="{cx}" y1="101" x2="{cx}" y2="{h - 70}"/>')

    for idx, (src_idx, tgt_idx, label, is_response) in enumerate(messages):
        m_num = idx + 1
        x1 = 160 + 140 * src_idx
        x2 = 160 + 140 * tgt_idx
        y = msg_start_y + idx * msg_step_y
        m_class = "arr-res" if is_response else "flow-line"
        m_marker = "url(#arr-l)" if is_response and x1 > x2 else "url(#arr-r)"
        if is_response and x1 < x2:
            m_marker = "url(#arr-r)"

        out.append(f'<g class="msg m{m_num}">')
        bx = min(x1, x2) + 20
        out.append(f'<circle class="step-badge" cx="{bx}" cy="{y - 8}" r="9"/>')
        out.append(f'<text class="badge-txt" x="{bx}" y="{y - 8}">{m_num}</text>')
        lx = (x1 + x2) / 2
        out.append(f'<text class="ts" x="{lx}" y="{y - 8}">{xml_escape(label)}</text>')
        x2_arrow = x2 - 5 if x2 > x1 else x2 + 5
        dash = ' stroke-dasharray="4 3"' if is_response else ''
        out.append(f'<line class="{m_class}" x1="{x1}" y1="{y}" x2="{x2_arrow}" y2="{y}"{dash} marker-end="{m_marker}"/>')
        out.append('</g>')

    out.append('<circle class="dot-amber" cx="0" cy="0" r="5"/>')

    cap_y = h - 45
    static_cap = captions[0] if captions else f"Execution flow across {len(participants)} service components."
    out.append(f'<text class="ts cap static" x="{w / 2}" y="{cap_y}">{xml_escape(static_cap)}</text>')
    for idx, cap in enumerate(captions):
        c_num = idx + 1
        out.append(f'<text class="th cap c{c_num}" x="{w / 2}" y="{cap_y}">{xml_escape(cap)}</text>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 4. ACTIVITY DIAGRAM BUILDER
# ==============================================================================

def generate_activity_svg(system_name, title_text, steps):
    w, h = 680, 520
    desc = f"Activity diagram detailing procedural workflow, decision branching, and terminal states for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="640" height="480"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    out.append('<circle cx="340" cy="75" r="10" fill="#2C2C2A"/>')
    out.append('<line class="flow-line" x1="340" y1="85" x2="340" y2="115" marker-end="url(#arr-r)"/>')

    cur_y = 115
    for idx, s in enumerate(steps[:4]):
        out.append('<g class="teal">')
        out.append(f'<rect class="box" x="200" y="{cur_y}" width="280" height="45" rx="22"/>')
        out.append(f'<text class="th" x="340" y="{cur_y + 23}">{xml_escape(s[:32])}</text>')
        out.append('</g>')

        if idx == 1:
            cur_y += 45
            out.append(f'<line class="flow-line" x1="340" y1="{cur_y}" x2="340" y2="{cur_y + 25}" marker-end="url(#arr-r)"/>')
            cur_y += 25
            out.append('<g class="amber">')
            out.append(f'<polygon points="340,{cur_y} 390,{cur_y + 25} 340,{cur_y + 50} 290,{cur_y + 25}" stroke="#B06000" stroke-width="1.5" fill="#FEF7E0"/>')
            out.append(f'<text class="badge" x="340" y="{cur_y + 25}" fill="#7A4100">Valid?</text>')
            out.append('</g>')
            out.append(f'<line class="flow-line" x1="340" y1="{cur_y + 50}" x2="340" y2="{cur_y + 80}" marker-end="url(#arr-r)"/>')
            out.append(f'<text class="lbl" x="355" y="{cur_y + 65}">[Yes]</text>')
            out.append(f'<path class="flow-line" d="M 290 {cur_y + 25} L 160 {cur_y + 25} L 160 137 L 200 137" marker-end="url(#arr-r)"/>')
            out.append(f'<text class="lbl" x="170" y="{cur_y + 15}">[Retry / Error]</text>')
            cur_y += 80
        else:
            if idx < 3:
                out.append(f'<line class="flow-line" x1="340" y1="{cur_y + 45}" x2="340" y2="{cur_y + 75}" marker-end="url(#arr-r)"/>')
                cur_y += 75

    cur_y += 55
    out.append(f'<line class="flow-line" x1="340" y1="{cur_y - 10}" x2="340" y2="{cur_y + 15}" marker-end="url(#arr-r)"/>')
    cur_y += 25
    out.append(f'<circle cx="340" cy="{cur_y}" r="12" fill="none" stroke="#2C2C2A" stroke-width="1.5"/>')
    out.append(f'<circle cx="340" cy="{cur_y}" r="7" fill="#2C2C2A"/>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 5. COLLABORATION / COMMUNICATION DIAGRAM BUILDER
# ==============================================================================

def generate_collaboration_svg(system_name, title_text, objects, interactions):
    w, h = 760, 480
    desc = f"Communication diagram detailing structural links and numbered invocation messages for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="440"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    positions = [
        (80, 100, "blue"),
        (480, 100, "purple"),
        (80, 320, "teal"),
        (480, 320, "amber"),
    ]

    for idx, obj in enumerate(objects[:4]):
        x, y, palette = positions[idx]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{x}" y="{y}" width="200" height="60"/>')
        out.append(f'<text class="th" x="{x + 100}" y="{y + 24}">:{xml_escape(obj[:18])}</text>')
        out.append(f'<line x1="{x + 20}" y1="{y + 36}" x2="{x + 180}" y2="{y + 36}" stroke="currentColor" stroke-width="1"/>')
        out.append(f'<text class="ts" x="{x + 100}" y="{y + 48}">Object Instance</text>')
        out.append('</g>')

    out.append('<line class="flow-line" x1="280" y1="130" x2="480" y2="130"/>')
    out.append('<line class="flow-line" x1="180" y1="160" x2="180" y2="320"/>')
    out.append('<line class="flow-line" x1="580" y1="160" x2="580" y2="320"/>')
    out.append('<line class="flow-line" x1="280" y1="350" x2="480" y2="350"/>')

    for idx, (link_loc, num_label, is_forward) in enumerate(interactions[:4]):
        label_str = xml_escape(num_label)
        if link_loc == "top":
            arrow = "→" if is_forward else "←"
            out.append(f'<text class="th" x="380" y="115">{label_str} {arrow}</text>')
        elif link_loc == "left":
            arrow = "↓" if is_forward else "↑"
            out.append(f'<text class="th" x="120" y="240">{label_str} {arrow}</text>')
        elif link_loc == "right":
            arrow = "↓" if is_forward else "↑"
            out.append(f'<text class="th" x="610" y="240">{label_str} {arrow}</text>')
        elif link_loc == "bottom":
            arrow = "→" if is_forward else "←"
            out.append(f'<text class="th" x="380" y="375">{label_str} {arrow}</text>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 6. STATE MACHINE / STATECHART DIAGRAM BUILDER
# ==============================================================================

def generate_statemachine_svg(system_name, title_text, states, transitions):
    w, h = 760, 480
    desc = f"State machine diagram illustrating discrete lifecycle states, transition triggers, and actions for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="440"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    out.append('<circle cx="60" cy="140" r="10" fill="#2C2C2A"/>')
    out.append('<line class="flow-line" x1="70" y1="140" x2="120" y2="140" marker-end="url(#arr-r)"/>')

    coords = [
        (120, 100, "blue"),
        (380, 100, "purple"),
        (380, 280, "teal"),
        (120, 280, "amber"),
    ]

    for idx, (s_name, s_actions) in enumerate(states[:4]):
        x, y, palette = coords[idx]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{x}" y="{y}" width="200" height="80"/>')
        out.append(f'<text class="th" x="{x + 100}" y="{y + 22}">{xml_escape(s_name)}</text>')
        out.append(f'<line x1="{x}" y1="{y + 36}" x2="{x + 200}" y2="{y + 36}" stroke="currentColor" stroke-width="1"/>')
        ay = y + 52
        for act in s_actions[:2]:
            out.append(f'<text class="lbl t-left" x="{x + 10}" y="{ay}">• {xml_escape(act)}</text>')
            ay += 16
        out.append('</g>')

    out.append('<line class="flow-line" x1="320" y1="130" x2="380" y2="130" marker-end="url(#arr-r)"/>')
    out.append(f'<text class="lbl" x="350" y="120" text-anchor="middle">{xml_escape(transitions[0] if transitions else "submit")}</text>')

    out.append('<line class="flow-line" x1="480" y1="180" x2="480" y2="280" marker-end="url(#arr-r)"/>')
    out.append(f'<text class="lbl" x="500" y="230" text-anchor="start">{xml_escape(transitions[1] if len(transitions) > 1 else "process")}</text>')

    out.append('<line class="flow-line" x1="380" y1="320" x2="320" y2="320" marker-end="url(#arr-r)"/>')
    out.append(f'<text class="lbl" x="350" y="340" text-anchor="middle">{xml_escape(transitions[2] if len(transitions) > 2 else "complete")}</text>')

    out.append('<line class="flow-line" x1="120" y1="320" x2="60" y2="320" marker-end="url(#arr-r)"/>')
    out.append('<circle cx="45" cy="320" r="12" fill="none" stroke="#2C2C2A" stroke-width="1.5"/>')
    out.append('<circle cx="45" cy="320" r="7" fill="#2C2C2A"/>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 7. COMPONENT DIAGRAM BUILDER
# ==============================================================================

def generate_component_svg(system_name, title_text, components, interfaces):
    w, h = 760, 460
    desc = f"Component diagram showing modular software architecture, ball-and-socket interfaces, and subsystem coupling for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="420"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    coords = [
        (60, 80, "blue"),
        (460, 80, "purple"),
        (60, 260, "teal"),
        (460, 260, "amber"),
    ]

    for idx, comp in enumerate(components[:4]):
        x, y, palette = coords[idx]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{x}" y="{y}" width="220" height="110"/>')
        out.append(f'<rect x="{x + 185}" y="{y + 10}" width="20" height="15" fill="none" stroke="currentColor" stroke-width="1"/>')
        out.append(f'<rect x="{x + 180}" y="{y + 12}" width="8" height="4" fill="currentColor"/>')
        out.append(f'<rect x="{x + 180}" y="{y + 18}" width="8" height="4" fill="currentColor"/>')
        out.append(f'<text class="ts" x="{x + 100}" y="{y + 35}">&lt;&lt;component&gt;&gt;</text>')
        out.append(f'<text class="th" x="{x + 100}" y="{y + 65}">{xml_escape(comp)}</text>')
        out.append('</g>')

    out.append('<line class="flow-line" x1="280" y1="135" x2="360" y2="135"/>')
    out.append('<circle cx="360" cy="135" r="7" fill="none" stroke="#444441" stroke-width="1.5"/>')
    out.append('<path d="M 370 125 A 10 10 0 0 1 370 145" fill="none" stroke="#444441" stroke-width="1.5"/>')
    out.append('<line class="flow-line" x1="370" y1="135" x2="460" y2="135"/>')
    out.append(f'<text class="lbl" x="365" y="115" text-anchor="middle">{xml_escape(interfaces[0] if interfaces else "IOrderAPI")}</text>')

    out.append('<line class="flow-line" x1="280" y1="315" x2="360" y2="315"/>')
    out.append('<circle cx="360" cy="315" r="7" fill="none" stroke="#444441" stroke-width="1.5"/>')
    out.append('<path d="M 370 305 A 10 10 0 0 1 370 325" fill="none" stroke="#444441" stroke-width="1.5"/>')
    out.append('<line class="flow-line" x1="370" y1="315" x2="460" y2="315"/>')
    out.append(f'<text class="lbl" x="365" y="295" text-anchor="middle">{xml_escape(interfaces[1] if len(interfaces) > 1 else "IDataAccess")}</text>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 8. DEPLOYMENT DIAGRAM BUILDER
# ==============================================================================

def generate_deployment_svg(system_name, title_text, nodes, artifacts):
    w, h = 760, 460
    desc = f"Deployment diagram displaying physical hardware execution nodes, runtime artifacts, and network protocols for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="420"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    node_coords = [
        (40, 90, "blue"),
        (280, 90, "purple"),
        (520, 90, "teal"),
    ]

    for idx, (n_type, n_name) in enumerate(nodes[:3]):
        x, y, palette = node_coords[idx]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{x}" y="{y}" width="200" height="260"/>')
        out.append(f'<text class="ts" x="{x + 100}" y="{y + 25}">&lt;&lt;{xml_escape(n_type)}&gt;&gt;</text>')
        out.append(f'<text class="th" x="{x + 100}" y="{y + 48}">{xml_escape(n_name)}</text>')
        out.append(f'<line x1="{x}" y1="{y + 65}" x2="{x + 200}" y2="{y + 65}" stroke="currentColor" stroke-width="1"/>')
        
        art_y = y + 85
        node_arts = artifacts[idx] if idx < len(artifacts) else ["application.war"]
        for art in node_arts:
            out.append('<g class="gray">')
            out.append(f'<rect class="box" x="{x + 15}" y="{art_y}" width="170" height="50"/>')
            out.append(f'<text class="ts" x="{x + 100}" y="{art_y + 18}">&lt;&lt;artifact&gt;&gt;</text>')
            out.append(f'<text class="th" x="{x + 100}" y="{art_y + 36}">{xml_escape(art)}</text>')
            out.append('</g>')
            art_y += 65
        out.append('</g>')

    out.append('<line class="flow-line" x1="240" y1="200" x2="280" y2="200"/>')
    out.append('<text class="lbl" x="260" y="190" text-anchor="middle">&lt;&lt;HTTPS&gt;&gt;</text>')

    out.append('<line class="flow-line" x1="480" y1="200" x2="520" y2="200"/>')
    out.append('<text class="lbl" x="500" y="190" text-anchor="middle">&lt;&lt;TCP/JDBC&gt;&gt;</text>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 9. CLASS DIAGRAM BUILDER
# ==============================================================================

def generate_class_svg(system_name, title_text, classes):
    w, h = 760, 460
    desc = f"Class model showing static domain entities, attributes, operations, and relationships for {system_name}."
    out = [make_header(w, h, title_text, desc)]
    out.append('<rect class="frame-box" x="20" y="20" width="720" height="420"/>')
    out.append(f'<text class="th t-left" x="35" y="45">{xml_escape(title_text.upper())}</text>')

    coords = [
        (40, 75, "blue"),
        (280, 75, "purple"),
        (520, 75, "teal"),
        (160, 260, "coral"),
        (400, 260, "amber"),
    ]

    for idx, (cls_name, attrs, methods) in enumerate(classes[:5]):
        x, y, palette = coords[idx]
        out.append(f'<g class="{palette}">')
        out.append(f'<rect class="box" x="{x}" y="{y}" width="200" height="150"/>')
        out.append(f'<rect x="{x}" y="{y}" width="200" height="32" rx="8" style="stroke:none;"/>')
        out.append(f'<text class="th" x="{x + 100}" y="{y + 16}">{xml_escape(cls_name)}</text>')
        out.append(f'<line x1="{x}" y1="{y + 32}" x2="{x + 200}" y2="{y + 32}" stroke="currentColor" stroke-width="1"/>')
        ay = y + 48
        for attr in attrs[:3]:
            out.append(f'<text class="lbl t-left" x="{x + 10}" y="{ay}">- {xml_escape(attr)}</text>')
            ay += 18
        out.append(f'<line x1="{x}" y1="{ay}" x2="{x + 200}" y2="{ay}" stroke="currentColor" stroke-width="0.75"/>')
        my = ay + 16
        for m in methods[:2]:
            out.append(f'<text class="lbl t-left" x="{x + 10}" y="{my}">+ {xml_escape(m)}()</text>')
            my += 18
        out.append('</g>')

    out.append('<line class="flow-line" x1="240" y1="150" x2="280" y2="150"/>')
    out.append('<line class="flow-line" x1="480" y1="150" x2="520" y2="150"/>')
    out.append('<line class="flow-line" x1="260" y1="225" x2="260" y2="260"/>')
    out.append('<line class="flow-line" x1="500" y1="225" x2="500" y2="260"/>')

    out.append('</svg>')
    return "".join(out)

# ==============================================================================
# 10. UI SCHEMATIC / INTERFACE WIREFRAME BUILDER
# ==============================================================================

def generate_ui_mockup_svg(system_name, title_text, screen_name, fields, action_button):
    w, h = 680, 460
    desc = f"User interface schematic and screen layout wireframe for {screen_name} in {system_name}."
    out = [make_header(w, h, title_text, desc)]

    out.append('<g class="gray">')
    out.append('<rect class="box" x="20" y="20" width="640" height="420" rx="8"/>')
    out.append('<rect x="20" y="20" width="640" height="35" rx="8" style="stroke:none;"/>')
    out.append('<line x1="20" y1="55" x2="660" y2="55" stroke="currentColor" stroke-width="1"/>')
    out.append('<circle cx="40" cy="37" r="5" fill="#E27B58"/>')
    out.append('<circle cx="56" cy="37" r="5" fill="#E3A024"/>')
    out.append('<circle cx="72" cy="37" r="5" fill="#3B9E7F"/>')
    url_clean = system_name.lower().replace(" ", "").replace("&", "").replace("-", "")
    screen_clean = screen_name.lower().replace(" ", "_").replace("&", "")
    out.append('<rect x="100" y="27" width="400" height="20" rx="4" fill="#FFFFFF" stroke="#888780" stroke-width="0.5"/>')
    out.append(f'<text class="lbl t-left" x="110" y="37">https://{url_clean}.org/app/{screen_clean}</text>')
    out.append('</g>')

    out.append('<g class="blue">')
    out.append('<rect class="box" x="50" y="75" width="580" height="340"/>')
    out.append(f'<text class="th t-left" x="80" y="105">{xml_escape(screen_name.upper())}</text>')
    out.append(f'<text class="ts t-left" x="80" y="125">{xml_escape(system_name)} • Operational Control Panel</text>')
    out.append('</g>')

    fy = 155
    for lbl, val in fields:
        out.append(f'<text class="th t-left" x="80" y="{fy}">{xml_escape(lbl)}</text>')
        out.append('<g class="gray">')
        out.append(f'<rect class="box" x="240" y="{fy - 14}" width="350" height="28"/>')
        out.append(f'<text class="ts t-left" x="255" y="{fy}">{xml_escape(val)}</text>')
        out.append('</g>')
        fy += 45

    out.append('<g class="teal">')
    out.append(f'<rect class="box" x="240" y="{fy + 10}" width="160" height="36"/>')
    out.append(f'<text class="th" x="320" y="{fy + 28}">{xml_escape(action_button)}</text>')
    out.append('</g>')

    out.append('<g class="coral">')
    out.append(f'<rect class="box" x="420" y="{fy + 10}" width="120" height="36"/>')
    out.append(f'<text class="th" x="480" y="{fy + 28}">Cancel / Reset</text>')
    out.append('</g>')

    out.append('</svg>')
    return "".join(out)


# ==============================================================================
# 11. MASTER REGISTRY OF ALL 75 CANONICAL FIGURES
# ==============================================================================

def build_all_canonical_diagrams():
    diagrams = {}

    # --- Chapter 1: Foundations ---
    c1 = "Chapter_01_Introduction_to_UML_Diagrams_and_Its_Com"
    diagrams[(c1, "Figure_1_1_Inception_phase.svg")] = generate_up_phase_svg(
        "Inception", "Problem Statement",
        ["Feasibility Analysis", "Scope Formulation", "7 Core Inception Questions"],
        "Feasibility Report"
    )
    diagrams[(c1, "Figure_1_2_Elaboration_phase.svg")] = generate_up_phase_svg(
        "Elaboration", "Feasibility Report",
        ["Core Architecture Baseline", "Project Schedule Formulation", "UML Use Case Modeling"],
        "Architectural Baseline"
    )
    diagrams[(c1, "Figure_1_3_Construction_phase.svg")] = generate_up_phase_svg(
        "Construction", "Architecture Baseline",
        ["Iterative Code Development", "Alpha Testing at Developer Site", "Developer Feedback Refinement"],
        "Verified Alpha Build"
    )
    diagrams[(c1, "Figure_1_4_Transition_phase.svg")] = generate_up_phase_svg(
        "Transition", "Alpha Software Build",
        ["Beta Testing at Client Site", "Production System Deployment", "Customer Feedback Fine-Tuning"],
        "Production Release"
    )
    diagrams[(c1, "Figure_1_5_Pyramid_of_UML_diagrams.svg")] = generate_pyramid_svg()

    # --- Chapter 2: Webmed Healthcare ---
    c2 = "Chapter_02_Design_of_UML_Diagrams_for_Webmed_Health"
    diagrams[(c2, "Figure_2_2_Level_0_DFD.svg")] = generate_dfd0_svg(
        "Webmed Healthcare Service System",
        ["Patient / Caregiver", "Service Provider (Doctor/Admin)"],
        ["Consultation Request", "Doctor Schedule & Services"],
        ["Diagnosis / Order Confirmation", "Patient Bookings & Reviews"]
    )
    diagrams[(c2, "Figure_2_3_Level_1_DFD.svg")] = generate_dfd1_svg(
        "Webmed Healthcare",
        [("1.0", "Patient Registration & Auth"), ("2.0", "Health A-Z Disease Lookup"),
         ("3.0", "Doctor Consultation Scheduling"), ("4.0", "Online Pharmacy & Medicine"),
         ("5.0", "Finance & Insurance Verification"), ("6.0", "Billing Settlement & Payment")],
        [("D1", "User Accounts"), ("D2", "Doctor Directory"), ("D3", "Disease DB"), ("D4", "Pharmacy Stock")]
    )
    diagrams[(c2, "Figure_2_6_UML_activity_diagram_1.svg")] = generate_activity_svg(
        "Webmed Healthcare", "Webmed Doctor Consultation & Medicine Ordering",
        ["Select Medical Symptom", "Verify Doctor Availability", "Authorize Payment / Insurance", "Confirm Appointment / Medicine Dispatch"]
    )

    # --- Chapter 3: Inventory Management System ---
    c3 = "Chapter_03_Design_of_UML_Diagrams_for_Inventory_Man"
    diagrams[(c3, "Figure_3_3_Change_password.svg")] = generate_ui_mockup_svg(
        "Inventory Management System", "Change Password Interface", "Change Password",
        [("Current Password", "••••••••••••"), ("New Password", "••••••••••••"), ("Confirm Password", "••••••••••••")],
        "Update Password"
    )
    diagrams[(c3, "Figure_3_10_Expired_goods.svg")] = generate_ui_mockup_svg(
        "Inventory Management System", "Expired Goods Inspection Dashboard", "Expired Goods Record",
        [("Batch Identifier", "BATCH-2026-09A"), ("Item Name & SKU", "Antibacterial Solution (SKU-882)"), ("Expiry Date", "2026-10-31 [Expired]"), ("Action Required", "Quarantine & Disposal")],
        "Quarantine Stock"
    )
    diagrams[(c3, "Figure_3_20_Case_1.svg")] = generate_ui_mockup_svg(
        "Inventory Management System", "Inventory Stock Inward Verification", "Add Inward Goods",
        [("Vendor Consignment", "VEND-NORTH-902"), ("Received Quantity", "500 Units"), ("Warehouse Bin", "Aisle 4 - Rack B2")],
        "Confirm Stock Inward"
    )
    diagrams[(c3, "Figure_3_22_Case_3.svg")] = generate_ui_mockup_svg(
        "Inventory Management System", "Stock Outward Dispatch Authorization", "Remove Outward Goods",
        [("Sales Order ID", "ORD-INV-2026-441"), ("Dispatched Units", "120 Units"), ("Logistics Courier", "Express Freight #88")],
        "Authorize Dispatch"
    )

    # --- Chapter 4: Business Process Outsourcing (BPO) ---
    c4 = "Chapter_04_Design_of_UML_Diagrams_for_Business_Proc"
    diagrams[(c4, "Figure_4_1_Login_page.svg")] = generate_ui_mockup_svg(
        "BPO Management System", "Secure BPO Portal Authentication", "BPO Login",
        [("User Email / ID", "corporate_client@bpo-enterprise.com"), ("Access Security Key", "••••••••••••"), ("Role Authorization", "Client Partner / Vendor Admin")],
        "Sign In to BPO"
    )
    diagrams[(c4, "Figure_4_2_Client_profile_Upload_request.svg")] = generate_ui_mockup_svg(
        "BPO Management System", "Client Project Request & SLA Upload", "Upload Project Request",
        [("Project Workstream", "Customer Support & Tech Operations"), ("Headcount Scope", "45 FTE Dedicated Agents"), ("SLA Requirement", "99.8% Resolution within 2 hrs")],
        "Submit Request"
    )
    diagrams[(c4, "Figure_4_3_Client_profile_Current_deals.svg")] = generate_ui_mockup_svg(
        "BPO Management System", "Client Contract & Active Deals Dashboard", "Active Client Deals",
        [("Contract ID", "BPO-DEAL-2026-881"), ("Delivery Partner", "Apex Global Solutions"), ("Monthly Spend", "$42,500.00 / mo"), ("Milestone Status", "Phase 2 Deployment Active")],
        "Review Contract"
    )
    diagrams[(c4, "Figure_4_4_Client_profile_Search_BPO_Organization.svg")] = generate_ui_mockup_svg(
        "BPO Management System", "Vendor Discovery & BPO Provider Search", "Search BPO Provider",
        [("Service Domain", "Back-Office Data Engineering & AI Tagging"), ("Geo-Location", "Regional Operations Hub"), ("Minimum Quality Rating", "4.8 / 5.0 (ISO 9001 Certified)")],
        "Search Vendors"
    )
    diagrams[(c4, "Figure_4_7_UML_activity_diagram_part_1.svg")] = generate_activity_svg(
        "BPO Management System", "BPO Client Registration & Verification Workflow",
        ["Submit Client Profile", "Perform Compliance Due Diligence", "Grant SLA Access & Sign Agreement", "Initialize Dedicated Account Dashboard"]
    )
    diagrams[(c4, "Figure_4_8_UML_activity_diagram_part_2.svg")] = generate_activity_svg(
        "BPO Management System", "BPO Project Sourcing & Tender Allocation",
        ["Broadcast Project RFP", "Receive Vendor Proposals", "Score Technical & Cost Feasibility", "Award BPO Engagement Contract"]
    )
    diagrams[(c4, "Figure_4_9_UML_activity_diagram_part_3.svg")] = generate_activity_svg(
        "BPO Management System", "BPO Milestone Tracking & Deliverable Approval",
        ["Submit Weekly Deliverables", "Audit Quality & Performance Metrics", "Release Escrow Payment", "Archive Milestone Completion Audit"]
    )
    diagrams[(c4, "Figure_4_11_UML_activity_diagram_part_5.svg")] = generate_activity_svg(
        "BPO Management System", "BPO Dispute Resolution & SLA Escrow Settlement",
        ["Log SLA Variance Incident", "Review Audit Telemetry Logs", "Execute Remediation Settlement", "Issue Penalty Credit or Full Release"]
    )
    diagrams[(c4, "Figure_4_12_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "BPO Management System", "BPO Deal Negotiation Communication Diagram",
        ["ClientPartner", "BPOBrokerService", "VendorDatabase", "ContractEscrow"],
        [("top", "1.0: RequestBPOQuote()", True), ("right", "2.0: MatchVendors()", True),
         ("bottom", "3.0: BindEscrowTerms()", False), ("left", "4.0: ConfirmDeal()", False)]
    )
    diagrams[(c4, "Figure_4_15_UML_state_machine_diagram_part_2.svg")] = generate_statemachine_svg(
        "BPO Management System", "BPO Contract Lifecycle State Machine",
        [("Draft", ["entry / initTerms", "do / formatSLA"]),
         ("UnderReview", ["entry / auditCompliance", "do / scoreRisk"]),
         ("ActiveExecution", ["entry / allocateFTE", "do / monitorSLA"]),
         ("SettledClosed", ["entry / auditFinals", "exit / archiveRecords"])],
        ["submitForAudit()", "approveSLA()", "finalizeTerms()"]
    )
    diagrams[(c4, "Figure_4_19_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "BPO Management System", "BPO Enterprise Deployment Topology",
        [("device", "Client Enterprise Browser"), ("execution environment", "BPO App Server (JBoss/EAP)"), ("device", "PostgreSQL Primary Node")],
        [["client_portal.js"], ["bpo_core.war", "contract_service.jar"], ["bpo_relational.db", "audit_log.db"]]
    )

    # --- Chapter 5: E-Ticketing for Buses ---
    c5 = "Chapter_05_Design_of_UML_Diagrams_for_E_Ticketing_f"
    diagrams[(c5, "Figure_5_9_UML_collaboration_diagram_part_2.svg")] = generate_collaboration_svg(
        "E-Ticketing for Buses", "Bus Ticket Cancellation & Refund Collaboration",
        ["Passenger", "BookingController", "SeatInventoryDB", "PaymentRefundGateway"],
        [("top", "1.0: CancelSeatRequest()", True), ("right", "2.0: ReleaseSeatLock()", True),
         ("bottom", "3.0: CalculatePenalty()", False), ("left", "4.0: DisburseRefund()", False)]
    )

    # --- Chapter 7: E-Province ---
    c7 = "Chapter_07_Design_of_UML_Diagrams_for_E_Province"
    diagrams[(c7, "Figure_7_7_UML_component_diagram.svg")] = generate_component_svg(
        "E-Province", "E-Province Provincial Citizen Service Components",
        ["CitizenPortalWeb", "CivicRegistryService", "RevenueTaxManager", "ProvincialStorageDB"],
        ["ICitizenService", "ITaxIntegration"]
    )
    diagrams[(c7, "Figure_7_8_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "E-Province", "E-Province Multi-Tier Physical Architecture",
        [("device", "Citizen Kiosk / Mobile"), ("execution environment", "E-Province Government Cluster"), ("device", "Secure Civil Data Center")],
        [["kiosk_agent.apk"], ["provincial_services.ear", "auth_service.jar"], ["citizen_records.db", "tax_history.db"]]
    )

    # --- Chapter 10: Product Recommendation System ---
    c10 = "Chapter_10_Design_of_UML_Diagrams_for_Product_Recom"
    diagrams[(c10, "Figure_10_5_UML_state_machine_diagram.svg")] = generate_statemachine_svg(
        "Product Recommendation System", "Recommendation Engine Model State Machine",
        [("ColdStart", ["entry / initFallback", "do / loadTrending"]),
         ("FeatureExtraction", ["entry / parseHistory", "do / computeVectors"]),
         ("InferenceScoring", ["entry / runCosineSim", "do / rankProducts"]),
         ("PersonalizedServed", ["entry / deliverFeed", "exit / logClickthrough"])],
        ["recordInteraction()", "generateEmbeddings()", "serveRecommendations()"]
    )

    # --- Chapter 11: Advocate Diary ---
    c11 = "Chapter_11_Design_of_UML_Diagrams_for_Advocate_Diar"
    diagrams[(c11, "Figure_11_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Advocate Diary", "Case Hearing Schedule Sequence Diagram",
        ["Advocate", "DiaryController", "CourtDBSync", "NotificationWorker"],
        [(0, 1, "1: LogCourtHearing(caseNo, date)", False),
         (1, 2, "2: QueryCourtCauselist(courtId)", False),
         (2, 1, "3: CauselistSyncResult(courtData)", True),
         (1, 3, "4: EnqueueHearingAlert(advocateId)", False),
         (3, 0, "5: DeliverSMSNotification(hearingDetails)", True)],
        ["Advocate logs new court hearing date into mobile diary.",
         "DiaryController queries court causelist API for bench updates.",
         "Court schedule synchronized and verified against official bench.",
         "NotificationWorker enqueues SMS and Push alerts.",
         "Hearing reminder successfully delivered to legal counsel."]
    )
    diagrams[(c11, "Figure_11_7_UML_component_diagram.svg")] = generate_component_svg(
        "Advocate Diary", "Advocate Diary Modular Software Components",
        ["LegalDiaryUI", "HearingScheduler", "CourtScraperModule", "AdvocateDataStore"],
        ["ICaseManagement", "ICourtDataSync"]
    )

    # --- Chapter 12: My Helper ---
    c12 = "Chapter_12_Design_of_UML_Diagrams_for_My_Helper"
    diagrams[(c12, "Figure_12_8_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "My Helper", "My Helper On-Demand Service Platform Deployment",
        [("device", "Customer & Worker Mobile App"), ("execution environment", "MyHelper Cloud Gateway (NodeJS)"), ("device", "Cloud SQL Postgres & Redis")],
        [["myhelper_react_native.apk"], ["service_broker.js", "dispatcher.js"], ["helper_profiles.db", "live_locations.redis"]]
    )

    # --- Chapter 13: COVID-19 Management System ---
    c13 = "Chapter_13_Design_of_UML_Diagrams_for_COVID_19_Mana"
    diagrams[(c13, "Figure_13_3_UML_activity_diagram_part_2.svg")] = generate_activity_svg(
        "COVID-19 Management System", "COVID-19 Quarantine & Recovery Monitoring",
        ["Quarantine Patient Intake", "Log Daily Vitals & Symptoms", "Authorize Clinical Escalation", "Issue Official Discharge Certificate"]
    )
    diagrams[(c13, "Figure_13_4_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "COVID-19 Management System", "COVID Test Booking & Result Sequence",
        ["Citizen", "HealthPortal", "LabSystem", "HealthRegistry"],
        [(0, 1, "1: BookRT_PCRTest(sampleSlot)", False),
         (1, 2, "2: AssignSampleBarcode(slotDetails)", False),
         (2, 3, "3: StoreLabTestResult(barcode, status)", False),
         (3, 1, "4: NotifyPortalOfResult(citizenHealthID)", True),
         (1, 0, "5: DeliverQRHealthCertificate(report)", True)],
        ["Citizen schedules RT-PCR swab test at local facility.",
         "HealthPortal assigns barcode and dispatches order to LabSystem.",
         "LabSystem logs PCR diagnostic result into HealthRegistry.",
         "HealthRegistry verifies outcome and signals HealthPortal.",
         "QR health certificate delivered securely to citizen device."]
    )
    diagrams[(c13, "Figure_13_5_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "COVID-19 Management System", "Vaccine Allocation Collaboration",
        ["HospitalAdmin", "VaccineDispatcher", "CentralColdChainDB", "ImmunizationAudit"],
        [("top", "1.0: RequestDoseQuota()", True), ("right", "2.0: ReserveVials()", True),
         ("bottom", "3.0: AuthorizeColdTransport()", False), ("left", "4.0: ConfirmDelivery()", False)]
    )
    diagrams[(c13, "Figure_13_7_UML_class_diagram.svg")] = generate_class_svg(
        "COVID-19 Management System", "COVID-19 Healthcare Domain Class Diagram",
        [("CitizenPatient", ["citizenID: String", "vaccinationStatus: String"], ["registerForTest", "downloadPass"]),
         ("DiagnosticTest", ["sampleBarcode: String", "testResult: String"], ["processSample", "certifyResult"]),
         ("VaccineDose", ["batchNumber: String", "manufacturer: String"], ["administerDose", "verifyExpiry"]),
         ("HospitalWard", ["wardNumber: Int", "icuBedsAvailable: Int"], ["admitPatient", "dischargePatient"])]
    )

    # --- Chapter 14: Car Care ---
    c14 = "Chapter_14_Design_of_UML_Diagrams_for_Car_Care"
    diagrams[(c14, "Figure_14_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Car Care", "Vehicle Service Booking & Inspection Sequence",
        ["VehicleOwner", "CarCarePortal", "ServiceStation", "BillingService"],
        [(0, 1, "1: RequestVehicleService(vehicleDetails, slot)", False),
         (1, 2, "2: AssignServiceBay(slotDetails)", False),
         (2, 3, "3: GenerateServiceEstimate(parts, labor)", False),
         (3, 1, "4: PresentInvoiceEstimate(invoiceID)", True),
         (1, 0, "5: ConfirmJobCardApproval(approvalToken)", True)],
        ["Vehicle owner books routine maintenance via mobile portal.",
         "CarCarePortal reserves diagnostic bay and technician schedule.",
         "Service station inspects vehicle and generates parts estimate.",
         "BillingService computes costs and presents invoice.",
         "Vehicle owner approves estimate to authorize repair work."]
    )

    # --- Chapter 15: E-Ration Shop ---
    c15 = "Chapter_15_Design_of_UML_Diagrams_for_E_Ration_Shop"
    diagrams[(c15, "Figure_15_4_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "E-Ration Shop", "Subsidized Grain Allocation Collaboration",
        ["RationBeneficiary", "FPS_Terminal", "CivilSuppliesRegistry", "BiometricAuthServer"],
        [("top", "1.0: ScanFingerprint()", True), ("right", "2.0: VerifyBeneficiaryQuota()", True),
         ("bottom", "3.0: DeductStockAllocation()", False), ("left", "4.0: DispenseGrains()", False)]
    )

    # --- Chapter 17: National Health ID 2020 ---
    c17 = "Chapter_17_Design_of_UML_Diagrams_for_National_Heal"
    diagrams[(c17, "Figure_17_8_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "National Health ID 2020", "National Electronic Health Record (EHR) Topology",
        [("device", "Clinical Provider Terminal"), ("execution environment", "National Health Gateway (Go / gRPC)"), ("device", "Federated Health Vault")],
        [["provider_ehr_client.exe"], ["ndhm_gateway.bin", "fhir_adapter.bin"], ["citizen_consent.db", "health_records.vault"]]
    )

    # --- Chapter 20: Crime Bureau ---
    c20 = "Chapter_20_Design_of_UML_Diagrams_for_Crime_Bureau"
    diagrams[(c20, "Figure_20_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Crime Bureau", "FIR Registration & Forensic Investigation Sequence",
        ["InvestigatingOfficer", "BureauPortal", "CriminalRecordDB", "ForensicLab"],
        [(0, 1, "1: RegisterFIR(incidentDetails, suspects)", False),
         (1, 2, "2: QueryCriminalHistory(fingerprintID)", False),
         (2, 1, "3: RecordMatchTelemetry(priorConvictions)", True),
         (1, 3, "4: DispatchEvidenceForForensics(sampleID)", False),
         (3, 0, "5: UploadForensicBallisticsReport(labFindings)", True)],
        ["Investigating officer registers First Information Report (FIR).",
         "BureauPortal queries centralized biometric criminal database.",
         "Historical priors and recidivism telemetry retrieved.",
         "Physical evidence samples dispatched to State Forensic Lab.",
         "Certified forensic findings attached to prosecution casefile."]
    )
    diagrams[(c20, "Figure_20_6_UML_class_diagram.svg")] = generate_class_svg(
        "Crime Bureau", "Crime Intelligence & Investigation Class Diagram",
        [("FIR_Record", ["firNumber: String", "dateFiled: DateTime"], ["recordStatement", "closeCase"]),
         ("SuspectProfile", ["biometricHash: String", "knownAliases: List"], ["matchFingerprint", "flagWanted"]),
         ("ForensicEvidence", ["evidenceTag: String", "chainOfCustody: List"], ["logCustody", "analyzeSpecimen"]),
         ("InvestigatingOfficer", ["badgeNumber: String", "policeStation: String"], ["assignInvestigation", "submitChargeSheet"])]
    )

    # --- Chapter 21: Smart Traffic Management System ---
    c21 = "Chapter_21_Design_of_UML_Diagrams_for_Smart_Traffic"
    diagrams[(c21, "Figure_21_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Smart Traffic Management System", "Automated Speed Violation Challan Sequence",
        ["ANPR_Camera", "TrafficEdgeController", "VehicleRegistryDB", "ChallanPaymentGateway"],
        [(0, 1, "1: CaptureSpeedingVehicle(licensePlate, speed)", False),
         (1, 2, "2: LookupVehicleOwner(licensePlate)", False),
         (2, 1, "3: VehicleOwnershipDetails(ownerContact)", True),
         (1, 3, "4: GenerateElectronicChallan(fineAmount)", False),
         (3, 0, "5: DispatchSMSNoticeAndPaymentLink(challanID)", True)],
        ["High-speed ANPR camera captures speeding vehicle violation.",
         "TrafficEdgeController queries national vehicle registry.",
         "Owner contact information and vehicle history returned.",
         "Electronic challan and fine ledger record created.",
         "SMS notice with digital settlement link sent to vehicle owner."]
    )

    # --- Chapter 24: Online Pharmacy Management System ---
    c24 = "Chapter_24_Design_of_UML_Diagrams_for_Online_Pharma"
    diagrams[(c24, "Figure_24_9_UML_collaboration_diagram_Admin.svg")] = generate_collaboration_svg(
        "Online Pharmacy Management System", "Admin Prescription Audit Collaboration",
        ["AdminPharmacist", "PrescriptionAuditManager", "DrugInventoryDB", "AuditComplianceLogger"],
        [("top", "1.0: ReviewPrescriptionScan()", True), ("right", "2.0: CheckControlledDrugSchedule()", True),
         ("bottom", "3.0: ApproveFulfillment()", False), ("left", "4.0: SignDigitalCompliance()", False)]
    )
    diagrams[(c24, "Figure_24_10_UML_collaboration_diagram_Delivery_Man.svg")] = generate_collaboration_svg(
        "Online Pharmacy Management System", "Delivery Agent Cold-Chain Dispatch Collaboration",
        ["DeliveryRider", "DispatchRoutingEngine", "PharmacyFulfillmentCenter", "CustomerTrackingSMS"],
        [("top", "1.0: AcceptDeliveryRoute()", True), ("right", "2.0: ScanMedicinePackageBarcode()", True),
         ("bottom", "3.0: VerifyColdChainPouch()", False), ("left", "4.0: NotifyCustomerETA()", False)]
    )
    diagrams[(c24, "Figure_24_11_UML_state_machine_diagram_Customer.svg")] = generate_statemachine_svg(
        "Online Pharmacy Management System", "Customer Medicine Order State Machine",
        [("CartPending", ["entry / selectMeds", "do / validateRx"]),
         ("RxReview", ["entry / uploadPrescription", "do / awaitPharmacist"]),
         ("PackedDispatched", ["entry / coldPack", "do / assignCourier"]),
         ("DeliveredComplete", ["entry / collectSignature", "exit / archiveInvoice"])],
        ["submitOrder()", "pharmacistApprove()", "confirmDelivery()"]
    )
    diagrams[(c24, "Figure_24_12_UML_state_machine_diagram_Admin.svg")] = generate_statemachine_svg(
        "Online Pharmacy Management System", "Admin Inventory & Batch Management State Machine",
        [("StockInward", ["entry / verifyInvoice", "do / scanBatch"]),
         ("QuarantineAudit", ["entry / sampleDrugQuality", "do / checkExpiry"]),
         ("ActiveInventory", ["entry / shelfStock", "do / monitorLowStock"]),
         ("Decommissioned", ["entry / incinerateExpired", "exit / reportRegulator"])],
        ["acceptBatch()", "certifyQuality()", "retireExpired()"]
    )
    diagrams[(c24, "Figure_24_13_UML_State_machine_diagram_Delivery_Man.svg")] = generate_statemachine_svg(
        "Online Pharmacy Management System", "Delivery Agent Trip State Machine",
        [("IdleAtDepot", ["entry / checkIn", "do / awaitAssignment"]),
         ("EnRouteToPharmacy", ["entry / navigateToHub", "do / scanPackages"]),
         ("InTransitToPatient", ["entry / monitorCoolerTemp", "do / streamGPS"]),
         ("DeliveredSigned", ["entry / captureSignature", "exit / syncProof"])],
        ["assignManifest()", "pickupPackage()", "completeDropoff()"]
    )
    diagrams[(c24, "Figure_24_17_UML_component_diagram_Customer.svg")] = generate_component_svg(
        "Online Pharmacy Management System", "Customer Portal Modular Components",
        ["CustomerWebMobileUI", "DrugCatalogSearch", "PrescriptionUploadService", "PaymentGatewayAdapter"],
        ["ISearchPrescription", "IPaymentService"]
    )
    diagrams[(c24, "Figure_24_19_UML_component_diagram_Delivery_Man.svg")] = generate_component_svg(
        "Online Pharmacy Management System", "Delivery Rider Logistics Components",
        ["RiderMobileApp", "RouteOptimizationEngine", "TemperatureSensorInterface", "ProofOfDeliveryStore"],
        ["IRouteNavigation", "ITelemetrySync"]
    )

    # --- Chapter 26: OTT Based System MINI REEL ---
    c26 = "Chapter_26_Design_of_UML_Diagrams_for_an_OTT_Based_"
    diagrams[(c26, "Figure_26_4_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "OTT System MINI REEL", "Video Streaming Session Initiation Collaboration",
        ["Subscriber", "StreamingEdgeGateway", "VideoTranscodingCDN", "DigitalRightsManagement"],
        [("top", "1.0: RequestVideoPlayback()", True), ("right", "2.0: ValidateDRMSubscription()", True),
         ("bottom", "3.0: IssuePlaybackManifest()", False), ("left", "4.0: StreamHLSChunks()", False)]
    )

    # --- Chapter 27: e-Med Medical Assistance Tool ---
    c27 = "Chapter_27_Design_of_UML_Diagrams_for_e_Med_Medical"
    diagrams[(c27, "Figure_27_4_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "e-Med Medical Assistance Tool", "Emergency Triage & Assistance Collaboration",
        ["PatientInDistress", "TriageIntelligenceEngine", "EmergencyEMS_Dispatcher", "HospitalEmergencyWard"],
        [("top", "1.0: TriggerSOSAlert()", True), ("right", "2.0: ScoreTriageSeverity()", True),
         ("bottom", "3.0: DispatchAmbulance()", False), ("left", "4.0: ReserveTraumaBed()", False)]
    )
    diagrams[(c27, "Figure_27_7_UML_component_diagram.svg")] = generate_component_svg(
        "e-Med Medical Assistance Tool", "e-Med Health Diagnostics Components",
        ["PatientTelehealthUI", "DiagnosticAI_Assistant", "DoctorConsultationHub", "ElectronicHealthVault"],
        ["IDiagnosisAdvisor", "IClinicalRecords"]
    )
    diagrams[(c27, "Figure_27_8_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "e-Med Medical Assistance Tool", "e-Med Real-Time Cloud Infrastructure",
        [("device", "Patient Smartphone / IoT Vitals"), ("execution environment", "e-Med High-Availability Kubernetes"), ("device", "HIPAA-Compliant Database Cluster")],
        [["emed_flutter.apk"], ["telehealth_server.jar", "webrtc_signaling.bin"], ["medical_records.db", "vitals_timeseries.db"]]
    )

    # --- Chapter 30: E-Visa Processing and Follow-Up System ---
    c30 = "Chapter_30_Design_of_UML_Diagrams_for_E_Visa_Proces"
    diagrams[(c30, "Figure_30_3_UML_activity_diagram_Scenario_2.svg")] = generate_activity_svg(
        "E-Visa Processing System", "Visa Application Biometrics & Embassy Background Check",
        ["Submit Application & Passport Scan", "Execute Interpol & Immigration Watchlist Check", "Authorize Consular Adjudication", "Issue Electronic Visa Grant Notice"]
    )
    diagrams[(c30, "Figure_30_4_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "E-Visa Processing System", "E-Visa Verification & Issuance Sequence",
        ["VisaApplicant", "VisaPortal", "ImmigrationWatchlist", "ConsularOfficer"],
        [(0, 1, "1: SubmitVisaApplication(passportData, travelDates)", False),
         (1, 2, "2: VerifyPassportValidity(passportNo)", False),
         (2, 1, "3: SecurityClearanceOutcome(noMatches)", True),
         (1, 3, "4: ForwardToConsularOfficer(dossierID)", False),
         (3, 0, "5: TransmitElectronicVisaGrant(eVisaPDF)", True)],
        ["Applicant submits international passport and travel dossier.",
         "VisaPortal runs automated check against immigration databases.",
         "Security clearance confirms applicant has no travel bans.",
         "Dossier forwarded to Consular Officer for final approval.",
         "Authenticated electronic visa grant document transmitted."]
    )
    diagrams[(c30, "Figure_30_6_UML_state_chart_diagram.svg")] = generate_statemachine_svg(
        "E-Visa Processing System", "E-Visa Application Statechart Diagram",
        [("ApplicationReceived", ["entry / validateFees", "do / parsePassport"]),
         ("SecurityVetting", ["entry / queryInterpol", "do / checkBorders"]),
         ("ConsularReview", ["entry / reviewInterview", "do / decideGrant"]),
         ("VisaIssuedApproved", ["entry / signCryptographicPDF", "exit / notifyApplicant"])],
        ["verifyDocuments()", "clearSecurity()", "grantVisa()"]
    )

    # --- Chapter 31: Placement Automation System ---
    c31 = "Chapter_31_Design_of_UML_Diagrams_for_Placement_Aut"
    diagrams[(c31, "Figure_31_4_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "Placement Automation System", "Campus Placement Drive Collaboration",
        ["StudentCandidate", "PlacementCellPortal", "CorporateRecruiterDB", "InterviewScheduleWorker"],
        [("top", "1.0: ApplyToJobDrive()", True), ("right", "2.0: FilterByCGPAAndResume()", True),
         ("bottom", "3.0: SlotInterviewRound()", False), ("left", "4.0: TransmitOfferLetter()", False)]
    )

    # --- Chapter 32: Farm Management System ---
    c32 = "Chapter_32_Design_of_UML_Diagrams_for_Farm_Manageme"
    diagrams[(c32, "Figure_32_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Farm Management System", "Automated Crop Irrigation & Weather Sequence",
        ["SoilMoistureSensor", "IoT_IrrigationNode", "WeatherForecastService", "FarmerMobileApp"],
        [(0, 1, "1: TelemetrySoilMoisture(moistureLevel = 22%)", False),
         (1, 2, "2: QueryRainForecast(fieldGPS)", False),
         (2, 1, "3: ForecastRainfall(probability = 0%)", True),
         (1, 3, "4: AlertFarmerIrrigationStart(pumpDuration = 30m)", False),
         (3, 0, "5: TelemetryFlowRateFeedback(pumpActive = true)", True)],
        ["Field sensor detects soil moisture below critical threshold.",
         "Irrigation controller queries satellite meteorological API.",
         "Forecast confirms zero precipitation expected over next 24h.",
         "Automated irrigation pump engaged; notice sent to farmer app.",
         "Closed-loop flow sensor confirms water delivery to crop zone."]
    )
    diagrams[(c32, "Figure_32_4_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "Farm Management System", "Crop Harvest & Silo Storage Collaboration",
        ["FarmManager", "CropHarvestController", "GrainSiloTelemetry", "AgriCommodityExchange"],
        [("top", "1.0: LogCropHarvestYield()", True), ("right", "2.0: CheckSiloCapacity()", True),
         ("bottom", "3.0: ReserveStorageBin()", False), ("left", "4.0: ListCommodityForAuction()", False)]
    )

    # --- Chapter 34: Art Gallery Management System ---
    c34 = "Chapter_34_Design_of_UML_Diagrams_for_Art_Gallery_M"
    diagrams[(c34, "Figure_34_2_UML_activity_diagram.svg")] = generate_activity_svg(
        "Art Gallery Management System", "Artwork Acquisition & Exhibition Cataloging",
        ["Receive Artwork Consignment", "Perform Provenance & Authenticity Appraisal", "Determine Reserve Auction Valuation", "Catalog Artwork into Public Exhibition"]
    )
    diagrams[(c34, "Figure_34_6_UML_class_diagram.svg")] = generate_class_svg(
        "Art Gallery Management System", "Art Gallery Domain Class Model",
        [("ArtPiece", ["artworkID: String", "title: String", "medium: String"], ["appraiseValue", "updateExhibition"]),
         ("ArtistCreator", ["artistID: String", "biography: String"], ["submitConsignment", "withdrawPiece"]),
         ("GalleryExhibition", ["exhibitionTitle: String", "curatorName: String"], ["scheduleOpening", "sellArtwork"]),
         ("ArtCollector", ["collectorID: String", "membershipTier: String"], ["placeAuctionBid", "purchasePiece"])]
    )

    # --- Chapter 36: Online Quiz System ---
    c36 = "Chapter_36_Design_of_UML_Diagrams_for_Online_Quiz_S"
    diagrams[(c36, "Figure_36_2_UML_activity_diagram_Scenario_1.svg")] = generate_activity_svg(
        "Online Quiz System", "Timed Quiz Examination & Submission Workflow",
        ["Start Timed Quiz Attempt", "Record Candidate Answers", "Evaluate Score & Grade Questions", "Display Result & Issue Certificate"]
    )
    diagrams[(c36, "Figure_36_3_UML_activity_diagram_Scenario_2.svg")] = generate_activity_svg(
        "Online Quiz System", "Educator Question Bank Authoring & Publication",
        ["Draft Multiple Choice Questions", "Validate Question Answers & Tags", "Publish Quiz to Student Cohort", "Export Performance Analytics Report"]
    )
    diagrams[(c36, "Figure_36_4_UML_sequence_diagram_Scenario_1.svg")] = generate_animated_sequence_svg(
        "Online Quiz System", "Live Quiz Session & Instant Grading Sequence",
        ["Student", "QuizUI_Client", "AssessmentEngine", "ScoreRegistryDB"],
        [(0, 1, "1: SubmitQuizResponses(quizID, responses)", False),
         (1, 2, "2: StreamAnswerBatchForGrading(payload)", False),
         (2, 3, "3: StoreCandidateScore(studentID, score)", False),
         (3, 2, "4: ScorePersistConfirmation(transactionID)", True),
         (2, 0, "5: RenderPerformanceBreakdown(reportCard)", True)],
        ["Student completes examination and submits all responses.",
         "Client application streams answers to AssessmentEngine.",
         "AssessmentEngine computes grades and writes to ScoreRegistry.",
         "Persistence confirmation acknowledges transaction.",
         "Real-time result breakdown and answer explanations presented."]
    )
    diagrams[(c36, "Figure_36_5_UML_sequence_diagram_Scenario_2.svg")] = generate_animated_sequence_svg(
        "Online Quiz System", "Anti-Cheating Proctoring & Telemetry Sequence",
        ["StudentBrowser", "ProctoringMonitor", "AI_AnomalyDetector", "ExamSupervisor"],
        [(0, 1, "1: StreamWebcamAndTabEvents(eventBatch)", False),
         (1, 2, "2: EvaluateBehavioralAnomalies(eventData)", False),
         (2, 1, "3: AnomalyFlagged(multiFaceDetected = true)", True),
         (1, 3, "4: TriggerSupervisorIntervention(studentSessionID)", False),
         (3, 0, "5: PauseExamAndRequestVerification(warningNotice)", True)],
        ["Student browser streams webcam video and tab switch events.",
         "ProctoringMonitor evaluates telemetry for unauthorized behavior.",
         "AI detector identifies multiple faces in candidate webcam.",
         "Automated security alert routed to live exam supervisor.",
         "Exam paused with prompt requiring candidate re-verification."]
    )
    diagrams[(c36, "Figure_36_10_UML_deployment_diagram.svg")] = generate_deployment_svg(
        "Online Quiz System", "Online Quiz Platform Scalable Cloud Deployment",
        [("device", "Student Web Browser"), ("execution environment", "Quiz Engine Cluster (NodeJS/Express)"), ("device", "PostgreSQL & Redis Cache")],
        [["quiz_app.js"], ["assessment_service.js", "proctoring_ai.bin"], ["quiz_questions.db", "session_cache.redis"]]
    )

    # --- Chapter 38: Website Development ---
    c38 = "Chapter_38_Design_of_UML_Diagrams_for_Website_Devel"
    diagrams[(c38, "Figure_38_3_UML_sequence_diagram.svg")] = generate_animated_sequence_svg(
        "Website Development", "CI/CD Pipeline Build & Deployment Sequence",
        ["Developer", "GitRepository", "CI_BuildServer", "CloudProductionCluster"],
        [(0, 1, "1: GitPushCommit(featureBranch)", False),
         (1, 2, "2: TriggerWebhook(commitHash)", False),
         (2, 3, "3: ExecuteAutomatedTestsAndBuild(dockerImage)", False),
         (3, 2, "4: CanaryDeploymentHealthCheck(status = Healthy)", True),
         (2, 0, "5: NotifyDeploymentSuccess(productionURL)", True)],
        ["Developer pushes tested commit to remote Git repository.",
         "Webhook automatically triggers CI build and lint runner.",
         "Docker image container built and integration tests executed.",
         "Canary deployment rolling update verified against health probe.",
         "Production deployment completed; notification sent to team."]
    )

    # --- Chapter 39: STARTUP MEET ---
    c39 = "Chapter_39_Design_of_UML_Diagrams_for_STARTUP_MEET"
    diagrams[(c39, "Figure_39_5_UML_state_chart_diagram.svg")] = generate_statemachine_svg(
        "STARTUP MEET", "Startup Pitch Competition Statechart",
        [("RegistrationPhase", ["entry / submitDeck", "do / verifyEligibility"]),
         ("ScreeningReview", ["entry / scoreDecks", "do / rankApplications"]),
         ("PitchEventLive", ["entry / presentToVCs", "do / logScores"]),
         ("FundingAwarded", ["entry / termSheetSign", "exit / disburseCapital"])],
        ["closeRegistration()", "shortlistFinalists()", "declareWinners()"]
    )

    # --- Chapter 40: Video Suggestion System ---
    c40 = "Chapter_40_Design_of_UML_Diagrams_for_Video_Suggest"
    diagrams[(c40, "Figure_40_2_UML_activity_diagram_Main_scenario.svg")] = generate_activity_svg(
        "Video Suggestion System", "Main Video Recommendation Pipeline Activity Workflow",
        ["Capture User Watch Session & Interaction", "Filter Candidate Videos via Collaborative Filtering", "Score & Rank Recommendations with Deep Learning", "Serve Personalized Video Feed to Mobile/Web Client"]
    )
    diagrams[(c40, "Figure_40_3_UML_activity_diagram_Other_videos_watched_by_simil.svg")] = generate_activity_svg(
        "Video Suggestion System", "Similar Audience Cross-Watch Suggestion Scenario",
        ["Cluster Similar Viewer Cohorts", "Identify Overlapping High-Engagement Videos", "Filter Out Already Viewed Content", "Inject Recommendations into Up-Next Shelf"]
    )
    diagrams[(c40, "Figure_40_4_UML_activity_diagram_Paid_promotion_videos_scenari.svg")] = generate_activity_svg(
        "Video Suggestion System", "Sponsored & Paid Promotion Video Recommendation Scenario",
        ["Retrieve Active Advertiser Campaigns", "Match Targeting Tags & Demographics", "Enforce Frequency Capping & Ad Disclosure", "Serve Promoted Video Card in Search Results"]
    )
    diagrams[(c40, "Figure_40_5_UML_activity_diagram_Similar_genre_videos_scenario.svg")] = generate_activity_svg(
        "Video Suggestion System", "Similar Genre & Topic Matching Activity Workflow",
        ["Extract Semantic Genre Metadata", "Compute Cosine Distance in Category Embeddings", "Select Top-K Highest Match Candidates", "Display Thematic Genre Playlist Carousel"]
    )
    diagrams[(c40, "Figure_40_6_UML_activity_diagram_Similar_tag_videos_scenario.svg")] = generate_activity_svg(
        "Video Suggestion System", "Tag-Based Content Clustering Recommendation Scenario",
        ["Extract Creator Hashtags & Keywords", "Perform Tag TF-IDF Frequency Analysis", "Filter Low-Quality Clickbait Matches", "Deliver Relevant Tag Recommendation Ribbon"]
    )
    diagrams[(c40, "Figure_40_7_UML_activity_diagram_Trending_videos_scenario.svg")] = generate_activity_svg(
        "Video Suggestion System", "Trending & Velocity-Ranked Video Recommendation Workflow",
        ["Calculate Real-Time View Acceleration (V/hr)", "Apply Decay Factor to Older Content", "Filter by Regional Geo-Localization", "Surface Real-Time Trending Top 50 Chart"]
    )
    diagrams[(c40, "Figure_40_8_UML_Activity_diagram_Video_attributes_scenario.svg")] = generate_activity_svg(
        "Video Suggestion System", "Video Attribute & Audio-Visual Feature Matching Workflow",
        ["Analyze Video Duration, Resolution, & Audio Fingerprint", "Match User Device & Network Bandwidth", "Optimize Bitrate & Thumbnail Pre-Fetch", "Stream Optimized Video Asset to Player"]
    )
    diagrams[(c40, "Figure_40_10_UML_collaboration_diagram.svg")] = generate_collaboration_svg(
        "Video Suggestion System", "Video Recommendation Retrieval Collaboration",
        ["ViewerApp", "RecommendationGateway", "EmbeddingVectorDB", "UserWatchHistoryService"],
        [("top", "1.0: GetFeedRecommendations()", True), ("right", "2.0: QueryANN_Vectors()", True),
         ("bottom", "3.0: ExcludeWatchedVideos()", False), ("left", "4.0: ReturnRankedFeed()", False)]
    )
    diagrams[(c40, "Figure_40_12_UML_class_diagram.svg")] = generate_class_svg(
        "Video Suggestion System", "Video Recommendation Architecture Class Model",
        [("VideoItem", ["videoID: String", "durationSeconds: Int", "genreCategory: String"], ["getEmbeddings", "incrementViews"]),
         ("UserViewer", ["userID: String", "preferredCategories: List"], ["watchVideo", "likeVideo"]),
         ("RecommendationModel", ["modelWeights: Matrix", "inferenceVersion: String"], ["predictCTR", "rankBatch"]),
         ("WatchSession", ["sessionID: String", "watchDurationPct: Float"], ["recordWatch", "computeEngagement"])]
    )

    return diagrams


def run():
    print("=" * 70)
    print("🚀 INITIATING CANONICAL CLAUDE DIAGRAM REMAKING PIPELINE")
    print("=" * 70)

    diagrams = build_all_canonical_diagrams()
    print(f"Loaded {len(diagrams)} Canonical Claude diagram specifications.")

    # 1. Generate, validate XML, and save SVGs
    valid_count = 0
    generated_canonical_files = set()

    for (sub_dir, filename), svg_code in diagrams.items():
        # Validate XML
        try:
            ET.fromstring(svg_code)
        except ET.ParseError as e:
            print(f"❌ XML Syntax Error in {sub_dir}/{filename}: {e}")
            sys.exit(1)

        target_dir = os.path.join(VECTOR_DIR, sub_dir)
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, filename)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(svg_code)

        generated_canonical_files.add((sub_dir, filename))
        valid_count += 1
        print(f"  ✓ Validated & Generated: {sub_dir}/{filename}")

    print(f"\n✨ Successfully validated and wrote {valid_count} Canonical Claude SVGs!")

    # 2. Update Chapter Markdown Files Safely
    print("\nUpdating chapter markdown files to embed Canonical Claude SVGs...")
    updated_links_total = 0

    for cf in sorted(os.listdir(CHAP_DIR)):
        if not cf.endswith(".md"):
            continue
        cpath = os.path.join(CHAP_DIR, cf)
        with open(cpath, "r", encoding="utf-8") as f:
            content = f.read()

        chap_updates = 0
        for sub_dir, filename in generated_canonical_files:
            base_name = os.path.splitext(filename)[0]
            # Replace link from ../images/<sub_dir>/<base_name>.png -> ../vector_images/<sub_dir>/<filename>
            old_png_pattern = rf"\(\.\./images/{sub_dir}/{base_name}\.png\)"
            new_svg_link = f"(../vector_images/{sub_dir}/{filename})"
            if re.search(old_png_pattern, content):
                content = re.sub(old_png_pattern, new_svg_link, content)
                chap_updates += 1

        if chap_updates > 0:
            with open(cpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ {cf}: Replaced {chap_updates} diagram link(s) with Canonical Claude SVGs.")
            updated_links_total += chap_updates

    print(f"\n🎉 Total links upgraded across all chapters: {updated_links_total}")
    print("=" * 70)


if __name__ == "__main__":
    run()
