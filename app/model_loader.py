from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


def load_model():

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME
    )

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer
    )

    return pipe