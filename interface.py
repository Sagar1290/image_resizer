from PIL import Image
import gradio as gr
import resizer

def image_resizer(input_img, input_size):
    return resizer.resize_and_crop_face_centered(input_img, input_size)


inputs = [
    gr.Image(sources=["upload", "clipboard"], type="pil"),
    gr.Dropdown(
        choices=[512, 768, 1024],
        value=512,
        allow_custom_value=True,
        info="Target size of images",
    ),
]
outputs = [
    gr.Image(label="resized image", format="JPEG"),
]
demo = gr.Interface(
    fn=image_resizer,
    inputs=inputs,
    outputs=outputs,
    title="Image Resizer",
)

demo.launch()