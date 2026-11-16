# High-fidelity 3D DevOps animation overlay

This package adds a richer 3D-inspired DevOps visual layer to your existing GitHub Pages portfolio.

## Features
- Animated orbital cloud globe with AWS / EC2 / S3 / RDS / EKS / VPC / CI-CD / IaC nodes
- Moving data packets and network mesh
- High-tech hero and terminal panel
- Animated CI/CD stages
- Kubernetes architecture visualization
- Illustrative telemetry sparklines
- Pointer-responsive 3D tilt and scroll reveal
- Responsive layout and reduced-motion accessibility

## Install without replacing your page content
1. Download and extract this package.
2. Clone your repository: `git clone https://github.com/Deepak11python/Deepak11python.git`
3. Copy the package's `assets` folder into the repository root (merge if it already exists).
4. Copy `apply-highfi.py` into the repository root.
5. Run `python apply-highfi.py`.
6. Inspect the generated `index.html` and its `index.html.highfi-backup`.
7. Commit and push the changes to GitHub Pages.

The script only injects stylesheet and JavaScript references. It does not replace your README content, project table, or existing links.

## Notes
- The animated telemetry is illustrative only; it is not connected to Prometheus, Grafana, AWS or a live cluster.
- The 3D globe is rendered with Canvas and does not require Three.js, npm or a build pipeline.
- No external JavaScript libraries are required.
- The overlay uses a generated hero section above the existing portfolio content.
- On narrow screens the panels stack vertically.
- `prefers-reduced-motion` is respected.
