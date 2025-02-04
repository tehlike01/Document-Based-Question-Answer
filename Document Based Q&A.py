# -*- coding: utf-8 -*-
"""qa.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1syePT4Hkrgj1Wfp6Gw4ZUdK1EcZslTR8
"""

!pip install transformers datasets torch tqdm

# Import necessary libraries
import torch
from datasets import load_dataset
from transformers import BertTokenizer, BertForQuestionAnswering
from tqdm import tqdm

# Load the SQuAD dataset
squad = load_dataset("squad")

# Load the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# Get an instance from the SQuAD dataset
instance = squad['train'][20]
context = instance['context']
question = instance['question']

# Find the given answer and its start position in the context
given_answer = instance['answers']['text'][0]  # Assuming the first answer is the correct one
given_answer_start = instance['answers']['answer_start'][0]

# Tokenize the example data
inputs = tokenizer(question, context, return_tensors='pt', max_length=512, truncation=True)

# Apply the BERT model to the example data
with torch.no_grad():
    output = model(**inputs)

# Get the predicted answer
start_idx = torch.argmax(output.start_logits)
end_idx = torch.argmax(output.end_logits)
predicted_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx + 1]))

# Evaluate the result of the example data
correct = (predicted_answer.lower() == given_answer.lower())
evaluation = 'Correct' if correct else f'Incorrect (Predicted: {predicted_answer}, Given: {given_answer})'
print(evaluation)

# Define a function to evaluate a single instance
def evaluate_instance(instance):
    context = instance['context']
    question = instance['question']
    given_answer = instance['answers']['text'][0]  # Assuming the first answer is the correct one

    # Tokenize the data
    inputs = tokenizer(question, context, return_tensors='pt', max_length=512, truncation=True)

    # Apply the BERT model
    with torch.no_grad():  # No need to calculate gradients
        output = model(**inputs)

    # Get the predicted answer
    start_idx = torch.argmax(output.start_logits)
    end_idx = torch.argmax(output.end_logits)
    predicted_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx + 1]))

    return predicted_answer.lower() == given_answer.lower()

# Evaluate the BERT model on a set of instances
correct_count = 0
total_count = 100

for i in tqdm(range(total_count)):
    correct_count += evaluate_instance(squad['train'][i])

# Calculate and output the accuracy
accuracy = correct_count / total_count
print(f'Accuracy: {accuracy * 100:.2f}%')

# Install necessary libraries
!pip install transformers torch

# Import necessary libraries
import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Load the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# Define the context and question
context = "Sedimentary rocks are formed by the process of sedimentation. Layer after layer of minerals is deposited over a great span of time, resulting in the formation of a sedimentary rock. As a result, each layer is different if the conditions under which its deposits were different. Thus we can say that a sedimentary rock is a sort of museum, holding the records of all the time over which it was formed, which by all means can be as long as a billion years."
question = " Fathers day."

# Tokenize the input
inputs = tokenizer(question, context, return_tensors='pt', max_length=512, truncation=True)

# Get the model's predictions
with torch.no_grad():
    outputs = model(**inputs)

start_logits = outputs.start_logits
end_logits = outputs.end_logits

start_idx = torch.argmax(start_logits)
end_idx = torch.argmax(end_logits)

# Extract the predicted answer
predicted_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx + 1]))
print(f"Predicted Answer: {predicted_answer}")

!pip install PyPDF2

# Import necessary libraries
import torch
from transformers import BertTokenizer, BertForQuestionAnswering
from PyPDF2 import PdfReader

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    reader = PdfReader(pdf_path)
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

# Load the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# Define the PDF file path and the question
pdf_path = '/content/data/pakistan.pdf'  # Replace with the path to your PDF file
question = "What is the capital of pakistan."  # Replace with your question

# Extract context from the PDF file
context = extract_text_from_pdf(pdf_path)

# Tokenize the input
inputs = tokenizer(question, context, return_tensors='pt', max_length=512, truncation=True)

# Get the model's predictions
with torch.no_grad():
    outputs = model(**inputs)

start_logits = outputs.start_logits
end_logits = outputs.end_logits

start_idx = torch.argmax(start_logits)
end_idx = torch.argmax(end_logits)

# Extract the predicted answer
predicted_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx + 1]))
print(f"Predicted Answer: {predicted_answer}")

!pip install streamlit pyngrok PyPDF2 transformers torch

!pip install streamlit pyngrok PyPDF2 transformers torch

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import torch
# from transformers import BertTokenizer, BertForQuestionAnswering
# from PyPDF2 import PdfReader
# import streamlit as st
# 
# def extract_text_from_pdf(pdf_path):
#     pdf_text = ""
#     reader = PdfReader(pdf_path)
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         pdf_text += page.extract_text()
#     return pdf_text
# 
# @st.cache(allow_output_mutation=True)
# def load_model():
#     tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
#     model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
#     return tokenizer, model
# 
# tokenizer, model = load_model()
# 
# st.title("PDF Question Answering System")
# st.markdown("""
# <style>
#     .main {
#         background-color: #f5f5f5;
#         color: #333;
#     }
#     .stButton button {
#         background-color: #4CAF50;
#         color: white;
#     }
#     .stTextInput > div > div > input {
#         background-color: #e6e6e6;
#     }
#     .stMarkdown {
#         font-size: 1.1em;
#     }
# </style>
# """, unsafe_allow_html=True)
# 
# st.header("Upload a PDF and Ask a Question")
# 
# uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
# 
# if uploaded_file is not None:
#     with st.spinner('Extracting text from PDF...'):
#         pdf_path = uploaded_file
#         context = extract_text_from_pdf(pdf_path)
#         st.success('Text extracted successfully!')
# 
#     question = st.text_input("Enter your question")
# 
#     if st.button("Get Answer"):
#         if question:
#             with st.spinner('Finding answer...'):
#                 inputs = tokenizer(question, context, return_tensors='pt', max_length=512, truncation=True)
# 
#                 with torch.no_grad():
#                     outputs = model(**inputs)
# 
#                 start_logits = outputs.start_logits
#                 end_logits = outputs.end_logits
# 
#                 start_idx = torch.argmax(start_logits)
#                 end_idx = torch.argmax(end_logits)
# 
#                 predicted_answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][start_idx:end_idx + 1]))
# 
#                 st.markdown(f"**Question:** {question}")
#                 st.markdown(f"**Predicted Answer:** {predicted_answer}")
#         else:
#             st.warning("Please enter a question.")
# else:
#     st.info("Please upload a PDF file to proceed.")
# 
# if __name__ == "__main__":
#     st.set_page_config(page_title="PDF QA System", page_icon=":books:", layout="wide")
#

from pyngrok import ngrok

# Run the Streamlit app
!streamlit run app.py &

# Create a public URL
public_url = ngrok.connect(port='8501')
public_url