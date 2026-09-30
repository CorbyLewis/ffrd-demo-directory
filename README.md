# ffrd-demo-directory

Demo of the standard directory structure for FFRD projects, with a description of what
belongs in each folder.

Site: https://usace-cloud-compute.github.io/ffrd-demo-directory/

## How it works

- `docs/basin-name/` is the template. Each folder holds an `index.md` describing its
  intended use. These files are data, not site pages (`exclude_docs` in `mkdocs.yml`):
  the site is a single home page with a folder browser. Every folder has an `index.md`, so
  no placeholder files are needed to keep folders in git.
- `hooks/ffrd_site.py` runs on every build and generates, without touching `docs/`:
  - `assets/tree.json`, which feeds the interactive folder browser on the home page
    (`docs/javascripts/ffrd-tree.js`);
  - `assets/ffrd-template.zip`, the empty template. `index.md` becomes `README.md` in
    every folder. Empty folders survive the download because the zip
    lists every folder explicitly and each one contains a `README.md`.
- Settings (template folder, zip name, README name) are under `extra.ffrd` in `mkdocs.yml`.

## Editing

1. Create a fork of the repository
2. Write or edit the folder's `index.md` on a separate branch. A folder with no description yet holds the
   placeholder text set in `mkdocs.yml` (`extra.ffrd.placeholder`); `fix_titles.py` adds it
   to any new or heading-only page (not the template root). Text before the first `##` heading is what the
   browser shows as the summary. A section on a parent page whose heading names a child
   folder (for example `## HOT-FIX`) is used for that child if its own page is empty.
3. Preview: run `serve.bat`, or `pip install -r requirements.txt` then `mkdocs serve`.
4. Create a pull request to the usace-cloud-compute/ffrd-demo-directory main.
5. A repo owner will review and approve and merge into `main`; the workflow deploys.

Add `?audit` to the home page URL to list folders that still have only the placeholder.
