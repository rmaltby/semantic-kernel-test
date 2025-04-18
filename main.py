import asyncio
import logging

from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.connectors.ai.ollama.ollama_prompt_execution_settings import (
    OllamaChatPromptExecutionSettings
)
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments

from ollama._types import ResponseError

from lights_plugin import LightsPlugin

async def main():
    print("Hello from semantic-kernel-test!")

    kernel = Kernel()

    chat_completion_service = OllamaChatCompletion(
        ai_model_id="llama3.2:1b",
        host="localhost:11434"
    )
    kernel.add_service(chat_completion_service)

    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    kernel.add_plugin(
        LightsPlugin(),
        plugin_name="Lights",
    )

    execution_settings = OllamaChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    history = ChatHistory()

    userInput = None
    while True:
        userInput = input("User > ")

        if userInput == "exit":
            break

        history.add_user_message(userInput)

        try:
            result = await chat_completion_service.get_chat_message_content(
                chat_history=history,
                settings=execution_settings,
                kernel=kernel
            )
            print("Assistant > " + str(result))

            history.add_message(result)
        except ConnectionError as e:
            print(f"Error connecting to LLM service: {str(e)}")
            break
        except ResponseError as e:
            print(f"The ollama server threw an error message: {str(e)}")
            continue


if __name__ == "__main__":
    asyncio.run(main())
