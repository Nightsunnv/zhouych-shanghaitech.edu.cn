import math
class Syntax:
    # implement your syntaxes here
    # ... or derive subclasses and implement there
    def charsToSyntaxes(symbols):
        # implement your conversion from symbols to syntaxes here
        pass
    def __hash__(self):
        # implement your hash algorithm for the symbols here
        # you may make use of the default hash algorithms of strings, numbers, etc.
        pass
    def __eq__(self, rhs):
        # implement your syntax equality determination here
        pass
    pass

class EvaluationContext:
    # implement your evaluation context here
    def __init__(self, prev):
        self.vars = {}
        self.pre = prev
    def store(self, name, value):
        self.vars[name] = value
    def load(self, name):
        if self.pre is None:
            return self.vars.get(name, default=None)
        else:
            if self.vars.get(name, default=None) is None:
                return self.pre.load(self.pre, name)
            else:
                return self.vars.get(name, default=None)
    def push(self):
        return EvaluationContext(self)
    def pop(self):
        return self.pre
    pass

class ASTNode:
    # implement your AST Nodes here
    # ... or derive subclasses and give actual implementations there
    def evaluate(self, eval_context):
        # implement your AST Node evaluation according to given context here
        pass
    pass

class AST:
    # implement your AST here
    def syntaxesToAST(syntaxes):
        # build your AST from syntaxes here
        pass
    def evaluate(self, eval_context):
        # implement your AST evaluation according to given context here
        pass
    pass

class Evaluator:
    # implement your evaluator here
    def getInputAsChars(self):
        # retrieve the input as characters from the input file here
        # ... generator is greatly recommended.
        pass
    def evaluate(self):
        chars = self.getInputAsChars()
        syntaxes = Syntax.charsToSyntaxes(chars)
        ast = AST.syntaxesToAST(syntaxes)
        ec = EvaluationContext(None)
        return ast.evaluate(ec)
    def stringifyResult(self, result):
        # implement your result stringify logic here
        pass
    def writeOutput(self, s):
        # store your output to required file here
        pass


if __name__ == "__main__":
    evaluator = Evaluator()
    result = evaluator.evaluate()
    s = evaluator.stringifyResult(result)
    evaluator.writeOutput(s)