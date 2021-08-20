env = dict()


class StatementNode:

    class MathNote:

        def __init__(self, _type, var1, var2):
            self.type = _type
            self.var1 = var1
            self.var2 = var2

    class EqualNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class NotEqualNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class GreaterThanNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class GreaterOrEqualsThanNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class SmallerThanNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class SmallerOrEqualsThanNode:

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class VarAssignNode:

        def __init__(self, name, value):
            self.var_name = name
            self.var_value = value

    class VarNode:

        def __init__(self, name):
            self.var_name = name