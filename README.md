## Experimenting with Semantic Kernel Package and LLM Extension
===========================================================

### Introduction

This project experiments with the semantic kernel package and extends the functionality of Large Language Models (LLMs) using various tools.

### Requirements

* Python 3.x
* `semantic-kernel` package (`pip install semantic-kernel`)
* `torch` library for tensor operations
* `transformers` library for LLM functionality

### Usage

To use this project, simply run the provided code and follow the output. The tool call will provide a response to your original question.

### Example Tool Call Response

```
{ "type": "function", "function": "Lights-get_lights", "parameters": { } }
```

This tool call retrieves the current state of the lights from the `lights` module.

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
