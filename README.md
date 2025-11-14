# Secure API Starter (FastAPI + DevSecOps)

Tiny FastAPI service with real guardrails: rate limiting, header API key, Prometheus metrics, security headers, Docker, and a CI pipeline that actually blocks bad changes (tests, lint, SBOM, dep audit, image vuln scan, baseline DAST).

![CI](https://img.shields.io/github/actions/workflow/status/adela117/pg-secure-api/ci.yml?label=CI)
![License](https://img.shields.io/badge/license-MIT-informational)
![Security](https://img.shields.io/badge/SBOM-CycloneDX-blue)
![DAST](https://img.shields.io/badge/DAST-ZAP%20baseline-purple)

- ✅ Automated tests on every push/PR using Pytest (/health and auth behavior)
- ✅ Style + lint gates with Black (auto-format + check) and Flake8 (fails on issues)
- ✅ Container build & run in CI: image built with Buildx, started in the workflow, and health-checked
- ✅ Baseline DAST: OWASP ZAP hits the running container’s /health to catch obvious regressions
- ✅ Software Bill of Materials (SBOM) generated as CycloneDX via Syft and uploaded as a build artifact
- ✅ Dependency vulnerability audit with pip-audit --strict (fails on known CVEs)
- ✅ Image vulnerability scan with Trivy (fails on HIGH/CRITICAL)
- ✅ Security static analysis with Bandit on the app/ code
- ✅ Runtime safeguards in the app code (validated by CI build): rate limiting on /health, header API key for protected routes, security headers, and Prometheus /metrics
- ✅ Branch-protection ready: mark lint, test, build_and_zap, sbom_and_deps, image_scan, and bandit as required checks to block unsafe merges
- ✅ Artifacts & logs: SBOM and scan reports are stored per-run in Actions for auditability

---
## Endpoints

Base URL (local): `http://127.0.0.1:8000`  
Swagger UI: `/docs`  
Metrics (Prometheus): `/metrics`

### Public
- `GET /health`  
  Response: `{"status":"ok","ts":<epoch>}`  
  Rate limited: **20/minute per IP**

---
## Quick start

```bash
# 1) run locally
pip install -r requirements.txt
uvicorn app.main:app --reload

# 2) or run in Docker
docker build -t secure-api .
docker run -p 8000:8000 secure-api
