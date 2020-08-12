class A:
   pass


b = A()

A.var_cls = 'a.var_cls'
b.var_inst = 'b.var_inst'

b.var_cls = 'b.var_cls'