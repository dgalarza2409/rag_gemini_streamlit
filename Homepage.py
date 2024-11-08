import streamlit as st

st.set_page_config (
    page_title= "Modelos LLM",
    page_icon= ':smiley:'

)

st.title("Instrucciones de uso")
st.sidebar.success("Seleccione una pagina")

st.markdown("""
### Compara el comportamiento de un LLM (Large Language Model) cuando no tiene contexto y cuando le proporcionas uno

Este chatbot se desarrollo usando Google's Generative AI model Gemini-PRO, Langchain y Streamlit. El contexto puede ser cualquier documento PDF que se separan en "chunks", se codifican y almacenan en una base de datos vectorial, que luego se consulta para obtener el contexto apropiado para que Gemini genere su mejor respuesta.


### Como funciona

Siga las siguientes instruciones:
            
1.- Seleccione una opcion del menu lateral.

2. **Ingrese su API Key**: Se necesita una clave (API key) para acceder al modelo. Obtenga su API key de https://makersuite.google.com/app/apikey.

3. **Haga una pregunta, si seleccionó la primera opción.**
            
4. **Si seleccionó la segunda, cargue sus documentos de contexto**: El sistema acepta multiples archivos PDF, revisando su contenido se generan las respuestas correctas.

5. **Haga una pregunta**: Despues de que los documentos se han procesado, haga cualquier pregunta relativa al contenido que se cargó.
"""
)
