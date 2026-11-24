import re
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def main():
    root = Path(__file__).resolve().parents[2]
    catalog_path = root / "topics" / "0.FUNDAMENTALS" / "Software Architecture and Modeling" / "1.ARCHITECTURE" / "2. Architecture Patterns" / "output" / "query_Architecture_Patterns" / "003_complete_architectural_patterns_catalog.md"
    images_dir = catalog_path.parent / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Clean up old underscore files
    for old_f in images_dir.glob("*_*.png"):
        try:
            old_f.unlink()
        except Exception:
            pass
            
    cache_dir = root / "engine" / "scripts" / "cache"
    mermaid_js_path = cache_dir / "mermaid.min.js"
    if not mermaid_js_path.exists():
        print("Error: mermaid.min.js not found in cache.")
        sys.exit(1)
        
    mermaid_js = mermaid_js_path.read_text(encoding="utf-8")
    
    # Diagram filenames using strictly HYPHENS (never underscores to prevent markdown italics parsing in URLs)
    diagram_meta = [
        ("01-overview-taxonomy.png", "Architectural Patterns Category Taxonomy Map"),
        ("02-mvc-pattern.png", "Model-View-Controller (MVC) Architecture"),
        ("03-mvvm-pattern.png", "Model-View-ViewModel (MVVM) Architecture"),
        ("04-mvp-pattern.png", "Model-View-Presenter (MVP) Architecture"),
        ("05-mvi-pattern.png", "Model-View-Intent (MVI) Unidirectional Data Flow"),
        ("06-front-controller.png", "Front Controller Pattern with Intercepting Filters"),
        ("07-cqrs-pattern.png", "Command Query Responsibility Segregation (CQRS) Architecture"),
        ("08-event-sourcing.png", "Event Sourcing with Snapshot Optimization"),
        ("09-saga-orchestration-vs-choreography.png", "Saga Pattern: Orchestration vs Choreography"),
        ("10-transactional-outbox.png", "Transactional Outbox Pattern with CDC / Debezium"),
        ("11-cache-aside.png", "Cache-Aside (Lazy Loading) Architecture"),
        ("12-read-write-through-behind.png", "Read-Through, Write-Through, and Write-Behind Caching"),
        ("13-database-sharding.png", "Database Horizontal Sharding Architecture"),
        ("14-api-gateway.png", "API Gateway Ingress Architecture"),
        ("15-backend-for-frontend-bff.png", "Backend-for-Frontend (BFF) Pattern"),
        ("16-aggregator-scatter-gather.png", "Aggregator vs Scatter-Gather Composition"),
        ("17-sidecar-ambassador.png", "Sidecar and Ambassador Pattern"),
        ("18-anti-corruption-layer-acl.png", "Anti-Corruption Layer (ACL) Gateway"),
        ("19-pipes-and-filters.png", "Pipes and Filters Pipeline Architecture"),
        ("20-blackboard-pattern.png", "Blackboard Coordination Architecture"),
        ("21-circuit-breaker-state-machine.png", "Circuit Breaker 3-State Machine"),
        ("22-bulkhead-isolation.png", "Bulkhead Resource Pool Isolation"),
        ("23-priority-queue-dlq.png", "Priority / Ambulance Queue and Dead Letter Queue (DLQ)"),
        ("24-hexagonal-ports-adapters.png", "Hexagonal Architecture (Ports and Adapters)"),
        ("25-clean-onion-architecture.png", "Clean / Onion Layered Architecture"),
        ("26-strangler-fig-pattern.png", "Strangler Fig Incremental Migration Pattern"),
        ("27-microkernel-plugin-pattern.png", "Microkernel (Plugin) Extensible Architecture"),
        ("28-broker-pattern.png", "Broker Distributed Coordination Pattern")
    ]
    
    # Re-run generator script to get fresh markdown with mermaid blocks if needed,
    # or replace existing image links if already replaced
    text = catalog_path.read_text(encoding="utf-8")
    
    # Check if text currently has image links or mermaid blocks
    if "images/01_overview_taxonomy.png" in text or "images/01-overview-taxonomy.png" in text:
        print("Updating existing image links in markdown to hyphenated paths...")
        for i, (fname, alt_text) in enumerate(diagram_meta):
            old_name = fname.replace("-", "_")
            text = text.replace(f"images/{old_name}", f"images/{fname}")
        catalog_path.write_text(text, encoding="utf-8")
    
    # Re-render all to hyphenated files
    # We can copy from underscore files if they exist, or render freshly
    render_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
{mermaid_js}
</script>
<style>
  body {{
    margin: 0;
    padding: 24px;
    background-color: white;
    display: inline-block;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  #graph {{
    background-color: white;
  }}
</style>
</head>
<body>
<div id="graph"></div>
<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'default',
    flowchart: {{ useMaxWidth: false, htmlLabels: true }},
    themeVariables: {{
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
    }}
  }});
  async function renderMermaid(code) {{
    try {{
      document.getElementById('graph').innerHTML = '';
      const id = 'svg_' + Math.random().toString(36).substring(2, 9);
      const {{ svg }} = await mermaid.render(id, code);
      document.getElementById('graph').innerHTML = svg;
      return {{ success: true }};
    }} catch (err) {{
      return {{ success: false, error: err.toString() }};
    }}
  }}
</script>
</body>
</html>"""

    html_file = cache_dir / "render_runner.html"
    html_file.write_text(render_html, encoding="utf-8")
    
    # Check if generator script has original mermaid code blocks
    from generate_graphical_patterns_catalog import content as original_mermaid_content
    mermaid_blocks = list(re.finditer(r'```mermaid\n([\s\S]*?)\n```', original_mermaid_content))
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        page.goto(f"file:///{html_file.resolve().as_posix()}")
        
        for i, match in enumerate(mermaid_blocks):
            code = match.group(1).strip()
            fname, alt_text = diagram_meta[i]
            target_png = images_dir / fname
            
            res = page.evaluate("renderMermaid", code)
            if not res.get("success"):
                print(f"Error rendering diagram {i+1} ({fname}): {res.get('error')}")
                continue
                
            page.wait_for_selector("#graph svg")
            svg_locator = page.locator("#graph svg")
            svg_locator.screenshot(path=str(target_png))
            print(f"[{i+1:02d}/{len(mermaid_blocks)}] Rendered {fname} ({target_png.stat().st_size} bytes)")
            
        browser.close()
        
    # Replace markdown with hyphenated image links from original content
    new_text = original_mermaid_content
    for i in reversed(range(len(mermaid_blocks))):
        m = mermaid_blocks[i]
        fname, alt_text = diagram_meta[i]
        replacement = f"![{alt_text}](images/{fname})"
        new_text = new_text[:m.start()] + replacement + new_text[m.end():]
        
    with open(catalog_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
        
    print(f"Successfully generated hyphenated image assets and updated {catalog_path}")

if __name__ == "__main__":
    main()
