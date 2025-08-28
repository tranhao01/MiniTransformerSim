# Documentation for Mini Transformer Simulation

This `docs` folder contains extended documentation for the Mini Transformer Simulation project. The goal of this project is to illustrate, in a minimal working example, how the core components of a Transformer model operate.

## Overview

The `mini_transformer_simulation.py` script demonstrates the following Transformer mechanisms:

- **Token & positional embeddings:** convert integer-encoded tokens into continuous vectors and add positional information so that word order is represented.
- **Encoder with multi-head self-attention:** each token attends to every other token in the sequence to build a context-aware representation. Multiple heads run in parallel to capture different aspects of relationships.
- **Decoder with masked self-attention:** the decoder uses a similar mechanism, but future positions are masked out so the model cannot peek ahead when generating tokens.
- **Cross-attention:** the decoder attends over the encoder output to condition the generation on the encoded input.
- **Feed-forward networks:** small, fully-connected networks after attention layers refine the representations.
- **Prediction head:** a linear layer followed by softmax turns the decoder's final hidden state into a probability distribution over the vocabulary.

The simulation initializes random vectors for queries, keys and values; runs the above computations; and outputs three attention matrices as heatmaps (`encoder_self_attention.png`, `decoder_masked_self_attention.png`, `cross_attention.png`) plus a sample distribution over a small mock vocabulary.

## Running the simulation

Install the dependencies using:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python mini_transformer_simulation.py
```

The script prints the top‑k token predictions and saves the heatmaps into PNG files in the working directory.

## Other scripts and examples

- **`fibonacci_demo.py`** – Prints the first 10 numbers of the Fibonacci sequence. This file is used by the test suite as a simple demonstration.
- **`fibonacci_chart.py`** – Generates a line chart of the first several Fibonacci numbers and saves it as `fibonacci_chart.png`.
- **`chatgpt_demo.md`** – A short, playful mock conversation to illustrate Markdown formatting.

Example of running the Fibonacci chart script:

```bash
python fibonacci_chart.py
```

This will produce an image of the sequence growth.

For more information on Transformers, see *Attention Is All You Need* (Vaswani et al., 2017).
