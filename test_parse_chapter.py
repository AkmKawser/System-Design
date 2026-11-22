import glob
import os
import re

folder = r"C:\Users\HP\Documents\GitHub\System-Design\topics\0.FUNDAMENTALS\System Requirements\UML-DIAGRAMMING\Data_Ingestion\Books\umlBook\chapters"

def parse_chapter(fpath):
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    # Title
    m_title = re.search(r"# (Chapter \d+: [^\n]+)", c)
    title = m_title.group(1) if m_title else os.path.basename(fpath)
    clean_sys = re.sub(r"^Chapter \d+:\s*", "", title)
    clean_sys = clean_sys.replace("Design of UML Diagrams for ", "").replace("UML Diagrams for ", "").strip()
    
    # Functional capabilities
    start_cap = c.find("## ⚙️ System Architecture & Functional Capabilities")
    end_cap = c.find("## 📊 Complete UML Diagram Suite")
    caps = []
    if start_cap != -1 and end_cap != -1:
        cap_text = c[start_cap:end_cap]
        caps = re.findall(r"- \*\*([^*]+)\*\*:\s*([^\n]+)", cap_text)
    
    # Problem statement
    start_ps = c.find("## 🎯 Problem Statement & Business Context")
    end_ps = c.find("---", start_ps) if start_ps != -1 else -1
    ps_text = c[start_ps:end_ps] if start_ps != -1 else ""
    
    return clean_sys, caps, ps_text

for fname in ["Chapter_02_Design_of_UML_Diagrams_for_Webmed_Healthcare_Service_System_Services.md",
              "Chapter_03_Design_of_UML_Diagrams_for_Inventory_Management_System.md"]:
    fpath = os.path.join(folder, fname)
    clean_sys, caps, ps = parse_chapter(fpath)
    print("System:", clean_sys)
    print("Capabilities count:", len(caps))
    for name, desc in caps[:3]:
        print(f"  * {name}: {desc[:60]}...")
    print()
