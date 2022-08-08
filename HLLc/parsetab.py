
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programnonassoc=<>LTEGTENETleft+-left*/%right^rightUMINUSUPLUSASSIGNOP BEGIN DO END FACTORIAL GTE ID IFTHEN LTE NET NUMBER POWER REPEAT SIN SQRT UNTIL WHILE WRITELNprogram : compound_statement '.'compound_statement : BEGIN optional_statements ENDexpression : IDempty :optional_statements : statement_listoptional_statements : emptystatement_list : statementstatement_list : statement_list ';' statementstatement : ID ASSIGNOP expressionstatement : REPEAT statement_list UNTIL expressionstatement : WHILE expression DO statementstatement : WRITELN '(' expression ')'statement : compound_statementexpression : expression '+' expression\n                  | expression '-' expression\n                  | expression '*' expression\n                  | expression '/' expression\n                  | expression '^' expression\n                  | expression '%' expression expression : POWER '(' expression ',' expression ')'expression : SQRT '(' expression ')'expression : IFTHEN '(' expression ',' expression ',' expression ')'expression : SIN '(' expression ')'expression : FACTORIAL '(' expression ')'expression : NUMBERexpression : '(' expression ')'expression : '-' expression %prec UMINUSexpression : '+' expression %prec UPLUSexpression : expression '=' expression\n                  | expression '<' expression\n                  | expression '>' expressionexpression : expression LTE expressionexpression : expression GTE expressionexpression : expression NET expression"
    
_lr_action_items = {'BEGIN':([0,3,10,15,33,],[3,3,3,3,3,]),'$end':([1,4,],[0,-1,]),'.':([2,14,],[4,-2,]),'END':([3,5,6,7,8,13,14,19,28,30,31,46,47,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,75,77,79,80,83,86,],[-4,14,-5,-6,-7,-13,-2,-3,-25,-8,-9,-28,-27,-10,-11,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-26,-12,-21,-23,-24,-20,-22,]),'ID':([3,10,11,15,16,20,21,23,29,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[9,9,19,9,19,19,19,19,19,19,9,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'REPEAT':([3,10,15,33,],[10,10,10,10,]),'WHILE':([3,10,15,33,],[11,11,11,11,]),'WRITELN':([3,10,15,33,],[12,12,12,12,]),';':([6,8,13,14,17,19,28,30,31,46,47,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,75,77,79,80,83,86,],[15,-7,-13,-2,15,-3,-25,-8,-9,-28,-27,-10,-11,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-26,-12,-21,-23,-24,-20,-22,]),'UNTIL':([8,13,14,17,19,28,30,31,46,47,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,75,77,79,80,83,86,],[-7,-13,-2,32,-3,-25,-8,-9,-28,-27,-10,-11,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-26,-12,-21,-23,-24,-20,-22,]),'ASSIGNOP':([9,],[16,]),'POWER':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'SQRT':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'IFTHEN':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'SIN':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'FACTORIAL':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'NUMBER':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'(':([11,12,16,20,21,22,23,24,25,26,27,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[23,29,23,23,23,48,23,50,51,52,53,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'-':([11,16,18,19,20,21,23,28,29,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,],[21,21,35,-3,21,21,21,-25,21,35,21,21,21,21,21,21,21,21,21,21,21,21,21,-28,-27,21,35,21,21,21,21,35,35,-14,-15,-16,-17,-18,-19,35,35,35,35,35,35,35,-26,35,35,35,35,21,-21,21,-23,-24,35,35,-20,21,35,-22,]),'+':([11,16,18,19,20,21,23,28,29,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,],[20,20,34,-3,20,20,20,-25,20,34,20,20,20,20,20,20,20,20,20,20,20,20,20,-28,-27,20,34,20,20,20,20,34,34,-14,-15,-16,-17,-18,-19,34,34,34,34,34,34,34,-26,34,34,34,34,20,-21,20,-23,-24,34,34,-20,20,34,-22,]),'DO':([18,19,28,46,47,57,58,59,60,61,62,63,64,65,66,67,68,70,77,79,80,83,86,],[33,-3,-25,-28,-27,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-26,-21,-23,-24,-20,-22,]),'*':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[36,-3,-25,36,-28,-27,36,36,36,36,36,-16,-17,-18,-19,36,36,36,36,36,36,36,-26,36,36,36,36,-21,-23,-24,36,36,-20,36,-22,]),'/':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[37,-3,-25,37,-28,-27,37,37,37,37,37,-16,-17,-18,-19,37,37,37,37,37,37,37,-26,37,37,37,37,-21,-23,-24,37,37,-20,37,-22,]),'^':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[38,-3,-25,38,-28,-27,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-26,38,38,38,38,-21,-23,-24,38,38,-20,38,-22,]),'%':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[39,-3,-25,39,-28,-27,39,39,39,39,39,-16,-17,-18,-19,39,39,39,39,39,39,39,-26,39,39,39,39,-21,-23,-24,39,39,-20,39,-22,]),'=':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[40,-3,-25,40,-28,-27,40,40,40,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,40,-26,40,40,40,40,-21,-23,-24,40,40,-20,40,-22,]),'<':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[41,-3,-25,41,-28,-27,41,41,41,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,41,-26,41,41,41,41,-21,-23,-24,41,41,-20,41,-22,]),'>':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[42,-3,-25,42,-28,-27,42,42,42,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,42,-26,42,42,42,42,-21,-23,-24,42,42,-20,42,-22,]),'LTE':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[43,-3,-25,43,-28,-27,43,43,43,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,43,-26,43,43,43,43,-21,-23,-24,43,43,-20,43,-22,]),'GTE':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[44,-3,-25,44,-28,-27,44,44,44,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,44,-26,44,44,44,44,-21,-23,-24,44,44,-20,44,-22,]),'NET':([18,19,28,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,77,79,80,81,82,83,85,86,],[45,-3,-25,45,-28,-27,45,45,45,-14,-15,-16,-17,-18,-19,None,None,None,None,None,None,45,-26,45,45,45,45,-21,-23,-24,45,45,-20,45,-22,]),')':([19,28,46,47,49,54,57,58,59,60,61,62,63,64,65,66,67,68,70,71,73,74,77,79,80,81,83,85,86,],[-3,-25,-28,-27,70,75,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,-26,77,79,80,-21,-23,-24,83,-20,86,-22,]),',':([19,28,46,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,77,79,80,82,83,86,],[-3,-25,-28,-27,-14,-15,-16,-17,-18,-19,-29,-30,-31,-32,-33,-34,76,-26,78,-21,-23,-24,84,-20,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'compound_statement':([0,3,10,15,33,],[2,13,13,13,13,]),'optional_statements':([3,],[5,]),'statement_list':([3,10,],[6,17,]),'empty':([3,],[7,]),'statement':([3,10,15,33,],[8,8,30,56,]),'expression':([11,16,20,21,23,29,32,34,35,36,37,38,39,40,41,42,43,44,45,48,50,51,52,53,76,78,84,],[18,31,46,47,49,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,81,82,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> compound_statement .','program',2,'p_program','pascal-lab1109.py',252),
  ('compound_statement -> BEGIN optional_statements END','compound_statement',3,'p_compound_statement','pascal-lab1109.py',269),
  ('expression -> ID','expression',1,'p_id_expr','pascal-lab1109.py',274),
  ('empty -> <empty>','empty',0,'p_empty','pascal-lab1109.py',281),
  ('optional_statements -> statement_list','optional_statements',1,'p_optional_statements','pascal-lab1109.py',286),
  ('optional_statements -> empty','optional_statements',1,'p_optional_statements2','pascal-lab1109.py',291),
  ('statement_list -> statement','statement_list',1,'p_statement_list','pascal-lab1109.py',296),
  ('statement_list -> statement_list ; statement','statement_list',3,'p_statement_list2','pascal-lab1109.py',303),
  ('statement -> ID ASSIGNOP expression','statement',3,'p_statement_asgn','pascal-lab1109.py',310),
  ('statement -> REPEAT statement_list UNTIL expression','statement',4,'p_statement_repeat','pascal-lab1109.py',317),
  ('statement -> WHILE expression DO statement','statement',4,'p_statement_while','pascal-lab1109.py',324),
  ('statement -> WRITELN ( expression )','statement',4,'p_statement_writeln','pascal-lab1109.py',332),
  ('statement -> compound_statement','statement',1,'p_statement_cs','pascal-lab1109.py',338),
  ('expression -> expression + expression','expression',3,'p_expression_binop','pascal-lab1109.py',346),
  ('expression -> expression - expression','expression',3,'p_expression_binop','pascal-lab1109.py',347),
  ('expression -> expression * expression','expression',3,'p_expression_binop','pascal-lab1109.py',348),
  ('expression -> expression / expression','expression',3,'p_expression_binop','pascal-lab1109.py',349),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','pascal-lab1109.py',350),
  ('expression -> expression % expression','expression',3,'p_expression_binop','pascal-lab1109.py',351),
  ('expression -> POWER ( expression , expression )','expression',6,'p_expression_power','pascal-lab1109.py',374),
  ('expression -> SQRT ( expression )','expression',4,'p_expression_sqrt','pascal-lab1109.py',381),
  ('expression -> IFTHEN ( expression , expression , expression )','expression',8,'p_expression_ifthen','pascal-lab1109.py',388),
  ('expression -> SIN ( expression )','expression',4,'p_expression_sin','pascal-lab1109.py',395),
  ('expression -> FACTORIAL ( expression )','expression',4,'p_expression_factorial','pascal-lab1109.py',402),
  ('expression -> NUMBER','expression',1,'p_expression_number','pascal-lab1109.py',408),
  ('expression -> ( expression )','expression',3,'p_expression_group','pascal-lab1109.py',414),
  ('expression -> - expression','expression',2,'p_expression_uminus','pascal-lab1109.py',420),
  ('expression -> + expression','expression',2,'p_expression_uplus','pascal-lab1109.py',428),
  ('expression -> expression = expression','expression',3,'p_expression_rel_op','pascal-lab1109.py',433),
  ('expression -> expression < expression','expression',3,'p_expression_rel_op','pascal-lab1109.py',434),
  ('expression -> expression > expression','expression',3,'p_expression_rel_op','pascal-lab1109.py',435),
  ('expression -> expression LTE expression','expression',3,'p_expression_lte','pascal-lab1109.py',442),
  ('expression -> expression GTE expression','expression',3,'p_expression_gte','pascal-lab1109.py',448),
  ('expression -> expression NET expression','expression',3,'p_expression_net','pascal-lab1109.py',454),
]
