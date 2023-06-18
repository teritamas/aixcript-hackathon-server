from google.cloud import vision
from app.facades.vision_ai import client
from app.facades.vision_ai.models import WebDetectionDto


def execute(content: bytes) -> WebDetectionDto:
    image = vision.Image(content=content)

    # WebDetectionの実行
    # https://cloud.google.com/vision/docs/detecting-web?hl=ja#vision_web_detection-python
    response = client.web_detection(image=image)

    # 整形
    annotations = response.web_detection
    dto = WebDetectionDto(
        best_guess_labels=annotations.best_guess_labels[0].label
        if annotations.best_guess_labels
        else "",
        full_math_url=[i.url for i in annotations.full_matching_images[:5]],
        partial_math_urls=[i.url for i in annotations.partial_matching_images[:5]],
        similar_urls=[i.url for i in annotations.visually_similar_images[:5]],
    )
    return dto


path = "./tests/assets/sample_1.jpeg"
with open(path, "rb") as image_file:
    content = image_file.read()

# print(execute(content))

