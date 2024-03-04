from dotenv import load_dotenv

load_dotenv()

import os
from llama_index.llms.openai import OpenAI
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
import openai

openai.api_key = os.environ.get("KEY")
print(os.environ.get("KEY"))
llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)

    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))
    return index


pdf_path = os.path.join("data", "Family_medicine.pdf")
family_medicine_pdf = PDFReader().load_data(file=pdf_path)
family_medicine_index = get_index(family_medicine_pdf, "medicine")
family_medicine_engine = family_medicine_index.as_query_engine()
