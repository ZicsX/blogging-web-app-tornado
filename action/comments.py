class CommentsInterceptor():
    def validator(name,email,content):
        msg = {'msg':'','status':'Submitted Successfully'}
        if email == "":
            msg['msg'] = "EMPTY_email"
            msg['status'] = "email cannot be EMPTY"
        if name == "":
            msg['msg'] = "EMPTY_name"
            msg['status'] = "name cannot be EMPTY"
        if content == "":
            msg['msg'] = "EMPTY_content"
            msg['status'] = "content cannot be EMPTY"
        return msg