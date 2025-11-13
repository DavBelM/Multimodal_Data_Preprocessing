"""
Utility functions for the CLI authentication system

This module provides helper functions for:
- Loading trained models
- Processing face images
- Processing voice recordings
- Making product predictions
- UI utilities
"""

import os
import sys
import time
import numpy as np
import pandas as pd
from pathlib import Path


# ANSI color codes for terminal output
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}


def print_colored(text, color='white', bold=False):
    """
    Print colored text to terminal
    
    Args:
        text: Text to print
        color: Color name (red, green, yellow, blue, magenta, cyan, white)
        bold: Whether to make text bold
    """
    color_code = COLORS.get(color, COLORS['white'])
    bold_code = COLORS['bold'] if bold else ''
    reset_code = COLORS['reset']
    
    print(f"{bold_code}{color_code}{text}{reset_code}")


def display_banner():
    """Display the application banner"""
    os.system('clear' if os.name != 'nt' else 'cls')
    
    print_colored("="*70, "cyan")
    print_colored("MULTIMODAL AUTHENTICATION SYSTEM", "cyan", bold=True)
    print_colored("="*70, "cyan")
    print_colored("\nThree-Tier Security System:", "white", bold=True)
    print("  Tier 1: Facial Recognition")
    print("  Tier 2: Voice Verification")
    print("  Tier 3: Product Recommendation")
    print_colored("\n" + "="*70, "cyan")


def simulate_processing(message, duration=1.0, steps=3):
    """
    Simulate processing with animated dots
    
    Args:
        message: Message to display
        duration: Total duration in seconds
        steps: Number of animation steps
    """
    step_duration = duration / steps
    for i in range(steps):
        dots = "." * (i + 1)
        print(f"\r{message}{dots}   ", end='', flush=True)
        time.sleep(step_duration)
    print(f"\r{message}... Done!", flush=True)


def load_models():
    """
    Load all trained models from the models directory
    
    Returns:
        dict: Dictionary containing loaded models
    """
    models = {
        'face_model': None,
        'voice_model': None,
        'product_model': None
    }
    
    project_root = Path(__file__).parent.parent
    models_dir = project_root / 'models'
    
    # Check if models directory exists
    if not models_dir.exists():
        print_colored("Warning: Models directory not found. Using mock models.", "yellow")
        return _load_mock_models()
    
    # Try to load face recognition model
    face_model_path = models_dir / 'face_recognition_model.pkl'
    if face_model_path.exists():
        try:
            import joblib
            models['face_model'] = joblib.load(face_model_path)
            print_colored("  - Face recognition model loaded", "green")
        except Exception as e:
            print_colored(f"  - Warning: Could not load face model: {e}", "yellow")
    else:
        print_colored("  - Face model not found, using mock", "yellow")
    
    # Try to load voice verification model
    voice_model_path = models_dir / 'voice_verification_model.pkl'
    if voice_model_path.exists():
        try:
            import joblib
            models['voice_model'] = joblib.load(voice_model_path)
            print_colored("  - Voice verification model loaded", "green")
        except Exception as e:
            print_colored(f"  - Warning: Could not load voice model: {e}", "yellow")
    else:
        print_colored("  - Voice model not found, using mock", "yellow")
    
    # Try to load product recommendation model
    product_model_path = models_dir / 'product_recommendation_model.pkl'
    if product_model_path.exists():
        try:
            import joblib
            models['product_model'] = joblib.load(product_model_path)
            print_colored("  - Product recommendation model loaded", "green")
        except Exception as e:
            print_colored(f"  - Warning: Could not load product model: {e}", "yellow")
    else:
        print_colored("  - Product model not found, using mock", "yellow")
    
    # If no models loaded, use mock models
    if all(model is None for model in models.values()):
        print_colored("\nNo trained models found. Using mock models for demonstration.", "yellow")
        return _load_mock_models()
    
    return models


def _load_mock_models():
    """
    Create mock models for demonstration purposes
    
    Returns:
        dict: Dictionary with mock model objects
    """
    return {
        'face_model': 'MOCK_FACE_MODEL',
        'voice_model': 'MOCK_VOICE_MODEL',
        'product_model': 'MOCK_PRODUCT_MODEL'
    }


def verify_face(model, image_path):
    """
    Verify face using the face recognition model
    
    Args:
        model: Trained face recognition model
        image_path: Path to the face image
        
    Returns:
        tuple: (success, user_name, confidence)
    """
    # If using mock model, simulate recognition
    if model == 'MOCK_FACE_MODEL':
        return _mock_face_verification(image_path)
    
    # TODO: Implement actual face recognition when model is ready
    # This will be filled in once Task 2 and Task 4 are complete
    try:
        # Load and preprocess image
        # Extract features
        # Make prediction
        # Return results
        pass
    except Exception as e:
        raise Exception(f"Face verification error: {str(e)}")


def _mock_face_verification(image_path):
    """Mock face verification for demonstration"""
    filename = os.path.basename(image_path).lower()
    
    # Check if filename contains a known user name
    known_users = ['mitali', 'blessing', 'liliane', 'mwai']
    for user in known_users:
        if user in filename:
            confidence = np.random.uniform(0.85, 0.98)
            return True, user.capitalize(), confidence
    
    # Unknown face
    return False, None, 0.0


def verify_voice(model, audio_path, expected_user=None):
    """
    Verify voice using the voice verification model
    
    Args:
        model: Trained voice verification model
        audio_path: Path to the audio recording
        expected_user: Expected username for verification
        
    Returns:
        tuple: (success, predicted_user, confidence)
    """
    # If using mock model, simulate verification
    if model == 'MOCK_VOICE_MODEL':
        return _mock_voice_verification(audio_path, expected_user)
    
    # TODO: Implement actual voice verification when model is ready
    # This will be filled in once Task 3 and Task 4 are complete
    try:
        # Load and preprocess audio
        # Extract features (MFCCs, etc.)
        # Make prediction
        # Return results
        pass
    except Exception as e:
        raise Exception(f"Voice verification error: {str(e)}")


def _mock_voice_verification(audio_path, expected_user):
    """Mock voice verification for demonstration"""
    filename = os.path.basename(audio_path).lower()
    
    # Check if filename contains the expected user
    if expected_user and expected_user.lower() in filename:
        confidence = np.random.uniform(0.80, 0.95)
        return True, expected_user, confidence
    
    # Check if filename contains a known user name
    known_users = ['mitali', 'blessing', 'liliane', 'mwai']
    for user in known_users:
        if user in filename:
            confidence = np.random.uniform(0.70, 0.85)
            return True, user.capitalize(), confidence
    
    # Unknown voice
    return False, None, 0.0


def predict_product(model, user_name):
    """
    Predict product recommendation for authenticated user
    
    Args:
        model: Trained product recommendation model
        user_name: Authenticated username
        
    Returns:
        tuple: (success, product_category, confidence, details)
    """
    # If using mock model, simulate prediction
    if model == 'MOCK_PRODUCT_MODEL':
        return _mock_product_prediction(user_name)
    
    # TODO: Implement actual product recommendation when model is ready
    # This will be filled in once Task 4 is complete
    try:
        # Load user data from merged dataset
        # Make prediction
        # Return results with details
        pass
    except Exception as e:
        raise Exception(f"Product prediction error: {str(e)}")


def _mock_product_prediction(user_name):
    """Mock product prediction for demonstration"""
    # Simulate product categories
    products = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports']
    product = np.random.choice(products)
    confidence = np.random.uniform(0.75, 0.92)
    
    # Simulate user details
    details = {
        'Engagement Score': np.random.randint(60, 95),
        'Purchase Interest': round(np.random.uniform(2.0, 5.0), 1),
        'Average Purchase': f"${np.random.randint(50, 300)}",
        'Social Platform': np.random.choice(['Facebook', 'Twitter', 'Instagram', 'LinkedIn'])
    }
    
    return True, product, confidence, details


def load_user_data(user_name):
    """
    Load user data from the merged dataset
    
    Args:
        user_name: Username to look up
        
    Returns:
        dict: User data or None if not found
    """
    project_root = Path(__file__).parent.parent
    data_path = project_root / 'data' / 'processed' / 'merged_customer_data.csv'
    
    if not data_path.exists():
        return None
    
    try:
        df = pd.read_csv(data_path)
        # TODO: Implement user lookup logic when data structure is finalized
        return None
    except Exception as e:
        print_colored(f"Error loading user data: {e}", "yellow")
        return None


def get_available_images():
    """Get list of available face images"""
    project_root = Path(__file__).parent.parent
    images_dir = project_root / 'data' / 'images'
    
    if not images_dir.exists():
        return []
    
    image_extensions = ['.jpg', '.jpeg', '.png']
    images = []
    
    for ext in image_extensions:
        images.extend(images_dir.glob(f'*{ext}'))
    
    return [str(img) for img in images]


def get_available_audio():
    """Get list of available audio recordings"""
    project_root = Path(__file__).parent.parent
    audio_dir = project_root / 'data' / 'audio'
    
    if not audio_dir.exists():
        return []
    
    audio_extensions = ['.wav', '.mp3', '.m4a', '.aac', '.flac']
    audio_files = []
    
    for ext in audio_extensions:
        audio_files.extend(audio_dir.glob(f'*{ext}'))
    
    return [str(audio) for audio in audio_files]
