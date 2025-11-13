#!/usr/bin/env python3
"""
Task 5: CLI System Simulation for Multimodal Authentication and Product Recommendation

This CLI application simulates a three-tier authentication system:
1. Face Recognition (Tier 1)
2. Voice Verification (Tier 2)
3. Product Recommendation (Tier 3)

Team Members: Mitali, Blessing, Liliane, Mwai
"""

import os
import sys
import time
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils import (
    load_models,
    verify_face,
    verify_voice,
    predict_product,
    display_banner,
    print_colored,
    simulate_processing
)


class MultimodalAuthSystem:
    """Main CLI application for multimodal authentication system"""
    
    def __init__(self):
        """Initialize the authentication system"""
        self.models = None
        self.authenticated_user = None
        
    def load_system(self):
        """Load all required models"""
        print_colored("\n" + "="*70, "cyan")
        print_colored("LOADING MULTIMODAL AUTHENTICATION SYSTEM", "cyan", bold=True)
        print_colored("="*70, "cyan")
        
        try:
            print("\nLoading models...")
            self.models = load_models()
            print_colored("System ready!", "green", bold=True)
            return True
        except Exception as e:
            print_colored(f"Error loading system: {str(e)}", "red", bold=True)
            return False
    
    def tier1_face_recognition(self, image_path=None):
        """
        Tier 1: Face Recognition
        
        Args:
            image_path: Path to user's face image
            
        Returns:
            tuple: (success, user_name)
        """
        print_colored("\n" + "="*70, "blue")
        print_colored("TIER 1: FACE RECOGNITION", "blue", bold=True)
        print_colored("="*70, "blue")
        
        if image_path is None:
            image_path = input("\nEnter path to your face image: ").strip()
        
        if not os.path.exists(image_path):
            print_colored(f"Error: Image not found at {image_path}", "red")
            return False, None
        
        print(f"\nProcessing face image: {os.path.basename(image_path)}")
        simulate_processing("Extracting facial features", duration=1.5)
        
        try:
            success, user_name, confidence = verify_face(self.models['face_model'], image_path)
            
            if success:
                print_colored(f"\nFace recognized: {user_name}", "green", bold=True)
                print(f"Confidence: {confidence:.2%}")
                return True, user_name
            else:
                print_colored("\nFace not recognized", "red", bold=True)
                print_colored("ACCESS DENIED", "red", bold=True)
                return False, None
                
        except Exception as e:
            print_colored(f"Error during face recognition: {str(e)}", "red")
            return False, None
    
    def tier2_voice_verification(self, audio_path=None, expected_user=None):
        """
        Tier 2: Voice Verification
        
        Args:
            audio_path: Path to user's voice recording
            expected_user: Username from face recognition
            
        Returns:
            bool: True if voice matches expected user
        """
        print_colored("\n" + "="*70, "yellow")
        print_colored("TIER 2: VOICE VERIFICATION", "yellow", bold=True)
        print_colored("="*70, "yellow")
        
        if audio_path is None:
            audio_path = input("\nEnter path to your voice recording: ").strip()
        
        if not os.path.exists(audio_path):
            print_colored(f"Error: Audio file not found at {audio_path}", "red")
            return False
        
        print(f"\nProcessing voice recording: {os.path.basename(audio_path)}")
        simulate_processing("Analyzing voice patterns", duration=2.0)
        
        try:
            success, predicted_user, confidence = verify_voice(
                self.models['voice_model'], 
                audio_path,
                expected_user
            )
            
            if success:
                print_colored(f"\nVoice verified: {predicted_user}", "green", bold=True)
                print(f"Confidence: {confidence:.2%}")
                return True
            else:
                print_colored("\nVoice verification failed", "red", bold=True)
                print_colored("ACCESS DENIED", "red", bold=True)
                return False
                
        except Exception as e:
            print_colored(f"Error during voice verification: {str(e)}", "red")
            return False
    
    def tier3_product_recommendation(self, user_name):
        """
        Tier 3: Product Recommendation
        
        Args:
            user_name: Authenticated username
            
        Returns:
            bool: True if recommendation successful
        """
        print_colored("\n" + "="*70, "magenta")
        print_colored("TIER 3: PRODUCT RECOMMENDATION", "magenta", bold=True)
        print_colored("="*70, "magenta")
        
        print(f"\nGenerating personalized recommendations for {user_name}...")
        simulate_processing("Analyzing purchase history and preferences", duration=1.5)
        
        try:
            success, product, confidence, details = predict_product(
                self.models['product_model'],
                user_name
            )
            
            if success:
                print_colored("\nRECOMMENDATION GENERATED", "green", bold=True)
                print_colored("="*70, "green")
                print(f"\nRecommended Product Category: {product}")
                print(f"Confidence: {confidence:.2%}")
                
                if details:
                    print("\nBased on your profile:")
                    for key, value in details.items():
                        print(f"  - {key}: {value}")
                
                return True
            else:
                print_colored("\nUnable to generate recommendation", "red")
                return False
                
        except Exception as e:
            print_colored(f"Error during product recommendation: {str(e)}", "red")
            return False
    
    def run_authentication_flow(self, image_path=None, audio_path=None):
        """
        Run the complete authentication flow
        
        Args:
            image_path: Optional path to face image
            audio_path: Optional path to voice recording
        """
        print_colored("\n" + "="*70, "cyan")
        print_colored("STARTING AUTHENTICATION SEQUENCE", "cyan", bold=True)
        print_colored("="*70, "cyan")
        
        # Tier 1: Face Recognition
        face_success, user_name = self.tier1_face_recognition(image_path)
        if not face_success:
            print_colored("\nAuthentication Failed at Tier 1", "red", bold=True)
            return False
        
        self.authenticated_user = user_name
        
        # Tier 2: Voice Verification
        voice_success = self.tier2_voice_verification(audio_path, user_name)
        if not voice_success:
            print_colored("\nAuthentication Failed at Tier 2", "red", bold=True)
            self.authenticated_user = None
            return False
        
        # Tier 3: Product Recommendation
        product_success = self.tier3_product_recommendation(user_name)
        
        # Final success message
        print_colored("\n" + "="*70, "green")
        print_colored("AUTHENTICATION COMPLETE", "green", bold=True)
        print_colored("="*70, "green")
        print_colored(f"\nWelcome, {user_name}!", "green", bold=True)
        
        return True
    
    def simulate_unauthorized_attempt(self):
        """Simulate an unauthorized access attempt"""
        print_colored("\n" + "="*70, "red")
        print_colored("SIMULATING UNAUTHORIZED ACCESS ATTEMPT", "red", bold=True)
        print_colored("="*70, "red")
        
        print("\nScenario: Unknown person attempting to access the system")
        
        # Tier 1: Should fail
        print_colored("\n" + "="*70, "blue")
        print_colored("TIER 1: FACE RECOGNITION", "blue", bold=True)
        print_colored("="*70, "blue")
        
        print("\nProcessing unknown face image...")
        simulate_processing("Extracting facial features", duration=1.5)
        
        print_colored("\nFace not in database", "red", bold=True)
        print_colored("ACCESS DENIED AT TIER 1", "red", bold=True)
        
        print_colored("\n" + "="*70, "red")
        print_colored("UNAUTHORIZED ACCESS BLOCKED", "red", bold=True)
        print_colored("="*70, "red")
        
        return False
    
    def run_menu(self):
        """Display and run the main menu"""
        while True:
            display_banner()
            
            print("\nMain Menu:")
            print("  1. Authorized User Authentication")
            print("  2. Simulate Unauthorized Attempt")
            print("  3. System Information")
            print("  4. Exit")
            
            choice = input("\nSelect an option (1-4): ").strip()
            
            if choice == "1":
                self.run_authentication_flow()
                input("\nPress Enter to continue...")
                
            elif choice == "2":
                self.simulate_unauthorized_attempt()
                input("\nPress Enter to continue...")
                
            elif choice == "3":
                self.show_system_info()
                input("\nPress Enter to continue...")
                
            elif choice == "4":
                print_colored("\nThank you for using the Multimodal Authentication System!", "cyan")
                print_colored("Goodbye!\n", "cyan")
                break
                
            else:
                print_colored("\nInvalid option. Please try again.", "red")
                time.sleep(1)
    
    def show_system_info(self):
        """Display system information"""
        print_colored("\n" + "="*70, "cyan")
        print_colored("SYSTEM INFORMATION", "cyan", bold=True)
        print_colored("="*70, "cyan")
        
        print("\nProject: Multimodal Data Preprocessing")
        print("Team: Mitali, Blessing, Liliane, Mwai")
        print("\nSystem Architecture:")
        print("  - Tier 1: Facial Recognition Model")
        print("  - Tier 2: Voice Verification Model")
        print("  - Tier 3: Product Recommendation Model")
        
        print("\nModel Status:")
        if self.models:
            for model_name, model in self.models.items():
                status = "Loaded" if model else "Not Available"
                print(f"  - {model_name}: {status}")
        else:
            print("  - Models not loaded")
        
        print("\nData Sources:")
        print("  - Facial Images: data/images/")
        print("  - Voice Recordings: data/audio/")
        print("  - Customer Data: data/processed/merged_customer_data.csv")


def main():
    """Main entry point for the CLI application"""
    try:
        # Initialize system
        system = MultimodalAuthSystem()
        
        # Load models
        if not system.load_system():
            print_colored("\nFailed to initialize system. Exiting...", "red", bold=True)
            return 1
        
        # Run main menu
        system.run_menu()
        
        return 0
        
    except KeyboardInterrupt:
        print_colored("\n\nOperation cancelled by user.", "yellow")
        return 130
        
    except Exception as e:
        print_colored(f"\nUnexpected error: {str(e)}", "red", bold=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
