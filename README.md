# Nexus Leads (Nexus Management Solutions LLC)

Static lead-gen sites for Nexus Solutions, Colorado cash home buyer.

- Root: desktop site, deployed to Vercel project `nexus-leads` (https://nexus-leads-chrisinvestor05-9546s-projects.vercel.app)
- `mobile/`: mobile-first site, deployed to Vercel project `nexus-leads-mobile` (https://nexus-leads-mobile-chrisinvestor05-9546s-projects.vercel.app)
- `source/`: generator (`build.py`), CSS sources and the logo PNG renderer (`render.js`).

Note: binary assets (JPG photos, PNG logo/favicon exports, favicon.ico) are not stored in this repo because the GitHub connector used for this push only supports text files. They are live on both Vercel deployments under /img and /brand. To rebuild locally run `python3 source/build.py` after restoring /img and /brand (see CREDITS.md for photo sources; `node source/render.js` regenerates PNGs from the SVGs). `favicon.svg` is identical to `brand/mark.svg`.
