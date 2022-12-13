class AnonymousServey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)

    def store_reponse(self, new_response):
        self.responses.append(new_response)
    
    def show_result(self):
        print("Survey result:")
        for response in self.responses:
            print(f"- {response}")