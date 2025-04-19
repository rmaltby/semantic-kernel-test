## Experimenting with Semantic Kernel Package and LLM Extension
===========================================================

### Introduction

This project experiments with the semantic kernel package and extends the functionality of Large Language Models (LLMs) using various tools.

### Requirements

* Python 3.x
* `semantic-kernel` package (`pip install semantic-kernel`)
* `torch` library for tensor operations
* `transformers` library for LLM functionality
* Ollama and an LLM model that can run on your local hardware

### Usage

This project was developed using [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/).
- Install Ollama
- Clone the repo
- Run Ollama (`ollama serve &`) and pull an appropriate model (`ollama pull llama3.2:1b`)
- Install uv (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- In the cloned directory, run `uv run main.py`

Chat with the bot, it can currently control and report the status of 3 imaginary lights.  Type `exit` to end the session.  Don't forget to `fg && ^C` to kill the running ollama session when you're done.

### Example Tool Call Response

```
{\"name\": \"Lights-change_state\", \"parameters\": {"\"id\": 1, \"is_on\": false}
```

This tool call changes the current state of the light with id=1 from the `lights` module.

### How it Works

1. The project uses the semantic kernel package to define a custom LLM with specific parameters.
2. The tool calls are generated using the `semantic-kernel` library, which provides a simple API for interacting with the custom LLM.
3. The output of each tool call is used as input to the next tool call, allowing for dynamic and flexible experimentation.

### Tools Used

* Semantic Kernel Package
* Python 3.x
* Torch Library
* Transformers Library

### Future Development

This project aims to explore the potential of extending the functionality of LLMs using custom tools. future development will focus on integrating additional tools and enhancing the overall user experience.

### Contributing

Contributions are welcome! Please submit pull requests with new tool calls or modifications to the existing codebase.

### License

This project is licensed under the MIT License. See `LICENSE` for details.

### Contact

For questions, suggestions, or contributions, please contact Robert Maltby at bmaltby@gmail.com.
