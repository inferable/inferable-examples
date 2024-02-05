import gradio as gr
import torch
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("./model")

def text_to_image(prompt):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    num_inference_steps = 50 if device == "cuda" else 1

    pipeline.to(device)
    image = pipeline(prompt, num_inference_steps=num_inference_steps).images[0]
    return image

def run():  
    interface = gr.Interface(text_to_image, "text", "image")
    interface.launch(server_name="0.0.0.0", server_port=80)

if __name__ == "__main__":
    run()
