def cond_prob(table, evidence, evidence_value, target, target_value):
  t_subset = up_table_subset(table, target, 'equals', target_value)
  e_list = up_get_column(t_subset, evidence)
  p_b_a = sum([1 if v==evidence_value else 0 for v in e_list])/len(e_list)
  return p_b_a + .01  #Laplace smoothing factor

def naive_bayes(table, row, target):
  names = up_list_column_names(table)
  ev_list = up_zip_lists(names[:-1], row)
  #compute P(Flu=0|...) by collecting cond_probs in a list, take the produce of the list, finally multiply by P(Flu=0)
  a1_bi = up_product([cond_prob(table, ev, ev_val, target, 0) for ev, ev_val in ev_list]) * (len(up_table_subset(table, target, 'equals', 0)) / len(up_get_column(table, target)))
  #do same for P(Flu=1|...)
  a2_bi = up_product([cond_prob(table, ev, ev_val, target, 1) for ev, ev_val in ev_list]) * (len(up_table_subset(table, target, 'equals', 1)) / len(up_get_column(table, target)))
  #return your 2 results in a list
  return [a1_bi, a2_bi]
