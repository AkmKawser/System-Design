# -*- coding: utf-8 -*-
import os
import re
from enhanced_derivation_generator import derive_components_and_steps

chapter_path = r"C:\Users\HP\Documents\GitHub\System-Design\topics\0.FUNDAMENTALS\System Requirements\UML-DIAGRAMMING\Data_Ingestion\Books\umlBook\chapters\Chapter_02_Design_of_UML_Diagrams_for_Webmed_Healthcare_Service_System_Services.md"

with open(chapter_path, "r", encoding="utf-8") as f:
    text = f.read()

# Get chapter title
title_m = re.search(r"# (Chapter \d+: [^\n]+)", text)
chapter_title = title_m.group(1) if title_m else "Webmed Healthcare"
clean_sys = re.sub(r"^Chapter \d+:\s*", "", chapter_title)
clean_sys = clean_sys.replace("Design of UML Diagrams for ", "").replace("UML Diagrams for ", "").strip()

# Extract capabilities
start_cap = text.find("## ⚙️ System Architecture & Functional Capabilities")
end_cap = text.find("## 📊 Complete UML Diagram Suite")
caps = []
if start_cap != -1 and end_cap != -1:
    cap_text = text[start_cap:end_cap]
    caps = re.findall(r"- \*\*([^*]+)\*\*:\s*([^\n]+)", cap_text)

# Extract problem statement text
start_ps = text.find("## 🎯 Problem Statement & Business Context")
end_ps = text.find("---", start_ps) if start_ps != -1 else -1
ps_text = text[start_ps:end_ps] if start_ps != -1 else ""

# Remove existing guides if any
text = re.sub(r"\n\n#### 🛠️ Step-by-Step Construction Guide[\s\S]*?(?=\n\n### |\n\n## |\Z)", "", text)
text = re.sub(r"\n\n#### 🔍 Component Derivation from Problem Requirements[\s\S]*?(?=\n\n### |\n\n## |\Z)", "", text)

# Find all figures
fig_regex = re.compile(
    r"(### (Figure \d+\.\d+:? [^\n]+)\n\n"
    r"\*\*Diagram Category\*\*:\s*`([^`]+)`\s*\n"
    r"\*\*Architectural Role\*\*:\s*([^\n]+)\n\n"
    r"\*\*System Design Analysis\*\*:\s*\n([^\n]+(?:\n[^\n]+)*?)\n\n"
    r"(!\[Figure [^\]]+\]\([^\)]+\)))",
    re.M
)

matches = list(fig_regex.finditer(text))
print(f"Matched {len(matches)} figures in Chapter 2")

new_text = text
for m in reversed(matches):
    full_block = m.group(1)
    fig_title = m.group(2)
    category = m.group(3)
    arch_role = m.group(4)
    analysis = m.group(5)
    img_tag = m.group(6)
    
    guide = derive_components_and_steps(fig_title, category, clean_sys, arch_role, caps, ps_text)
    replacement = f"{full_block}\n\n{guide}"
    
    start, end = m.span(1)
    new_text = new_text[:start] + replacement + new_text[end:]

with open(chapter_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Chapter 2 updated with Component Derivation and Step-by-Step guide!")
