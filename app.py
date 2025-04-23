"""
Image Summarization Example using Pydantic AI
"""

from typing import List
from pydantic import BaseModel

from config import settings

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from openai.types.chat.chat_completion_content_part_param import (
    ChatCompletionContentPartTextParam, 
    ChatCompletionContentPartImageParam
)
from openai.types.chat.chat_completion_content_part_image_param import (
    ImageURL
)


class Summary(BaseModel):
    """
    Structured model for summarizing image content
    """
    animals: str
    setting: str
    interaction: str
    oddity: str
    emotion: str


class ImageSummarizer:
    """
    A class to summarize images using LLM
    """

    def __init__(
        self, 
        model_name: str = settings.LLM_MODEL, 
        api_key: str = settings.OPENAI_API_KEY
    ):
        """
        Initialize the image summarizer with an AI model
        
        Args:
            model_name: Name of the AI model to use
            api_key: API key for authentication
        """
        self._model = OpenAIModel(model_name, api_key=api_key)
        self._agent = Agent(
            model=self._model,
            system_prompt="You are a helpful assistant that can summarize images", 
            result_type=Summary,
            model_settings={"temperature": 0, "max_tokens": 10000}
        )

    def summarize(
        self, 
        image_urls: List[str], 
        prompt: str
    ) -> Summary:
        """
        Summarize images using the AI agent
        
        Args:
            image_urls: List of image URLs to summarize
            prompt: Instruction for image summarization
        
        Returns:
            Structured summary of the image
        """
        # Prepare image parameters
        image_params = [
            ChatCompletionContentPartImageParam(
                type='image_url', 
                image_url=ImageURL(url=url, detail='low')
            ) for url in image_urls
        ]

        # Run summarization
        result = self._agent.run_sync([
            ChatCompletionContentPartTextParam(text=prompt, type='text'),
            *image_params
        ])

        return result.data


def main():
    """
    Demonstrate image summarization
    """
    # Example image URLs
    image_urls = [
        'https://test1-emgndhaqd0c9h2db.a01.azurefd.net/images/54d6e0e7-2506-4e17-8c72-0b0c477ec5f5.png',
    ]

    # Prompt for any additional instructions
    prompt = "describe the image in detail"
    # Create summarizer and run analysis
    summarizer = ImageSummarizer()
    summary = summarizer.summarize(image_urls, prompt)

    # Print results
    print("Image Summary:")
    print(summary)


if __name__ == "__main__":
    main()