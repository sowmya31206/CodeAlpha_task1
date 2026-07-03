!pip install deep-translator

!pip install deep-translator gradio

import gradio as gr
from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):
    try:
        translated = GoogleTranslator(
            source=source_lang.lower(),
            target=target_lang.lower()
        ).translate(text)
        return translated
    except Exception:
        return "Invalid language name. Example: english, tamil, hindi, french"

app = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter Text", lines=4),
        gr.Textbox(label="Source Language (Example: english)"),
        gr.Textbox(label="Target Language (Example: tamil)")
    ],
    outputs=gr.Textbox(label="Translated Text"),
    title="Language Translation Tool",
    description="Enter the text, source language, and target language."
)

app.launch()