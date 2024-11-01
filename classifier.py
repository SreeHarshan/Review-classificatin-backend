from transformers import RobertaForSequenceClassification, RobertaTokenizer
import torch
import pandas as pd
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

model_name = "roberta-base"
model = RobertaForSequenceClassification.from_pretrained(model_name)
tokenizer = RobertaTokenizer.from_pretrained(model_name)

# model.load_state_dict(data['model_state_dict'],strict=False)
model.to(device)

def predict(query):
    tokens = tokenizer.encode(query)
    all_tokens = len(tokens)
    tokens = tokens[:tokenizer.model_max_length - 2]
    used_tokens = len(tokens)
    tokens = torch.tensor([tokenizer.bos_token_id] + tokens + [tokenizer.eos_token_id]).unsqueeze(0)
    mask = torch.ones_like(tokens)

    with torch.no_grad():
        logits = model(tokens.to(device), attention_mask=mask.to(device))[0]
        probs = logits.softmax(dim=-1)

    fake, real = probs.detach().cpu().flatten().numpy().tolist()
    print(fake,real)

    return "Real" if real>fake else "Fake"
