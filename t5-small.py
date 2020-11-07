# Install Transformers
# pip install transformers

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-small')

model = T5ForConditionalGeneration.from_pretrained('t5-small', return_dict=True)

input = "My name is Wolfgang and I live in Berlin"

# We can also use "translate English to French" and "translate English to Romanian"
input_ids = tokenizer("translate English to German: "+input, return_tensors="pt").input_ids  # Batch size 1

outputs = model.generate(input_ids)

decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(decoded)
