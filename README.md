# Language-Translation
This repo will assist you to translate one language into another using different state-of-the-art open-source models.

Mainly, we will be using Transformers. :hugs:

## State-of-the-art Models

* **T5-Small**

  The T5 model was presented in [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf) by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.

  This model allows you to translate English into three different languages with just a small change in code :smiley:. Refer `t5-small.py`:
  * English to German (Use `translate English to German`, if target language is German)
  * English to French (Use `translate English to French`, if target language is French)
  * English to Romanian (Use `translate English to Romanian`, if target language is Romanian)
  
  **Let's Run:** :man_technologist:
   * Install Transformers `pip install transformers`
   * Run this command in terminal `python t5-small.py`
   
   That's it, you are done.:v:
  
  Run inference directly using high end GPU [here](https://huggingface.co/t5-small "t5-small") :rocket:
  
  Read more about [T5 Model - Hugging Face](https://huggingface.co/transformers/model_doc/t5.html "T5 - Hugging Face") :hugs:
  
  --------------
  
* **FSMT**

  We have already created a model (t5-small) in which we translated English into 3 different languages i.e. German, French and Romanian. In this section, we will translate German to English using Facebook's FSMT model.
  
  FSMT (FairSeq Machine Translation) models were introduced in [Facebook FAIR’s WMT19 News Translation Task Submission](https://arxiv.org/abs/1907.06616) by Nathan Ng, Kyra Yee, Alexei Baevski, Myle Ott, Michael Auli, Sergey Edunov.
  
  This model allows you to translate German language into English :smiley:. Refer `wmt-de2en.py`
  
  **Let's Run:** :man_technologist:
   * Install Transformers `pip install transformers`
   * Run this command in terminal `python wmt-de2en.py`
   
   That's it, you are done.:v:
   
  Run inference directly using high end GPU [here](https://huggingface.co/facebook/wmt19-de-en "wmt19-de-en") :rocket:
  
  Read more about [FSMT - Hugging Face](https://huggingface.co/transformers/model_doc/fsmt.html "FSMT - Hugging Face") :hugs:
