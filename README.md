# Language-Translation
This repo will assist you to translate one language into another using different open-source models.

Mainly, we will be using Transformers models.

## Models

* **T5-Small**

  The T5 model was presented in [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf) by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.

  This model allows you to translate English into three different languages with just a small change in code:
  * English to German (Use `translate English to German`, if source language is English and target language is German)
  * English to French (Use `translate English to French`, if source language is English and target language is French)
  * English to Romanian (Use `translate English to Romanian`, if source language is English and target language is Romanian)
  
  **Run:**
   * Install Transformers `pip install transformers`
   * Run this command in terminal `python t5-small.py`
  
  Run inference directly using high end GPU [here](https://huggingface.co/t5-small "t5-small")
  
  Read more about [T5 - Hugging Face](https://huggingface.co/transformers/model_doc/t5.html "T5 - Hugging Face")
