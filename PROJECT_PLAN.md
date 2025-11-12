# Multimodal Data Preprocessing - Project Plan

## Team Members

- Mitali
- Blessing
- Liliane
- Mwai

## Project Goal

Build a User Identity and Product Recommendation System with multi-modal authentication:

1. Face Recognition (Image-based)
2. Voice Verification (Audio-based)
3. Product Recommendation (Tabular data)

---

## Workflow

### Phase 1: Data Collection & Preparation

**Duration:** Day 1

#### Task 1: Tabular Data (ALL)

- [ ] Download customer_social_profiles.csv and customer_transactions.csv
- [ ] Perform EDA (statistics, distributions, correlations)
- [ ] Clean data (handle nulls, duplicates, data types)
- [ ] Merge datasets with justified join logic
- [ ] Feature engineering for product prediction
- [ ] Save merged dataset to `data/processed/merged_customer_data.csv`

#### Task 2: Image Data (EACH MEMBER)

- [ ] **Mitali**: Submit 3 images (neutral, smile, surprised)
- [ ] **Blessing**: Submit 3 images (neutral, smile, surprised)
- [ ] **Liliane**: Submit 3 images (neutral, smile, surprised)
- [ ] **Mwai**: Submit 3 images (neutral, smile, surprised)
- [ ] Save to `data/images/{name}_{expression}.jpg`

#### Task 3: Audio Data (EACH MEMBER)

- [ ] **Mitali**: Record 2 phrases ("Yes, approve", "Confirm transaction")
- [ ] **Blessing**: Record 2 phrases
- [ ] **Liliane**: Record 2 phrases
- [ ] **Mwai**: Record 2 phrases
- [ ] Save to `data/audio/{name}_{phrase}.wav`

---

### Phase 2: Data Processing & Feature Extraction

**Duration:** Day 1-2

#### Image Processing (ALL - Collaborative)

- [ ] Load and display all images
- [ ] Apply ≥2 augmentations per image (rotation, flip, brightness, grayscale)
- [ ] Extract features (use CNN embeddings or color histograms)
- [ ] Save to `data/processed/image_features.csv`
  - Columns: `member_name`, `expression`, `feature_1`, ..., `feature_n`, `label`

#### Audio Processing (ALL - Collaborative)

- [ ] Load and visualize waveforms
- [ ] Create spectrograms
- [ ] Apply ≥2 augmentations (pitch shift, time stretch, noise)
- [ ] Extract MFCCs, spectral roll-off, energy
- [ ] Save to `data/processed/audio_features.csv`
  - Columns: `member_name`, `phrase`, `mfcc_1`, ..., `mfcc_n`, `spectral_rolloff`, `energy`, `label`

---

### Phase 3: Model Development

**Duration:** Day 2

#### Model 1: Facial Recognition (Mitali & Blessing)

- [ ] Train classifier on `image_features.csv`
- [ ] Models to try: Random Forest, XGBoost, Logistic Regression
- [ ] Evaluate: Accuracy, F1-Score, Confusion Matrix
- [ ] Save model to `models/face_recognition_model.pkl`

#### Model 2: Voice Verification (Liliane & Mwai)

- [ ] Train classifier on `audio_features.csv`
- [ ] Models to try: Random Forest, XGBoost, SVM
- [ ] Evaluate: Accuracy, F1-Score, Confusion Matrix
- [ ] Save model to `models/voice_verification_model.pkl`

#### Model 3: Product Recommendation (ALL)

- [ ] Train predictor on merged tabular data
- [ ] Predict product category/type
- [ ] Evaluate: Accuracy, F1-Score, Loss
- [ ] Save model to `models/product_recommendation_model.pkl`

---

### Phase 4: System Integration

**Duration:** Day 3

#### CLI Application (ALL - Collaborative)

- [ ] Create `src/main.py` - Command-line interface
- [ ] Implement flow:
  1. Load face image → Facial Recognition
  2. If authorized → Load voice audio → Voice Verification
  3. If verified → Request customer data → Product Prediction
  4. Display result or "Access Denied"
- [ ] Test with authorized users
- [ ] Test with unauthorized samples (fake face/voice)

---

### Phase 5: Documentation & Submission

**Duration:** Day 3

- [ ] Create detailed report (`reports/final_report.pdf`)
- [ ] Record system demonstration video
- [ ] Document individual contributions
- [ ] Finalize GitHub repository
- [ ] Submit all deliverables

---

## Deliverables Checklist

### Data Files

- [ ] `data/raw/customer_social_profiles.csv`
- [ ] `data/raw/customer_transactions.csv`
- [ ] `data/processed/merged_customer_data.csv`
- [ ] `data/processed/image_features.csv`
- [ ] `data/processed/audio_features.csv`
- [ ] `data/images/` (12 images total)
- [ ] `data/audio/` (8 audio files total)

### Code Files

- [ ] `notebooks/01_data_merge_eda.ipynb`
- [ ] `notebooks/02_image_processing.ipynb`
- [ ] `notebooks/03_audio_processing.ipynb`
- [ ] `notebooks/04_model_training.ipynb`
- [ ] `src/main.py` (CLI application)
- [ ] `src/face_recognition.py`
- [ ] `src/voice_verification.py`
- [ ] `src/product_recommendation.py`
- [ ] `src/utils.py`

### Models

- [ ] `models/face_recognition_model.pkl`
- [ ] `models/voice_verification_model.pkl`
- [ ] `models/product_recommendation_model.pkl`

### Documentation

- [ ] `reports/final_report.pdf`
- [ ] `README.md` (with setup instructions)
- [ ] System demo video link
- [ ] Team contributions document

---

## Suggested Division of Work

### Mitali

- Lead: Tabular data merge & EDA
- Support: Image processing & CLI integration

### Blessing

- Lead: Image collection & facial recognition model
- Support: Product recommendation model

### Liliane

- Lead: Audio processing & feature extraction
- Support: Voice verification model

### Mwai

- Lead: Voice verification model
- Support: CLI application & system integration

**Note:** All members contribute to data collection (images & audio) and review all components.

---

## Next Steps

1. **Get dataset links** from instructor
2. **Set up GitHub repository** and invite team members
3. **Install required packages**: `pip install -r requirements.txt`
4. **Collect personal data**: Each member submits images + audio
5. **Start with Task 1**: Data merge and EDA

---

## Communication

- Use GitHub Issues for task tracking
- Regular team meetings (2x per week)
- Code reviews before merging
- Document decisions in commit messages
