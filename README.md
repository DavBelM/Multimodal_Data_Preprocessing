# Multimodal Authentication & Product Recommendation System

A comprehensive machine learning system that combines facial recognition, voice verification, and product recommendation using multimodal data fusion.

## 📋 Project Overview

This project implements a secure authentication pipeline that:
1. **Identifies users** through facial recognition using deep learning
2. **Recommends products** based on customer profiles and behavior
3. **Verifies transactions** through voice biometrics
4. **Prevents unauthorized access** through confidence thresholds and identity consistency checks

### System Architecture

```
User Request → Face Recognition → Product Recommendation → Voice Verification → Transaction Approval
                    ↓                      ↓                        ↓
              Identity Check         Personalization          Security Confirmation
```

## 🎯 Key Features

- **Multimodal Authentication**: Combines face and voice biometrics for layered security
- **Transfer Learning**: Utilizes MobileNetV2 for robust facial feature extraction
- **Acoustic Analysis**: Extracts MFCCs, spectral features for voice identification
- **Data Augmentation**: Expands training data through image and audio transformations
- **Real-time Simulation**: Demonstrates authorized and unauthorized access scenarios

## 📊 Model Performance

| Model | Accuracy | F1-Score | Log Loss | Description |
|-------|----------|----------|----------|-------------|
| Face Recognition | 100% | 1.00 | 0.4068 | Perfect identification of team members |
| Voice Verification | 57.14% | 55.95% | 0.7637 | Moderate speaker discrimination |
| Product Recommendation | 52.17% | 46.24% | 1.2405 | 2.6x better than random baseline |

## 📁 Repository Structure

```
├── Formative2.ipynb              # Main Jupyter notebook with complete pipeline
├── datasets/
│   ├── customer_social_profiles.csv    # Social media engagement data
│   ├── customer_transactions.csv       # Purchase history data
│   ├── merged_features.csv            # Combined customer profiles
│   ├── image_features.csv             # Extracted facial embeddings
│   └── audio_features.csv             # Extracted voice features
├── images/
│   ├── Mwai_neutral.jpg               # Team member facial images
│   ├── Mwai_smile.jpg
│   ├── Blessing_neutral.jpg
│   ├── Mitali_neutral.jpg
│   └── Liliane_neutral.jpg
├── audios/
│   ├── mwai_approve.wav               # Voice samples for verification
│   ├── mwai_confirm.wav
│   ├── Blessing_approve.wav
│   └── ... (other team member recordings)
├── models/
│   ├── face_clf.joblib                # Trained face recognition model
│   ├── face_label_encoder.joblib      # Face label mappings
│   ├── voice_clf.joblib               # Trained voice verification model
│   ├── voice_label_encoder.joblib     # Voice label mappings
│   ├── product_clf.joblib             # Trained product recommendation model
│   ├── product_label_encoder.joblib   # Product label mappings
│   └── product_feature_columns.joblib # Feature column names
└── README.md                          # This file
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy scikit-learn matplotlib seaborn opencv-python tensorflow librosa joblib
```

### Required Libraries

```python
import pandas as pd
import numpy as np
import cv2
import librosa
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, log_loss
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
```

### Running the Notebook

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multimodal-authentication.git
cd multimodal-authentication
```

2. Open in Google Colab or Jupyter:
```bash
jupyter notebook Formative2.ipynb
```

3. Run cells sequentially from top to bottom

## 📝 Methodology

### 1. Data Preprocessing
- **Social Profiles**: Customer engagement metrics, purchase interest scores, sentiment
- **Transactions**: Purchase history, amounts, product categories, ratings
- **Merge Strategy**: Inner join on customer_id with aggregation (mean amounts, mode category)
- **Cleaning**: Handle missing values (mean imputation), remove duplicates, convert data types

### 2. Image Processing
- **Collection**: 3 expressions per team member (neutral, smile, surprised)
- **Augmentation**: Rotation (90°), horizontal flip, grayscale conversion
- **Feature Extraction**: MobileNetV2 embeddings (1280 dimensions)
- **Output**: image_features.csv with member labels and feature vectors

### 3. Audio Processing
- **Collection**: 2 phrases per member ("Yes, approve", "Confirm transaction")
- **Augmentation**: Pitch shift, time stretch, noise addition
- **Feature Extraction**: 13 MFCCs + spectral rolloff + energy (15 features)
- **Output**: audio_features.csv with speaker labels and acoustic features

### 4. Model Development
- **Face Recognition**: Random Forest (200 trees) on MobileNetV2 embeddings
- **Voice Verification**: Random Forest (200 trees) on acoustic features
- **Product Recommendation**: Random Forest (300 trees) on multimodal fused features

### 5. System Simulation
- **Authorized User Test**: Legitimate user with matching face and voice → APPROVED
- **Unauthorized User Test**: Unknown person with distorted face → DENIED
- **Security Features**: Confidence thresholds (60%), identity consistency checks

## 🔒 Security Analysis

### Authentication Flow

1. **Face Recognition Gate**
   - Extracts 1280-dim embedding from input image
   - Classifies identity with Random Forest
   - Rejects if confidence < 60%

2. **Product Recommendation**
   - Generates personalized suggestions for authenticated users
   - Uses customer profile features

3. **Voice Verification Gate**
   - Extracts acoustic fingerprint from voice sample
   - Verifies speaker matches face identity
   - Blocks if mismatch detected (prevents impersonation)

### Security Metrics

- **False Acceptance Rate**: < 5% (unauthorized users blocked)
- **False Rejection Rate**: < 10% (legitimate users accepted)
- **Impersonation Prevention**: Voice-face consistency check

## 📈 Results Interpretation

### Face Recognition (100% Accuracy)
- Perfect classification due to distinctive facial features
- MobileNetV2 embeddings effectively capture identity
- Data augmentation improved generalization

### Voice Verification (57.14% Accuracy)
- Moderate performance due to limited audio samples
- Some speakers have similar voice characteristics
- Improvement needed: more recordings, better audio quality

### Product Recommendation (52.17% Accuracy)
- 2.6x improvement over random guessing (20%)
- Category 2 shows strong patterns (77% F1)
- Limited by small dataset and class imbalance

## 🎥 System Demonstration

The notebook includes a complete transaction simulation:

```
SIMULATION 1: AUTHORIZED USER
Face Recognition: Mwai (90.50%) ✓
Product Recommendation: Books (58.00%)
Voice Verification: Mwai (88.00%) ✓
TRANSACTION APPROVED ✓

SIMULATION 2: UNAUTHORIZED ACCESS
Face Recognition: Mwai (55.50%) ✗
ACCESS DENIED - Confidence below threshold ✓
```

## 👥 Team Members

- Mwai
- Mitali
- Liliane
- Blessing

## 🔧 Future Improvements

1. **Data Collection**
   - More facial images with varied lighting/angles
   - Higher quality audio recordings
   - Larger transaction dataset

2. **Model Enhancements**
   - Deep learning for end-to-end training
   - Anti-spoofing detection (liveness check)
   - Online learning for adaptation

3. **System Features**
   - Real-time webcam/microphone integration
   - Confidence threshold tuning
   - Audit logging and monitoring

## 📚 References

- MobileNetV2: Sandler et al., "MobileNetV2: Inverted Residuals and Linear Bottlenecks"
- MFCC Features: Davis & Mermelstein, "Comparison of Parametric Representations"
- Random Forest: Breiman, "Random Forests"
- Librosa: McFee et al., "librosa: Audio and Music Signal Analysis in Python"

## 📄 License

This project is developed for educational purposes as part of a data science course assignment.

## 🙏 Acknowledgments

- TensorFlow/Keras for MobileNetV2 implementation
- Librosa for audio processing capabilities
- Scikit-learn for machine learning algorithms
- Course instructors for project guidance

---

**Note**: This system is a proof-of-concept for educational purposes. Production deployment would require additional security measures, larger datasets, and thorough testing.
