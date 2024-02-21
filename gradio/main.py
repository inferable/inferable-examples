import gradio as gr

def text_to_image(prompt):
    return "hello"

def run():  
    interface = gr.Interface(text_to_image, "text", "text")
    interface.launch(server_name="0.0.0.0", server_port=80)

if __name__ == "__main__":
    run()
