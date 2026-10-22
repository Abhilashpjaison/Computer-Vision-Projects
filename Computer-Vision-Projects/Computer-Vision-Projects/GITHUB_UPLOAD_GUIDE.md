# Upload to GitHub

This ZIP does not create a remote repository automatically.

1. Sign in at https://github.com/
2. Select **+ → New repository** and name it `Computer-Vision-Projects`.
3. Choose Public or Private according to your assignment instructions.
4. Extract this ZIP on your computer.
5. Upload the extracted files using **Add file → Upload files**, or use Git:

```bash
git init
git add .
git commit -m "Add five computer vision project scaffolds"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Computer-Vision-Projects.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Verify all five folders appear online.

Before submission, implement and run each project, add real screenshots/results, evaluate against matched ground-truth labels, and replace placeholders with measured findings.
