# Multimodal Data Preprocessing: User Identity & Product Recommendation System

A comprehensive machine learning system that combines facial recognition, voice verification, and product recommendation using multimodal data preprocessing techniques.

## 👥 Team Members

- **Mitali** - Tabular Data & Integration
- **Blessing** - Image Processing & Facial Recognition
- **Liliane** - Audio Processing
- **Mwai** - Voice Verification & CLI Development

## 📋 Project Overview

This system implements a three-tier authentication and recommendation pipeline:

1. **Facial Recognition** - Verifies user identity through image analysis
2. **Voice Verification** - Confirms authorization through voice analysis
3. **Product Recommendation** - Predicts product preferences based on customer data

### System Flow

```
User Input (Face Image)
    → Facial Recognition Model
        → ✅ Authorized: Proceed to Voice Verification
        → ❌ Denied: Access Denied
            → Voice Input (Audio Sample)
                → Voice Verification Model
                    → ✅ Verified: Proceed to Prediction
                    → ❌ Denied: Access Denied
                        → Product Recommendation Model
                            → Display Recommended Product
```

## 🗂️ Project Structure

```
Multimodal_Data_Preprocessing/
├── data/
│   ├── raw/                          # Original datasets
│   │   ├── customer_social_profiles.csv
│   │   └── customer_transactions.csv
│   ├── processed/                    # Processed features
│   │   ├── merged_customer_data.csv
│   │   ├── image_features.csv
│   │   └── audio_features.csv
│   ├── images/                       # Facial images (12 total)
│   │   ├── mitali_neutral.jpg
│   │   ├── mitali_smile.jpg
│   │   ├── mitali_surprised.jpg
│   │   └── ... (for each member)
│   └── audio/                        # Voice samples (8 total)
│       ├── mitali_approve.wav
│       ├── mitali_confirm.wav
│       └── ... (for each member)
├── notebooks/
│   ├── 01_data_merge_eda.ipynb      # EDA & data merging
│   ├── 02_image_processing.ipynb     # Image augmentation & features
│   ├── 03_audio_processing.ipynb     # Audio augmentation & features
│   └── 04_model_training.ipynb       # Model training & evaluation
├── src/
│   ├── main.py                       # CLI application
│   ├── face_recognition.py           # Facial recognition module
│   ├── voice_verification.py         # Voice verification module
│   ├── product_recommendation.py     # Product prediction module
│   └── utils.py                      # Helper functions
├── models/
│   ├── face_recognition_model.pkl
│   ├── voice_verification_model.pkl
│   └── product_recommendation_model.pkl
├── reports/
│   └── final_report.pdf
├── requirements.txt
├── PROJECT_PLAN.md
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/DavBelM/Multimodal_Data_Preprocessing.git
cd Multimodal_Data_Preprocessing
```

2. **Create virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate   # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download datasets**
   Place the following files in `data/raw/`:

- `customer_social_profiles.csv`
- `customer_transactions.csv`

## 📊 Usage

### 1. Data Preprocessing

Run the Jupyter notebooks in order:

```bash
jupyter notebook notebooks/01_data_merge_eda.ipynb
```

### 2. Feature Extraction

Process images and audio:

```bash
jupyter notebook notebooks/02_image_processing.ipynb
jupyter notebook notebooks/03_audio_processing.ipynb
```

### 3. Model Training

Train all three models:

```bash
jupyter notebook notebooks/04_model_training.ipynb
```

### 4. Run the System

Execute the command-line application:

```bash
python src/main.py
```

Follow the prompts to:

- Upload a face image
- Provide a voice sample
- Receive product recommendations

## 🎯 Features

### Image Processing

- ✅ Multiple facial expressions (neutral, smile, surprised)
- ✅ Augmentations: rotation, flipping, grayscale, brightness adjustment
- ✅ Feature extraction: CNN embeddings / color histograms
- ✅ 12 total images (3 per team member)

### Audio Processing

- ✅ Voice command recognition ("Yes, approve", "Confirm transaction")
- ✅ Augmentations: pitch shift, time stretch, background noise
- ✅ Feature extraction: MFCCs, spectral roll-off, energy
- ✅ Waveform and spectrogram visualization
- ✅ 8 total audio samples (2 per team member)

### Models

- **Facial Recognition**: Classifies team members from face images
- **Voice Verification**: Authenticates authorized voice samples
- **Product Recommendation**: Predicts customer purchase preferences

### Evaluation Metrics

- Accuracy
- F1-Score
- Confusion Matrix
- Loss (for regression tasks)

## 📈 Model Performance

| Model                  | Accuracy | F1-Score | Notes                         |
| ---------------------- | -------- | -------- | ----------------------------- |
| Facial Recognition     | TBD      | TBD      | Random Forest / XGBoost       |
| Voice Verification     | TBD      | TBD      | Random Forest / SVM           |
| Product Recommendation | TBD      | TBD      | Logistic Regression / XGBoost |

_(To be updated after training)_

## 🎥 Demo

📹 **System Demonstration Video**: [Link to be added]

The demo includes:

1. Authorized user transaction (full flow)
2. Unauthorized face attempt (denied)
3. Unauthorized voice attempt (denied)

## 🤝 Contributing

### Team Workflow

1. Create feature branch: `git checkout -b feature/your-feature-name`
2. Commit changes: `git commit -m "Add feature description"`
3. Push to branch: `git push origin feature/your-feature-name`
4. Create Pull Request for team review

### Code Standards

- Follow PEP 8 for Python code
- Add docstrings to functions
- Comment complex logic
- Update README for major changes

## 📚 Resources

- **Dataset Source**: [Links to be added]
- **Project Plan**: See `PROJECT_PLAN.md`
- **Final Report**: See `reports/final_report.pdf`

## 📝 License

This project is part of an academic assignment.

## 🙏 Acknowledgments

- Course Instructor
- Team Members: Mitali, Blessing, Liliane, Mwai

---

**Last Updated**: November 11, 2025
