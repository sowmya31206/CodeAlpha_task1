!pip install deep-translator



!pip install deep-translator gradio

from deep_translator import GoogleTranslator
import gradio as gr

def translate_text(text, source, target):
    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

app = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=3, label="Enter Text"),
        gr.Textbox(label="Source Language (en, ta, hi, fr...)"),
        gr.Textbox(label="Target Language (en, ta, hi, fr...)")
    ],
    outputs=gr.Textbox(label="Translated Text"),
    title="🌍 Language Translation Tool",
    description="Translate text between different languages using Google Translator API."
)

app.launch()