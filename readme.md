Steps for building database:
1)Get data from multiple rss fields. done
2)Format retrieved data using a llm.
3)Save data into a postgres database

Steps user side:
1)Ask user to enter query regarding news.
2)Convert the prompt to a sql query using a llm model.
3)Run the query on our database.
4)Store response.
5)Enter the response into our llm and generate a summary.
6)Print summary to the user.
