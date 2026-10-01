---
name: dev-auto-commit
trigger: any docs/*.md change
action: git add . && git commit -m "docs update: $(date +%Y-%m-%d %H:%M)" && git push
---
