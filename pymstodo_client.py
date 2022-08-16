from pymstodo import ToDoConnection

client_id = 'a9891cf3-1551-454b-9ebc-438c6a2afca8'
client_secret = 'PJa8Q~A3Lav2cJqN.Gt4ihpPOmRrbho6oyH-Ba0L'

auth_url = ToDoConnection.get_auth_url(client_id)
redirect_resp = input(f'Go here and authorize:\n{auth_url}\n\nPaste the full redirect URL below:\n')

#https://localhost/login/authorized?code=M.R3_SN1.93b1ab04-bd45-4fa4-5c65-d52257abc5fa&state=6SKu5F7ZjHzWWSN541fKVnN8l7GjLI

token = ToDoConnection.get_token(client_id, client_secret, redirect_resp)
todo_client = ToDoConnection(client_id=client_id, client_secret=client_secret, token=token)

lists = todo_client.get_lists()
task_list = lists[0]
tasks = todo_client.get_tasks(task_list.list_id)

print(task_list)
#TEST
print(*tasks, sep='\n')