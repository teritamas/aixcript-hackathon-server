from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from app.utils.logging import logger

from app.facades.chatgpt.models import CreateChatTitle
from app.facades.chatgpt import chatOpenAi, _convert_json


def execute(content: str) -> CreateChatTitle:
    if content == "":
        logger.warn("content is empty")
        return CreateChatTitle(
            title="タイトルなし",
        )

    report_title_prompt = [
        SystemMessage(
            content="""「概要」と「AIによって画像から検出されたタグ」を利用して、次のフォーマットで値を抽出せよ。
{
  "title": 文章を15文字以下で要約したタイトルで、必ず日本語で返す,
  "tags": 文章から生成したタグのリスト,[tag, tag, tag]の形式,タグは英語で返す
}
titleには、「AIによって画像から検出されたタグ」のうち、1つ以上を必ず含ませる
キーは必ず含ませる。
JSON以外の情報は削除する。

要約して欲しい文章は次の値
"""
        ),
    ]
    report_title_prompt.append(HumanMessage(content=content))
    response = chatOpenAi(
        report_title_prompt,
    )
    response_json = _convert_json(response.content)
    logger.info(f"response_json: {response_json}")
    return CreateChatTitle.parse_obj(response_json)


# デバッグ用です
# logger.info(create_report_title("街の風景を撮影した画像です"))
