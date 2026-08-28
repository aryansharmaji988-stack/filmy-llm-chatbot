import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Hugging Face se GGUF / fine-tuned model load karne ke liye setup
MODEL_ID = "aryankaush1kkk/filmy-llama-3.2-gguf" # Apne HF repo ID ke hisab se check kar lena

def generate_dialogue(prompt, history):
    # Model inference logic
    # Agar tuning model load kiya hai to direct prompt pass karke response return kar
    formatted_prompt = f"### Instruction:\n{prompt}\n\n### Response:\n"
    
    # Placeholder example for space deployment
    response = f"Filmy Style Response to: {prompt}"
    return response

# Custom Clean Styling & UI
with gr.Blocks(theme=gr.themes.Soft(primary_hue="red", neutral_hue="slate")) as demo:
    gr.Markdown(
        """
        # 🎬 Filmy LLM Chatbot
        ### *Custom Fine-Tuned Llama-3.2 1B via Unsloth & QLoRA*
        *Prompt in Bollywood style and test the fine-tuned personality!*
        """
    )
    
    chatbot = gr.ChatInterface(
        fn=generate_dialogue,
        textbox=gr.Textbox(placeholder="E.g., Gabbar style mein dialogue bol..."),
        examples=[
            ["Amrish Puri ka villain dialogue de"],
            ["Babu Rao ke style mein funny baat bol"],
            ["Akshay Kumar ka dialogue suna"]
        ]
    )

if __name__ == "__main__":
    demo.queue().launch()
