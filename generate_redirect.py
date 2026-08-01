#!/usr/bin/env python3
"""
Generate redirect.html with customizable origin parameter.
Usage: python3 generate_redirect.py --origin "https://whatever.com"
"""

import argparse
from pathlib import Path


def generate_redirect_html(origin: str = "/") -> str:
    """
    Generate redirect.html content with customizable origin.
    
    Args:
        origin: The default redirect destination (default: "/")
    
    Returns:
        HTML content as a string
    """
    html_content = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Redirecting...</title>
  <meta name="robots" content="noindex">
  <script>
    // Get the redirect URL from query parameter or use configured origin
    const params = new URLSearchParams(window.location.search);
    const redirectTo = params.get('to') || '{origin}';
    
    // Redirect after a short delay
    setTimeout(() => {{
      window.location.href = redirectTo;
    }}, 500);
  </script>
  <style>
    :root{{--bg:#0f1724;--card:#0b1220;--accent:#7dd3fc;--muted:#93a7bd}}
    html,body{{height:100%;margin:0;font-family:Inter, Roboto, -apple-system, system-ui, "Segoe UI", "Helvetica Neue", Arial; background:linear-gradient(180deg,#071027 0%, #0f1724 100%);color:#e6f0fb}}
    .wrap{{min-height:100%;display:flex;align-items:center;justify-content:center;padding:48px}}
    .card{{max-width:820px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border:1px solid rgba(255,255,255,0.03);padding:48px;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.3)}}
    h2{{margin:0 0 16px;font-size:20px;color:#eaf6ff}}
    p{{margin:0 0 18px;color:var(--muted)}}
    .spinner{{width:40px;height:40px;border:3px solid rgba(125,211,252,0.2);border-top:3px solid var(--accent);border-radius:50%;animation:spin 1s linear infinite;margin-bottom:20px}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .actions{{display:flex;gap:12px;margin-top:8px}}
    .btn{{display:inline-block;padding:10px 16px;border-radius:8px;text-decoration:none;color:#072433;background:#e6f0fb;border:0;font-weight:600}}
    .btn.secondary{{background:transparent;color:var(--accent);border:1px solid rgba(125,211,252,0.16)}}
    @media (max-width:640px){{.card{{padding:28px}}}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="spinner"></div>
      <h2>Redirecting...</h2>
      <p>Please wait while we redirect you to the correct page.</p>
      <div class="actions">
        <a class="btn secondary" href="{origin}">Go to homepage instead</a>
      </div>
    </div>
  </div>
</body>
</html>'''
    return html_content


def main():
    parser = argparse.ArgumentParser(
        description="Generate redirect.html with customizable origin parameter"
    )
    parser.add_argument(
        "--origin",
        type=str,
        default="/",
        help='Default redirect destination (default: "/")',
    )
    parser.add_argument(
        "--output",
        type=str,
        default="redirect.html",
        help="Output file path (default: redirect.html)",
    )

    args = parser.parse_args()

    # Generate HTML
    html_content = generate_redirect_html(origin=args.origin)

    # Write to file
    output_path = Path(args.output)
    output_path.write_text(html_content)

    print(f"✅ Generated {args.output}")
    print(f"📍 Default origin: {args.origin}")
    print(f"\nUsage examples:")
    print(f"  - {args.output}?to=/about → redirects to /about")
    print(f"  - {args.output}?to=https://example.com → redirects to external URL")
    print(f"  - {args.output} → redirects to {args.origin}")


if __name__ == "__main__":
    main()
