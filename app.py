import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, api_key=OPENAI_API_KEY)

from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(api_key = TAVILY_API_KEY)

def rus_crypto_crew(topic):
    researcher = Agent(
        role = 'Market Researcher',
        goal = f'Uncover emerging trend and investment opportunities in the cryptocurrency market in 2024. Focus on topic {topic}',
        backstory = 'Identify groundbreaking trend and actionable insights.',
        verbose = True,
        tools = [search_tool],
        allow_delegation = False,
        llm = llm,
        max_iter = 5,
        max_rpm = 20
    )

    analyst = Agent(
        role = 'investment analyst',
        goal = f'Analyze cryptocurrency market data to extract actionable insights and investment leads. Focus on topic {topic}',
        backstory = 'Draw meaningful conclusion from market data.',
        verbose = True,
        allow_delegation = False,
        llm = llm
    )

    translator = Agent(
        role = 'translator',
        goal = 'Translate report about cryptocurrency market data into korean',
        backstory = 'Translate this sentence into very natural Korean.',
        verbose = True,
        allow_delegation = False,
        llm = llm
    )


    research_task = Task(
        description = 'Explore the internet to pinpoint emerging trends and potential investment opportunities.',
        agent = researcher,
        expected_output='A detailed summary of the reserch results in string format'
    )

    analyze_task = Task(
        description = 'Analyze the provided cryptocurrency market data to extract key insights and compile a concise report.',
        agent = analyst,
        expected_output='A refined finalized version of the report in string format'
    )

    translate_task = Task(
        description = 'Translate documents written by analyst into korean.',
        agent = translator,
        expected_output = 'A translated report written by analyst(english into korean).'
    )

    crypto_crew = Crew(
        agents = [researcher, analyst, translator],
        tasks = [research_task, analyze_task, translate_task],
        process = Process.sequential
    )

    result = crypto_crew.kickoff()
    return result

import gradio as gr

def process_query(message, history):
    return rus_crypto_crew(message)

app = gr.ChatInterface(
    fn = process_query,
    title = 'Crypto Investment Advisor Bot',
    description = '암호화폐 관련 트렌드를 파악하여 투자 인사이트를 제공해드립니다.'
)
app.launch()