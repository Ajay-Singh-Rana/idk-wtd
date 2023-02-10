# h3avren

with open('.vcs/vcs_stage.vcs' , 'r+') as file:
    staged_content = file.read()
    files = staged_content.split("\n")[:-1]
    for file_name in files:
        with open(file_name, 'r') as staged_file:
            contents = staged_file.read()
        with open(".vcs/" + file_name + ".vcs", 'w') as commit_file:
            commit_file.write(contents)
        staged_content = staged_content.replace(file_name + '\n', "")
    file.truncate(0)
    file.write(staged_content)
