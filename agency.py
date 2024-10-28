from agency_swarm import set_openai_key, Agency, Agent
from tools import Search_web_tool, Rewrite_Tool, FilePathFinder_Tool, PDFRewrite_Tool, DocxRewrite_Tool, GPDFFile_Tool, Delete_File_Tool

import os
from dotenv import load_dotenv

load_dotenv
openai_key = os.environ.get("OPENAI_API_KEY")
set_openai_key(openai_key)


ceo = Agent(name="CEO",
              description="You are a CEO of this agency.",
              instructions="./instructions_ceo.md",
              tools=[FilePathFinder_Tool, Delete_File_Tool],
              temperature=0.3,
              max_prompt_tokens=25000
            )

websearcher = Agent(name="Timi",
              description="You are Timi, the websearcher. ",
              instructions="Your main task is to search the web with the Search_web_tool. ",
              tools=[Search_web_tool],
              temperature=0.3,
              max_prompt_tokens=25000
            )

pdf_rewriter = Agent(name="Rade",
                 description="You are Rade, agent specifically trained on rewritting files in pdf format. ",
                 instructions="./instructions_Rade.md",
                 tools=[ PDFRewrite_Tool],
                 temperature=0.1,
                 max_prompt_tokens=25000)

docx_rewriter = Agent(name="Teobald",
                    description="You are Teobald, agent specifically trained on rewritting files in docx format.",
                    instructions="./instructions_Teobald.md",
                    tools=[DocxRewrite_Tool],
                    temperature=0.1,
                    max_prompt_tokens=25000)


agency = Agency([
    ceo,
    [ceo, pdf_rewriter],
    [ceo, websearcher],
    [ceo, docx_rewriter],
])
agency.demo_gradio(height=900)
# agency.run_demo()
