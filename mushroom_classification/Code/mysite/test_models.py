#!/usr/bin/env python
"""
Test script for Mushroom Classification ML models
"""

import pickle
import pandas as pd
import os
import sys

def test_ml_models():
    """Test the ML models with sample data"""
    
    print("🍄 Testing Mushroom Classification Models")
    print("=" * 50)
    
    # Check if model files exist
    model_dir = os.path.join(os.path.dirname(__file__), 'polls')
    pca_path = os.path.join(model_dir, 'MushsPCA.pickle')
    model_path = os.path.join(model_dir, 'Mushs.pickle')
    
    if not os.path.exists(pca_path):
        print(f"❌ PCA model not found: {pca_path}")
        return False
    
    if not os.path.exists(model_path):
        print(f"❌ Classification model not found: {model_path}")
        return False
    
    print("✅ Model files found")
    
    try:
        # Load models
        print("📦 Loading models...")
        pca = pickle.load(open(pca_path, 'rb'))
        model = pickle.load(open(model_path, 'rb'))
        print("✅ Models loaded successfully")
        
        # Test with sample data
        print("\n🧪 Testing with sample data...")
        
        # Sample data for an edible mushroom
        sample_data = {
            'cap-shape': 5,  # Convex
            'cap-surface': 2,  # Smooth
            'cap-color': 4,  # Brown
            'bruises': 1,  # Yes
            'odor': 5,  # None
            'gill-attachment': 1,  # Free
            'gill-spacing': 1,  # Crowded
            'gill-size': 0,  # Broad
            'gill-color': 10,  # White
            'stalk-shape': 0,  # Enlarging
            'stalk-root': 1,  # Bulbous
            'stalk-surface-above-ring': 2,  # Smooth
            'stalk-surface-below-ring': 2,  # Smooth
            'stalk-color-above-ring': 7,  # White
            'stalk-color-below-ring': 7,  # White
            'veil-type': 0,  # Partial
            'veil-color': 2,  # White
            'ring-number': 1,  # One
            'ring-type': 4,  # Pendant
            'spore-print-color': 7,  # White
            'population': 3,  # Scattered
            'habitat': 0  # Woods
        }
        
        # Create DataFrame
        df = pd.DataFrame([sample_data])
        print(f"📊 Input shape: {df.shape}")
        
        # Apply PCA transformation
        data_pca = pca.transform(df)
        print(f"🔄 PCA transformed shape: {data_pca.shape}")
        
        # Make prediction
        prediction = model.predict(data_pca)
        print(f"🔮 Raw prediction: {prediction}")
        
        # Interpret result
        if prediction[0] == 0:
            result = "edible"
            emoji = "✅"
        else:
            result = "poisonous"
            emoji = "☠️"
        
        print(f"\n{emoji} Prediction: {result.upper()}")
        
        # Test with poisonous characteristics
        print("\n🧪 Testing with poisonous characteristics...")
        poisonous_data = sample_data.copy()
        poisonous_data['odor'] = 2  # Foul odor
        
        df_poisonous = pd.DataFrame([poisonous_data])
        data_pca_poisonous = pca.transform(df_poisonous)
        prediction_poisonous = model.predict(data_pca_poisonous)
        
        if prediction_poisonous[0] == 0:
            result_p = "edible"
            emoji_p = "✅"
        else:
            result_p = "poisonous"
            emoji_p = "☠️"
        
        print(f"{emoji_p} Prediction: {result_p.upper()}")
        
        print("\n✅ All tests completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_ml_models()
    sys.exit(0 if success else 1)
