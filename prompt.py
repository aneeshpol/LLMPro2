from langchain_core.prompts import PromptTemplate
#from langchain_community.agent_toolkits.sql.prompt import SQL_PROMPT


custom_prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""
You are an agent designed to interact with SQL databases.

Given an input question, create a syntactically correct SQL query to run. Use the following tools:

{tools}

You have access to the following tables:
Use table and column names as they appear.

When you get the answer, return the result directly — do not explain what you did.
Only include SQL results. Do not say "Here is the result" or "The following output shows".

Begin!

Question: {input}
{agent_scratchpad}
"""
)



#default_template = SQL_PROMPT.template
#suffix_prompt = "only return sql query, SQL:"
#custom_prompt = default_template + suffix_prompt
prompt ="""
You are an expert SQL assistant. Your job is to convert natural language questions into valid SQL queries based on the given database schema.

Only output the SQL query. Do not include explanations or comments.

Here is the schema:

Table: articles
- link (TEXT, PRIMARY KEY)
- title (TEXT)
- summary (TEXT)

Here are a few examples:

Q: List all articles that mention "AI".
SQL: SELECT * FROM articles WHERE title ILIKE '%AI%' OR summary ILIKE '%AI%';

Q: Show the title and link of all articles about climate change.
SQL: SELECT title, link FROM articles WHERE title ILIKE '%climate change%' OR summary ILIKE '%climate change%';

Q: Find articles where the summary includes the word "election".
SQL: SELECT * FROM articles WHERE summary ILIKE '%election%';

Q: Get all articles with "technology" in the title.
SQL: SELECT * FROM articles WHERE title ILIKE '%technology%';
SQL:
          """
