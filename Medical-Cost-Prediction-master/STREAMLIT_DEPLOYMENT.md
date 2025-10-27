# 🚀 Streamlit Deployment Guide

## Overview
This guide will help you deploy the Medical Insurance Cost Prediction app on Streamlit Cloud (completely FREE).

---

## Step 1: Prerequisites
- ✅ Python 3.8 or higher
- ✅ Git account (for GitHub)
- ✅ GitHub repository (your code)
- ✅ Streamlit account (free)

---

## Step 2: Prepare Your Repository

### 2.1 Push to GitHub
1. Create a new repository on GitHub (e.g., `Medical-Cost-Prediction`)
2. Push your project files including:
   - `streamlit_app.py` ← **Main app file**
   - `rf_tuned.pkl` ← **Model file**
   - `requirements_streamlit.txt` ← **Dependencies**
   - `.streamlit/config.toml` ← **Configuration**

```bash
git init
git add .
git commit -m "Initial commit - Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2.2 Ensure File Structure
```
your-repo/
├── streamlit_app.py           # Main Streamlit app
├── rf_tuned.pkl               # Pre-trained model
├── requirements_streamlit.txt # Dependencies
├── .streamlit/
│   └── config.toml           # Streamlit config
├── README.md                  # Project description
└── insurance.csv             # Dataset (optional)
```

---

## Step 3: Create Streamlit Account

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **Sign up** (use your GitHub account)
3. Authorize Streamlit to access your GitHub repositories
4. Verify your email

---

## Step 4: Deploy on Streamlit Cloud

### 4.1 Create New App
1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Click **"Create app"** button
3. Select:
   - **Repository**: `YOUR_USERNAME/Medical-Cost-Prediction`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`

### 4.2 Configure & Deploy
4. Click **"Deploy"**
5. Wait for deployment (2-5 minutes)
6. Your app will be live at: `https://your-username-medical-cost-prediction.streamlit.app`

---

## Step 5: Run Locally (Before Deployment)

Test your app locally before deploying:

```bash
# Install dependencies
pip install -r requirements_streamlit.txt

# Run the app
streamlit run streamlit_app.py
```

Your local app will open at: `http://localhost:8501`

---

## Step 6: Update & Redeploy

### To update your app:
1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Updated features"
   git push
   ```
3. Streamlit Cloud automatically redeploys! ✨

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Make sure `requirements_streamlit.txt` includes all dependencies

### Issue: "FileNotFoundError: rf_tuned.pkl not found"
**Solution**: 
- Ensure `rf_tuned.pkl` is in the same directory as `streamlit_app.py`
- Push the file to GitHub (it may be large, ~50MB+)

### Issue: App loads slowly or times out
**Solution**: 
- Use `@st.cache_resource` decorator for model loading (already done ✅)
- Model is loaded once and reused

### Issue: Model file too large for GitHub
**Solution**: Use Git LFS (Large File Storage)
```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes *.pkl
git commit -m "Add large model file"
git push
```

---

## Performance Tips

✅ **Already Implemented:**
- Model caching with `@st.cache_resource`
- Efficient NumPy operations
- Streamlined UI with 2-column layout

✅ **Additional Tips:**
- Use `st.cache_data` for datasets
- Minimize external API calls
- Optimize images/media

---

## Free Tier Limitations

- ✅ 1GB deployment limit (model should fit)
- ✅ 1 GB of memory per app
- ✅ 1 CPU
- ✅ **No credit card required**
- ✅ Unlimited apps

---

## Alternative Deployment Options

If Streamlit Cloud doesn't work:

1. **Heroku** (Deploy with Procfile)
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

2. **PythonAnywhere** - Simple Python hosting

3. **AWS/Azure/GCP** - More advanced options

---

## Support & Resources

- 📚 [Streamlit Docs](https://docs.streamlit.io/)
- 💬 [Streamlit Community](https://discuss.streamlit.io/)
- 🐛 [GitHub Issues](https://github.com/streamlit/streamlit/issues)

---

## Success Checklist

- [ ] Code pushed to GitHub
- [ ] All files in repository (streamlit_app.py, rf_tuned.pkl, requirements_streamlit.txt)
- [ ] Streamlit Cloud account created
- [ ] App deployed
- [ ] App link shared with others
- [ ] App tested and working

---

**You're ready to deploy! 🎉**

Questions? Check the troubleshooting section above.