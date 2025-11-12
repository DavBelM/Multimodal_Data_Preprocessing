# Approach Discussion: Multimodal Data Preprocessing Assignment

## Quick Summary

**Team:** Mitali, Blessing, Liliane, Mwai  
**Project:** User Identity & Product Recommendation System  
**Components:** Facial Recognition + Voice Verification + Product Recommendation

---

## 🎯 STREAMLINED ACTION PLAN

### **Phase 1: IMMEDIATE (Do Now - No Dependencies)**

#### **ALL 4 MEMBERS (Parallel - Start Today)**

1. **Clone repo & create your branch:**

```bash
git clone https://github.com/DavBelM/Multimodal_Data_Preprocessing.git
cd Multimodal_Data_Preprocessing
git checkout -b feature/your-name
```

2. **Take 3 photos of yourself:**

   - `{yourname}_neutral.jpg`
   - `{yourname}_smile.jpg`
   - `{yourname}_surprised.jpg`
   - Save to `data/images/`

3. **Record 2 audio clips:**

   - `{yourname}_approve.wav` - Say "Yes, approve"
   - `{yourname}_confirm.wav` - Say "Confirm transaction"
   - Save to `data/audio/`

4. **Push your personal data:**

```bash
git add data/images/{yourname}_*.jpg data/audio/{yourname}_*.wav
git commit -m "Add personal images and audio for {yourname}"
git push origin feature/your-name
```

**⏱️ Deadline: By tomorrow**

---

### **Phase 2: DATA PREP (Sequential - Needs datasets)**

#### **MITALI - Acts FIRST** ⭐

**Branch:** `feature/data-merge`  
**Wait for:** Dataset links from instructor

**Tasks:**

1. Download datasets to `data/raw/`:
   - `customer_social_profiles.csv`
   - `customer_transactions.csv`
2. Complete `notebooks/01_data_merge_eda.ipynb`:
   - EDA with 3+ plots
   - Clean data
   - Merge datasets
   - Engineer features
   - Save `data/processed/merged_customer_data.csv`
3. Push to your branch, create PR

**⏱️ Time: 2-3 days**

---

#### **BLESSING - Acts SECOND** (Waits for images)

**Branch:** `feature/image-processing`  
**Wait for:** All team members upload their 12 images total

**Tasks:**

1. Create `notebooks/02_image_processing.ipynb`
2. Load all 12 team images
3. Apply 2+ augmentations per image
4. Extract features (CNN embeddings or histograms)
5. Save `data/processed/image_features.csv`
6. Push branch, create PR

**⏱️ Time: 2-3 days**

---

#### **LILIANE - Acts SECOND** (Waits for audio)

**Branch:** `feature/audio-processing`  
**Wait for:** All team members upload their 8 audio files total

**Tasks:**

1. Create `notebooks/03_audio_processing.ipynb`
2. Load all 8 audio files
3. Display waveforms + spectrograms
4. Apply 2+ augmentations per audio
5. Extract MFCCs, spectral roll-off, energy
6. Save `data/processed/audio_features.csv`
7. Push branch, create PR

**⏱️ Time: 2-3 days**

---

### **Phase 3: MODELS (Parallel - After Phase 2)**

#### **BLESSING - Facial Recognition**

**Branch:** `feature/face-model`  
**Wait for:** `image_features.csv` exists

**Tasks:**

1. Train facial recognition model (Random Forest/XGBoost)
2. Evaluate: Accuracy, F1-score
3. Save `models/face_recognition_model.pkl`
4. Create `src/face_recognition.py`

**⏱️ Time: 1-2 days**

---

#### **MWAI - Voice Verification**

**Branch:** `feature/voice-model`  
**Wait for:** `audio_features.csv` exists

**Tasks:**

1. Train voice verification model (Random Forest/SVM)
2. Evaluate: Accuracy, F1-score
3. Save `models/voice_verification_model.pkl`
4. Create `src/voice_verification.py`

**⏱️ Time: 1-2 days**

---

#### **MITALI & MWAI - Product Recommendation**

**Branch:** `feature/product-model`  
**Wait for:** `merged_customer_data.csv` exists

**Tasks:**

1. Train product prediction model (XGBoost/Logistic Regression)
2. Evaluate: Accuracy, F1-score, Loss
3. Save `models/product_recommendation_model.pkl`
4. Create `src/product_recommendation.py`

**⏱️ Time: 1-2 days**

---

### **Phase 4: INTEGRATION (Sequential - After all models)**

#### **MWAI - CLI Application**

**Branch:** `feature/cli-app`  
**Wait for:** All 3 models exist

**Tasks:**

1. Create `src/main.py` - command-line app
2. Implement flow: Face → Voice → Product
3. Add "Access Denied" logic
4. Test with all team members + fake data
5. Push branch, create PR

**⏱️ Time: 2 days**

---

### **Phase 5: DOCUMENTATION (Parallel - Final week)**

#### **ALL MEMBERS**

- **Mitali:** Final report writing
- **Blessing:** Video recording/editing
- **Liliane:** README updates
- **Mwai:** GitHub repo cleanup

**⏱️ Time: 2-3 days**

---

## 📊 Critical Path (Who Blocks Who)

```
START → ALL (photos/audio) → Blessing (images) → Face Model
                           → Liliane (audio) → Voice Model
      → Mitali (data merge) → Product Model

ALL MODELS DONE → Mwai (CLI) → Documentation → SUBMIT
```

---

## 🌿 Branch Strategy

```bash
# Main branch (protected)
main

# Feature branches (create your own)
feature/mitali        # Mitali's personal data
feature/blessing      # Blessing's personal data
feature/liliane       # Liliane's personal data
feature/mwai          # Mwai's personal data

feature/data-merge    # Mitali
feature/image-processing  # Blessing
feature/audio-processing  # Liliane
feature/face-model    # Blessing
feature/voice-model   # Mwai
feature/product-model # Mitali + Mwai
feature/cli-app       # Mwai
```

**Merge strategy:** Each person creates PR → 1 other person reviews → Merge to main

---

## 🚨 Critical Dependencies

**BLOCKER 1:** No datasets = Can't start data merge  
**BLOCKER 2:** No images = Can't start image processing  
**BLOCKER 3:** No audio = Can't start audio processing  
**BLOCKER 4:** No models = Can't start CLI

**Solution:** Everyone does personal data collection NOW while waiting for datasets.

---

## 📞 Sync Points

- **Meeting 1:** After everyone uploads personal data
- **Meeting 2:** After data merge done (Mitali notifies)
- **Meeting 3:** After all models trained
- **Meeting 4:** After CLI built (final testing)

---

## ✅ MITALI'S IMMEDIATE TODO

1. **Today:**

   - Take your 3 photos, record 2 audios
   - Create branch: `git checkout -b feature/mitali`
   - Upload your files
   - Push branch

2. **Get dataset links from instructor** (THIS IS BLOCKING)

3. **Once you have datasets:**

   - Create branch: `git checkout -b feature/data-merge`
   - Complete EDA notebook
   - Push & create PR
   - Notify team: "Data merge done, you can start processing"

4. **After Blessing & Liliane finish:**
   - Work with Mwai on product model

---

---

## 📋 Technical Requirements Summary

### Data Collection

**Images:** Each member needs 3 photos

- Neutral, Smile, Surprised
- Format: JPG/PNG, consistent lighting
- Naming: `{name}_neutral.jpg`, `{name}_smile.jpg`, `{name}_surprised.jpg`

**Audio:** Each member records 2 phrases

- "Yes, approve" + "Confirm transaction"
- Format: WAV (16kHz or 44.1kHz)
- Naming: `{name}_approve.wav`, `{name}_confirm.wav`

### Models to Use

- **Facial Recognition:** Random Forest or XGBoost
- **Voice Verification:** Random Forest or SVM
- **Product Recommendation:** XGBoost or Logistic Regression

### Image Processing Requirements

- **≥2 augmentations:** rotation, flip, brightness, grayscale
- **Features:** CNN embeddings OR color histograms
- **Output:** `image_features.csv`

### Audio Processing Requirements

- **≥2 augmentations:** pitch shift, time stretch, noise
- **Features:** MFCCs, spectral roll-off, energy
- **Visualizations:** Waveforms + Spectrograms
- **Output:** `audio_features.csv`

### Evaluation Metrics (All Models)

- Accuracy
- F1-Score
- Confusion Matrix
- Loss (where applicable)

---

## 📈 Rubric Points to Maximize (40 Points Total)

| Criteria              | Points | Requirements for Full Credit                  |
| --------------------- | ------ | --------------------------------------------- |
| EDA Quality           | 4      | ≥3 labeled plots, statistics, insights        |
| Data Cleaning & Merge | 4      | Nulls handled, join justified, validated      |
| Image Quantity        | 4      | All 4 members × 3 expressions = 12 images     |
| Image Augmentation    | 4      | ≥2 augmentations, features in CSV             |
| Audio Quality         | 4      | 8 clean recordings, waveform + spectrogram    |
| Audio Augmentation    | 4      | ≥2 augmentations, MFCCs + features in CSV     |
| Model Implementation  | 4      | All 3 models trained and functional           |
| Evaluation & Logic    | 4      | Metrics for each model, multimodal flow clear |
| System Simulation     | 4      | Full demo + unauthorized attempts             |
| Submission Quality    | 4      | Clean code, documentation, organized repo     |

**Target: 38-40 points**

---

## 🗣️ Communication & Collaboration

### When to Sync

- **After Phase 1:** Everyone has uploaded personal data
- **After Phase 2:** Mitali completes data merge
- **After Phase 3:** All models trained
- **Before Submission:** Final testing complete

### GitHub Workflow

```bash
# Each person works on their branch
git checkout -b feature/your-task
# Make changes
git add .
git commit -m "Descriptive message"
git push origin feature/your-task
# Create Pull Request on GitHub
# Get 1 team member to review
# Merge to main
```

---

## 💡 Quick Reference

### Installation

```bash
pip install -r requirements.txt
```

### Project Structure

```
data/
  raw/           ← Place datasets here
  processed/     ← Generated CSVs
  images/        ← 12 team photos
  audio/         ← 8 team recordings
notebooks/       ← Jupyter notebooks (4 total)
src/             ← Python scripts
models/          ← Trained models (.pkl files)
```

### Key Files to Generate

1. `data/processed/merged_customer_data.csv`
2. `data/processed/image_features.csv`
3. `data/processed/audio_features.csv`
4. `models/face_recognition_model.pkl`
5. `models/voice_verification_model.pkl`
6. `models/product_recommendation_model.pkl`
7. `src/main.py` (CLI application)

---

## 🎬 Final Deliverables

- [ ] GitHub repository with all code
- [ ] 4 Jupyter notebooks (EDA, image, audio, models)
- [ ] 3 trained models
- [ ] CLI application working
- [ ] Video demonstration (authorized + unauthorized attempts)
- [ ] Final report (PDF)
- [ ] Team contributions documented

---

_Document created: November 11, 2025_  
_Team: Mitali, Blessing, Liliane, Mwai_
