class QueryStatment :
    def __init__(self,QuerySyntax,QNumber,PTable,*TableHeaders):
        self.Query=QuerySyntax
        self.QueryNumber=QNumber
        self.Headers = TableHeaders
        self.Table=PTable


