import torch
from transformers import AutoProcessor, ClapModel

class VibeEngine:
    def __init__(self):
        print("Loading CLAP model from Hugging Face...")
        # 'fused' models are better for matching specific vibes to audio
        self.model_id = "laion/clap-htsat-fused"
        
        # Load the model and processor
        self.model = ClapModel.from_pretrained(self.model_id)
        self.processor = AutoProcessor.from_pretrained(self.model_id)
        
        # Set to evaluation mode (no training)
        self.model.eval()
        
    def get_text_vibe(self, text_description):
        """Converts a user vibe (text) into a 512D vector."""
        inputs = self.processor(text=[text_description], return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = self.model.get_text_features(**inputs)
        
        # If it's an object, try to get the first element or a common attribute
        if hasattr(outputs, 'text_embeds'):
            return outputs.text_embeds
        elif hasattr(outputs, 'pooler_output'):
            return outputs.pooler_output
        elif isinstance(outputs, (list, tuple)):
            return outputs[0]
        else:
            # If all else fails, return the object itself and we'll handle it in build_index
            return outputs
if __name__ == "__main__":
    try:
        engine = VibeEngine()
        test_vibe = "A peaceful morning with slow flute music"
        vector = engine.get_text_vibe(test_vibe)
        print(f"\n--- SUCCESS! ---")
        print(f"Vibe: '{test_vibe}'")
        print(f"Generated Vector Shape: {vector.shape}")
    except Exception as e:
        print(f"An error occurred: {e}")