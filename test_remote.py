import remote_execution as remote

'''
PythonScriptTypes.cpp in UE4.26 Source Code
{ "EPythonCommandExecutionMode::ExecuteFile", (int64)EPythonCommandExecutionMode::ExecuteFile },
{ "EPythonCommandExecutionMode::ExecuteStatement", (int64)EPythonCommandExecutionMode::ExecuteStatement },
{ "EPythonCommandExecutionMode::EvaluateStatement", (int64)EPythonCommandExecutionMode::EvaluateStatement },
			    
'''


def execute_command(command):
    remote_exec = remote.RemoteExecution()
    remote_exec.start()
    remote_exec.open_command_connection(remote_exec.remote_nodes)
    exec_mode = 'ExecuteFile' 
    rec = remote_exec.run_command(command, exec_mode=exec_mode)
    if rec['success'] == True:
        return rec['result']
    return None


json_file_name = 'a.json'

command= 'S:\\Gosh_Project\\publicExchange\\personal\\Johnny\\temp\\ue_fbx_import.py -json "' + json_file_name + '"'

print(command)

execute_command(command)
