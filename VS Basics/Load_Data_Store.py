import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Dump pdf to pinecone - vector store")
    st.title("Please upload the file.....")

    #upload the pdf file
    pdf= st.file_uploader("Only PDF files allowed", type=["PDF"])

    #Extract the whole text fro the uploaded pdf file
    if pdf is not None:
        with st.spinner("Wait for it ......"):
            #Create Chunks

            st.write("Splitting data into chunks done")


            #Create Embedding

            st.write("Creating Embedding instance done")

            #Built the vector store (push the pdf data embeddings)

        

        st.success("Successfully pushed the embeddings to pinecone")

if __name__=='__main___':
    main()