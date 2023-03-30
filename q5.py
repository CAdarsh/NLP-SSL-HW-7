secret_key = "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"
import os
import openai

openai.api_key = secret_key
prompt = """In addition to writing awesome reviews of your professors, you can design prompts to
get GPT-3 to do all sorts of surprising things. For instance, GPT-3 can perform few-shot learning. Given a few
examples of a task, it can learn a pattern very quickly and then be used for classification tasks. It often helps
to tell the model what you want it to do.
Here’s an example from the paper that introduced GPT-3. It shows a few-show learning example for correct-
ing grammatically incorrect English sentences.
Poor English input: I eated the purple berries.
Good English output: I ate the purple berries.
Poor English input: Thank you for picking me as your designer. I’d appreciate it.
Good English output: Thank you for choosing me as your designer. I appreciate it.
Poor English input: The mentioned changes have done. or I did the alteration that you requested. or I
changed things you wanted and did the modifications.
Good English output: The requested changes have been made. or I made the alteration that you requested. or
I changed things you wanted and made the modifications.
Poor English input: I’d be more than happy to work with you in another project. What will you get?"""

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response["choices"][0]["text"])