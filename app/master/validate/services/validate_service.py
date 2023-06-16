from fastapi import File
from app.facades.vision_ai import web_detection

from app.facades.vision_ai.models import WebDetectionDto
from app.master.validate.models.domain import ValidateResult


async def execute(file: File):
    """画像の検証を行い類似画像が存在するかを確認する"""
    image_file = await file.read()
    web_detection_dto: WebDetectionDto = web_detection.execute(image_file)

    validation_result = ValidateResult.parse_obj(
        {
            **web_detection_dto.dict(),
            "is_registerable": False
            if len(web_detection_dto.full_math_url) > 0
            else True,
            "tags": web_detection_dto.best_guess_labels.split(" "),
        }
    )

    return validation_result
