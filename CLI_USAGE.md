# CLI System Test Script

## Quick Test

To test the CLI system with mock models:

```bash
# Make the script executable
chmod +x src/main.py

# Run the CLI
python3 src/main.py
```

## Menu Options

The CLI provides 4 options:

### 1. Authorized User Authentication
Runs the complete authentication flow:
- Tier 1: Face Recognition
- Tier 2: Voice Verification  
- Tier 3: Product Recommendation

You'll be prompted to enter:
- Path to face image (e.g., `data/images/Mitali_neutral.jpeg`)
- Path to voice recording (e.g., `data/audio/Mitali_approve.aac`)

### 2. Simulate Unauthorized Attempt
Demonstrates system security by showing how unauthorized access is blocked at Tier 1.

### 3. System Information
Displays system status and model information.

### 4. Exit
Closes the application.

## Testing with Actual Files

Once models are trained (Tasks 2-4 complete), you can test with real user data:

```bash
# Example for Mitali
Face Image: data/images/Mitali_neutral.jpeg
Voice Audio: data/audio/Mitali_approve.aac

# Example for Blessing
Face Image: data/images/Blessing_smile.jpeg
Voice Audio: data/audio/Blessing_confirm.aac

# Example for Liliane
Face Image: data/images/Liliane_surprised.jpeg
Voice Audio: data/audio/Liliane_approve.m4a
```

## Current Status

- CLI Skeleton: Complete
- Mock Models: Functional (for demonstration)
- Real Models: Pending (Tasks 2-4)

The system will automatically use mock models until real trained models are placed in the `models/` directory.

## Integration Points

When models are ready, they should be saved as:
- `models/face_recognition_model.pkl`
- `models/voice_verification_model.pkl`
- `models/product_recommendation_model.pkl`

The CLI will automatically detect and load them.
