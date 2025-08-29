from get_movie_list import get_movie_list

result = get_movie_list.lambda_handler("local command", "local context")
print(result)