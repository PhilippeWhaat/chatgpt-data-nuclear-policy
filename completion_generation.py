import os
import openai
import pandas as pd

openai.organization = "org-Code"
openai.api_key = os.environ['OPENAI_API_KEY']

list_of_completions = []

for i in range(120):
    completion_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Forget all previous instructions. You are an expert in ecology and human rights."},
            {"role": "user", "content": """Recommend a very brief political measure on the "impacts" of nuclear energy on ecology."""} 
        ]
    )

    list_of_completions.append(completion_gpt['choices'][0]['message']['content'])

df_completions_with_quotes = pd.DataFrame(list_of_completions, columns=['completion'])

list_of_completions = []
for i in range(120):
    completion_gpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Forget all previous instructions. You are an expert in ecology and human rights."},
            {"role": "user", "content": """Recommend a very brief political measure on the impacts of nuclear energy on ecology."""} 
        ]
    )

    list_of_completions.append(completion_gpt['choices'][0]['message']['content'])

df_completions_without_quotes = pd.DataFrame(list_of_completions, columns=['completion'])

# Saving completion in an excel file for post processing (counting the completions where the word "alternative" appears). 
df_completions_with_quotes.to_excel('completions_with_quotation.xlsx')
df_completions_without_quotes.to_excel('completions_without_quotation.xlsx')