# How to Push Event Management Project to GitHub

## Step-by-Step Guide

### Step 1: Initialize Git (if not already done)

```bash
git init
```

### Step 2: Add All Files to Git

```bash
git add .
```

This will add all files except those in `.gitignore`.

### Step 3: Make Your First Commit

```bash
git commit -m "Initial commit: Event Management System with PostgreSQL"
```

### Step 4: Add Your GitHub Repository as Remote

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/Event_Management_Project.git
```

**OR if you're using SSH:**

```bash
git remote add origin git@github.com:YOUR_USERNAME/Event_Management_Project.git
```

### Step 5: Check Your Remote (Optional)

```bash
git remote -v
```

This should show your repository URL.

### Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

If you get an error about the branch name, try:

```bash
git push -u origin master
```

## Complete Command Sequence

Copy and paste these commands one by one (replace YOUR_USERNAME):

```bash
# 1. Initialize git
git init

# 2. Add all files
git add .

# 3. Commit
git commit -m "Initial commit: Event Management System with PostgreSQL"

# 4. Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/Event_Management_Project.git

# 5. Push to GitHub
git branch -M main
git push -u origin main
```

## If You Get Authentication Errors

### Option 1: Use Personal Access Token (Recommended)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Copy the token
5. When prompted for password, paste the token instead

### Option 2: Use GitHub CLI

```bash
# Install GitHub CLI first, then:
gh auth login
```

### Option 3: Use SSH Keys

1. Generate SSH key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. Add to GitHub: Settings → SSH and GPG keys → New SSH key
3. Use SSH URL: `git@github.com:YOUR_USERNAME/Event_Management_Project.git`

## Verify Your Push

After pushing, check your GitHub repository:

- Go to: `https://github.com/YOUR_USERNAME/Event_Management_Project`
- You should see all your project files

## Future Updates

When you make changes and want to push updates:

```bash
git add .
git commit -m "Description of your changes"
git push
```

## Troubleshooting

### "Repository not found" error

- Check your repository name is correct
- Verify you have access to the repository
- Make sure the repository exists on GitHub

### "Authentication failed" error

- Use Personal Access Token instead of password
- Or set up SSH keys

### "Branch main does not exist" error

- Try: `git push -u origin master` instead
- Or create main branch on GitHub first
