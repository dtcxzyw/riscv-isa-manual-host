import json
import sys
import subprocess

release = json.loads(open(sys.argv[1]).read())
files = []

for assets in release["assets"]:
    name = assets["name"]
    url = assets["browser_download_url"]
    asset_type = assets["content_type"]

    if name.endswith(".html") and asset_type == "text/html":
        if name.startswith("riscv-unprivileged"):
            files.append(("unpriv-isa-asciidoc.html", url))
        elif name.startswith("riscv-privileged"):
            files.append(("priv-isa-asciidoc.html", url))

for name, url in files:
    subprocess.check_output(["wget", url, "-O", name])
