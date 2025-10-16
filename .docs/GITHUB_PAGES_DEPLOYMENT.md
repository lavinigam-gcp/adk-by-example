# GitHub Pages Deployment Guide for ADK by Example

## 🎉 Yes, GitHub Pages is FREE and Perfect for This Project!

GitHub Pages is a **completely free** static site hosting service provided by GitHub. It's ideal for the ADK by Example project because:
- ✅ **100% Free** for public repositories
- ✅ **No credit card required**
- ✅ **Automatic HTTPS**
- ✅ **Custom domain support** (optional)
- ✅ **Automatic deployment** on push

## Quick Setup (< 5 minutes)

### Option 1: Simple GitHub Pages (Easiest)

1. **Create/Push Your Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/adk-by-example.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repo on GitHub
   - Click **Settings** → **Pages** (left sidebar)
   - Source: Select **Deploy from a branch**
   - Branch: Select **main** (or master)
   - Folder: Select **/ (root)** or **/docs** if your site is in docs folder
   - Click **Save**

3. **Access Your Site**
   - Your site will be available at:
   - `https://YOUR_USERNAME.github.io/adk-by-example/`
   - Takes 2-10 minutes for first deployment

### Option 2: GitHub Pages with Custom Structure

Since our website files are in `/website` folder:

1. **Create `.github/workflows/deploy.yml`**
   ```yaml
   name: Deploy to GitHub Pages

   on:
     push:
       branches: [ main ]
     workflow_dispatch:

   jobs:
     deploy:
       runs-on: ubuntu-latest
       permissions:
         contents: read
         pages: write
         id-token: write

       steps:
         - uses: actions/checkout@v4

         - name: Setup Pages
           uses: actions/configure-pages@v4

         - name: Upload artifact
           uses: actions/upload-pages-artifact@v3
           with:
             path: './website'

         - name: Deploy to GitHub Pages
           uses: actions/deploy-pages@v4
   ```

2. **Enable GitHub Pages with Actions**
   - Go to **Settings** → **Pages**
   - Source: Select **GitHub Actions**

3. **Push and Deploy**
   ```bash
   git add .github/workflows/deploy.yml
   git commit -m "Add GitHub Pages deployment"
   git push
   ```

## Project Structure for GitHub Pages

```
adk-by-example/
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions deployment
├── website/                  # Static site files
│   ├── index.html            # Main page
│   ├── style.css            # Styles
│   ├── script.js            # Interactive features
│   └── examples.json        # Generated from examples
├── examples/                 # ADK examples (not deployed)
│   └── ...
└── README.md                # GitHub repo page
```

## Website Implementation

### Simple `website/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADK by Example - Copy-paste solutions for ADK developers</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>🚀 ADK by Example</h1>
            <p>Copy-paste solutions for common ADK tasks</p>
            <div class="quick-links">
                <a href="https://github.com/YOUR_USERNAME/adk-by-example" class="btn">GitHub</a>
                <a href="#getting-started" class="btn primary">Get Started</a>
            </div>
        </div>
    </header>

    <nav>
        <div class="container">
            <input type="search" id="search" placeholder="Search: 'google search', 'deploy', 'oauth'...">
        </div>
    </nav>

    <main class="container">
        <section id="getting-started">
            <h2>🎯 I need to...</h2>
            <div class="examples-grid">
                <a href="#first-agent" class="example-card">
                    <h3>Create my first agent</h3>
                    <p>Working agent in 10 lines</p>
                    <code>adk create my-agent --from first-agent</code>
                </a>
                <a href="#search-google" class="example-card">
                    <h3>Search Google</h3>
                    <p>Add web search to my agent</p>
                    <code>adk create my-agent --from search-google</code>
                </a>
                <!-- More examples -->
            </div>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

### Simple `website/style.css`
```css
:root {
    --primary: #4285f4;
    --text: #202124;
    --bg: #ffffff;
    --card: #f8f9fa;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

header {
    background: var(--primary);
    color: white;
    padding: 2rem 0;
    text-align: center;
}

.examples-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.example-card {
    background: var(--card);
    padding: 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    color: var(--text);
    transition: transform 0.2s;
}

.example-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

code {
    background: #202124;
    color: #fff;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.9em;
}
```

## Advanced Features

### 1. Custom Domain (Optional)
If you have a domain (e.g., `adkbyexample.com`):

1. **Add CNAME file** to `/website/CNAME`:
   ```
   adkbyexample.com
   ```

2. **Configure DNS** at your domain registrar:
   - A record: `185.199.108.153`
   - A record: `185.199.109.153`
   - A record: `185.199.110.153`
   - A record: `185.199.111.153`
   - CNAME: `www` → `YOUR_USERNAME.github.io`

3. **Enable in GitHub**:
   - Settings → Pages → Custom domain
   - Enter your domain
   - Check "Enforce HTTPS"

### 2. Generate Examples Index Automatically

Create `scripts/generate_site.py`:
```python
#!/usr/bin/env python3
import json
import os
from pathlib import Path

def generate_examples_json():
    examples = []
    examples_dir = Path("examples")

    for category_dir in examples_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('_'):
            for example_dir in category_dir.iterdir():
                if example_dir.is_dir():
                    # Read metadata.json if exists
                    metadata_file = example_dir / "metadata.json"
                    if metadata_file.exists():
                        with open(metadata_file) as f:
                            metadata = json.load(f)
                            metadata['path'] = str(example_dir.relative_to(examples_dir))
                            examples.append(metadata)

    # Write to website directory
    with open("website/examples.json", "w") as f:
        json.dump(examples, f, indent=2)

    print(f"Generated {len(examples)} examples")

if __name__ == "__main__":
    generate_examples_json()
```

Run before deploying:
```bash
python scripts/generate_site.py
git add website/examples.json
git commit -m "Update examples index"
git push
```

## Deployment Checklist

- [ ] Repository is public (required for free GitHub Pages)
- [ ] Website files in `/website` or `/docs` folder
- [ ] `index.html` exists as entry point
- [ ] All links use relative paths
- [ ] GitHub Pages enabled in Settings
- [ ] Deployment successful (check Actions tab)
- [ ] Site accessible at `https://USERNAME.github.io/REPO/`

## Alternative: GitHub Pages + Jekyll

GitHub Pages has built-in Jekyll support for more features:

1. **Create `website/_config.yml`**:
   ```yaml
   title: ADK by Example
   description: Copy-paste solutions for ADK developers
   theme: minima

   collections:
     examples:
       output: true
       permalink: /:collection/:name
   ```

2. **Use Markdown files** for examples
3. **Automatic generation** of navigation, search, etc.

## Limitations

- **Public repos only** for free tier (perfect for open-source)
- **1GB site size limit** (more than enough)
- **100GB bandwidth/month** (plenty for documentation)
- **10 builds per hour** (rarely an issue)

## Summary

GitHub Pages is the **perfect free solution** for ADK by Example because:
1. ✅ Completely free
2. ✅ Automatic deployment
3. ✅ HTTPS included
4. ✅ Great performance (CDN)
5. ✅ No maintenance required
6. ✅ Integrated with your repo

**Total Cost: $0/month forever** 🎉

## Next Steps

1. Push your code to GitHub
2. Enable GitHub Pages (2 clicks)
3. Wait 5 minutes
4. Share your site URL!

Your site will be live at:
`https://[YOUR_GITHUB_USERNAME].github.io/adk-by-example/`